#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1608-Special-Array-With-X-Elements-Greater-Than-or-Equal-X.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-12
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1608 - (Easy) - Special Array With X Elements Greater Than or Equal X
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

Description & Requirement:
    You are given an array nums of non-negative integers. 
    nums is considered special if there exists a number x such that 
    there are exactly x numbers in nums that are greater than or equal to x.

    Notice that x does not have to be an element in nums.

    Return x if the array is special, otherwise, return -1. 
    It can be proven that if nums is special, the value for x is unique.

Example 1:
    Input: nums = [3,5]
    Output: 2
    Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
Example 2:
    Input: nums = [0,0]
    Output: -1
    Explanation: No numbers fit the criteria for x.
        If x = 0, there should be 0 numbers >= x, but there are 2.
        If x = 1, there should be 1 number >= x, but there are 0.
        If x = 2, there should be 2 numbers >= x, but there are 0.
        x cannot be greater since there are only 2 numbers in nums.
Example 3:
    Input: nums = [0,4,3,0,4]
    Output: 3
    Explanation: There are 3 values that are greater than or equal to 3.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
"""


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        for num in nums:
            assert isinstance(num, int) and num >= 0
        # main method: (sort in a descending order)
        return self._specialArray(nums)

    def _specialArray(self, nums: List[int]) -> int:
        """
        Runtime: 40 ms, faster than 90.64% of Python3 submissions for Special Array With X Elements >= X.
        Memory Usage: 13.8 MB, less than 97.53% of Python3 submissions for Special Array With X Elements >= X.
        """
        assert isinstance(nums, list) and len(nums) >= 1

        nums.sort(reverse=True)
        n = len(nums)

        for idx in range(1, n + 1):
            if nums[idx - 1] >= idx and (idx == n or nums[idx] < idx):
                return idx

        return -1


def main():
    # Example 1: Output: 2
    # nums = [3, 5]

    # Example 2: Output: -1
    # nums = [0, 0]

    # Example 3: Output: 3
    nums = [0, 4, 3, 0, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.specialArray(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
