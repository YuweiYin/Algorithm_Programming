#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0264-Ugly-Number-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-14
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0264 - (Medium) - Ugly Number II
https://leetcode.com/problems/ugly-number-ii/

Description & Requirement:
    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

    Given an integer n, return the n-th ugly number.

Example 1:
    Input: n = 10
    Output: 12
    Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:
    Input: n = 1
    Output: 1
    Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Constraints:
    1 <= n <= 1690
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n > 0
        # main method: (expand ugly number set by multiply 2, 3, and 5)
        #     optimize 1: use heap rather than set, keep slow expanding speed
        #     optimize 2: use list & dynamic programming to expand numbers (three pointers for multiplier 2, 3, and 5)
        return self._nthUglyNumber(n)

    def _nthUglyNumber(self, n: int) -> int:

        ugly_set = {1, 2, 3, 5}
        multiplier_list = [2, 3, 5]

        ugly_set_max_size = n * 5
        while len(ugly_set) < ugly_set_max_size:
            new_ugly_set = ugly_set.copy()
            # each time, multiply ugly_num with 2/3/5
            for ugly_num in ugly_set:
                for multiplier in multiplier_list:
                    new_ugly_num = ugly_num * multiplier
                    if new_ugly_num not in new_ugly_set:
                        new_ugly_set.add(new_ugly_num)
            ugly_set = new_ugly_set

        ugly_list = list(ugly_set)
        ugly_list.sort()
        return ugly_list[n - 1]


def main():
    # Example 1: Output: 12
    #     Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
    n = 10

    # Example 2: Output: 1
    # n = 1

    # Example 3: Output: 2123366400
    # n = 1690

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.nthUglyNumber(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
