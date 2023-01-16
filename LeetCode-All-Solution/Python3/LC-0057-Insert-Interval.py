#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0057-Insert-Interval.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-16
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0057 - (Medium) - Insert Interval
https://leetcode.com/problems/insert-interval/

Description & Requirement:
    You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] 
    represent the start and the end of the i-th interval and intervals is sorted in ascending order by start_i. 
    You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and 
    intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

    Return intervals after the insertion.

Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]
Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
    0 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= start_i <= end_i <= 10^5
    intervals is sorted by start_i in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 10^5
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # exception case
        assert isinstance(intervals, list)
        assert isinstance(newInterval, list) and len(newInterval) == 2
        # main method: (enumerate overlapping conditions)
        return self._insert(intervals, newInterval)

    def _insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        assert isinstance(intervals, list)
        assert isinstance(newInterval, list) and len(newInterval) == 2

        left, right = newInterval
        overlap = False

        res = []
        for left_i, right_i in intervals:
            if left_i > right:
                if not overlap:
                    res.append([left, right])
                    overlap = True
                res.append([left_i, right_i])
            elif right_i < left:
                res.append([left_i, right_i])
            else:
                left = min(left, left_i)
                right = max(right, right_i)

        if not overlap:
            res.append([left, right])

        return res


def main():
    # Example 1: Output: [[1,5],[6,9]]
    # intervals = [[1, 3], [6, 9]]
    # newInterval = [2, 5]

    # Example 2: Output: [[1,2],[3,10],[12,16]]
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.insert(intervals, newInterval)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
