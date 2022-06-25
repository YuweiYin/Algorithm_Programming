#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0665-Non-decreasing-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-25
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0665 - (Medium) - Non-decreasing Array
https://leetcode.com/problems/non-decreasing-array/

Description & Requirement:
    Given an array nums with n integers, your task is to check 
    if it could become non-decreasing by modifying at most one element.

    We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) 
    such that (0 <= i <= n - 2).

Example 1:
    Input: nums = [4,2,3]
    Output: true
    Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
    Input: nums = [4,2,1]
    Output: false
    Explanation: You can't get a non-decreasing array by modify at most one element.

Constraints:
    n == nums.length
    1 <= n <= 10^4
    -10^5 <= nums[i] <= 10^5
"""


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (scan the array, find decreasing element, try to modify)
        return self._checkPossibility(nums)

    def _checkPossibility(self, nums: List[int]) -> bool:
        assert isinstance(nums, list) and len(nums) >= 1
        if len(nums) <= 2:
            return True

        for idx in range(1, len(nums)):
            pre_num, cur_num = nums[idx - 1], nums[idx]
            if pre_num > cur_num:
                # 1: try to modify nums[idx - 1]
                nums[idx - 1] = cur_num
                if nums == sorted(nums):
                    return True
                # 2: try to modify nums[idx]
                nums[idx - 1] = pre_num  # recover nums[idx - 1]
                nums[idx] = pre_num
                return nums == sorted(nums)

        return True


def main():
    # Example 1: Output: true
    nums = [4, 2, 3]

    # Example 2: Output: false
    # nums = [4, 2, 1]

    # Example 3: Output: false
    # nums = [3, 4, 2, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.checkPossibility(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
