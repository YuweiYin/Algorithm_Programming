#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1779-Find-Nearest-Point-That-Has-the-Same-X-or-Y-Coordinate.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-01
=================================================================="""

import sys
import time
from typing import List
# import itertools

"""
LeetCode - 1779 - (Easy) - Find Nearest Point That Has the Same X or Y Coordinate
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

Description & Requirement:
    You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). 
    You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). 
    A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

    Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. 
    If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

    The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

Example 1:
    Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
    Output: 2
    Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. 
        Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, 
        with a distance of 1. [2,4] has the smallest index, so return 2.
Example 2:
    Input: x = 3, y = 4, points = [[3,4]]
    Output: 0
    Explanation: The answer is allowed to be on the same location as your current location.
Example 3:
    Input: x = 3, y = 4, points = [[2,3]]
    Output: -1
    Explanation: There are no valid points.

Constraints:
    1 <= points.length <= 10^4
    points[i].length == 2
    1 <= x, y, ai, bi <= 10^4
"""


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # exception case
        assert isinstance(x, int) and x >= 1
        assert isinstance(y, int) and x >= 1
        for point in points:
            assert isinstance(point, list) and len(point) == 2 and point[0] >= 1 and point[1] >= 1
        # main method: (scan and update the minimal gap of the x index and y index)
        return self._nearestValidPoint(x, y, points)

    def _nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        assert isinstance(x, int) and x >= 1
        assert isinstance(y, int) and x >= 1

        best_dist, best_idx = float("inf"), -1
        for idx, (px, py) in enumerate(points):
            if x == px:
                cur_dist = abs(y - py)
                if cur_dist < best_dist:
                    best_dist = cur_dist
                    best_idx = idx
            elif y == py:
                cur_dist = abs(x - px)
                if cur_dist < best_dist:
                    best_dist = cur_dist
                    best_idx = idx

        return best_idx


def main():
    # Example 1: Output: 2
    x = 3
    y = 4
    points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]

    # Example 2: Output: 0
    # x = 3
    # y = 4
    # points = [[3, 4]]

    # Example 3: Output: -1
    # x = 3
    # y = 4
    # points = [[2, 3]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.nearestValidPoint(x, y, points)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
