#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1984-Minimum-Difference-Between-Highest-and-Lowest-of-K-Scores.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-11
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1984 - (Easy) - Minimum Difference Between Highest and Lowest of K Scores
https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

Description & Requirement:
    You are given a 0-indexed integer array nums, 
    where nums[i] represents the score of the ith student. 
    You are also given an integer k.

    Pick the scores of any k students from the array so that 
    the difference between the highest and the lowest of the k scores is minimized.

    Return the minimum possible difference.

Example 1:
    Input: nums = [90], k = 1
    Output: 0
    Explanation: There is one way to pick score(s) of one student:
        - [90]. The difference between the highest and lowest score is 90 - 90 = 0.
        The minimum possible difference is 0.
Example 2:
    Input: nums = [9,4,1,7], k = 2
    Output: 2
    Explanation: There are six ways to pick score(s) of two students:
        - [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
        - [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
        - [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
        - [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
        - [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
        - [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
        The minimum possible difference is 2.

Constraints:
    1 <= k <= nums.length <= 1000
    0 <= nums[i] <= 10^5
"""


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        assert isinstance(k, int) and k >= 1
        if len(nums) == 1 or k == 1:
            return 0
        # main method: (sort, then the min diff interval must be a contiguous subarray of the sorted nums list, scan it)
        return self._minimumDifference(nums, k)

    def _minimumDifference(self, nums: List[int], k: int) -> int:
        len_nums = len(nums)
        assert len_nums >= 2

        nums.sort()
        res = nums[-1] - nums[0]  # max diff possible

        interval_start = 0
        max_interval_start = len_nums - k
        # the min diff interval must be a contiguous subarray of the sorted nums list, scan it
        while interval_start <= max_interval_start:
            cur_diff = nums[interval_start + k - 1] - nums[interval_start]
            res = min(res, cur_diff)
            interval_start += 1

        return res


def main():
    # Example 1: Output: 0
    # nums = [90]
    # k = 1

    # Example 2: Output: 2
    nums = [9, 4, 1, 7]
    k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumDifference(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
