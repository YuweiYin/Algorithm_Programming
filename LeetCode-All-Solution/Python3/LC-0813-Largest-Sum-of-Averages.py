#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0813-Largest-Sum-of-Averages.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-28
=================================================================="""

import sys
import time
from typing import List
import itertools

"""
LeetCode - 0813 - (Medium) - Largest Sum of Averages
https://leetcode.com/problems/largest-sum-of-averages/

Description & Requirement:
    You are given an integer array nums and an integer k. 
    You can partition the array into at most k non-empty adjacent subarrays. 
    The score of a partition is the sum of the averages of each subarray.

    Note that the partition must use every integer in nums, and that the score is not necessarily an integer.

    Return the maximum score you can achieve of all the possible partitions. 
    Answers within 10^{-6} of the actual answer will be accepted.

Example 1:
    Input: nums = [9,1,2,3,9], k = 3
    Output: 20.00000
    Explanation: 
        The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
        We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
        That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
Example 2:
    Input: nums = [1,2,3,4,5,6,7], k = 4
    Output: 20.50000

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 10^4
    1 <= k <= nums.length
"""


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert all([num >= 1 for num in nums])
        assert isinstance(k, int) and 1 <= k <= len(nums)
        # main method: (dynamic programming & prefix sum)
        return self._largestSumOfAverages(nums, k)

    def _largestSumOfAverages(self, nums: List[int], k: int) -> float:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and 1 <= k <= len(nums)

        n = len(nums)
        prefix_sum = list(itertools.accumulate(nums, initial=0))
        print(prefix_sum)

        dp = [[0.0 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = prefix_sum[i] / i

        for j in range(2, k + 1):
            for i in range(j, n + 1):
                for x in range(j - 1, i):
                    dp[i][j] = max(dp[i][j], dp[x][j - 1] + (prefix_sum[i] - prefix_sum[x]) / (i - x))
        return float(dp[-1][-1])


def main():
    # Example 1: Output: 20.00000
    # nums = [9, 1, 2, 3, 9]
    # k = 3

    # Example 2: Output: 20.50000
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largestSumOfAverages(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
