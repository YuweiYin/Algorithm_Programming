#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2366-Minimum-Replacements-to-Sort-the-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-30
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2366 - (Hard) Minimum Replacements to Sort the Array
https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

Description & Requirement:
    You are given a 0-indexed integer array nums. In one operation you can replace any element 
    of the array with any two elements that sum to it.

    For example, consider nums = [5,6,7]. In one operation, 
    we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].

    Return the minimum number of operations to make an array that is sorted in non-decreasing order.

Example 1:
    Input: nums = [3,9,3]
    Output: 2
    Explanation: Here are the steps to sort the array in non-decreasing order:
        - From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
        - From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
        There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.
Example 2:
    Input: nums = [1,2,3,4,5]
    Output: 0
    Explanation: The array is already in non-decreasing order. Therefore, we return 0. 

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
"""


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (simulation)
        return self._minimumReplacement(nums)

    def _minimumReplacement(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        res, m = 0, nums[-1]
        for num in reversed(nums):
            k = (num - 1) // m
            res += k
            m = num // (k + 1)

        return res


def main():
    # Example 1: Output: 2
    # nums = [3, 9, 3]

    # Example 2: Output: 0
    nums = [1, 2, 3, 4, 5]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minimumReplacement(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
