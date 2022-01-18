#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0539-Minimum-Time-Difference.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-18
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0539 - (Medium) - Minimum Time Difference
https://leetcode.com/problems/minimum-time-difference/

Description & Requirement:
    Given a list of 24-hour clock time points in "HH:MM" format, 
    return the minimum minutes difference between any two time-points in the list.

Example 1:
    Input: timePoints = ["23:59","00:00"]
    Output: 1
Example 2:
    Input: timePoints = ["00:00","23:59","00:00"]
    Output: 0

Constraints:
    2 <= timePoints <= 2 * 10^4
    timePoints[i] is in the format "HH:MM".
"""


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # exception case
        if not isinstance(timePoints, list) or len(timePoints) <= 1:
            return -1  # Error input type
        # main method: (sort, for time[i], consider abs(time[i] - time[i-1]), if i==0, time[-1] is time[last] - "24:00")
        # other trick: keep each time pointer p and p+"24:00", and then scan for the min diff pair
        return self._findMinDifference(timePoints)

    def _findMinDifference(self, timePoints: List[str]) -> int:
        len_time_point = len(timePoints)
        assert len_time_point > 1

        ONE_DAY_MINUTE = 1440  # int(24 * 60)
        time_list = []
        for time_point in timePoints:
            assert isinstance(time_point, str) and len(time_point) == 5
            assert time_point[0: 2].isdigit() and time_point[3:].isdigit()
            time_hour = int(time_point[0: 2])
            time_minute = int(time_point[3:])
            cur_time = int(60 * time_hour + time_minute)
            time_list.append(cur_time)  # convert into integer minutes and store

        INF = sys.maxsize
        res = INF
        time_list.sort()  # sort
        len_time_list = len(time_list)
        cur_time_index = 1
        while cur_time_index < len_time_list:  # for time[i] (i >= 1), consider abs(time[i] - time[i-1])
            cur_diff = abs(time_list[cur_time_index] - time_list[cur_time_index - 1])
            res = min(res, int(cur_diff))
            cur_time_index += 1
        # when i == 0, time_list[-1] is time_list[last] - "24:00"
        last_day_minute = time_list[len_time_list - 1] - ONE_DAY_MINUTE
        first_gap = abs(time_list[0] - last_day_minute)
        res = min(res, int(first_gap))

        return res if res < INF else -1


def main():
    # Example 1: Output: 1
    # timePoints = ["23:59", "00:00"]

    # Example 2: Output: 0
    timePoints = ["00:00", "23:59", "00:00"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findMinDifference(timePoints)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
