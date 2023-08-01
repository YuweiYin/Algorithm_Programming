#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2681-Power-of-Heroes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-01
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 2681 - (Medium) - Power of Heroes
https://leetcode.com/problems/power-of-heroes/

Description & Requirement:
    You are given a 0-indexed integer array nums representing the strength of some heroes. 
    The power of a group of heroes is defined as follows:

        Let i0, i1, ... ,ik be the indices of the heroes in a group. 
        Then, the power of this group is max(nums[i0], nums[i1], ... ,nums[ik])2 * 
        min(nums[i0], nums[i1], ... ,nums[ik]).

    Return the sum of the power of all non-empty groups of heroes possible. Since the sum could be very large, return it modulo 109 + 7.

Example 1:
    Input: nums = [2,1,4]
    Output: 141
    Explanation: 
        1st group: [2] has power = 22 * 2 = 8.
        2nd group: [1] has power = 12 * 1 = 1. 
        3rd group: [4] has power = 42 * 4 = 64. 
        4th group: [2,1] has power = 22 * 1 = 4. 
        5th group: [2,4] has power = 42 * 2 = 32. 
        6th group: [1,4] has power = 42 * 1 = 16. 
        7th group: [2,1,4] has power = 42 * 1 = 16. 
        The sum of powers of all groups is 8 + 1 + 64 + 4 + 32 + 16 + 16 = 141.
Example 2:
    Input: nums = [1,1,1]
    Output: 7
    Explanation: A total of 7 groups are possible, and the power of each group will be 1. 
        Therefore, the sum of the powers of all groups is 7.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
"""


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (sorting)
        return self._sumOfPower(nums)

    def _sumOfPower(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        MOD = int(1e9+7)
        nums.sort()

        res = s = 0
        for num in nums:
            res = (res + num * num * (num + s)) % MOD
            s = (s * 2 + num) % MOD

        return int(res % MOD)


def main():
    # Example 1: Output: 141
    nums = [2, 1, 4]

    # Example 2: Output: 7
    # nums = [1, 1, 1]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.sumOfPower(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
