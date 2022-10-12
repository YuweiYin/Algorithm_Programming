#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0976-Largest-Perimeter-Triangle.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-12
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0976 - (Easy) - Largest Perimeter Triangle
https://leetcode.com/problems/largest-perimeter-triangle/

Description & Requirement:
    Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, 
    formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:
    Input: nums = [2,1,2]
    Output: 5
Example 2:
    Input: nums = [1,2,1]
    Output: 0

Constraints:
    3 <= nums.length <= 10^4
    1 <= nums[i] <= 10^6
"""


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 3
        for num in nums:
            assert isinstance(num, int) and num >= 1
        # main method: (greedily choose the longest sides)
        return self._largestPerimeter(nums)

    def _largestPerimeter(self, nums: List[int]) -> int:
        """
        Runtime: 213 ms, faster than 86.56% of Python3 online submissions for Largest Perimeter Triangle.
        Memory Usage: 15.4 MB, less than 45.85% of Python3 online submissions for Largest Perimeter Triangle.
        """
        assert isinstance(nums, list) and len(nums) >= 3

        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i + 2] + nums[i + 1] > nums[i]:
                return nums[i + 2] + nums[i + 1] + nums[i]

        return 0


def main():
    # Example 1: Output: 5
    # nums = [2, 1, 2]

    # Example 2: Output: 0
    nums = [1, 2, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largestPerimeter(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
