#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0747-Largest-Number-At-Least-Twice-of-Others.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-13
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0747 - (Easy) - Largest Number At Least Twice of Others
https://leetcode.com/problems/largest-number-at-least-twice-of-others/

Description & Requirement:
    You are given an integer array nums where the largest integer is unique.

    Determine whether the largest element in the array is 
    at least twice as much as every other number in the array. 
    If it is, return the index of the largest element, or return -1 otherwise.

Example 1:
    Input: nums = [3,6,1,0]
    Output: 1
    Explanation: 6 is the largest integer.
        For every other number in the array x, 6 is at least twice as big as x.
        The index of value 6 is 1, so we return 1.
Example 2:
    Input: nums = [1,2,3,4]
    Output: -1
    Explanation: 4 is less than twice the value of 3, so we return -1.
Example 3:
    Input: nums = [1]
    Output: 0
    Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.

Constraints:
    1 <= nums.length <= 50
    0 <= nums[i] <= 100
    The largest element in nums is unique.
"""


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return 0
        # main method: (one scan, find the largest number and second-largest number)
        return self._dominantIndex(nums)

    def _dominantIndex(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums >= 2

        largest_num = nums[0]
        largest_idx = 0
        second_largest_num = -1
        second_largest_idx = -1

        cur_idx = 1
        while cur_idx < len_nums:
            cur_num = nums[cur_idx]
            if cur_num > largest_num:  # update largest and second-largest
                second_largest_num = largest_num
                second_largest_idx = largest_idx
                largest_num = cur_num
                largest_idx = cur_idx
            else:
                if cur_num > second_largest_num:  # update second-largest only
                    second_largest_num = cur_num
                    second_largest_idx = cur_idx
            cur_idx += 1

        if second_largest_idx == -1:
            return largest_idx

        if largest_num >= (second_largest_num << 1):
            return largest_idx
        else:
            return -1


def main():
    # Example 1: Output: 1
    nums = [3, 6, 1, 0]

    # Example 2: Output: -1
    # nums = [1, 2, 3, 4]

    # Example 3: Output: 0
    # nums = [1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.dominantIndex(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
