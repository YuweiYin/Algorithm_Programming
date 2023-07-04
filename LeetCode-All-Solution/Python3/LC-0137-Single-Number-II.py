#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0137-Single-Number-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-04
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 0137 - (Medium) - Single Number II
https://leetcode.com/problems/single-number-ii/

Description & Requirement:
    Given an integer array nums where every element appears three times except for one, 
    which appears exactly once. Find the single element and return it.

    You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
    Input: nums = [2,2,3,2]
    Output: 3
Example 2:
    Input: nums = [0,1,0,1,0,1,99]
    Output: 99

Constraints:
    1 <= nums.length <= 3 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    Each element in nums appears exactly three times except for one element which appears once.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (scan the array, count the frequency)
        return self._singleNumber(nums)

    def _singleNumber(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        freq = collections.Counter(nums)
        res = [num for num, occ in freq.items() if occ == 1][0]

        return res


def main():
    # Example 1: Output: 3
    # nums = [2, 2, 3, 2]

    # Example 2: Output: 99
    nums = [0, 1, 0, 1, 0, 1, 99]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.singleNumber(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
