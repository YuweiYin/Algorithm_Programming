#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1799-Maximize-Score-After-N-Operations.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-22
=================================================================="""

import sys
import time
from typing import List
import math
# import collections
# import functools

"""
LeetCode - 1799 - (Hard) - Maximize Score After N Operations
https://leetcode.com/problems/maximize-score-after-n-operations/

Description & Requirement:
    You are given nums, an array of positive integers of size 2 * n. 
    You must perform n operations on this array.

    In the ith operation (1-indexed), you will:
        Choose two elements, x and y.
        Receive a score of i * gcd(x, y).
        Remove x and y from nums.

    Return the maximum score you can receive after performing n operations.

    The function gcd(x, y) is the greatest common divisor of x and y.

Example 1:
    Input: nums = [1,2]
    Output: 1
    Explanation: The optimal choice of operations is:
        (1 * gcd(1, 2)) = 1
Example 2:
    Input: nums = [3,4,6,8]
    Output: 11
    Explanation: The optimal choice of operations is:
        (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:
    Input: nums = [1,2,3,4,5,6]
    Output: 14
    Explanation: The optimal choice of operations is:
        (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14

Constraints:
    1 <= n <= 7
    nums.length == 2 * n
    1 <= nums[i] <= 10^6
"""


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2 and len(nums) & 0x01 == 0
        # main method: (dynamic programming)
        return self._maxScore(nums)

    def _maxScore(self, nums: List[int]) -> int:
        """
        Time: beats 98.10%; Space: beats 90.48%
        """
        assert isinstance(nums, list) and len(nums) >= 2 and len(nums) & 0x01 == 0

        n = len(nums)
        dp = [0 for _ in range(1 << n)]
        gcd_dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                gcd_dp[i][j] = math.gcd(nums[i], nums[j])

        max_num = 1 << n
        for num in range(1, max_num):
            # bit_cnt = num.bit_count()
            bit_cnt = bin(num).count("1")
            if bit_cnt & 0x01 == 1:
                continue
            for i in range(n):
                if (num >> i) & 0x01 == 1:
                    for j in range(i + 1, n):
                        if (num >> j) & 0x01 == 1:
                            dp[num] = max(dp[num], dp[num ^ (1 << i) ^ (1 << j)] + (bit_cnt >> 1) * gcd_dp[i][j])

        return dp[-1]


def main():
    # Example 1: Output: 1
    nums = [1, 2]

    # Example 2: Output: 11
    # nums = [3, 4, 6, 8]

    # Example 3: Output: 14
    # nums = [1, 2, 3, 4, 5, 6]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxScore(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
