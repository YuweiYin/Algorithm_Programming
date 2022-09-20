#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0698-Partition-to-K-Equal-Sum-Subsets.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-20
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0698 - (Medium) - Partition to K Equal Sum Subsets
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Description & Requirement:
    Given an integer array nums and an integer k, 
    return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
    Input: nums = [4,3,2,3,5,2,1], k = 4
    Output: true
    Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:
    Input: nums = [1,2,3,4], k = 3
    Output: false

Constraints:
    1 <= k <= nums.length <= 16
    1 <= nums[i] <= 10^4
    The frequency of each element is in the range [1, 4].
"""


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # exception case
        assert isinstance(nums, list) and isinstance(k, int) and 1 <= k <= len(nums)
        for num in nums:
            assert isinstance(num, int) and num >= 1
        # main method: (dynamic programming)
        return self._canPartitionKSubsets(nums, k)

    def _canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        assert isinstance(nums, list) and isinstance(k, int) and 1 <= k <= len(nums)

        total = sum(nums)
        if total % k:
            return False
        per = total // k

        nums.sort()
        if nums[-1] > per:
            return False
        n = len(nums)

        dp = [False for _ in range(1 << n)]
        dp[0] = True

        cur_sum = [0 for _ in range(1 << n)]
        for i in range(0, 1 << n):
            if not dp[i]:
                continue
            for j in range(n):
                if cur_sum[i] + nums[j] > per:
                    break
                if (i >> j & 1) == 0:
                    _next = i | (1 << j)
                    if not dp[_next]:
                        cur_sum[_next] = (cur_sum[i] + nums[j]) % per
                        dp[_next] = True

        return dp[(1 << n) - 1]


def main():
    # Example 1: Output: true
    # nums = [4, 3, 2, 3, 5, 2, 1]
    # k = 4

    # Example 2: Output: false
    nums = [1, 2, 3, 4]
    k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canPartitionKSubsets(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
