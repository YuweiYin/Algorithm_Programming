#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1749-Maximum-Absolute-Sum-of-Any-Subarray.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-08
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 1749 - (Medium) - Maximum Absolute Sum of Any Subarray
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

Description & Requirement:
    You are given an integer array nums. The absolute sum of a subarray 
    [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

    Return the maximum absolute sum of any (possibly empty) subarray of nums.

    Note that abs(x) is defined as follows:
        If x is a negative integer, then abs(x) = -x.
        If x is a non-negative integer, then abs(x) = x.

Example 1:
    Input: nums = [1,-3,2,3,-4]
    Output: 5
    Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:
    Input: nums = [2,-5,1,-4,3,-2]
    Output: 8
    Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
"""


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (dynamic programming)
        return self._maxAbsoluteSum(nums)

    def _maxAbsoluteSum(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        pos_max, neg_min = 0, 0
        pos_sum, neg_sum = 0, 0

        for num in nums:
            pos_sum += num
            pos_max = max(pos_max, pos_sum)
            pos_sum = max(0, pos_sum)

            neg_sum += num
            neg_min = min(neg_min, neg_sum)
            neg_sum = min(0, neg_sum)

        return max(pos_max, -neg_min)


def main():
    # Example 1: Output: 5
    nums = [1, -3, 2, 3, -4]

    # Example 2: Output: 8
    # nums = [2, -5, 1, -4, 3, -2]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.maxAbsoluteSum(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
