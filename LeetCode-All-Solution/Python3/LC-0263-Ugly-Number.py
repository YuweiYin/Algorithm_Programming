#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0263-Ugly-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-18
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0263 - (Easy) - Ugly Number
https://leetcode.com/problems/ugly-number/

Description & Requirement:
    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

    Given an integer n, return true if n is an ugly number.

Example 1:
    Input: n = 6
    Output: true
    Explanation: 6 = 2 × 3
Example 2:
    Input: n = 1
    Output: true
    Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
Example 3:
    Input: n = 14
    Output: false
    Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:
    -2^31 <= n <= 2^31 - 1
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        # exception case
        assert isinstance(n, int)
        # main method: (True if n == 1 after getting divided by all 2, 3, 5)
        return self._isUgly(n)

    def _isUgly(self, n: int) -> bool:
        assert isinstance(n, int)
        if n <= 0:
            return False

        while n & 0x01 == 0:
            n >>= 1
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5

        return n == 1


def main():
    # Example 1: Output: true
    # n = 6

    # Example 2: Output: true
    # n = 1

    # Example 3: Output: false
    n = 14

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isUgly(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
