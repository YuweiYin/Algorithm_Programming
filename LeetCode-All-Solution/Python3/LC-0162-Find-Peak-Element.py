#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0162-Find-Peak-Element.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-15
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0162 - (Medium) - Find Peak Element
https://leetcode.com/problems/find-peak-element/

Description & Requirement:
    A peak element is an element that is strictly greater than its neighbors.

    Given an integer array nums, find a peak element, and return its index. 
    If the array contains multiple peaks, return the index to any of the peaks.

    You may imagine that nums[-1] = nums[n] = -∞.
    You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:
    Input: nums = [1,2,1,3,5,6,4]
    Output: 5
    Explanation: Your function can return either index number 1 where the peak element is 2, 
        or index number 5 where the peak element is 6.

Constraints:
    1 <= nums.length <= 1000
    -2^31 <= nums[i] <= 2^31 - 1
    nums[i] != nums[i + 1] for all valid i.
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        # main method: (Binary Search)
        #     idea: each time, either go left or go right, depending on nums[i] > nums[i+1] or nums[i] > nums[i-1]
        return self._findPeakElement(nums)

    def _findPeakElement(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums > 2

        INF = sys.maxsize

        def __binary_search_find_peak(left_idx: int, right_idx: int):
            if left_idx > right_idx:
                return INF  # not a peak

            mid_idx = (left_idx + right_idx) >> 1
            mid_num = nums[mid_idx]
            if mid_idx == 0:  # at the leftmost position (can only go right)
                if mid_num > nums[mid_idx + 1]:
                    return mid_idx  # this is a peak
                else:
                    return __binary_search_find_peak(mid_idx + 1, right_idx)
            elif mid_idx == len_nums - 1:  # at the rightmost position (can only go left)
                if mid_num > nums[mid_idx - 1]:
                    return mid_idx  # this is a peak
                else:
                    return __binary_search_find_peak(left_idx, mid_idx - 1)
            elif nums[mid_idx - 1] < mid_num and nums[mid_idx + 1] < mid_num:
                return mid_idx  # this is a peak
            elif mid_num < nums[mid_idx - 1]:  # go left, because left is higher
                return __binary_search_find_peak(left_idx, mid_idx - 1)
            elif mid_num < nums[mid_idx + 1]:  # go right, because right is higher
                return __binary_search_find_peak(mid_idx + 1, right_idx)
            else:  # mid_num == nums[mid_idx - 1] or mid_num == nums[mid_idx + 1], Error input type
                return INF  # Error input type: not a peak

        res = __binary_search_find_peak(0, len_nums - 1)
        return res  # default -1: can't find a peak element


def main():
    # Example 1: Output: 2
    nums = [1, 2, 3, 1]

    # Example 2: Output: 5
    # nums = [1, 2, 1, 3, 5, 6, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findPeakElement(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
