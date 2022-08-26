#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0869-Reordered-Power-of-2.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-26
=================================================================="""

import sys
import time
from typing import Tuple
# import collections
# import functools

"""
LeetCode - 0869 - (Medium) - Reordered Power of 2
https://leetcode.com/problems/reordered-power-of-2/

Description & Requirement:
    You are given an integer n. We reorder the digits in any order (including the original order) 
    such that the leading digit is not zero.

    Return true if and only if we can do this so that the resulting number is a power of two.

Example 1:
    Input: n = 1
    Output: true
Example 2:
    Input: n = 10
    Output: false

Constraints:
    1 <= n <= 10^9
"""


class Solution:
    def __init__(self):
        self.power_of_2_digits = {self._count_digits(1 << i) for i in range(30)}

    @staticmethod
    def _count_digits(n: int) -> Tuple[int]:
        BASE = 10
        cnt = [0 for _ in range(BASE)]
        while n:
            cnt[n % BASE] += 1
            n //= BASE
        return tuple(cnt)

    def reorderedPowerOf2(self, n: int) -> bool:
        # exception case
        assert isinstance(n, int)
        # main method: (hash mapping)
        return self._reorderedPowerOf2(n)

    def _reorderedPowerOf2(self, n: int) -> bool:
        assert isinstance(n, int)

        return self._count_digits(n) in self.power_of_2_digits


def main():
    # Example 1: Output: true
    # n = 1

    # Example 2: Output: false
    n = 10

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reorderedPowerOf2(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
