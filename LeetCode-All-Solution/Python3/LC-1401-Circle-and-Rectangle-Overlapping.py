#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1401-Circle-and-Rectangle-Overlapping.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-25
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 1401 - (Medium) - Circle and Rectangle Overlapping
https://leetcode.com/problems/circle-and-rectangle-overlapping/

Description & Requirement:
    You are given a circle represented as (radius, xCenter, yCenter) and 
    an axis-aligned rectangle represented as (x1, y1, x2, y2), where 
    (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) 
    are the coordinates of the top-right corner of the rectangle.

    Return true if the circle and rectangle are overlapped otherwise return false. 
    In other words, check if there is any point (xi, yi) that 
    belongs to the circle and the rectangle at the same time.

Example 1:
    Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
    Output: true
    Explanation: Circle and rectangle share the point (1,0).
Example 2:
    Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
    Output: false
Example 3:
    Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
    Output: true

Constraints:
    1 <= radius <= 2000
    -10^4 <= xCenter, yCenter <= 10^4
    -10^4 <= x1 < x2 <= 10^4
    -10^4 <= y1 < y2 <= 10^4
"""


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # exception case
        assert isinstance(radius, int) and radius >= 1
        assert isinstance(xCenter, int) and isinstance(yCenter, int)
        assert isinstance(x1, int) and isinstance(x2, int) and x1 < x2
        assert isinstance(y1, int) and isinstance(y2, int) and y1 < y2
        # main method: (mathematics)
        return self._checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)

    def _checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        assert isinstance(radius, int) and radius >= 1
        assert isinstance(xCenter, int) and isinstance(yCenter, int)
        assert isinstance(x1, int) and isinstance(x2, int) and x1 < x2
        assert isinstance(y1, int) and isinstance(y2, int) and y1 < y2

        dist = 0
        if xCenter < x1 or xCenter > x2:
            dist += min((x1 - xCenter) ** 2, (x2 - xCenter) ** 2)
        if yCenter < y1 or yCenter > y2:
            dist += min((y1 - yCenter) ** 2, (y2 - yCenter) ** 2)

        return dist <= (radius ** 2)


def main():
    # Example 1: Output: true
    radius = 1
    xCenter = 0
    yCenter = 0
    x1 = 1
    y1 = -1
    x2 = 3
    y2 = 1

    # Example 2: Output: false
    # radius = 1
    # xCenter = 1
    # yCenter = 1
    # x1 = 1
    # y1 = -3
    # x2 = 2
    # y2 = -1

    # Example 3: Output: true
    # radius = 1
    # xCenter = 0
    # yCenter = 0
    # x1 = -1
    # y1 = 0
    # x2 = 0
    # y2 = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
