#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0775-Global-and-Local-Inversions.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-16
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0775 - (Medium) - Global and Local Inversions
https://leetcode.com/problems/global-and-local-inversions/

Description & Requirement:
    You are given an integer array nums of length n which 
    represents a permutation of all the integers in the range [0, n - 1].

    The number of global inversions is the number of the different pairs (i, j) where:
        0 <= i < j < n
        nums[i] > nums[j]

    The number of local inversions is the number of indices i where:
        0 <= i < n - 1
        nums[i] > nums[i + 1]

    Return true if the number of global inversions is equal to the number of local inversions.

Example 1:
    Input: nums = [1,0,2]
    Output: true
    Explanation: There is 1 global inversion and 1 local inversion.
Example 2:
    Input: nums = [1,2,0]
    Output: false
    Explanation: There are 2 global inversions and 1 local inversion.

Constraints:
    n == nums.length
    1 <= n <= 10^5
    0 <= nums[i] < n
    All the integers of nums are unique.
    nums is a permutation of all the numbers in the range [0, n - 1].
"""


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (maintain the minimum of the suffix)
        return self._isIdealPermutation(nums)

    def _isIdealPermutation(self, nums: List[int]) -> bool:
        assert isinstance(nums, list) and len(nums) >= 1

        # return all(abs(x - i) <= 1 for i, x in enumerate(nums))

        min_suffix = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if nums[i - 1] > min_suffix:
                return False
            min_suffix = min(min_suffix, nums[i])

        return True


def main():
    # Example 1: Output: true
    nums = [1, 0, 2]

    # Example 2: Output: false
    # nums = [1, 2, 0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isIdealPermutation(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
