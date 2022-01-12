#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0334-Increasing-Triplet-Subsequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-12
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0334 - (Medium) - Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/

Description & Requirement:
    Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
    such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.
Example 2:
    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.
Example 3:
    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
    1 <= nums.length <= 5 * 10^5
    -2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 2:
            return False  # Error input type
        if len(nums) == 3:
            return True if (nums[0] < nums[1] < nums[2]) else False
        # main method: (1. one-dimension dynamic programming  2. dfs & backtrack / greedy search)
        return self._increasingTriplet(nums)

    def _increasingTriplet(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        assert len_nums > 3

        INF = sys.maxsize
        triplet_first = nums[0]  # the first number in target triplet
        triplet_second = INF  # the second number in target triplet (not find yet, so default INF)

        cur_index = 1
        while cur_index < len_nums:
            cur_num = nums[cur_index]
            if cur_num > triplet_second:
                return True  # triplet_first < triplet_second < cur_num
            else:
                if cur_num > triplet_first:  # this means: triplet_first < cur_num <= triplet_second
                    triplet_second = cur_num  # find the second one
                else:  # this means: cur_num <= triplet_second and cur_num <= triplet_first
                    triplet_first = cur_num  # keep triplet_first is a small one
                    # take nums = [5, 6, 0, 7] as an example:
                    # cur_index == 1: cur_num = 6, first = 5, second = 6
                    # cur_index == 2: cur_num = 0, first = 0, second = 6
                    # cur_index == 3: cur_num = 7, first = 0, second = 6, bingo!
                    #     kinda wierd because the sequence should not be [0, 6, 7] but [5, 6, 7]
                    #     but this problem do not need to record the sequence, so this method is correct
                    #     plus, if num[3] == 2, then cur_index == 3: cur_num = 2, first = 0, second = 2
                    #         then the "?" in triplet [0, 2, ?] is searched in the rest numbers nums[4:]
            cur_index += 1

        return False


def main():
    # Example 1: Output: true
    # nums = [1, 7, 3, 4]

    # Example 2: Output: false
    # nums = [5, 4, 3, 2, 1]

    # Example 3: Output: true
    # nums = [2, 1, 5, 0, 4, 6]

    # Example 4: Output: false
    nums = [5, 6, 0, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.increasingTriplet(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
