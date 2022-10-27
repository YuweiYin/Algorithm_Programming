#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0523-Continuous-Subarray-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-26
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0523 - (Medium) - Continuous Subarray Sum
https://leetcode.com/problems/continuous-subarray-sum/

Description & Requirement:
    Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least 
    two whose elements sum up to a multiple of k, or false otherwise.

    An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:
    Input: nums = [23,2,4,6,7], k = 6
    Output: true
    Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:
    Input: nums = [23,2,6,4,7], k = 6
    Output: true
    Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
        42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:
    Input: nums = [23,2,6,4,7], k = 13
    Output: false

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
    0 <= sum(nums[i]) <= 2^31 - 1
    1 <= k <= 2^31 - 1
"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and 1 <= k
        # main method: (prefix sum)
        return self._checkSubarraySum(nums, k)

    def _checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Runtime: 2283 ms, faster than 50.45% of Python3 online submissions for Continuous Subarray Sum.
        Memory Usage: 28.7 MB, less than 96.91% of Python3 online submissions for Continuous Subarray Sum.
        """
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and 1 <= k

        modes = set()
        pre_sum = 0
        for num in nums:
            last = pre_sum
            pre_sum += num
            pre_sum %= k
            if pre_sum in modes:
                return True
            modes.add(last)

        return False


def main():
    # Example 1: Output: true
    # nums = [23, 2, 4, 6, 7]
    # k = 6

    # Example 2: Output: true
    nums = [23, 2, 6, 4, 7]
    k = 6

    # Example 3: Output: false
    # nums = [23, 2, 6, 4, 7]
    # k = 13

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.checkSubarraySum(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
