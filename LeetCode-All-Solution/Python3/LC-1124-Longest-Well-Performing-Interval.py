#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1124-Longest-Well-Performing-Interval.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-14
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1124 - (Medium) - Longest Well-Performing Interval
https://leetcode.com/problems/longest-well-performing-interval/

Description & Requirement:
    We are given hours, a list of the number of hours worked per day for a given employee.

    A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

    A well-performing interval is an interval of days for which 
    the number of tiring days is strictly larger than the number of non-tiring days.

    Return the length of the longest well-performing interval.

Example 1:
    Input: hours = [9,9,6,0,6,6,9]
    Output: 3
    Explanation: The longest well-performing interval is [9,9,6].
Example 2:
    Input: hours = [6,6,6]
    Output: 0

Constraints:
    1 <= hours.length <= 10^4
    0 <= hours[i] <= 16
"""


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # exception case
        assert isinstance(hours, list) and len(hours) >= 1
        for hour in hours:
            assert isinstance(hour, int) and hour >= 0
        # main method: (prefix sum)
        return self._longestWPI(hours)

    def _longestWPI(self, hours: List[int]) -> int:
        assert isinstance(hours, list) and len(hours) >= 1
        n = len(hours)

        score = [0] * n
        for i in range(n):
            if hours[i] > 8:
                score[i] = 1
            else:
                score[i] = -1

        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + score[i - 1]

        res = 0
        stack = []

        for i in range(n + 1):
            if not stack or prefix_sum[stack[-1]] > prefix_sum[i]:
                stack.append(i)

        i = n
        while i > res:
            while stack and prefix_sum[stack[-1]] < prefix_sum[i]:
                res = max(res, i - stack[-1])
                stack.pop()
            i -= 1

        return res


def main():
    # Example 1: Output: 3
    hours = [9, 9, 6, 0, 6, 6, 9]

    # Example 2: Output: 0
    # hours = [6, 6, 6]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestWPI(hours)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
