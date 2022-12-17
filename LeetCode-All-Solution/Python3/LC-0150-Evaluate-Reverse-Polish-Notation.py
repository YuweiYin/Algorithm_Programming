#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0150-Evaluate-Reverse-Polish-Notation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-17
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0150 - (Medium) - Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Description & Requirement:
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

    Note that division between two integers should truncate toward zero.

    It is guaranteed that the given RPN expression is always valid. 
    That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Example 1:
    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9
Example 2:
    Input: tokens = ["4","13","5","/","+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6
Example 3:
    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
        = ((10 * (6 / (12 * -11))) + 17) + 5
        = ((10 * (6 / -132)) + 17) + 5
        = ((10 * 0) + 17) + 5
        = (0 + 17) + 5
        = 17 + 5
        = 22

Constraints:
    1 <= tokens.length <= 10^4
    tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # exception case
        assert isinstance(tokens, list) and len(tokens) >= 1
        # main method: (stack simulation)
        return self._evalRPN(tokens)

    def _evalRPN(self, tokens: List[str]) -> int:
        """
        Time: beats 97.81%; Space: beats 22.27%
        """
        assert isinstance(tokens, list) and len(tokens) >= 1

        stack = []
        ops = {"+", "-", "*", "/"}
        for token in tokens:
            if token in ops:
                if len(stack) >= 2 and isinstance(stack[-1], int) and isinstance(stack[-2], int):
                    num_2 = stack.pop()
                    num_1 = stack.pop()
                    if token == "+":
                        stack.append(num_1 + num_2)
                    elif token == "-":
                        stack.append(num_1 - num_2)
                    elif token == "*":
                        stack.append(num_1 * num_2)
                    elif token == "/":
                        stack.append(int(num_1 / num_2))
                    else:
                        pass
                else:
                    pass
            else:
                stack.append(int(token))

        return stack[0]


def main():
    # Example 1: Output: 9
    tokens = ["2", "1", "+", "3", "*"]

    # Example 2: Output: 6
    # tokens = ["4", "13", "5", "/", "+"]

    # Example 3: Output: 22
    # tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.evalRPN(tokens)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
