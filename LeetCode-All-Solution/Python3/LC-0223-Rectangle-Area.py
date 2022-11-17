#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0223-Rectangle-Area.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-16
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0223 - (Medium) - Rectangle Area
https://leetcode.com/problems/rectangle-area/

Description & Requirement:
    Given the coordinates of two rectilinear rectangles in a 2D plane, 
    return the total area covered by the two rectangles.

    The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

    The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

Example 1:
    Rectangle Area
    Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
    Output: 45
Example 2:
    Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
    Output: 16

Constraints:
    -10^4 <= ax1 <= ax2 <= 10^4
    -10^4 <= ay1 <= ay2 <= 10^4
    -10^4 <= bx1 <= bx2 <= 10^4
    -10^4 <= by1 <= by2 <= 10^4
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # exception case
        # assert isinstance(ax1, int) and isinstance(ax2, int) and ax1 <= ax2
        # main method: (computational geography)
        return self._computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)

    def _computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # assert isinstance(ax1, int) and isinstance(ax2, int) and ax1 <= ax2

        area_1 = (ax2 - ax1) * (ay2 - ay1)
        area_2 = (bx2 - bx1) * (by2 - by1)

        overlap_width = min(ax2, bx2) - max(ax1, bx1)
        overlap_height = min(ay2, by2) - max(ay1, by1)
        area_overlap = max(overlap_width, 0) * max(overlap_height, 0)

        return area_1 + area_2 - area_overlap


def main():
    # Example 1: Output: 45
    # ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2

    # Example 2: Output: 16
    ax1 = -2
    ay1 = -2
    ax2 = 2
    ay2 = 2
    bx1 = -2
    by1 = -2
    bx2 = 2
    by2 = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
