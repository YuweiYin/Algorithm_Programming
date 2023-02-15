#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1250-Check-If-It-Is-a-Good-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-15
=================================================================="""

import sys
import time
from typing import List
import math
import functools
# import collections

"""
LeetCode - 1250 - (Hard) - Check If It Is a Good Array
https://leetcode.com/problems/check-if-it-is-a-good-array/

Description & Requirement:
    Given an array nums of positive integers. Your task is to select some subset of nums, 
    multiply each element by an integer and add all these numbers. The array is said to be good 
    if you can obtain a sum of 1 from the array by any possible subset and multiplicand.

    Return True if the array is good otherwise return False.

Example 1:
    Input: nums = [12,5,7,23]
    Output: true
    Explanation: Pick numbers 5 and 7.
        5*3 + 7*(-2) = 1
Example 2:
    Input: nums = [29,6,10]
    Output: true
    Explanation: Pick numbers 29, 6 and 10.
        29*1 + 6*(-3) + 10*(-1) = 1
Example 3:
    Input: nums = [3,6]
    Output: false

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
"""


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (mathematics)
        return self._isGoodArray(nums)

    def _isGoodArray(self, nums: List[int]) -> bool:
        assert isinstance(nums, list) and len(nums) >= 1

        return functools.reduce(math.gcd, nums) == 1


def main():
    # Example 1: Output: true
    nums = [12, 5, 7, 23]

    # Example 2: Output: true
    # nums = [29, 6, 10]

    # Example 3: Output: false
    # nums = [3, 6]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isGoodArray(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
