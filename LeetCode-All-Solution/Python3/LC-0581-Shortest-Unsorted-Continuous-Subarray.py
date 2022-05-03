#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0581-Shortest-Unsorted-Continuous-Subarray.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-03
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0581 - (Medium) - Shortest Unsorted Continuous Subarray
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

Description & Requirement:
    Given an integer array nums, you need to find one continuous subarray that 
    if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

    Return the shortest such subarray and output its length.

Example 1:
    Input: nums = [2,6,4,8,10,9,15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:
    Input: nums = [1,2,3,4]
    Output: 0
Example 3:
    Input: nums = [1]
    Output: 0

Constraints:
    1 <= nums.length <= 10^4
    -10^5 <= nums[i] <= 10^5

Follow up:
    Can you solve it in O(n) time complexity?
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (1. sort and confine left/right border, O(n log n); 2. two pointers, linearly scan, O(n))
        return self._findUnsortedSubarray(nums)

    def _findUnsortedSubarray(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        len_nums = len(nums)
        if len_nums == 1:
            return 0
        if len_nums == 2:
            return 0 if nums[0] <= nums[1] else 2

        min_num, max_num = int(1e9+7), - int(1e9+7)  # -10^5 <= nums[i] <= 10^5
        left, right = -1, -1

        for idx in range(len_nums):
            if max_num > nums[idx]:  # move right cursor
                right = idx
            else:  # update max_num
                max_num = nums[idx]

            if min_num < nums[len_nums - 1 - idx]:  # move left cursor
                left = len_nums - 1 - idx
            else:  # update min_num
                min_num = nums[len_nums - 1 - idx]

        # right == -1 means the whole array has already in ascending order
        return 0 if right == -1 else right - left + 1


def main():
    # Example 1: Output: 5
    nums = [2, 6, 4, 8, 10, 9, 15]

    # Example 2: Output: 0
    # nums = [1, 2, 3, 4]

    # Example 3: Output: 0
    # nums = [1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findUnsortedSubarray(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
