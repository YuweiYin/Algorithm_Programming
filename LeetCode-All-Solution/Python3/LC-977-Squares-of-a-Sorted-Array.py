#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-977-Squares-of-a-Sorted-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-02
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 977 - (Easy) - Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

Description:
    Given an integer array nums sorted in non-decreasing order, 
    return an array of the squares of each number sorted in non-decreasing order.

Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].
Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.

Follow up:
    Squaring each element and sorting the new array is very trivial, 
    could you find an O(n) solution using a different approach?
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # exception case
        if not isinstance(nums, list) or len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums[0] * nums[0]]
        # main method: (loop) binary search of sorted list
        return self._sortedSquares(nums)

    def _sortedSquares(self, nums: List[int]) -> List[int]:
        start_index, end_index = 0, len(nums) - 1  # double pointers, moving from two ends until meeting each other
        res_list = []  # the bigger number, the latter position
        # (Inserting items in the first position in an array list is much more time-consuming than append in the end)
        # (So I use append method and at last apply a whole list reverse)
        while start_index < end_index:
            start_num, end_num = nums[start_index], nums[end_index]  # cache variable
            if abs(start_num) < abs(end_num):
                res_list.append(end_num * end_num)  # append the bigger one into the res_list
                end_index -= 1  # move closer to start_index
            else:
                res_list.append(start_num * start_num)  # append the bigger one into the res_list
                start_index += 1  # move closer to end_index
            cur_index = (end_index + start_index) >> 1  # current cursor
            cur_num = nums[cur_index]  # cache variable
        if start_index == end_index:  # this must be true, but for robustness
            res_list.append(nums[start_index] * nums[start_index])
        res_list.reverse()  # apply a whole list reverse
        return res_list


def main():
    # Example 1: Output: [0,1,9,16,100]
    nums = [-4, -1, 0, 3, 10]

    # Example 2: Output: [4,9,9,49,121]
    # nums = [-7, -3, 2, 3, 11]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sortedSquares(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
