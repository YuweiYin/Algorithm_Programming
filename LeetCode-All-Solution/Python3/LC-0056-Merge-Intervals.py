#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0056-Merge-Intervals.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-12
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0056 - (Medium) - Merge Intervals
https://leetcode.com/problems/merge-intervals/

Description & Requirement:
    Given an array of intervals where intervals[i] = [start_i, end_i], 
    merge all overlapping intervals, and return an array of the non-overlapping intervals 
    that cover all the intervals in the input.

Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    1 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= start_i <= end_i <= 10^4
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(intervals, list) and len(intervals) > 0
        # main method: (sort and merge)
        return self._merge(intervals)

    def _merge(self, intervals: List[List[int]]) -> List[List[int]]:
        len_intervals = len(intervals)
        assert len_intervals > 0

        res = []

        # sort start_i in ascending order, sort end_i in descending order
        intervals.sort(key=lambda x: (x[0], -x[1]))
        cur_start = intervals[0][0]
        cur_end = intervals[0][1]
        for interval in intervals[1:]:
            # cur_start must be less than or equal to interval[0]
            if cur_end >= interval[0]:  # if overlapped
                cur_end = max(cur_end, interval[1])  # extend the end_i of the overlapped interval
            else:
                res.append([cur_start, cur_end])  # record an interval
                cur_start = interval[0]  # update start_i
                cur_end = interval[1]  # update end_i
        res.append([cur_start, cur_end])  # record the last interval

        return res


def main():
    # Example 1: Output: [[1,6],[8,10],[15,18]]
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

    # Example 2: Output: [[1,5]]
    intervals = [[1, 4], [4, 5]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.merge(intervals)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
