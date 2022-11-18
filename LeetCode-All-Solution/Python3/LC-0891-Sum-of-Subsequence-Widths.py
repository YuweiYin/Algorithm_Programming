#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0891-Sum-of-Subsequence-Widths.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-18
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0891 - (Hard) - Sum of Subsequence Widths
https://leetcode.com/problems/sum-of-subsequence-widths/

Description & Requirement:
    The width of a sequence is the difference between the maximum and minimum elements in the sequence.

    Given an array of integers nums, return the sum of the widths of all the non-empty subsequences of nums. 
    Since the answer may be very large, return it modulo 109 + 7.

    A subsequence is a sequence that can be derived from an array by deleting some or no elements without 
    changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
    Input: nums = [2,1,3]
    Output: 6
    Explanation: The subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
        The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
        The sum of these widths is 6.
Example 2:
    Input: nums = [2]
    Output: 0

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
"""


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (Mathematics)
        return self._sumSubseqWidths(nums)

    def _sumSubseqWidths(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        nums.sort()
        res = 0
        MOD = int(1e9+7)

        x, y = nums[0], 2
        for j in range(1, len(nums)):
            res = (res + nums[j] * (y - 1) - x) % MOD
            x = ((x << 1) + nums[j]) % MOD
            y = (y << 1) % MOD

        return (res + MOD) % MOD


def main():
    # Example 1: Output: 6
    nums = [2, 1, 3]

    # Example 2: Output: 0
    # nums = [2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sumSubseqWidths(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
