#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1043-Partition-Array-for-Maximum-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-19
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1043 - (Medium) - Partition Array for Maximum Sum
https://leetcode.com/problems/partition-array-for-maximum-sum/

Description & Requirement:
    Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. 
    After partitioning, each subarray has their values changed to become the maximum value of that subarray.

    Return the largest sum of the given array after partitioning. 
    Test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
    Input: arr = [1,15,7,9,2,5,10], k = 3
    Output: 84
    Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:
    Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
    Output: 83
Example 3:
    Input: arr = [1], k = 1
    Output: 1

Constraints:
    1 <= arr.length <= 500
    0 <= arr[i] <= 10^9
    1 <= k <= arr.length
"""


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (dynamic programming)
        return self._maxSumAfterPartitioning(arr, k)

    def _maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        assert isinstance(arr, list) and len(arr) >= 1
        assert isinstance(k, int) and k >= 1

        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            max_value = arr[i - 1]
            for j in range(i - 1, max(-1, i - k - 1), -1):
                dp[i] = max(dp[i], dp[j] + max_value * (i - j))
                if j > 0:
                    max_value = max(max_value, arr[j - 1])

        return dp[-1]


def main():
    # Example 1: Output: 84
    # arr = [1, 15, 7, 9, 2, 5, 10]
    # k = 3

    # Example 2: Output: 83
    arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
    k = 4

    # Example 3: Output: 1
    # arr = [1]
    # k = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxSumAfterPartitioning(arr, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
