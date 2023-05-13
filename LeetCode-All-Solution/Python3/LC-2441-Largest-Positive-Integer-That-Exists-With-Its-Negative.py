#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2441-Largest-Positive-Integer-That-Exists-With-Its-Negative.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-13
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2441 - (Easy) - Largest Positive Integer That Exists With Its Negative
https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

Description & Requirement:
    Given an integer array nums that does not contain any zeros, 
    find the largest positive integer k such that -k also exists in the array.

    Return the positive integer k. If there is no such integer, return -1.

Example 1:
    Input: nums = [-1,2,-3,3]
    Output: 3
    Explanation: 3 is the only valid k we can find in the array.
Example 2:
    Input: nums = [-1,10,6,7,-7,1]
    Output: 7
    Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
Example 3:
    Input: nums = [-10,8,6,7,-2,-3]
    Output: -1
    Explanation: There is no a single valid k, we return -1.

Constraints:
    1 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    nums[i] != 0
"""


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (hash set)
        return self._findMaxK(nums)

    def _findMaxK(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        res = -1
        hash_set = set(nums)
        for num in nums:
            if -num in hash_set:
                res = max(res, num)

        return res


def main():
    # Example 1: Output: 3
    # nums = [-1, 2, -3, 3]

    # Example 2: Output: 7
    # nums = [-1, 10, 6, 7, -7, 1]

    # Example 3: Output: -1
    nums = [-10, 8, 6, 7, -2, -3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findMaxK(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
