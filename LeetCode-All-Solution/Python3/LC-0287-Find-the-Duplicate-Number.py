#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0287-Find-the-Duplicate-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-29
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0287 - (Medium) - Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/

Description & Requirement:
    Given an array of integers nums containing n + 1 integers 
    where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2
Example 2:
    Input: nums = [3,1,3,4,2]
    Output: 3

Constraints:
    1 <= n <= 10^5
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
    How can we prove that at least one duplicate number must exist in nums?
    Can you solve the problem in linear runtime complexity?
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        # main method: (Floyd cycle, similar to LC-0142-Linked-List-Cycle-II)
        return self._findDuplicate(nums)

    def _findDuplicate(self, nums: List[int]) -> int:
        """
        Runtime: 620 ms, faster than 96.19% of Python3 online submissions for Find the Duplicate Number.
        Memory Usage: 28.4 MB, less than 28.09% of Python3 online submissions for Find the Duplicate Number.
        """
        ptr_slow = 0
        ptr_fast = 0

        while True:
            ptr_slow = nums[ptr_slow]  # slow move 1 step
            ptr_fast = nums[nums[ptr_fast]]  # fast move 2 step
            if ptr_slow == ptr_fast:  # move until slow and fast meet
                break

        # now slow move from the starting point 0
        ptr_slow = 0
        while ptr_slow != ptr_fast:  # slow and fast move at the same pace, till they meet
            ptr_slow = nums[ptr_slow]
            ptr_fast = nums[ptr_fast]

        return ptr_slow


def main():
    # Example 1: Output: 2
    # nums = [1, 3, 4, 2, 2]

    # Example 2: Output: 3
    nums = [3, 1, 3, 4, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findDuplicate(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
