#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2444-Count-Subarrays-With-Fixed-Bounds.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-04
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2444 - (Hard) - Count Subarrays With Fixed Bounds
https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

Description & Requirement:
    You are given an integer array nums and two integers minK and maxK.

    A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
        The minimum value in the subarray is equal to minK.
        The maximum value in the subarray is equal to maxK.

    Return the number of fixed-bound subarrays.

    A subarray is a contiguous part of an array.

Example 1:
    Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
    Output: 2
    Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:
    Input: nums = [1,1,1,1], minK = 1, maxK = 1
    Output: 10
    Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

Constraints:
    2 <= nums.length <= 10^5
    1 <= nums[i], minK, maxK <= 10^6
"""


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        assert isinstance(minK, int) and minK >= 1
        assert isinstance(maxK, int) and maxK >= 1
        # main method: (scan the array)
        return self._countSubarrays(nums, minK, maxK)

    def _countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 2
        assert isinstance(minK, int) and minK >= 1
        assert isinstance(maxK, int) and maxK >= 1

        res = 0
        min_i = max_i = i_0 = -1
        for idx, num in enumerate(nums):
            if num == minK:
                min_i = idx
            if num == maxK:
                max_i = idx
            if not minK <= num <= maxK:
                i_0 = idx
            res += max(min(min_i, max_i) - i_0, 0)

        return res


def main():
    # Example 1: Output: 2
    nums = [1, 3, 5, 2, 7, 5]
    minK = 1
    maxK = 5

    # Example 2: Output: 10
    # nums = [1, 1, 1, 1]
    # minK = 1
    # maxK = 1

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.countSubarrays(nums, minK, maxK)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
