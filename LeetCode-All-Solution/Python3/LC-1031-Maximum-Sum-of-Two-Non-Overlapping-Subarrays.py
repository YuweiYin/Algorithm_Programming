#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1031-Maximum-Sum-of-Two-Non-Overlapping-Subarrays.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-26
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1031 - (Medium) - Maximum Sum of Two Non-Overlapping Subarrays
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

Description & Requirement:
    Given an integer array nums and two integers firstLen and secondLen, 
    return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

    The array with length firstLen could occur before or after the array with length secondLen, 
    but they have to be non-overlapping.

    A subarray is a contiguous part of an array.

Example 1:
    Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
    Output: 20
    Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
Example 2:
    Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
    Output: 29
    Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
Example 3:
    Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
    Output: 31
    Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8] with length 3.

Constraints:
    1 <= firstLen, secondLen <= 1000
    2 <= firstLen + secondLen <= 1000
    firstLen + secondLen <= nums.length <= 1000
    0 <= nums[i] <= 1000
"""


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # exception case
        assert isinstance(firstLen, int) and firstLen >= 1
        assert isinstance(secondLen, int) and secondLen >= 1
        assert isinstance(nums, list) and firstLen + secondLen <= len(nums)
        # main method: (dynamic programming & sliding window)
        return self._maxSumTwoNoOverlap(nums, firstLen, secondLen)

    def _maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        assert isinstance(firstLen, int) and firstLen >= 1
        assert isinstance(secondLen, int) and secondLen >= 1
        assert isinstance(nums, list) and firstLen + secondLen <= len(nums)

        def __find_max(_firstLen, _secondLen):
            sum_left = 0
            for i in range(0, _firstLen):
                sum_left += nums[i]
            max_sum_left = sum_left

            sum_right = 0
            for i in range(_firstLen, _firstLen + _secondLen):
                sum_right += nums[i]
            res = max_sum_left + sum_right

            j = _firstLen
            for i in range(_firstLen + _secondLen, len(nums)):
                sum_left += nums[j] - nums[j - _firstLen]
                max_sum_left = max(max_sum_left, sum_left)
                sum_right += nums[i] - nums[i - _secondLen]
                res = max(res, max_sum_left + sum_right)
                j += 1
            return res

        return max(__find_max(firstLen, secondLen), __find_max(secondLen, firstLen))


def main():
    # Example 1: Output: 20
    # nums = [0, 6, 5, 2, 2, 5, 1, 9, 4]
    # firstLen = 1
    # secondLen = 2

    # Example 2: Output: 29
    # nums = [3, 8, 1, 3, 2, 1, 8, 9, 0]
    # firstLen = 3
    # secondLen = 2

    # Example 3: Output: 31
    nums = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8]
    firstLen = 4
    secondLen = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxSumTwoNoOverlap(nums, firstLen, secondLen)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
