#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0081-Search-in-Rotated-Sorted-Array-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-28
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0081 - (Medium) - Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

Description & Requirement:
    There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

    Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) 
    such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
    For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

    Given the array nums after the rotation and an integer target, 
    return true if target is in nums, or false if it is not in nums.

    You must decrease the overall operation steps as much as possible.

Example 1:
    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true
Example 2:
    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: false

Constraints:
    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    nums is guaranteed to be rotated at some pivot.
    -10^4 <= target <= 10^4

Follow up:
    This problem is similar to Search in Rotated Sorted Array, 
    https://leetcode.com/problems/search-in-rotated-sorted-array/description/
    but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return False  # Error input type
        if len(nums) == 1:
            return nums[0] == target
        elif len(nums) == 2:
            return nums[0] == target or nums[1] == target
        # main method: (Binary search)
        return self._search(nums, target)

    def _search(self, nums: List[int], target: int) -> bool:
        """
        Runtime: 55 ms, faster than 89.28% of Python3 online submissions for Search in Rotated Sorted Array II.
        Memory Usage: 15 MB, less than 5.13% of Python3 online submissions for Search in Rotated Sorted Array II.
        """
        len_nums = len(nums)
        assert len_nums >= 3

        def __binary_search_rotated(left_idx: int, right_idx: int):
            if left_idx > right_idx:
                return -1

            mid_idx = (left_idx + right_idx) >> 1
            mid_num = nums[mid_idx]
            if target == mid_num:  # bingo
                return mid_idx
            if nums[left_idx] == nums[mid_idx]:  # can't tell the rotation point is left or right
                left_res = __binary_search_rotated(left_idx, mid_idx - 1)
                if 0 <= left_res < len_nums:
                    return left_res
                right_res = __binary_search_rotated(mid_idx + 1, right_idx)
                if 0 <= right_res < len_nums:
                    return right_res
                return -1
            elif nums[left_idx] < nums[mid_idx]:  # the left part is ascending (it means the right part maybe rotated)
                if nums[left_idx] <= target < nums[mid_idx]:  # if target is in there, go to the left part
                    return __binary_search_rotated(left_idx, mid_idx - 1)
                else:  # else, go to the right part
                    return __binary_search_rotated(mid_idx + 1, right_idx)
            else:  # the right part is ascending (it means the left part maybe rotated)
                if nums[mid_idx] < target <= nums[len_nums - 1]:  # if target is in there, go to the right part
                    return __binary_search_rotated(mid_idx + 1, right_idx)
                else:  # else, go to the left part
                    return __binary_search_rotated(left_idx, mid_idx - 1)

        return 0 <= __binary_search_rotated(0, len_nums - 1) < len_nums


def main():
    # Example 1: Output: true
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0

    # Example 2: Output: false
    # nums = [2, 5, 6, 0, 0, 1, 2]
    # target = 3

    # Example 3: Output: true
    # nums = [1, 0, 1, 1, 1]
    # target = 0

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
