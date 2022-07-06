#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0736-Parse-Lisp-Expression.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-06
=================================================================="""

import sys
import time
from collections import defaultdict
# from typing import List
# import functools

"""
LeetCode - 0128 - (Hard) - Parse Lisp Expression
https://leetcode.com/problems/parse-lisp-expression/

Description & Requirement:
    You are given a string expression representing a Lisp-like expression to return the integer value of.

    The syntax for these expressions is given as follows.

    - An expression is either an integer, let expression, add expression, mult expression, or an assigned variable. 
        Expressions always evaluate to a single integer.
    - (An integer could be positive or negative.)
    - A let expression takes the form "(let v1 e1 v2 e2 ... vn en expr)", where let is always the string "let", 
        then there are one or more pairs of alternating variables and expressions, 
        meaning that the first variable v1 is assigned the value of the expression e1, 
        the second variable v2 is assigned the value of the expression e2, and so on sequentially; 
        and then the value of this let expression is the value of the expression expr.
    - An add expression takes the form "(add e1 e2)" where add is always the string "add", 
        there are always two expressions e1, e2 and 
        the result is the addition of the evaluation of e1 and the evaluation of e2.
    - A mult expression takes the form "(mult e1 e2)" where mult is always the string "mult", 
        there are always two expressions e1, e2 and 
        the result is the multiplication of the evaluation of e1 and the evaluation of e2.
    - For this question, we will use a smaller subset of variable names. 
        A variable starts with a lowercase letter, then zero or more lowercase letters or digits. 
        Additionally, for your convenience, the names "add", "let", and "mult" are protected and 
        will never be used as variable names.
    - Finally, there is the concept of scope. When an expression of a variable name is evaluated, 
        within the context of that evaluation, the innermost scope (in terms of parentheses) 
        is checked first for the value of that variable, and then outer scopes are checked sequentially. 
        It is guaranteed that every expression is legal. Please see the examples for more details on the scope.

Example 1:
    Input: expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
    Output: 14
    Explanation: In the expression (add x y), when checking for the value of the variable x,
        we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
        Since x = 3 is found first, the value of x is 3.
Example 2:
    Input: expression = "(let x 3 x 2 x)"
    Output: 2
    Explanation: Assignment in let statements is processed sequentially.
Example 3:
    Input: expression = "(let x 1 y 2 x (add x y) (add x y))"
    Output: 5
    Explanation: The first (add x y) evaluates as 3, and is assigned to x.
        The second (add x y) evaluates as 3+2 = 5.

Constraints:
    1 <= expression.length <= 2000
    There are no leading or trailing spaces in expression.
    All tokens are separated by a single space in expression.
    The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
    The expression is guaranteed to be legal and evaluate to an integer.
"""


class Solution:
    def evaluate(self, expression: str) -> int:
        # exception case
        assert isinstance(expression, str) and len(expression) >= 1
        # main method: (recursive parsing)
        return self._evaluate(expression)

    def _evaluate(self, expression: str) -> int:
        assert isinstance(expression, str) and len(expression) >= 1
        i, n = 0, len(expression)

        def __parse_var() -> str:
            nonlocal i
            i0 = i
            while i < n and expression[i] != ' ' and expression[i] != ')':
                i += 1
            return expression[i0:i]

        def __parse_int() -> int:
            nonlocal i
            sign, x = 1, 0
            if expression[i] == '-':
                sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                x = x * 10 + int(expression[i])
                i += 1
            return sign * x

        scope = defaultdict(list)

        def __innerEvaluate() -> int:
            nonlocal i
            if expression[i] != '(':  # not expression, might be either a variable or an integer
                if expression[i].islower():  # variable
                    return scope[__parse_var()][-1]
                return __parse_int()  # integer
            i += 1  # remove the left parenthesis
            if expression[i] == 'l':  # let expression
                i += 4  # skip string "let "
                vars = []
                while True:
                    if not expression[i].islower():
                        res = __innerEvaluate()  # the value of the last expr in let expression
                        break
                    var = __parse_var()
                    if expression[i] == ')':
                        res = scope[var][-1]  # the value of the last expr in let expression
                        break
                    vars.append(var)
                    i += 1  # remove space
                    scope[var].append(__innerEvaluate())
                    i += 1  # remove space
                for var in vars:
                    scope[var].pop()  # remove variables in the current scope
            elif expression[i] == 'a':  # add expression
                i += 4  # skip string "add "
                e1 = __innerEvaluate()
                i += 1  # remove space
                e2 = __innerEvaluate()
                res = e1 + e2
            else:  # mult expression
                i += 5  # skip string "mult "
                e1 = __innerEvaluate()
                i += 1  # remove space
                e2 = __innerEvaluate()
                res = e1 * e2
            i += 1  # remove the right parenthesis
            return res

        return __innerEvaluate()


def main():
    # Example 1: Output: 14
    expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"

    # Example 2: Output: 2
    # expression = "(let x 3 x 2 x)"

    # Example 3: Output: 5
    # expression = "(let x 1 y 2 x (add x y) (add x y))"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.evaluate(expression)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
