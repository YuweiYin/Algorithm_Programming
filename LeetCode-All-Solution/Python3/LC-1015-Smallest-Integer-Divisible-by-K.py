#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1015-Smallest-Integer-Divisible-by-K.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-10
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1015 - (Medium) - Smallest Integer Divisible by K
https://leetcode.com/problems/smallest-integer-divisible-by-k/

Description & Requirement:
    Given a positive integer k, you need to find the length of the smallest positive integer n 
    such that n is divisible by k, and n only contains the digit 1.

    Return the length of n. If there is no such n, return -1.

    Note: n may not fit in a 64-bit signed integer.

Example 1:
    Input: k = 1
    Output: 1
    Explanation: The smallest answer is n = 1, which has length 1.
Example 2:
    Input: k = 2
    Output: -1
    Explanation: There is no such positive integer n divisible by 2.
Example 3:
    Input: k = 3
    Output: 3
    Explanation: The smallest answer is n = 111, which has length 3.

Constraints:
    1 <= k <= 10^5
"""


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # exception case
        assert isinstance(k, int) and k >= 1
        # main method: (simulate the division process)
        return self._smallestRepunitDivByK(k)

    def _smallestRepunitDivByK(self, k: int) -> int:
        assert isinstance(k, int) and k >= 1

        if k % 2 == 0 or k % 5 == 0:
            return -1

        res, residual = 1, 1
        while residual % k != 0:
            residual = (residual % k) * (10 % k) + 1
            res += 1

        return res


def main():
    # Example 1: Output: 1
    # k = 1

    # Example 2: Output: -1
    # k = 2

    # Example 3: Output: 3
    k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.smallestRepunitDivByK(k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
