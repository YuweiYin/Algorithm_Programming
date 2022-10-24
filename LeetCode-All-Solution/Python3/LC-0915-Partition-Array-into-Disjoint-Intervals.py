#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0915-Partition-Array-into-Disjoint-Intervals.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-24
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0915 - (Medium) - Partition Array into Disjoint Intervals
https://leetcode.com/problems/partition-array-into-disjoint-intervals/

Description & Requirement:
    Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:
        Every element in left is less than or equal to every element in right.
        left and right are non-empty.
        left has the smallest possible size.

    Return the length of left after such a partitioning.

    Test cases are generated such that partitioning exists.

Example 1:
    Input: nums = [5,0,3,8,6]
    Output: 3
    Explanation: left = [5,0,3], right = [8,6]
Example 2:
    Input: nums = [1,1,1,0,6,12]
    Output: 4
    Explanation: left = [1,1,1,0], right = [6,12]

Constraints:
    2 <= nums.length <= 10^5
    0 <= nums[i] <= 10^6
    There is at least one valid answer for the given input.
"""


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        for num in nums:
            assert isinstance(num, int) and num >= 0
        # main method: (scan twice: right to left and left to right)
        return self._partitionDisjoint(nums)

    def _partitionDisjoint(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 2
        n = len(nums)

        min_right = [0 for _ in range(n)]
        min_right[-1] = nums[-1]

        for idx in range(n - 2, 0, -1):
            min_right[idx] = min(min_right[idx + 1], nums[idx])

        max_left = nums[0]
        for idx in range(1, n):
            if max_left <= min_right[idx]:
                return idx
            max_left = max(max_left, nums[idx])

        return 1


def main():
    # Example 1: Output: 3
    # nums = [5, 0, 3, 8, 6]

    # Example 2: Output: 4
    nums = [1, 1, 1, 0, 6, 12]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.partitionDisjoint(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
