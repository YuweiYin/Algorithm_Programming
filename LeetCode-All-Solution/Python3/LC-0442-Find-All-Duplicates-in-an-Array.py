#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0442-Find-All-Duplicates-in-an-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-08
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0442 - (Medium) - Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/

Description & Requirement:
    Given an integer array nums of length n where all the integers of nums are in the range [1, n] and 
    each integer appears once or twice, return an array of all the integers that appears twice.

    You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [2,3]
Example 2:
    Input: nums = [1,1,2]
    Output: [1]
Example 3:
    Input: nums = [1]
    Output: []

Constraints:
    n == nums.length
    1 <= n <= 10^5
    1 <= nums[i] <= n
    Each element in nums appears once or twice.
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (1 <= nums[i] <= len(nums), so if any number repeat more than once, some number must be missing)
        return self._findDuplicates(nums)  # Time: O(n); Space: O(1)

    def _findDuplicates(self, nums: List[int]) -> List[int]:
        assert isinstance(nums, list) and len(nums) >= 1
        len_nums = len(nums)
        for idx in range(len_nums):
            while nums[idx] != nums[nums[idx] - 1]:  # put number into the "right" slot
                nums[nums[idx] - 1], nums[idx] = nums[idx], nums[nums[idx] - 1]
        return [num for idx, num in enumerate(nums) if (num - 1) != idx]


def main():
    # Example 1: Output: [2,3]
    nums = [4, 3, 2, 7, 8, 2, 3, 1]

    # Example 2: Output: [1]
    # nums = [1, 1, 2]

    # Example 3: Output: []
    # nums = [1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findDuplicates(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
