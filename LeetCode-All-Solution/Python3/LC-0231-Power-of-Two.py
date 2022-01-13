#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0231-Power-of-Two.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-13
=================================================================="""

import sys
import time
# from typing import List

"""
LeetCode - 0231 - (Easy) - Power of Two
https://leetcode.com/problems/power-of-two/

Description & Requirement:
    Given an integer n, return true if it is a power of two. Otherwise, return false.
    An integer n is a power of two, if there exists an integer x such that n == 2^x.

Example 1:
    Input: n = 1
    Output: true
    Explanation: 2^0 = 1
Example 2:
    Input: n = 16
    Output: true
    Explanation: 2^4 = 16
Example 3:
    Input: n = 3
    Output: false

Constraints:
    -2^31 <= n <= 2^31 - 1
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # exception case
        if not isinstance(n, int) or n <= 0:
            return False  # Error input type
        # main method: (Bit Manipulation)
        #     idea: if n is a power of two, then its binary representation must be 0b1000...000,
        #     and (n-1) is 0b0111...111, so n & (n-1) == 0
        return self._isPowerOfTwo(n)

    def _isPowerOfTwo(self, n: int) -> bool:
        return not bool(n & (n - 1))


def main():
    # Example 1: Output: true
    # n = 1

    # Example 2: Output: true
    # n = 16

    # Example 3: Output: false
    n = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isPowerOfTwo(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
