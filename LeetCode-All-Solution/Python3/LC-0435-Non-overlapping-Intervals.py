#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0435-Non-overlapping-Intervals.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-14
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0435 - (Medium) - Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/

Description & Requirement:
    Given an array of intervals intervals where intervals[i] = [start_i, end_i], 
    return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:
    Input: intervals = [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:
    Input: intervals = [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
    1 <= intervals.length <= 10^5
    intervals[i].length == 2
    -5 * 10^4 <= start_i < end_i <= 5 * 10^4
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # exception case
        assert isinstance(intervals, list) and len(intervals) > 0
        for interval in intervals:
            assert isinstance(interval, list) and len(interval) == 2
        # main method: (sort both start_i and end_i in ascending order, check overlapped intervals)
        return self._eraseOverlapIntervals(intervals)

    def _eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Runtime: 1524 ms, faster than 80.58% of Python3 online submissions for Non-overlapping Intervals.
        Memory Usage: 53.1 MB, less than 17.86% of Python3 online submissions for Non-overlapping Intervals.
        """
        len_intervals = len(intervals)
        assert len_intervals > 0

        # sort both start_i and end_i in ascending order
        intervals.sort(key=lambda x: (x[0], x[1]))

        res = 0
        cur_end = intervals[0][1]
        for interval in intervals[1:]:
            # cur_start must be less than or equal to interval[0]
            if cur_end > interval[0]:  # if overlapped, erase the interval that has bigger end_i
                cur_end = min(cur_end, interval[1])  # retain the smaller end_i of the overlapped interval
                res += 1
            else:
                cur_end = interval[1]  # update end_i

        return res


def main():
    # Example 1: Output: 1
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]

    # Example 2: Output: 2
    # intervals = [[1, 2], [1, 2], [1, 2]]

    # Example 3: Output: 0
    # intervals = [[1, 2], [2, 3]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.eraseOverlapIntervals(intervals)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
