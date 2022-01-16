#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0015-3Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-16
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0015 - (Medium) - 3Sum
https://leetcode.com/problems/3sum/

Description & Requirement:
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
Example 2:
    Input: nums = []
    Output: []
Example 3:
    Input: nums = [0]
    Output: []

Constraints:
    0 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 2:
            return []
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
        # main method: (sort + 2Sum (two pointers))
        return self._threeSum(nums)

    def _threeSum(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        assert len_nums > 3

        res = []
        nums.sort()

        for first_index in range(len_nums):
            if first_index > 0 and nums[first_index] == nums[first_index - 1]:
                continue  # skip adjacent same number

            third_index = len_nums - 1  # set the third number as the last one
            two_sum = 0 - nums[first_index]  # the target sum of the second number and the third number

            # scan search all valid second number
            for second_index in range(first_index + 1, len_nums):
                if second_index > first_index + 1 and nums[second_index] == nums[second_index - 1]:
                    continue  # skip adjacent same number
                while second_index < third_index and nums[second_index] + nums[third_index] > two_sum:
                    third_index -= 1  # move third index till nums[second_index] + nums[third_index] <= two_sum
                if second_index >= third_index:
                    break  # pointer cross, break
                if nums[second_index] + nums[third_index] == two_sum:  # find a valid combo
                    res.append([nums[first_index], nums[second_index], nums[third_index]])

        return res


def main():
    # Example 1: Output: [[-1,-1,2],[-1,0,1]]
    nums = [-1, 0, 1, 2, -1, -4]

    # Example 2: Output: []
    # nums = []

    # Example 3: Output: []
    # nums = [0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.threeSum(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
