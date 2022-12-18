#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1703-Minimum-Adjacent-Swaps-for-K-Consecutive-Ones.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-18
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1703 - (Hard) - Minimum Adjacent Swaps for K Consecutive Ones
https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

Description & Requirement:
    You are given an integer array, nums, and an integer k. nums comprises of only 0's and 1's. 
    In one move, you can choose two adjacent indices and swap their values.

    Return the minimum number of moves required so that nums has k consecutive 1's.

Example 1:
    Input: nums = [1,0,0,1,0,1], k = 2
    Output: 1
    Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive 1's.
Example 2:
    Input: nums = [1,0,0,0,0,0,1,1], k = 3
    Output: 5
    Explanation: In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,1,1,1].
Example 3:
    Input: nums = [1,1,0,1], k = 2
    Output: 0
    Explanation: nums already has 2 consecutive 1's.

Constraints:
    1 <= nums.length <= 10^5
    nums[i] is 0 or 1.
    1 <= k <= sum(nums)
"""


class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (greedy & prefix sum)
        return self._minMoves(nums, k)

    def _minMoves(self, nums: List[int], k: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        greedy, pre_sum = [], [0]
        for i, num in enumerate(nums):
            if num == 1:
                greedy.append(i - len(greedy))
                pre_sum.append(pre_sum[-1] + greedy[-1])

        n, res = len(greedy), float("inf")
        for i in range(n - k + 1):
            mid = i + k // 2
            r = greedy[mid]
            res = min(res, (1 - k % 2) * r + (pre_sum[i + k] - pre_sum[mid + 1]) - (pre_sum[mid] - pre_sum[i]))

        return res


def main():
    # Example 1: Output: 1
    nums = [1, 0, 0, 1, 0, 1]
    k = 2

    # Example 2: Output: 5
    # nums = [1, 0, 0, 0, 0, 0, 1, 1]
    # k = 3

    # Example 3: Output: 0
    # nums = [1, 1, 0, 1]
    # k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minMoves(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
