#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1037-Valid-Boomerang.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-08
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1037 - (Easy) - Valid Boomerang
https://leetcode.com/problems/valid-boomerang/

Description & Requirement:
    Given an array points where points[i] = [x_i, y_i] represents a point on the X-Y plane, 
    return true if these points are a boomerang.

    A boomerang is a set of three points that are all distinct and not in a straight line.

Example 1:
    Input: points = [[1,1],[2,3],[3,2]]
    Output: true
Example 2:
    Input: points = [[1,1],[2,2],[3,3]]
    Output: false

Constraints:
    points.length == 3
    points[i].length == 2
    0 <= x_i, y_i <= 100
"""


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # exception case
        assert isinstance(points, list) and len(points) == 3
        for point in points:
            assert isinstance(point, list) and len(point) == 2
        # main method: (computational geometry: cross product)
        return self._isBoomerang(points)

    def _isBoomerang(self, points: List[List[int]]) -> bool:
        assert isinstance(points, list) and len(points) == 3

        def __cross_product(p_1: List[int], p_2: List[int], p_3: List[int]) -> int:
            return (p_2[0] - p_1[0]) * (p_3[1] - p_2[1]) - (p_2[1] - p_1[1]) * (p_3[0] - p_2[0])

        return __cross_product(points[0], points[1], points[2]) != 0


def main():
    # Example 1: Output: true
    # points = [[1, 1], [2, 3], [3, 2]]

    # Example 2: Output: false
    points = [[1, 1], [2, 2], [3, 3]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isBoomerang(points)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
