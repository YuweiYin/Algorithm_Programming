#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1870-Minimum-Speed-to-Arrive-on-Time.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-26
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 1870 - (Medium) - Minimum Speed to Arrive on Time
https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

Description & Requirement:
    You are given a floating-point number hour, representing the amount of time you have to reach the office. 
    To commute to the office, you must take n trains in sequential order. 
    You are also given an integer array dist of length n, where dist[i] describes the distance 
    (in kilometers) of the ith train ride.

    Each train can only depart at an integer hour, so you may need to wait in between each train ride.

    - For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours 
        before you can depart on the 2nd train ride at the 2 hour mark.

    Return the minimum positive integer speed (in kilometers per hour) that all the trains must 
    travel at for you to reach the office on time, or -1 if it is impossible to be on time.

    Tests are generated such that the answer will not exceed 107 and hour will have at most two digits 
    after the decimal point.

Example 1:
    Input: dist = [1,3,2], hour = 6
    Output: 1
    Explanation: At speed 1:
        - The first train ride takes 1/1 = 1 hour.
        - Since we are already at an integer hour, we depart immediately at the 1 hour mark. 
            The second train takes 3/1 = 3 hours.
        - Since we are already at an integer hour, we depart immediately at the 4 hour mark. 
            The third train takes 2/1 = 2 hours.
        - You will arrive at exactly the 6 hour mark.
Example 2:
    Input: dist = [1,3,2], hour = 2.7
    Output: 3
    Explanation: At speed 3:
        - The first train ride takes 1/3 = 0.33333 hours.
        - Since we are not at an integer hour, we wait until the 1 hour mark to depart. 
            The second train ride takes 3/3 = 1 hour.
        - Since we are already at an integer hour, we depart immediately at the 2 hour mark. 
            The third train takes 2/3 = 0.66667 hours.
        - You will arrive at the 2.66667 hour mark.
Example 3:
    Input: dist = [1,3,2], hour = 1.9
    Output: -1
    Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.

Constraints:
    n == dist.length
    1 <= n <= 10^5
    1 <= dist[i] <= 10^5
    1 <= hour <= 10^9
    There will be at most two digits after the decimal point in hour.
"""


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # exception case
        assert isinstance(dist, list) and len(dist) >= 1
        assert isinstance(hour, float) and hour >= 1.0
        # main method: (binary search)
        return self._minSpeedOnTime(dist, hour)

    def _minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        assert isinstance(dist, list) and len(dist) >= 1
        assert isinstance(hour, float) and hour >= 1

        n = len(dist)
        hr = round(hour * 100)
        if hr <= 100 * (n - 1):
            return -1

        def __check_speed(speed: int) -> bool:
            t = 0
            for i in range(n - 1):
                t += (dist[i] - 1) // speed + 1
            t *= speed
            t += dist[-1]
            return t * 100 <= hr * speed

        left, right = 1, int(1e9+7)
        while left < right:
            mid = (left + right) >> 1
            if __check_speed(mid):
                right = mid
            else:
                left = mid + 1

        return left



def main():
    # Example 1: Output: 1
    # dist = [1, 3, 2]
    # hour = 6

    # Example 2: Output: 3
    dist = [1, 3, 2]
    hour = 2.7

    # Example 3: Output: -1
    # dist = [1, 3, 2]
    # hour = 1.9

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minSpeedOnTime(dist, hour)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
