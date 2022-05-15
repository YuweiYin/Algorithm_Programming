#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0812-Largest-Triangle-Area.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-15
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0812 - (Easy) - Largest Triangle Area
https://leetcode.com/problems/largest-triangle-area/

Description & Requirement:
    Given an array of points on the X-Y plane points where points[i] = [xi, yi], 
    return the area of the largest triangle that can be formed by any three different points. 
    Answers within 10^{-5} of the actual answer will be accepted.

Example 1:
    Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    Output: 2.00000
    Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:
    Input: points = [[1,0],[0,0],[0,1]]
    Output: 0.50000

Constraints:
    3 <= points.length <= 50
    -50 <= xi, yi <= 50
    All the given points are unique.
"""


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # exception case
        assert isinstance(points, list) and len(points) >= 3
        # main method: (Convex Hull)
        return self._largestTriangleArea(points)

    def _get_convex_hull(self, points: List[List[int]]) -> List[List[int]]:
        assert isinstance(points, list) and len(points) >= 3
        len_points = len(points)
        if len_points == 3:
            return points

        def __cross_product(p_1: List[int], p_2: List[int], p_3: List[int]) -> int:
            return (p_2[0] - p_1[0]) * (p_3[1] - p_2[1]) - (p_2[1] - p_1[1]) * (p_3[0] - p_2[0])

        points.sort()
        convex_hull = []  # stack
        for idx, point in enumerate(points):
            while len(convex_hull) > 1 and __cross_product(convex_hull[-2], convex_hull[-1], point) <= 0:
                convex_hull.pop()
            convex_hull.append(point)

        len_hull = len(convex_hull)
        for idx in range(len_points - 2, -1, -1):
            point = points[idx]
            while len(convex_hull) > len_hull and __cross_product(convex_hull[-2], convex_hull[-1], point) <= 0:
                convex_hull.pop()
            convex_hull.append(point)

        convex_hull.pop()  # get rid of the duplicated convex_hull[0] element
        return convex_hull

    def _largestTriangleArea(self, points: List[List[int]]) -> float:
        """
        Runtime: 70 ms, faster than 99.68% of Python3 online submissions for Largest Triangle Area.
        Memory Usage: 14 MB, less than 10.71% of Python3 online submissions for Largest Triangle Area.
        """
        assert isinstance(points, list) and len(points) >= 3
        # len_points = len(points)

        def __get_triangle_area(p_1: List[int], p_2: List[int], p_3: List[int]) -> float:
            return float(abs(p_1[0] * p_2[1] + p_2[0] * p_3[1] + p_3[0] * p_1[1] -
                             p_1[0] * p_3[1] - p_2[0] * p_1[1] - p_3[0] * p_2[1])) / 2

        convex_hull = self._get_convex_hull(points)
        len_hull = len(convex_hull)
        res = float(0.0)

        for p_1_idx, p_1 in enumerate(convex_hull):
            p_3_idx = p_1_idx + 2
            for p_2_idx in range(p_1_idx + 1, len_hull - 1):
                p_2 = convex_hull[p_2_idx]
                while p_3_idx + 1 < len_hull:
                    cur_area = __get_triangle_area(p_1, p_2, convex_hull[p_3_idx])
                    next_area = __get_triangle_area(p_1, p_2, convex_hull[p_3_idx + 1])
                    if cur_area >= next_area:
                        break
                    p_3_idx += 1
                res = max(res, __get_triangle_area(p_1, p_2, convex_hull[p_3_idx]))

        return float(res)


def main():
    # Example 1: Output: 2.00000
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]

    # Example 2: Output: 0.50000
    # points = [[1, 0], [0, 0], [0, 1]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largestTriangleArea(points)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
