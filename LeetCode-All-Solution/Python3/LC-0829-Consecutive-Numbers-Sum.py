#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0829-Consecutive-Numbers-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-03
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0829 - (Hard) - Consecutive Numbers Sum
https://leetcode.com/problems/consecutive-numbers-sum/

Description & Requirement:
    Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.

Example 1:
    Input: n = 5
    Output: 2
    Explanation: 5 = 2 + 3
Example 2:
    Input: n = 9
    Output: 3
    Explanation: 9 = 4 + 5 = 2 + 3 + 4
Example 3:
    Input: n = 15
    Output: 4
    Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Constraints:
    1 <= n <= 10^9
"""


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (Mathematics: arithmetic progression)
        return self._consecutiveNumbersSum(n)

    def _consecutiveNumbersSum(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1

        def __is_k_consecutive(_k: int) -> bool:
            if _k & 0x01 == 1:  # odd
                return (n % _k) == 0
            else:  # even
                return (n % _k) and ((n << 1) % _k) == 0

        res = 0
        k = 1
        n_2 = n << 1
        while k * (k + 1) <= n_2:
            if __is_k_consecutive(k):
                res += 1
            k += 1

        return res


def main():
    # Example 1: Output: 2
    # n = 5

    # Example 2: Output: 3
    # n = 9

    # Example 3: Output: 4
    n = 15

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.consecutiveNumbersSum(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
