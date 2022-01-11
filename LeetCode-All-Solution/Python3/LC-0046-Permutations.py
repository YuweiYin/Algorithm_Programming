#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0046-Permutations.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-11
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0046 - (Medium) - Permutations
https://leetcode.com/problems/permutations/

Description & Requirement:
    Given an array nums of distinct integers, return all the possible permutations. 
    You can return the answer in any order.

Example 1:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
    Input: nums = [0,1]
    Output: [[0,1],[1,0]]
Example 3:
    Input: nums = [1]
    Output: [[1]]

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return []  # Error input type
        if len(nums) == 1:
            return [nums]
        elif len(nums) == 2:
            return [nums] if nums[0] == nums[1] else [nums, [nums[1], nums[0]]]
        # main method: (dfs & backtrack)
        return self._permute(nums)

    def _permute(self, nums: List[int]) -> List[List[int]]:
        res_permute = []  # stack
        len_nums = len(nums)

        def __dfs(cur_permute: List[int], cur_used: List[bool], cur_index: int):
            if len(cur_permute) == len_nums:  # end of recursion
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
    # Example 1: Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    # nums = [1, 2, 3]

    # Example 2: Output: [[0,1],[1,0]]
    # nums = [0, 1]

    # Example 3: Output: [[1]]
    # nums = [1]

    # Example 4: Output:
    nums = [1, 2, 3, 4, 5, 6]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.permute(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
