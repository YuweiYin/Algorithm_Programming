#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2544-Alternating-Digit-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-12
=================================================================="""

import sys
import time
# from typing import List
# import functools
# import itertools

"""
LeetCode - 2544 - (Easy) - Alternating Digit Sum
https://leetcode.com/problems/alternating-digit-sum/

Description & Requirement:
    You are given a positive integer n. 
    Each digit of n has a sign according to the following rules:
        The most significant digit is assigned a positive sign.
        Each other digit has an opposite sign to its adjacent digits.

    Return the sum of all digits with their corresponding sign.

Example 1:
    Input: n = 521
    Output: 4
    Explanation: (+5) + (-2) + (+1) = 4.
Example 2:
    Input: n = 111
    Output: 1
    Explanation: (+1) + (-1) + (+1) = 1.
Example 3:
    Input: n = 886996
    Output: 0
    Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.

Constraints:
    1 <= n <= 10^9
"""


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (mathematics)
        return self._alternateDigitSum(n)

    def _alternateDigitSum(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1

        res, sign = 0, 1
        while n:
            res += n % 10 * sign
            sign = -sign
            n //= 10

        return -sign * res


def main():
    # Example 1: Output: 4
    # n = 521

    # Example 2: Output: 1
    # n = 111

    # Example 3: Output: 0
    n = 886996

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.alternateDigitSum(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
