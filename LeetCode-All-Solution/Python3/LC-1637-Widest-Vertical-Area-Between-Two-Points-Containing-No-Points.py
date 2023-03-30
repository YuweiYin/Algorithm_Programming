#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1637-Widest-Vertical-Area-Between-Two-Points-Containing-No-Points.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-30
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1637 - (Medium) - Widest Vertical Area Between Two Points Containing No Points
https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

Description & Requirement:
    Given n points on a 2D plane where points[i] = [xi, yi], 
    Return the widest vertical area between two points such that no points are inside the area.

    A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). 
    The widest vertical area is the one with the maximum width.

    Note that points on the edge of a vertical area are not considered included in the area.

Example 1:
    Input: points = [[8,7],[9,9],[7,4],[9,7]]
    Output: 1
    Explanation: Both the red and the blue area are optimal.
Example 2:
    Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    Output: 3

Constraints:
    n == points.length
    2 <= n <= 10^5
    points[i].length == 2
    0 <= xi, yi <= 10^9
"""


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # exception case
        assert isinstance(points, list) and len(points) >= 2
        # main method: (sorting)
        return self._maxWidthOfVerticalArea(points)

    def _maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        assert isinstance(points, list) and len(points) >= 2

        points.sort()
        res = 0
        for idx in range(1, len(points)):
            res = max(res, points[idx][0] - points[idx - 1][0])

        return res


def main():
    # Example 1: Output: 1
    # points = [[8, 7], [9, 9], [7, 4], [9, 7]]

    # Example 2: Output: 3
    points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxWidthOfVerticalArea(points)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
