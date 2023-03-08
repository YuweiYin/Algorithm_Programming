#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2187-Minimum-Time-to-Complete-Trips.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-07
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2187 - (Medium) - Minimum Time to Complete Trips
https://leetcode.com/problems/minimum-time-to-complete-trips/

Description & Requirement:
    You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

    Each bus can make multiple trips successively; that is, the next trip can start immediately after 
    completing the current trip. Also, each bus operates independently; that is, 
    the trips of one bus do not influence the trips of any other bus.

    You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. 
    Return the minimum time required for all buses to complete at least totalTrips trips.

Example 1:
    Input: time = [1,2,3], totalTrips = 5
    Output: 3
    Explanation:
        - At time t = 1, the number of trips completed by each bus are [1,0,0]. 
          The total number of trips completed is 1 + 0 + 0 = 1.
        - At time t = 2, the number of trips completed by each bus are [2,1,0]. 
          The total number of trips completed is 2 + 1 + 0 = 3.
        - At time t = 3, the number of trips completed by each bus are [3,1,1]. 
          The total number of trips completed is 3 + 1 + 1 = 5.
        So the minimum time needed for all buses to complete at least 5 trips is 3.
Example 2:
    Input: time = [2], totalTrips = 1
    Output: 2
    Explanation:
        There is only one bus, and it will complete its first trip at t = 2.
        So the minimum time needed to complete 1 trip is 2.

Constraints:
    1 <= time.length <= 10^5
    1 <= time[i], totalTrips <= 10^7
"""


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # exception case
        assert isinstance(time, list) and len(time) >= 1
        assert isinstance(totalTrips, int) and totalTrips >= 1
        # main method: (binary search)
        return self._minimumTime(time, totalTrips)

    def _minimumTime(self, time: List[int], totalTrips: int) -> int:
        assert isinstance(time, list) and len(time) >= 1
        assert isinstance(totalTrips, int) and totalTrips >= 1

        def __check(t: int) -> bool:
            cnt = 0
            for period in time:
                cnt += t // period
            return cnt >= totalTrips

        left, right = 1, totalTrips * max(time)
        while left < right:
            mid = (left + right) >> 1
            if __check(mid):
                right = mid
            else:
                left = mid + 1

        return left


def main():
    # Example 1: Output: 3
    _time = [1, 2, 3]
    totalTrips = 5

    # Example 2: Output: 2
    # _time = [2]
    # totalTrips = 1

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minimumTime(_time, totalTrips)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
