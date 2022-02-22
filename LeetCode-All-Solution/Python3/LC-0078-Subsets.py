#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0078-Subsets.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-22
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0078 - (Medium) - Subsets
https://leetcode.com/problems/subsets/

Description & Requirement:
    Given an integer array nums of unique elements, 
    return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. 
    Return the solution in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:
    Input: nums = [0]
    Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return [[]] # Error input type
        if len(nums) == 1:
            return [[], nums]
        # main method: (dfs & backtrace.)
        return self._subsets(nums)

    def _subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Runtime: 32 ms, faster than 87.17% of Python3 online submissions for Subsets.
        Memory Usage: 14.4 MB, less than 78.39% of Python3 online submissions for Subsets.
        """
        len_nums = len(nums)
        assert len_nums > 1

        res_list = [[]]  # [] must be a subset

        def __dfs(cur_subset: List[int], cur_num_index: int):
            if cur_num_index >= len_nums:
                return
            cur_subset.append(nums[cur_num_index])
            res_list.append(cur_subset[:])  # new res
            for next_num_index in range(cur_num_index + 1, len_nums):  # explore all left numbers
                __dfs(cur_subset, next_num_index)  # go deeper
            cur_subset.pop()  # backtrace

        for start_num_index in range(len_nums):  # start from every number
            __dfs([], start_num_index)
        return res_list


def main():
    # Example 1: Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    nums = [1, 2, 3]

    # Example 2: Output: [[],[0]]
    # nums = [0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.subsets(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
