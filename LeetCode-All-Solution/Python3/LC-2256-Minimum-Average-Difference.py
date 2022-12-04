#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2256-Minimum-Average-Difference.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-04
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2256 - (Medium) - Minimum Average Difference
https://leetcode.com/problems/minimum-average-difference/

Description & Requirement:
    You are given a 0-indexed integer array nums of length n.

    The average difference of the index i is the absolute difference between the average of the first i + 1 elements 
    of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

    Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

    Note:
        The absolute difference of two numbers is the absolute value of their difference.
        The average of n elements is the sum of the n elements divided (integer division) by n.
        The average of 0 elements is considered to be 0.

Example 1:
    Input: nums = [2,5,3,9,5,3]
    Output: 3
    Explanation:
        - The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
        - The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
        - The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
        - The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
        - The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
        - The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
        The average difference of index 3 is the minimum average difference so return 3.
Example 2:
    Input: nums = [0]
    Output: 0
    Explanation:
        The only index is 0 so return 0.
        The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^5
"""


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (prefix sum)
        return self._minimumAverageDifference(nums)

    def _minimumAverageDifference(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        n = len(nums)
        total_sum = sum(nums)
        prefix_sum = 0
        res = (float('inf'), -1)

        for idx in range(n):
            prefix_sum += nums[idx]
            suffix_sum = total_sum - prefix_sum
            if idx == n - 1:
                diff = prefix_sum // (idx + 1)
            else:
                diff = abs(prefix_sum // (idx + 1) - suffix_sum // (n - idx - 1))

            if diff < res[0]:
                res = (diff, idx)

        return res[1]


def main():
    # Example 1: Output: 3
    nums = [2, 5, 3, 9, 5, 3]

    # Example 2: Output: 0
    # nums = [0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumAverageDifference(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
