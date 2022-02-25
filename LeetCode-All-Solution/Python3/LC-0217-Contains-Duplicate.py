#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0217-Contains-Duplicate.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-25
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0217 - (Easy) - Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Description & Requirement:
    Given an integer array nums, 
    return true if any value appears at least twice in the array, 
    and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true
Example 2:
    Input: nums = [1,2,3,4]
    Output: false
Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return False  # Error input type
        if len(nums) == 1:
            return False
        # main method: (scan once, store numbers in hash set, if duplicate, stop and return True)
        return self._containsDuplicate(nums)

    def _containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)

        return False


def main():
    # Example 1: Output: true
    # nums = [1, 2, 3, 1]

    # Example 2: Output: false
    # nums = [1, 2, 3, 4]

    # Example 3: Output: true
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.containsDuplicate(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
