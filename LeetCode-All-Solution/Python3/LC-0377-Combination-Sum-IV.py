#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0377-Combination-Sum-IV.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-24
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0377 - (Medium) - Combination Sum IV
https://leetcode.com/problems/combination-sum-iv/

Description & Requirement:
    Given an array of distinct integers nums and a target integer target, 
    return the number of possible combinations that add up to target.

    The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:
    Input: nums = [1,2,3], target = 4
    Output: 7
    Explanation:
        The possible combination ways are:
        (1, 1, 1, 1)
        (1, 1, 2)
        (1, 2, 1)
        (1, 3)
        (2, 1, 1)
        (2, 2)
        (3, 1)
        Note that different sequences are counted as different combinations.
Example 2:
    Input: nums = [9], target = 3
    Output: 0

Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= 1000
    All the elements of nums are unique.
    1 <= target <= 1000

Related Problem:
    LC-0039-Combination-Sum
    LC-0040-Combination-Sum-II
    LC-0216-Combination-Sum-III
    LC-0377-Combination-Sum-IV
    LC-0518-Coin-Change-2
"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) > 0 and isinstance(target, int) and target > 0
        # main method: (1. sort & dfs & backtrace.)
        # return self._combinationSum4Dfs(nums, target)
        # method 2: Dynamic Programming
        #     dp[i] is the number of possible combinations that add up to i
        #     dp equation: dp[i] = sum(dp[i-j]) where j is a number in nums and i >= j
        #     dp init: dp[0] = 1, other elements in dp table is 0
        #     dp aim: get dp[-1]
        return self._combinationSum4Dp(nums, target)

    def _combinationSum4Dfs(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        assert len_nums > 0

        # res_list = []
        res = [0]
        dup_set = set()  # to avoid duplication

        nums.sort()  # more easily to find duplication

        def __dfs(cur_combo: List[int], cur_sum: int, cur_num_index: int):
            if cur_num_index >= len_nums or cur_sum > target:
                return
            cur_combo.append(nums[cur_num_index])
            cur_sum += nums[cur_num_index]
            if cur_sum > target:
                return
            if cur_sum == target:
                if tuple(cur_combo) not in dup_set:
                    dup_set.add(tuple(cur_combo))
                    # res_list.append(cur_combo[:])
                    res[0] += 1
            for next_num_index in range(len_nums):  # explore more numbers
                __dfs(cur_combo, cur_sum, next_num_index)  # go deeper
                cur_combo.pop()  # backtrace

        for start_num_index in range(len_nums):  # start from every number
            __dfs([], 0, start_num_index)

        # print(res_list)
        # return len(res_list)
        return res[0]

    def _combinationSum4Dp(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        assert len_nums > 0

        nums.sort()  # more easily to find duplication

        # dp[i] is the number of possible combinations that add up to i
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1  # dp init: dp[0] = 1, other elements in dp table is 0

        for i in range(1, target + 1):
            # note that one number can be repeatedly used
            for j in nums:
                if i >= j:
                    # accumulate dp[i], there are more combination to make up the current target i
                    # dp equation: dp[i] = sum(dp[i-j]) where j is a number in nums and i >= j
                    dp[i] += dp[i - j]

        # dp aim: get dp[-1]
        # print(dp)
        return dp[-1]


def main():
    # Example 1: Output: 7
    nums = [1, 2, 3]
    target = 4

    # Example 2: Output: 0
    # nums = [9]
    # target = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.combinationSum4(nums, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
