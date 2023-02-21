#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1326-Minimum-Number-of-Taps-to-Open-to-Water-a-Garden.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-21
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1326 - (Hard) - Minimum Number of Taps to Open to Water a Garden
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

Description & Requirement:
    There is a one-dimensional garden on the x-axis. 
    The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

    There are n + 1 taps located at points [0, 1, ..., n] in the garden.

    Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means 
    the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

    Return the minimum number of taps that should be open to water the whole garden, 
    If the garden cannot be watered return -1.

Example 1:
    Input: n = 5, ranges = [3,4,1,1,0,0]
    Output: 1
    Explanation: The tap at point 0 can cover the interval [-3,3]
        The tap at point 1 can cover the interval [-3,5]
        The tap at point 2 can cover the interval [1,3]
        The tap at point 3 can cover the interval [2,4]
        The tap at point 4 can cover the interval [4,4]
        The tap at point 5 can cover the interval [5,5]
        Opening Only the second tap will water the whole garden [0,5]
Example 2:
    Input: n = 3, ranges = [0,0,0,0]
    Output: -1
    Explanation: Even if you activate all the four taps you cannot water the whole garden.

Constraints:
    1 <= n <= 10^4
    ranges.length == n + 1
    0 <= ranges[i] <= 100
"""


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(ranges, list) and len(ranges) == n + 1
        # main method: (dynamic programming)
        return self._minTaps(n, ranges)

    def _minTaps(self, n: int, ranges: List[int]) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(ranges, list) and len(ranges) == n + 1

        intervals = []
        for i, r in enumerate(ranges):
            start = max(0, i - r)
            end = min(n, i + r)
            intervals.append((start, end))
        intervals.sort()

        INF = float("inf")
        dp = [INF] * (n + 1)
        dp[0] = 0

        for start, end in intervals:
            if dp[start] == INF:
                return -1
            for j in range(start, end + 1):
                dp[j] = min(dp[j], dp[start] + 1)

        return int(dp[-1])


def main():
    # Example 1: Output: 1
    n = 5
    ranges = [3, 4, 1, 1, 0, 0]

    # Example 2: Output: -1
    # n = 3
    # ranges = [0, 0, 0, 0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minTaps(n, ranges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
