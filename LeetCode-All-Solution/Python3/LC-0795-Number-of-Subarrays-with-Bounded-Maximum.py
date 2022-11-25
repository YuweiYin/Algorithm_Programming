#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0795-Number-of-Subarrays-with-Bounded-Maximum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-24
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0795 - (Medium) - Number of Subarrays with Bounded Maximum
https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

Description & Requirement:
    Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays 
    such that the value of the maximum array element in that subarray is in the range [left, right].

    The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
    Input: nums = [2,1,4,3], left = 2, right = 3
    Output: 3
    Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Example 2:
    Input: nums = [2,9,2,5,6], left = 2, right = 8
    Output: 7

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
    0 <= left <= right <= 10^9
"""


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # exception case
        assert isinstance(left, int) and isinstance(right, int) and 0 <= left <= right
        assert isinstance(nums, list) and len(nums) >= 1
        for num in nums:
            assert isinstance(num, int) and num >= 0
        # main method: (scan and record the indices that smaller than LEFT or larger than RIGHT)
        return self._numSubarrayBoundedMax(nums, left, right)

    def _numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        """
        Runtime: 920 ms, faster than 71.07% of Python3 submissions for Number of Subarrays with Bounded Maximum.
        Memory Usage: 22.5 MB, less than 27.33% of Python3 submissions for Number of Subarrays with Bounded Maximum.
        """
        assert isinstance(left, int) and isinstance(right, int) and 0 <= left <= right
        assert isinstance(nums, list) and len(nums) >= 1

        res = 0
        smaller_than_left = -1
        larger_than_right = -1
        for idx, num in enumerate(nums):
            if left <= num <= right:
                smaller_than_left = idx
            elif num > right:
                larger_than_right = idx
                smaller_than_left = -1
            if smaller_than_left != -1:
                res += smaller_than_left - larger_than_right

        return res


def main():
    # Example 1: Output: 3
    # nums = [2, 1, 4, 3]
    # left = 2
    # right = 3

    # Example 2: Output: 7
    nums = [2, 9, 2, 5, 6]
    left = 2
    right = 8

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numSubarrayBoundedMax(nums, left, right)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
