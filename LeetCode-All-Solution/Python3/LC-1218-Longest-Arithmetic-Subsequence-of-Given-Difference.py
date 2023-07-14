#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1218-Longest-Arithmetic-Subsequence-of-Given-Difference.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-14
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 1218 - (Medium) - Longest Arithmetic Subsequence of Given Difference
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

Description & Requirement:
    Given an integer array arr and an integer difference, 
    return the length of the longest subsequence in arr which is an arithmetic sequence such that 
    the difference between adjacent elements in the subsequence equals difference.

    A subsequence is a sequence that can be derived from arr by deleting some or no elements 
    without changing the order of the remaining elements.

Example 1:
    Input: arr = [1,2,3,4], difference = 1
    Output: 4
    Explanation: The longest arithmetic subsequence is [1,2,3,4].
Example 2:
    Input: arr = [1,3,5,7], difference = 1
    Output: 1
    Explanation: The longest arithmetic subsequence is any single element.
Example 3:
    Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
    Output: 4
    Explanation: The longest arithmetic subsequence is [7,5,3,1].

Constraints:
    1 <= arr.length <= 10^5
    -10^4 <= arr[i], difference <= 10^4
"""


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 1
        assert isinstance(difference, int)
        # main method: (dynamic programming)
        return self._longestSubsequence(arr, difference)

    def _longestSubsequence(self, arr: List[int], difference: int) -> int:
        assert isinstance(arr, list) and len(arr) >= 1
        assert isinstance(difference, int)

        dp = collections.defaultdict(int)
        for ele in arr:
            dp[ele] = dp[ele - difference] + 1

        return max(dp.values())


def main():
    # Example 1: Output: 4
    # arr = [1, 2, 3, 4]
    # difference = 1

    # Example 2: Output: 1
    # arr = [1, 3, 5, 7]
    # difference = 1

    # Example 3: Output: 4
    arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    difference = -2

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.longestSubsequence(arr, difference)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
