#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2369-Check-if-There-is-a-Valid-Partition-For-The-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-13
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 2369 - (Medium) - Check if There is a Valid Partition For The Array
https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

Description & Requirement:
    You are given a 0-indexed integer array nums. 
    You have to partition the array into one or more contiguous subarrays.

    We call a partition of the array valid if each of 
    the obtained subarrays satisfies one of the following conditions:

        1. The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
        2. The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
        3. The subarray consists of exactly 3 consecutive increasing elements, that is, 
            the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, 
            but the subarray [1,3,5] is not.

    Return true if the array has at least one valid partition. Otherwise, return false.

Example 1:
    Input: nums = [4,4,4,5,6]
    Output: true
    Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
        This partition is valid, so we return true.
Example 2:
    Input: nums = [1,1,1,2]
    Output: false
    Explanation: There is no valid partition for this array.

Constraints:
    2 <= nums.length <= 10^5
    1 <= nums[i] <= 10^6
"""


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        # main method: (dynamic programming)
        return self._validPartition(nums)

    def _validPartition(self, nums: List[int]) -> bool:
        assert isinstance(nums, list) and len(nums) >= 2

        n = len(nums)
        dp = [True] + [False] * n

        for i, x in enumerate(nums):
            if (i > 0 and dp[i - 1] and x == nums[i - 1]) or \
                    (i > 1 and dp[i - 2] and (x == nums[i - 1] == nums[i - 2] or
                                              x == nums[i - 1] + 1 == nums[i - 2] + 2)):
                dp[i + 1] = True

        return dp[n]


def main():
    # Example 1: Output: true
    nums = [4, 4, 4, 5, 6]

    # Example 2: Output: false
    # nums = [1, 1, 1, 2]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.validPartition(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
