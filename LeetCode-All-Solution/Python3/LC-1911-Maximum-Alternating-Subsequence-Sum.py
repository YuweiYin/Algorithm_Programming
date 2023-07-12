#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1911-Maximum-Alternating-Subsequence-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-12
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 1911 - (Medium) - Maximum Alternating Subsequence Sum
https://leetcode.com/problems/maximum-alternating-subsequence-sum/

Description & Requirement:
    The alternating sum of a 0-indexed array is defined as the sum of the elements 
    at even indices minus the sum of the elements at odd indices.

        For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.

    Given an array nums, return the maximum alternating sum of any subsequence of nums 
    (after reindexing the elements of the subsequence).

    A subsequence of an array is a new array generated from the original array by 
    deleting some elements (possibly none) without changing the remaining elements' relative order. 
    For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.

Example 1:
    Input: nums = [4,2,5,3]
    Output: 7
    Explanation: It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.
Example 2:
    Input: nums = [5,6,7,8]
    Output: 8
    Explanation: It is optimal to choose the subsequence [8] with alternating sum 8.
Example 3:
    Input: nums = [6,2,1,2,4,5]
    Output: 10
    Explanation: It is optimal to choose the subsequence [6,1,5] 
        with alternating sum (6 + 5) - 1 = 10.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
"""


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (dynamic programming)
        return self._maxAlternatingSum(nums)

    def _maxAlternatingSum(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        even, odd = nums[0], 0
        for i in range(1, len(nums)):
            even, odd = max(even, odd + nums[i]), max(odd, even - nums[i])

        return even


def main():
    # Example 1: Output: 7
    # nums = [4, 2, 5, 3]

    # Example 2: Output: 8
    # nums = [5, 6, 7, 8]

    # Example 3: Output: 10
    nums = [6, 2, 1, 2, 4, 5]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.maxAlternatingSum(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
