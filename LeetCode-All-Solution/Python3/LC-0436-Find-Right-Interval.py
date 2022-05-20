#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0436-Find-Right-Interval.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-20
=================================================================="""

import sys
import time
from typing import List
import bisect
# import functools

"""
LeetCode - 0436 - (Medium) - Find Right Interval
https://leetcode.com/problems/find-right-interval/

Description & Requirement:
    You are given an array of intervals, where intervals[i] = [start_i, end_i] and each start_i is unique.

    The right interval for an interval i is an interval j such that start_j >= end_i and start_j is minimized. 
    Note that i may equal j.

    Return an array of right interval indices for each interval i. 
    If no right interval exists for interval i, then put -1 at index i.

Example 1:
    Input: intervals = [[1,2]]
    Output: [-1]
    Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:
    Input: intervals = [[3,4],[2,3],[1,2]]
    Output: [-1,0,1]
    Explanation: There is no right interval for [3,4].
        The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
        The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.
Example 3:
    Input: intervals = [[1,4],[2,3],[3,4]]
    Output: [-1,2,-1]
    Explanation: There is no right interval for [1,4] and [3,4].
        The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.

Constraints:
    1 <= intervals.length <= 2 * 10^4
    intervals[i].length == 2
    -10^6 <= start_i <= end_i <= 10^6
    The start point of each interval is unique.
"""


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(intervals, list) and len(intervals) >= 1
        # main method: (sort & binary search)
        return self._findRightInterval(intervals)

    def _findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """
        Runtime: 304 ms, faster than 92.64% of Python3 online submissions for Find Right Interval.
        Memory Usage: 20.2 MB, less than 50.56% of Python3 online submissions for Find Right Interval.
        """
        assert isinstance(intervals, list) and len(intervals) >= 1
        len_intervals = len(intervals)
        if len_intervals == 1:
            return [-1]

        for idx in range(len_intervals):  # append index to each interval
            intervals[idx].append(idx)
        intervals.sort()

        res = [-1 for _ in range(len_intervals)]
        for _start, _end, _idx in intervals:
            bs_idx = bisect.bisect_left(intervals, [_end])
            if 0 <= bs_idx < len_intervals:
                res[_idx] = intervals[bs_idx][-1]

        return res


def main():
    # Example 1: Output: [-1]
    # intervals = [[1, 2]]

    # Example 2: Output: [-1,0,1]
    # intervals = [[3, 4], [2, 3], [1, 2]]

    # Example 3: Output: [-1,2,-1]
    intervals = [[1, 4], [2, 3], [3, 4]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findRightInterval(intervals)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
