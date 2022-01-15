#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0153-Find-Minimum-in-Rotated-Sorted-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-15
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0153 - (Medium) - Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Description & Requirement:
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
    For example, the array nums = [0,1,2,4,5,6,7] might become:
        [4,5,6,7,0,1,2] if it was rotated 4 times.
        [0,1,2,4,5,6,7] if it was rotated 7 times.
    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results 
    in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

    Given the sorted rotated array nums of unique elements, 
    return the minimum element of this array.

    You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [3,4,5,1,2]
    Output: 1
    Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:
    Input: nums = [4,5,6,7,0,1,2]
    Output: 0
    Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:
    Input: nums = [11,13,15,17]
    Output: 11
    Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

Constraints:
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
    nums is sorted and rotated between 1 and n times.
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return -1  # Error input type
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        # main method: (Binary Search find the rotated position)
        return self._findMin(nums)

    def _findMin(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums > 2

        INF = sys.maxsize

        def __binary_search_find_pivot(left_idx: int, right_idx: int):
            if left_idx > right_idx:
                return INF

            mid_idx = (left_idx + right_idx) >> 1
            mid_num = nums[mid_idx]
            if nums[left_idx] <= mid_num:  # the left part is ascending (it means the right part maybe rotated)
                # consider the min in the left part, i.e., nums[left_idx], then go to the right part
                return min(nums[left_idx], __binary_search_find_pivot(mid_idx + 1, right_idx))
            else:  # the right part is ascending (it means the left part maybe rotated)
                # consider the min in the right part, i.e., mid_num, then go to the left part
                return min(mid_num, __binary_search_find_pivot(left_idx, mid_idx - 1))

        res = __binary_search_find_pivot(0, len_nums - 1)
        return res


def main():
    # Example 1: Output: 1
    # nums = [3, 4, 5, 1, 2]

    # Example 2: Output: 0
    nums = [4, 5, 6, 7, 0, 1, 2]

    # Example 3: Output: 11
    # nums = [11, 13, 15, 17]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findMin(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
