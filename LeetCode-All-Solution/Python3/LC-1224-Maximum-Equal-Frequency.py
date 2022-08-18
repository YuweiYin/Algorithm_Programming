#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1224-Maximum-Equal-Frequency.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-18
=================================================================="""

import sys
import time
from typing import List
import collections

# import functools

"""
LeetCode - 1224 - (Hard) - Maximum Equal Frequency
https://leetcode.com/problems/maximum-equal-frequency/

Description & Requirement:
    Given an array nums of positive integers, return the longest possible length of an array prefix of nums, 
    such that it is possible to remove exactly one element from this prefix so that 
    every number that has appeared in it will have the same number of occurrences.

    If after removing one element there are no remaining elements, 
    it's still considered that every appeared number has the same number of ocurrences (0).

Example 1:
    Input: nums = [2,2,1,1,5,3,3,5]
    Output: 7
    Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, 
        if we remove nums[4] = 5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.
Example 2:
    Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
    Output: 13

Constraints:
    2 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
"""


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        # main method: (hash dict counter)
        return self._maxEqualFreq(nums)

    def _maxEqualFreq(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 2

        nums_cnt = collections.Counter()
        freq_cnt = collections.Counter()
        f_max = 0
        res = 0

        for idx, num in enumerate(nums):
            if nums_cnt[num]:
                freq_cnt[nums_cnt[num]] -= 1
            nums_cnt[num] += 1
            f_max = max(f_max, nums_cnt[num])
            freq_cnt[nums_cnt[num]] += 1

            if f_max == 1 or \
                    (freq_cnt[f_max] * f_max + freq_cnt[f_max - 1] * (f_max - 1) == idx + 1 and
                     freq_cnt[f_max] == 1) or \
                    (freq_cnt[f_max] * f_max + 1 == idx + 1 and freq_cnt[1] == 1):
                res = max(res, idx + 1)

        return res


def main():
    # Example 1: Output: 7
    nums = [2, 2, 1, 1, 5, 3, 3, 5]

    # Example 2: Output: 13
    # nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxEqualFreq(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
