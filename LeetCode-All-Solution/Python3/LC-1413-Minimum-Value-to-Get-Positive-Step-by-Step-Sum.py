#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1413-Minimum-Value-to-Get-Positive-Step-by-Step-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-09
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1413 - (Easy) - Minimum Value to Get Positive Step by Step Sum
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

Description & Requirement:
    Given an array of integers nums, you start with an initial positive value startValue.

    In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

    Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Example 1:
    Input: nums = [-3,2,-3,4,2]
    Output: 5
    Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
    step by step sum
    startValue = 4 | startValue = 5 | nums
      (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
      (1 +2 ) = 3  | (2 +2 ) = 4    |   2
      (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
      (0 +4 ) = 4  | (1 +4 ) = 5    |   4
      (4 +2 ) = 6  | (5 +2 ) = 7    |   2
Example 2:
    Input: nums = [1,2]
    Output: 1
    Explanation: Minimum start value should be positive. 
Example 3:
    Input: nums = [1,-2,-3]
    Output: 5

Constraints:
    1 <= nums.length <= 100
    -100 <= nums[i] <= 100
"""


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (start from 0, add num[i] from i=0 to i=len(num)-1)
        return self._minStartValue(nums)

    def _minStartValue(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        cur_min = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            cur_min = min(cur_min, cur_sum)

        return 1 - cur_min


def main():
    # Example 1: Output: 5
    # nums = [-3, 2, -3, 4, 2]

    # Example 2: Output: 1
    nums = [1, 2]

    # Example 3: Output: 5
    # nums = [1, -2, -3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minStartValue(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
