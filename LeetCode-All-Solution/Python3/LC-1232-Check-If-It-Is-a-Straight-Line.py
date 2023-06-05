#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1232-Check-If-It-Is-a-Straight-Line.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-05
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1232 - (Easy) - Check If It Is a Straight Line
https://leetcode.com/problems/check-if-it-is-a-straight-line/

Description & Requirement:
    You are given an array coordinates, coordinates[i] = [x, y], 
    where [x, y] represents the coordinate of a point. 
    Check if these points make a straight line in the XY plane.

Example 1:
    Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    Output: true
Example 2:
    Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    Output: false

Constraints:
    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.
"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # exception case
        assert isinstance(coordinates, list) and len(coordinates) >= 2
        # main method: (scan the array)
        return self._checkStraightLine(coordinates)

    def _checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        assert isinstance(coordinates, list) and len(coordinates) >= 2

        for i in range(2, len(coordinates)):
            if not (coordinates[i][0] - coordinates[0][0]) * (coordinates[1][1] - coordinates[0][1]) == \
                   (coordinates[i][1] - coordinates[0][1]) * (coordinates[1][0] - coordinates[0][0]):
                return False

        return True


def main():
    # Example 1: Output: true
    # coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]

    # Example 2: Output: false
    coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.checkStraightLine(coordinates)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
