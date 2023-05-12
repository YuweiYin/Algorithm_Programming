#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1330-Reverse-Subarray-To-Maximize-Array-Value.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-12
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1330 - (Hard) - Reverse Subarray To Maximize Array Value
https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

Description & Requirement:
    You are given an integer array nums. The value of this array is defined as 
    the sum of |nums[i] - nums[i + 1]| for all 0 <= i < nums.length - 1.

    You are allowed to select any subarray of the given array and reverse it. 
    You can perform this operation only once.

    Find maximum possible value of the final array.

Example 1:
    Input: nums = [2,3,1,5,4]
    Output: 10
    Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.
Example 2:
    Input: nums = [2,4,9,24,2,1,10]
    Output: 68

Constraints:
    1 <= nums.length <= 3 * 10^4
    -10^5 <= nums[i] <= 10^5
"""


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (scan the array)
        return self._maxValueAfterReverse(nums)

    def _maxValueAfterReverse(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        value, n = 0, len(nums)
        for i in range(n - 1):
            value += abs(nums[i] - nums[i + 1])

        max_num_1 = 0
        for i in range(1, n - 1):
            max_num_1 = max(max_num_1, abs(nums[0] - nums[i + 1]) - abs(nums[i] - nums[i + 1]))
            max_num_1 = max(max_num_1, abs(nums[-1] - nums[i - 1]) - abs(nums[i] - nums[i - 1]))

        max_num_2, min_num_2 = -int(1e9+7), int(1e9+7)
        for i in range(n - 1):
            x, y = nums[i], nums[i + 1]
            max_num_2 = max(max_num_2, min(x, y))
            min_num_2 = min(min_num_2, max(x, y))

        return value + max(max_num_1, 2 * (max_num_2 - min_num_2))


def main():
    # Example 1: Output: 10
    # nums = [2, 3, 1, 5, 4]

    # Example 2: Output: 68
    nums = [2, 4, 9, 24, 2, 1, 10]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxValueAfterReverse(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
