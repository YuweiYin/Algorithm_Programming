#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1106-Parsing-A-Boolean-Expression.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-05
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1106 - (Hard) - Parsing A Boolean Expression
https://leetcode.com/problems/parsing-a-boolean-expression/

Description & Requirement:
    A boolean expression is an expression that evaluates to either true or false. 
    It can be in one of the following shapes:
        't' that evaluates to true.
        'f' that evaluates to false.
        '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
        '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND 
            of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
        '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR 
            of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.

    Given a string expression that represents a boolean expression, return the evaluation of that expression.

    It is guaranteed that the given expression is valid and follows the given rules.

Example 1:
    Input: expression = "&(|(f))"
    Output: false
    Explanation: 
        First, evaluate |(f) --> f. The expression is now "&(f)".
        Then, evaluate &(f) --> f. The expression is now "f".
        Finally, return false.
Example 2:
    Input: expression = "|(f,f,f,t)"
    Output: true
    Explanation: The evaluation of (false OR false OR false OR true) is true.
Example 3:
    Input: expression = "!(&(f,t))"
    Output: true
    Explanation: 
        First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
        Then, evaluate !(f) --> NOT false --> true. We return true.

Constraints:
    1 <= expression.length <= 2 * 10^4
    expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.
"""


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # exception case
        assert isinstance(expression, str) and len(expression) >= 1
        # main method: (stack simulation)
        return self._parseBoolExpr(expression)

    def _parseBoolExpr(self, expression: str) -> bool:
        assert isinstance(expression, str) and len(expression) >= 1

        stack = []
        for ch in expression:
            if ch == ',':
                continue
            if ch != ')':
                stack.append(ch)
                continue

            t = f = 0
            while stack[-1] != '(':
                if stack.pop() == 't':
                    t += 1
                else:
                    f += 1
            stack.pop()

            op = stack.pop()
            if op == '!':
                stack.append('t' if f == 1 else 'f')
            elif op == '&':
                stack.append('t' if f == 0 else 'f')
            elif op == '|':
                stack.append('t' if t else 'f')

        return stack[-1] == 't'


def main():
    # Example 1: Output: false
    # expression = "&(|(f))"

    # Example 2: Output: true
    # expression = "|(f,f,f,t)"

    # Example 3: Output: true
    expression = "!(&(f,t))"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.parseBoolExpr(expression)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
