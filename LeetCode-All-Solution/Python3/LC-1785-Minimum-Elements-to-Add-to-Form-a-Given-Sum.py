#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1785-Minimum-Elements-to-Add-to-Form-a-Given-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-16
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1785 - (Medium) - Minimum Elements to Add to Form a Given Sum
https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

Description & Requirement:
    You are given an integer array nums and two integers limit and goal. 
    The array nums has an interesting property that abs(nums[i]) <= limit.

    Return the minimum number of elements you need to add to make the sum of the array equal to goal. 
    The array must maintain its property that abs(nums[i]) <= limit.

    Note that abs(x) equals x if x >= 0, and -x otherwise.

Example 1:
    Input: nums = [1,-1,1], limit = 3, goal = -4
    Output: 2
    Explanation: You can add -2 and -3, then the sum of the array will be 1 - 1 + 1 - 2 - 3 = -4.
Example 2:
    Input: nums = [1,-10,9,1], limit = 100, goal = 0
    Output: 1

Constraints:
    1 <= nums.length <= 10^5
    1 <= limit <= 10^6
    -limit <= nums[i] <= limit
    -10^9 <= goal <= 10^9
"""


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(limit, int) and limit >= 1 and isinstance(goal, int)
        # main method: (greedy)
        return self._minElements(nums, limit, goal)

    def _minElements(self, nums: List[int], limit: int, goal: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(limit, int) and limit >= 1 and isinstance(goal, int)

        gap = abs(goal - sum(nums))
        res, remainder = divmod(gap, limit)

        return res if remainder == 0 else res + 1


def main():
    # Example 1: Output: 2
    # nums = [1, -1, 1]
    # limit = 3
    # goal = -4

    # Example 2: Output: 1
    nums = [1, -10, 9, 1]
    limit = 100
    goal = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minElements(nums, limit, goal)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
