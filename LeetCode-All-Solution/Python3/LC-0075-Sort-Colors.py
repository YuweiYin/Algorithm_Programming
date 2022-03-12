#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0075-Sort-Colors.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-12
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0075 - (Medium) - Sort Colors
https://leetcode.com/problems/sort-colors/

Description & Requirement:
    Given an array nums with n objects colored red, white, or blue, 
    sort them in-place so that objects of the same color are adjacent, 
    with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.

Example 1:
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
Example 2:
    Input: nums = [2,0,1]
    Output: [0,1,2]

Constraints:
    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # exception case
        assert isinstance(nums, list) and len(nums) > 0
        # method: (1. hash dict record color counter; 2. scan twice: swap all 0 to the front, swap all 2 to the end)
        self._sortColors(nums)

    def _sortColors(self, nums: List[int]) -> None:
        len_nums = len(nums)
        assert len_nums > 0

        color_dict = dict({0: 0, 1: 0, 2: 0})  # key: color (0/1/2); value: counter of this color
        for num in nums:  # get color counter
            if num in color_dict:
                color_dict[num] += 1

        # modify nums
        cur_color = 0
        idx = 0
        while idx < len_nums:
            if cur_color in color_dict:
                while color_dict[cur_color] > 0:
                    color_dict[cur_color] -= 1
                    nums[idx] = cur_color
                    idx += 1
                cur_color += 1
            else:
                break


def main():
    # Example 1: Output: [0,0,1,1,2,2]
    nums = [2, 0, 2, 1, 1, 0]

    # Example 2: Output: [0,1,2]
    # nums = [2, 0, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.sortColors(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(nums)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
