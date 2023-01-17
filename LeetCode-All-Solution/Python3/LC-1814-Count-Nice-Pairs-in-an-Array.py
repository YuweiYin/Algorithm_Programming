#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1814-Count-Nice-Pairs-in-an-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-17
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1814 - (Medium) - Count Nice Pairs in an Array
https://leetcode.com/problems/count-nice-pairs-in-an-array/

Description & Requirement:
    You are given an array nums that consists of non-negative integers. 
    Let us define rev(x) as the reverse of the non-negative integer x. 
    For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice 
    if it satisfies all of the following conditions:

        0 <= i < j < nums.length
        nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

    Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

Example 1:
    Input: nums = [42,11,1,97]
    Output: 2
    Explanation: The two pairs are:
        - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
        - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
Example 2:
    Input: nums = [13,10,35,24,76]
    Output: 4

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
"""


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (hash counter)
        return self._countNicePairs(nums)

    def _countNicePairs(self, nums: List[int]) -> int:
        """
        Time: beats 72.33%; Space: beats 64.33%
        """
        assert isinstance(nums, list) and len(nums) >= 1

        MOD = int(1e9+7)
        cnt = collections.Counter()
        res = 0
        for num in nums:
            target = int(str(num)[::-1])
            res += cnt[num - target] % MOD
            cnt[num - target] += 1

        return res % MOD


def main():
    # Example 1: Output: 2
    # nums = [42, 11, 1, 97]

    # Example 3: Output: 4
    nums = [13, 10, 35, 24, 76]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countNicePairs(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
