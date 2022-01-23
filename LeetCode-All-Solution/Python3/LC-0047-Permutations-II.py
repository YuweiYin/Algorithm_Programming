#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0047-Permutations-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-23
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0047 - (Medium) - Permutations II
https://leetcode.com/problems/permutations-ii/

Description & Requirement:
    Given a collection of numbers, nums, that might contain duplicates, 
    return all possible unique permutations in any order.

Example 1:
    Input: nums = [1,1,2]
    Output:
    [[1,1,2],
     [1,2,1],
     [2,1,1]]
Example 2:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
    1 <= nums.length <= 8
    -10 <= nums[i] <= 10
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return []  # Error input type
        if len(nums) == 1:
            return [nums]
        elif len(nums) == 2:
            return [nums] if nums[0] == nums[1] else [nums, [nums[1], nums[0]]]
        # main method: (dfs & backtrack) optimize: sort nums, and avoid dfs choose adjacent same number (skip)
        return self._permuteUnique(nums)

    def _permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res_permute = []  # stack
        len_nums = len(nums)
        dup_set = set()  # to avoid duplication

        def __dfs(cur_permute: List[int], cur_used: List[bool], cur_index: int):
            if len(cur_permute) == len_nums:  # end of recursion
                if tuple(cur_permute) not in dup_set:  # avoid duplication
                    dup_set.add(tuple(cur_permute))
                    res_permute.append(cur_permute[:])
                return

            for num_index in range(0, len_nums):
                if not cur_used[num_index]:  # only consider those unused numbers
                    cur_permute.append(nums[num_index])  # move on
                    cur_used[num_index] = True  # record: lock this number
                    __dfs(cur_permute, cur_used, num_index + 1)  # dfs
                    cur_permute.pop()  # backtrack
                    cur_used[num_index] = False  # release this number

        permute = []
        used = [False for _ in range(len_nums)]  # used[i] == True means nums[i] has been considered
        start_index = 0
        __dfs(permute, used, start_index)

        return res_permute


def main():
    # Example 1: Output: [
    #     [1,1,2],
    #     [1,2,1],
    #     [2,1,1]
    # ]
    nums = [1, 1, 2]

    # Example 2: Output: [
    #     [1,2,3],
    #     [1,3,2],
    #     [2,1,3],
    #     [2,3,1],
    #     [3,1,2],
    #     [3,2,1]
    # ]
    # nums = [1, 2, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.permuteUnique(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
