#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0338-Counting-Bits.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-01
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0338 - (Easy) - Counting Bits
https://leetcode.com/problems/counting-bits/

Description & Requirement:
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
    ans[i] is the number of 1's in the binary representation of i.

Example 1:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
Example 2:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        3 --> 11
        4 --> 100
        5 --> 101

Constraints:
    0 <= n <= 10^5
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        # exception case
        # method 1: O(n^2): count 1s of every number, scan every bit
        # method 2: O(n log n): count 1s of every number, use Brian Kernighan's algorithm to count
        # method 3: O(n): Dynamic Programming. dp[i] is the counter of number i;
        #     dp equation: dp[i] = dp[j] + 1, where 0 <= j < i
        #         remove the highest bit in i to get j, dp[i] must be equal to dp[j] + 1
        #     dp init: dp[0] = 0
        # return self._countBits(n)
        # return self._countBitsBrianKernighan(n)
        return self._countBitsDp(n)

    def _countBits(self, n: int) -> List[int]:
        assert isinstance(n, int) and n >= 0

        def __count_binary_1(number: int) -> int:
            ans = 0
            while number > 0:
                if number & 0x01 == 1:  # check the lowest bit
                    ans += 1
                number >>= 1
            return ans

        res = []
        for num in range(n + 1):
            res.append(__count_binary_1(num))

        return res

    def _countBitsBrianKernighan(self, n: int) -> List[int]:
        assert isinstance(n, int) and n >= 0

        def __count_binary_1(number: int) -> int:
            ans = 0
            while number > 0:
                number &= (number - 1)
                ans += 1
            return ans

        res = []
        for num in range(n + 1):
            res.append(__count_binary_1(num))

        return res

    def _countBitsDp(self, n: int) -> List[int]:
        """
        Runtime: 80 ms, faster than 93.17% of Python3 online submissions for Counting Bits.
        Memory Usage: 21 MB, less than 20.83% of Python3 online submissions for Counting Bits.
        """
        assert isinstance(n, int) and n >= 0

        # dp[i] is the counter of number i
        dp = [0]  # dp init: dp[0] = 0

        # dp equation: dp[i] = dp[j] + 1, where 0 <= j < i
        #     remove the highest bit in i to get j, dp[i] must be equal to dp[j] + 1
        highest_bit = 0  # the current highest bit in number {0, 1, 2, ..., i}
        for i in range(1, n + 1):
            if i & (i - 1) == 0:  # if i == 2^k
                highest_bit = i  # update the highest_bit (must be in ascending order)
            dp.append(dp[i - highest_bit] + 1)

        return dp


def main():
    # Example 1: Output: [0,1,1]
    # n = 2

    # Example 2: Output: [0,1,1,2,1,2]
    # n = 5

    # method 1: O(n^2)  266.65600 ms
    # method 2: O(n log n)  140.18800 ms
    # method 3: O(n)  26.23900 ms
    n = int(1e5)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countBits(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
