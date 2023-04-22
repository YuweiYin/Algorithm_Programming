#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1027-Longest-Arithmetic-Subsequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-22
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1027 - (Medium) - Longest Arithmetic Subsequence
https://leetcode.com/problems/longest-arithmetic-subsequence/

Description & Requirement:
    Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

    Note that:
        A subsequence is an array that can be derived from another array by 
            deleting some or no elements without changing the order of the remaining elements.
        A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value 
            (for 0 <= i < seq.length - 1).

Example 1:
    Input: nums = [3,6,9,12]
    Output: 4
    Explanation: The whole array is an arithmetic sequence with steps of length = 3.
Example 2:
    Input: nums = [9,4,7,2,10]
    Output: 3
    Explanation: The longest arithmetic subsequence is [4,7,10].
Example 3:
    Input: nums = [20,1,15,3,10,5,8]
    Output: 4
    Explanation: The longest arithmetic subsequence is [20,15,10,5].

Constraints:
    2 <= nums.length <= 1000
    0 <= nums[i] <= 500
"""


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        # main method: (dynamic programming)
        return self._longestArithSeqLength(nums)

    def _longestArithSeqLength(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 2

        diff = max(nums) - min(nums)
        res = 1

        for cur_diff in range(-diff, diff + 1):
            dp_dict = dict()
            for num in nums:
                if (prev := num - cur_diff) in dp_dict:
                    dp_dict[num] = max(dp_dict.get(num, 0), dp_dict[prev] + 1)
                    res = max(res, dp_dict[num])
                dp_dict[num] = max(dp_dict.get(num, 0), 1)

        return res


def main():
    # Example 1: Output: 4
    nums = [3, 6, 9, 12]

    # Example 2: Output: 3
    # nums = [9, 4, 7, 2, 10]

    # Example 3: Output: 4
    # nums = [20, 1, 15, 3, 10, 5, 8]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestArithSeqLength(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
