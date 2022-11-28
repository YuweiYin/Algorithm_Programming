#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1752-Check-if-Array-Is-Sorted-and-Rotated.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-27
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1752 - (Easy) - Check if Array Is Sorted and Rotated
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

Description & Requirement:
    Given an array nums, return true if the array was originally sorted in non-decreasing order, 
    then rotated some number of positions (including zero). Otherwise, return false.

    There may be duplicates in the original array.

    Note: An array A rotated by x positions results in an array B of the same length such that 
    A[i] == B[(i+x) % A.length], where % is the modulo operation.

Example 1:
    Input: nums = [3,4,5,1,2]
    Output: true
    Explanation: [1,2,3,4,5] is the original sorted array.
        You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:
    Input: nums = [2,1,3,4]
    Output: false
    Explanation: There is no sorted array once rotated that can make nums.
Example 3:
    Input: nums = [1,2,3]
    Output: true
    Explanation: [1,2,3] is the original sorted array.
        You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100
"""


class Solution:
    def check(self, nums: List[int]) -> bool:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        for num in nums:
            assert isinstance(num, int) and num >= 1
        # main method: (scan the array)
        return self._check(nums)

    def _check(self, nums: List[int]) -> bool:
        assert isinstance(nums, list) and len(nums) >= 1
        n = len(nums)

        d_idx = 0  # find the first descending number
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                d_idx = i
                break

        if d_idx == 0:
            return True

        for i in range(d_idx + 1, n):
            if nums[i] < nums[i - 1]:
                return False

        return nums[0] >= nums[-1]


def main():
    # Example 1: Output: true
    nums = [3, 4, 5, 1, 2]

    # Example 2: Output: false
    # nums = [2, 1, 3, 4]

    # Example 3: Output: true
    # nums = [1, 2, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.check(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
