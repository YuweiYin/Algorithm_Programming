#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0213-House-Robber-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-25
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0213 - (Medium) - House Robber II
https://leetcode.com/problems/house-robber-ii/

Description & Requirement:
    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
    That means the first house is the neighbor of the last one. 
    Meanwhile, adjacent houses have a security system connected, 
    and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, 
    return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.
Example 3:
    Input: nums = [1,2,3]
    Output: 3

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) <= 3:
            return max(nums)
        # main method: (1. one-dimension dynamic programming  2. dfs & backtrack)
        #     dp equation: dp[i] = max((nums[i] + pre_max), cur_max)  i = 0, 1, 2, ..., max_len-1
        #     explanation: when reach i, cur_max is max(dp[0, ..., i-1]) and pre_max is max(dp[0, ..., i-2])
        #         only pre_max can + nums[i], because cannot rob adjacent houses.
        # because the houses form a cycle, robber can't rob both the first house and the last house
        # so apply DP algorithm on nums[0: -1] and num[1: ], then choose the bigger result
        return self._rob(nums)

    def _rob(self, nums: List[int]) -> int:
        """
        Runtime: 32 ms, faster than 76.38% of Python3 online submissions for House Robber II.
        Memory Usage: 14 MB, less than 93.68% of Python3 online submissions for House Robber II.
        """
        len_nums = len(nums)
        assert len_nums > 3

        def __do_dp(cur_nums: List[int]) -> int:
            pre_max = 0
            cur_max = 0

            for cur_house in range(len(cur_nums)):
                temp = cur_max  # record cur_max as pre_max at next step
                cur_max = max(pre_max + cur_nums[cur_house], cur_max)  # update cur_max
                pre_max = temp  # update pre_max
            return cur_max

        res_rob_first = __do_dp(nums[0: -1])  # can rob the first house, but cannot rob the last house
        res_not_rob_first = __do_dp(nums[1:])  # cannot rob the first house, but can rob the last house

        return max(res_rob_first, res_not_rob_first)


def main():
    # Example 1: Output: 3
    # nums = [2, 3, 2]

    # Example 2: Output: 4
    nums = [1, 2, 3, 1]

    # Example 3: Output: 3
    # nums = [1, 2, 3]

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
