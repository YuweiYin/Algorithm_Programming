#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0224-Basic-Calculator.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-18
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0224 - (Hard) - Basic Calculator
https://leetcode.com/problems/basic-calculator/

Description & Requirement:
    Given a string s representing a valid expression, implement a basic calculator to evaluate it, 
    and return the result of the evaluation.

    Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, 
    such as eval().

Example 1:
    Input: s = "1 + 1"
    Output: 2
Example 2:
    Input: s = " 2-1 + 2 "
    Output: 3
Example 3:
    Input: s = "(1+(4+5+2)-3)+(6+8)"
    Output: 23

Constraints:
    1 <= s.length <= 3 * 10^5
    s consists of digits, '+', '-', '(', ')', and ' '.
    s represents a valid expression.
    '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
    '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
    There will be no two consecutive operators in the input.
    Every number and running calculation will fit in a signed 32-bit integer.
"""


class Solution:
    def calculate(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (stack)
        return self._calculate(s)

    def _calculate(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1

        ops = [1]
        sign = 1

        res = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                res += num * sign

        return res


def main():
    # Example 1: Output: 2
    # s = "1 + 1"

    # Example 2: Output: 3
    # s = " 2-1 + 2 "

    # Example 3: Output: 23
    s = "(1+(4+5+2)-3)+(6+8)"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.calculate(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
