#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0198-House-Robber.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-12
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0198 - (Medium) - House Robber
https://leetcode.com/problems/house-robber/

Description:
    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, 
    the only constraint stopping you from robbing each of them is that 
    adjacent houses have security systems connected and it will automatically contact the police 
    if two adjacent houses were broken into on the same night.

Requirement:
    Given an integer array nums representing the amount of money of each house, 
    return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.
Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
        Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 400
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] if nums[0] >= nums[1] else nums[1]
        # main method: (1. one-dimension dynamic programming  2. dfs & backtrack)
        #     dp equation: dp[i] = max((nums[i] + pre_max), cur_max)  i = 0, 1, 2, ..., max_len-1
        #     explanation: when reach i, cur_max is max(dp[0, ..., i-1]) and pre_max is max(dp[0, ..., i-2])
        #         only pre_max can + nums[i], because cannot rob adjacent houses.
        return self._rob(nums)

    def _rob(self, nums: List[int]) -> int:
        len_nums = len(nums)

        pre_max = 0
        cur_max = 0

        for cur_house in range(len_nums):
            temp = cur_max  # record cur_max as pre_max at next step
            cur_max = max(pre_max + nums[cur_house], cur_max)  # update cur_max
            pre_max = temp  # update pre_max

        return cur_max


def main():
    # Example 1: Output: 4
    # nums = [1, 2, 3, 1]

    # Example 2: Output: 12
    # nums = [2, 7, 9, 3, 1]

    # Example 3: Output: 4
    nums = [2, 1, 1, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.rob(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
