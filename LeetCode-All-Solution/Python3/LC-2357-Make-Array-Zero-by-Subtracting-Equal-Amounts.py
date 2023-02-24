#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2357-Make-Array-Zero-by-Subtracting-Equal-Amounts.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-24
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2357 - (Easy) - Make Array Zero by Subtracting Equal Amounts
https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

Description & Requirement:
    You are given a non-negative integer array nums. In one operation, you must:
        Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
        Subtract x from every positive element in nums.

    Return the minimum number of operations to make every element in nums equal to 0.

Example 1:
    Input: nums = [1,5,0,3,5]
    Output: 3
    Explanation:
        In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
        In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
        In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
Example 2:
    Input: nums = [0]
    Output: 0
    Explanation: Each element in nums is already 0 so no operations are needed.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 100
"""


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (hash set)
        return self._minimumOperations(nums)

    def _minimumOperations(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        return len(set(nums) - {0})


def main():
    # Example 1: Output: 3
    nums = [1, 5, 0, 3, 5]

    # Example 2: Output: 0
    # nums = [0]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minimumOperations(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
