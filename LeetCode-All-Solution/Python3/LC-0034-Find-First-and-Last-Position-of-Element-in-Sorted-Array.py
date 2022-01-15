#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0034-Find-First-and-Last-Position-of-Element-in-Sorted-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-15
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0034 - (Medium) - Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Description & Requirement:
    Given an array of integers nums sorted in non-decreasing order, 
    find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]

Constraints:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    nums is a non-decreasing array.
    -10^9 <= target <= 10^9
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return [-1, -1]  # Error input type
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        # main method: (Binary search)
        # return self._searchRange(nums, target)
        return self._searchRangeAllBinarySearch(nums, target)

    def _searchRange(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        assert len_nums > 1

        def __binary_search(left_idx: int, right_idx: int):
            if left_idx > right_idx:
                return -1

            mid_idx = (left_idx + right_idx) >> 1
            mid_num = nums[mid_idx]
            if target == mid_num:  # bingo
                return mid_idx
            elif target < mid_num:  # go left
                return __binary_search(left_idx, mid_idx - 1)
            else:  # go right
                return __binary_search(mid_idx + 1, right_idx)

        find_idx = __binary_search(0, len_nums - 1)
        if find_idx < 0 or find_idx >= len_nums:  # can't find target
            return [-1, -1]
        # O(n): scan towards left, find the left boundary
        if nums[0] == target:
            left_boundary = 0
        else:
            left_boundary = find_idx
            while left_boundary > 0 and nums[left_boundary] == target:
                left_boundary -= 1
            left_boundary += 1
        # O(n): scan towards right, find the right boundary
        if nums[len_nums - 1] == target:
            right_boundary = len_nums - 1
        else:
            right_boundary = find_idx
            while right_boundary < len_nums and nums[right_boundary] == target:
                right_boundary += 1
            right_boundary -= 1
        return [left_boundary, right_boundary]

    def _searchRangeAllBinarySearch(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        assert len_nums > 1

        def __binary_search(left_idx: int, right_idx: int):
            if left_idx > right_idx:
                return -1

            mid_idx = (left_idx + right_idx) >> 1
            mid_num = nums[mid_idx]
            if target == mid_num:  # bingo
                return mid_idx
            elif target < mid_num:  # go left
                return __binary_search(left_idx, mid_idx - 1)
            else:  # go right
                return __binary_search(mid_idx + 1, right_idx)

        def __binary_search_less_than_target(left_idx: int, right_idx: int):
            if left_idx > right_idx:
                return -1

            mid_idx = (left_idx + right_idx) >> 1
            mid_num = nums[mid_idx]
            if target == mid_num:
                if mid_idx == 0:
                    return 0
                else:  # assert mid_idx > 0
                    if nums[mid_idx - 1] < target:  # find the lesser one
                        return mid_idx
                    else:  # keep searching left
                        return __binary_search_less_than_target(left_idx, mid_idx - 1)
            elif mid_num > target:  # go left
                return __binary_search_less_than_target(left_idx, mid_idx - 1)
            else:  # go right
                if mid_idx == len_nums - 1:
                    return -1  # can't find the lesser one
                else:
                    if nums[mid_idx + 1] == target:  # find the lesser one
                        return mid_idx + 1
                    else:
                        return __binary_search_less_than_target(mid_idx + 1, right_idx)

        def __binary_search_greater_than_target(left_idx: int, right_idx: int):
            if left_idx > right_idx:
                return -1

            mid_idx = (left_idx + right_idx) >> 1
            mid_num = nums[mid_idx]
            if target == mid_num:
                if mid_idx == len_nums - 1:
                    return len_nums - 1
                else:  # assert mid_idx < len_nums - 1
                    if nums[mid_idx + 1] > target:  # find the greater one
                        return mid_idx
                    else:  # keep searching right
                        return __binary_search_greater_than_target(mid_idx + 1, right_idx)
            elif mid_num > target:  # go left
                if mid_idx == 0:
                    return -1  # can't find the greater one
                else:
                    if nums[mid_idx - 1] == target:  # find the greater one
                        return mid_idx - 1
                    else:
                        return __binary_search_greater_than_target(left_idx, mid_idx - 1)
            else:  # go right
                return __binary_search_greater_than_target(mid_idx + 1, right_idx)

        find_idx = __binary_search(0, len_nums - 1)
        if find_idx < 0 or find_idx >= len_nums:  # can't find target
            return [-1, -1]
        # O(lg n): binary search find the left boundary
        if nums[0] == target:
            left_boundary = 0
        else:
            left_boundary = __binary_search_less_than_target(0, find_idx)
            if left_boundary < 0:
                left_boundary = find_idx
        # O(lg n): binary search find the right boundary
        if nums[len_nums - 1] == target:
            right_boundary = len_nums - 1
        else:
            right_boundary = __binary_search_greater_than_target(find_idx, len_nums)
            if right_boundary < 0:
                right_boundary = find_idx
        return [left_boundary, right_boundary]


def main():
    # Example 1: Output: [3,4]
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8

    # Example 2: Output: [-1,-1]
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 6

    # Example 3: Output: [-1,-1]
    # nums = []
    # target = 0

    # Example 4: Output: [0,1]
    # nums = [2, 2]
    # target = 2

    # Example 5: Output: [10,13]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 8, 10, 10]
    target = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.searchRange(nums, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
