#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1288-Remove-Covered-Intervals.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-20
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1288 - (Medium) - Remove Covered Intervals
https://leetcode.com/problems/remove-covered-intervals/

Description & Requirement:
    Given an array intervals where intervals[i] = [l_i, r_i] represent the interval [l_i, r_i), 
    remove all intervals that are covered by another interval in the list.

    The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

    Return the number of remaining intervals.

Example 1:
    Input: intervals = [[1,4],[3,6],[2,8]]
    Output: 2
    Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:
    Input: intervals = [[1,4],[2,3]]
    Output: 1

Constraints:
    1 <= intervals.length <= 1000
    intervals[i].length == 2
    0 <= l_i <= r_i <= 10^5
    All the given intervals are unique.
"""


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # exception case
        if not isinstance(intervals, list) or len(intervals) <= 0:
            return 0  # Error input type
        for interval in intervals:
            assert isinstance(interval, list) and len(interval) == 2
        if len(intervals) == 1:
            return 1
        # main method: (sorting & greedily scan)
        return self._removeCoveredIntervals(intervals)

    def _removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        len_intervals = len(intervals)
        assert len_intervals >= 2

        # sort: left_border in ascending order, right_border in descending order
        # so if several intervals have the same left_border, the first one is the largest interval among them
        intervals.sort(key=lambda x: (x[0], -x[1]))

        res = 0
        pre_r_border = intervals[0][1] - 1  # guarantee that first interval will be count in
        for cur_l_border, cur_r_border in intervals:
            # cur_l_border must <= pre_l_border
            if cur_r_border > pre_r_border:
                res += 1
                pre_r_border = cur_r_border
            # else: l_border must <= last_l_border, so cur_interval is covered by the pre_interval, skip counting it

        return res


def main():
    # Example 1: Output: 2
    intervals = [[1, 4], [3, 6], [2, 8]]

    # Example 2: Output: 1
    # intervals = [[1, 4], [2, 3]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.removeCoveredIntervals(intervals)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
