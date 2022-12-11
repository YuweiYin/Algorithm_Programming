#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1827-Minimum-Operations-to-Make-the-Array-Increasing.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-11
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1827 - (Easy) - Minimum Operations to Make the Array Increasing
https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

Description & Requirement:
    You are given an integer array nums (0-indexed). 
    In one operation, you can choose an element of the array and increment it by 1.

    For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].

    Return the minimum number of operations needed to make nums strictly increasing.

    An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. 
    An array of length 1 is trivially strictly increasing.

Example 1:
    Input: nums = [1,1,1]
    Output: 3
    Explanation: You can do the following operations:
        1) Increment nums[2], so nums becomes [1,1,2].
        2) Increment nums[1], so nums becomes [1,2,2].
        3) Increment nums[2], so nums becomes [1,2,3].
Example 2:
    Input: nums = [1,5,2,4,1]
    Output: 14
Example 3:
    Input: nums = [8]
    Output: 0

Constraints:
    1 <= nums.length <= 5000
    1 <= nums[i] <= 10^4
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        for num in nums:
            assert isinstance(num, int) and num >= 1
        # main method: (greedy, accumulate the minimal gaps that make the array increasing)
        return self._minOperations(nums)

    def _minOperations(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        res = 0
        prev = nums[0] - 1
        for num in nums:
            prev = max(prev + 1, num)
            res += prev - num

        return res


def main():
    # Example 1: Output: 3
    # nums = [1, 1, 1]

    # Example 2: Output: 14
    nums = [1, 5, 2, 4, 1]

    # Example 3: Output: 0
    # nums = [8]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minOperations(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
