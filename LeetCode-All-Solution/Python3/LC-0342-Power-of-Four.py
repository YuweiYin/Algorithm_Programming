#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0342-Power-of-Four.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-22
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0342 - (Easy) - Power of Four
https://leetcode.com/problems/power-of-four/

Description & Requirement:
    Given an integer n, return true if it is a power of four. Otherwise, return false.

    An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
    Input: n = 16
    Output: true
Example 2:
    Input: n = 5
    Output: false
Example 3:
    Input: n = 1
    Output: true

Constraints:
    -2^31 <= n <= 2^31 - 1

Follow up:
    Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # exception case
        assert isinstance(n, int)
        # main method: (bit manipulation: n is the power of 2 if n & (n - 1))
        return self._isPowerOfFour(n)

    def _isPowerOfFour(self, n: int) -> bool:
        assert isinstance(n, int)

        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0


def main():
    # Example 1: Output: true
    n = 16

    # Example 2: Output: false
    # n = 5

    # Example 3: Output: true
    # n = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isPowerOfFour(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
