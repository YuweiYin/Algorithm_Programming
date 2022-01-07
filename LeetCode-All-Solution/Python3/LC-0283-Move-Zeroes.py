#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0283-Move-Zeroes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-03
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0283 - (Easy) - Move Zeroes
https://leetcode.com/problems/move-zeroes/

Description:
    Given an integer array nums, move all 0's to the end of it 
    while maintaining the relative order of the non-zero elements.

Requirement:
    Note that you must do this in-place without making a copy of the array.

Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
Example 2:
    Input: nums = [0]
    Output: [0]

Constraints:
    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # exception case
        if not isinstance(nums, list) or len(nums) <= 1:
            return
        # main method: (two pointer)
        # zero_ptr find the leftmost zero,
        # while non_z_ptr find every non-zero num on the right or zero_ptr
        self._moveZeroes(nums)

    def _moveZeroes(self, nums: List[int]) -> None:
        len_num = len(nums)
        zero_ptr = 0
        while zero_ptr < len_num:
            if nums[zero_ptr] == 0:  # find the leftmost zero,
                break
            else:
                zero_ptr += 1
        if zero_ptr == len_num:
            return  # there's no zero in the whole list

        non_z_ptr = zero_ptr + 1  # find every non-zero num on the right or zero_ptr
        while non_z_ptr < len_num:
            if nums[non_z_ptr] != 0:
                self._swap_list_item_in_place(nums, zero_ptr, non_z_ptr)
                zero_ptr += 1  # the next number must be 0 (zero_ptr is slow pointer)
            non_z_ptr += 1  # non_z_ptr is fast pointer that will first reach the end of the list
        # assert non_z_ptr == len_num  # there's no non-zero num on the right of zero_ptr (also: all 0 are in the end)

    @staticmethod
    def _swap_list_item_in_place(nums: List[int], x_index: int, y_index: int) -> None:
        temp_num = nums[x_index]
        nums[x_index] = nums[y_index]
        nums[y_index] = temp_num


def main():
    # Example 1: Output: [1,3,12,0,0]
    # nums = [0, 1, 0, 3, 12]

    # Example 2: Output: [0]
    nums = [0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.moveZeroes(nums)
    ans = nums
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
