#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2651-Calculate-Delayed-Arrival-Time.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-08
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2651 - (Easy) Calculate Delayed Arrival Time
https://leetcode.com/problems/calculate-delayed-arrival-time/

Description & Requirement:
    You are given a positive integer arrivalTime denoting the arrival time of a train in hours, 
    and another positive integer delayedTime denoting the amount of delay in hours.

    Return the time when the train will arrive at the station.

    Note that the time in this problem is in 24-hours format.

Example 1:
    Input: arrivalTime = 15, delayedTime = 5 
    Output: 20 
    Explanation: Arrival time of the train was 15:00 hours. It is delayed by 5 hours. 
        Now it will reach at 15+5 = 20 (20:00 hours).
Example 2:
        Input: arrivalTime = 13, delayedTime = 11
        Output: 0
        Explanation: Arrival time of the train was 13:00 hours. It is delayed by 11 hours. 
            Now it will reach at 13+11=24 (Which is denoted by 00:00 in 24 hours format so return 0).

Constraints:
    1 <= arrivaltime < 24
    1 <= delayedTime <= 24
"""


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        # exception case
        assert isinstance(arrivalTime, int) and arrivalTime >= 1
        assert isinstance(delayedTime, int) and delayedTime >= 1
        # main method: (math)
        return self._findDelayedArrivalTime(arrivalTime, delayedTime)

    def _findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        assert isinstance(arrivalTime, int) and arrivalTime >= 1
        assert isinstance(delayedTime, int) and delayedTime >= 1

        return (arrivalTime + delayedTime) % 24


def main():
    # Example 1: Output: 20
    arrivalTime = 15
    delayedTime = 5

    # Example 2: Output: 0
    # arrivalTime = 13
    # delayedTime = 11

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.findDelayedArrivalTime(arrivalTime, delayedTime)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
