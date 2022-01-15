#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0033-Search-in-Rotated-Sorted-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-15
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0033 - (Medium) - Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

Description & Requirement:
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated 
    at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is 
    [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target, 
    return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
Example 3:
    Input: nums = [1], target = 0
    Output: -1

Constraints:
    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -10^4 <= target <= 10^4
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return -1  # Error input type
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        elif len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1
        # main method: (Binary search)
        return self._search(nums, target)

    def _search(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        assert len_nums > 2

        def __binary_search_rotated(left_idx: int, right_idx: int):
            if left_idx > right_idx:
                return -1

            mid_idx = (left_idx + right_idx) >> 1
            mid_num = nums[mid_idx]
            if target == mid_num:  # bingo
                return mid_idx
            if nums[left_idx] <= nums[mid_idx]:  # the left part is ascending (it means the right part maybe rotated)
                if nums[left_idx] <= target < nums[mid_idx]:  # if target is in there, go to the left part
                    return __binary_search_rotated(left_idx, mid_idx - 1)
                else:  # else, go to the right part
                    return __binary_search_rotated(mid_idx + 1, right_idx)
            else:  # the right part is ascending (it means the left part maybe rotated)
                if nums[mid_idx] < target <= nums[len_nums - 1]:  # if target is in there, go to the right part
                    return __binary_search_rotated(mid_idx + 1, right_idx)
                else:  # else, go to the left part
                    return __binary_search_rotated(left_idx, mid_idx - 1)

        return __binary_search_rotated(0, len_nums - 1)


def main():
    # Example 1: Output: 4
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 0

    # Example 2: Output: -1
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 3

    # Example 3: Output: -1
    # nums = [1]
    # target = 0

    # Example 4: Output: 0
    # nums = [5, 1, 3]
    # target = 5

    # Example 5: Output: 4
    nums = [4, 5, 6, 7, 8, 1, 2, 3]
    target = 8

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.search(nums, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
