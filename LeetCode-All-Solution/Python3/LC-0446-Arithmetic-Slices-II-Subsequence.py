#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0446-Arithmetic-Slices-II-Subsequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-27
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0446 - (Hard) - Arithmetic Slices II - Subsequence
https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

Description & Requirement:
    Given an integer array nums, return the number of all the arithmetic subsequences of nums.

    A sequence of numbers is called arithmetic if it consists of at least three elements and 
    if the difference between any two consecutive elements is the same.

        For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
        For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.

    A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

        For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].

    The test cases are generated so that the answer fits in 32-bit integer.

Example 1:
    Input: nums = [2,4,6,8,10]
    Output: 7
    Explanation: All arithmetic subsequence slices are:
        [2,4,6]
        [4,6,8]
        [6,8,10]
        [2,4,6,8]
        [4,6,8,10]
        [2,4,6,8,10]
        [2,6,10]
Example 2:
    Input: nums = [7,7,7,7,7]
    Output: 16
    Explanation: Any subsequence of this array is arithmetic.

Constraints:
    1  <= nums.length <= 1000
    -2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (dynamic programming)
        return self._numberOfArithmeticSlices(nums)

    def _numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Runtime: 958 ms, faster than 92.68% of Python3 online submissions for Arithmetic Slices II - Subsequence.
        Memory Usage: 68.7 MB, less than 59.76% of Python3 online submissions for Arithmetic Slices II - Subsequence.
        """
        assert isinstance(nums, list) and len(nums) >= 1

        res = 0
        dp = [collections.defaultdict(int) for _ in nums]
        for i, num in enumerate(nums):
            for j in range(i):
                diff = num - nums[j]
                cnt = dp[j][diff]
                res += cnt
                dp[i][diff] += cnt + 1

        return res


def main():
    # Example 1: Output: 7
    nums = [2, 4, 6, 8, 10]

    # Example 2: Output: 16
    # nums = [7, 7, 7, 7, 7]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numberOfArithmeticSlices(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
