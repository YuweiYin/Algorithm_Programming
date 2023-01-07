#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0041-First-Missing-Positive.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-07
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0041 - (Hard) - First Missing Positive
https://leetcode.com/problems/first-missing-positive/

Description & Requirement:
    Given an unsorted integer array nums, return the smallest missing positive integer.

    You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
    Input: nums = [1,2,0]
    Output: 3
    Explanation: The numbers in the range [1,2] are all in the array.
Example 2:
    Input: nums = [3,4,-1,1]
    Output: 2
    Explanation: 1 is in the array but 2 is missing.
Example 3:
    Input: nums = [7,8,9,11,12]
    Output: 1
    Explanation: The smallest positive integer 1 is missing.

Constraints:
    1 <= nums.length <= 10^5
    -2^31 <= nums[i] <= 2^31 - 1
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (simulate the hash table)
        return self._firstMissingPositive(nums)

    def _firstMissingPositive(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


def main():
    # Example 1: Output: 3
    # nums = [1, 2, 0]

    # Example 2: Output: 2
    # nums = [3, 4, -1, 1]

    # Example 3: Output: 1
    nums = [7, 8, 9, 11, 12]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.firstMissingPositive(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
