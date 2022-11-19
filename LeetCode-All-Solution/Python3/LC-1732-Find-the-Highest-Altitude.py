#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1732-Find-the-Highest-Altitude.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-19
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1732 - (Easy) - Find the Highest Altitude
https://leetcode.com/problems/find-the-highest-altitude/

Description & Requirement:
    There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
    The biker starts his trip on point 0 with altitude equal 0.

    You are given an integer array gain of length n where gain[i] is the net gain in altitude between 
    points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example 1:
    Input: gain = [-5,1,5,0,-7]
    Output: 1
    Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:
    Input: gain = [-4,-3,-2,-1,4,3,2]
    Output: 0
    Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

Constraints:
    n == gain.length
    1 <= n <= 100
    -100 <= gain[i] <= 100
"""


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # exception case
        assert isinstance(gain, list) and len(gain) >= 1
        # main method: (simulate the process)
        return self._largestAltitude(gain)

    def _largestAltitude(self, gain: List[int]) -> int:
        assert isinstance(gain, list) and len(gain) >= 1

        cur_altitude = 0
        res = 0
        for g in gain:
            cur_altitude += g
            res = max(res, cur_altitude)

        return res


def main():
    # Example 1: Output: 1
    gain = [-5, 1, 5, 0, -7]

    # Example 2: Output: 0
    # gain = [-4, -3, -2, -1, 4, 3, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largestAltitude(gain)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
