#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0149-Max-Points-on-a-Line.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-03
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0149 - (Hard) - Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/

Description & Requirement:
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
    return the maximum number of points that lie on the same straight line.

Example 1:
    Input: points = [[1,1],[2,2],[3,3]]
    Output: 3
Example 2:
    Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    Output: 4

Constraints:
    1 <= points.length <= 300
    points[i].length == 2
    -10^4 <= xi, yi <= 10^4
    All the points are unique.
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # exception case
        if not isinstance(points, list) or len(points) <= 0:
            return 0  # Error input type
        if len(points) == 1:
            return 1
        for point in points:  # assert points[i].length == 2
            if not isinstance(point, list) or len(point) != 2:
                return False
        # main method: (every two points will form a line, consider how many other points are also in this line, O(n^3))
        return self._maxPoints(points)

    def _maxPoints(self, points: List[List[int]]) -> int:
        """
        Time: O(n^3).  Space: O(1)
        Runtime: 2546 ms, faster than 5.02% of Python3 online submissions for Max Points on a Line.
        Memory Usage: 13.9 MB, less than 99.34% of Python3 online submissions for Max Points on a Line.
        """
        len_points = len(points)
        assert len_points >= 2

        res = 2  # the biggest number of points in a line (at least 2 points in a line)

        def __three_points_in_line(line_p1: List[int], line_p2: List[int], test_p: List[int]) -> int:
            # return 1 if (test_p[0] - line_p1[0]) / (test_p[1] - line_p1[1]) == \
            #             (test_p[0] - line_p2[0]) / (test_p[1] - line_p2[1]) else 0
            return 1 if (test_p[0] - line_p1[0]) * (test_p[1] - line_p2[1]) == \
                        (test_p[0] - line_p2[0]) * (test_p[1] - line_p1[1]) else 0

        # TODO: there are many repeated calculation, can be optimized (using hash table to store some information)
        for line_point1 in points:
            for line_point2 in points:  # line_point1 and line_point2 form a line
                if line_point1 == line_point2:
                    continue
                # consider how many other points are also in this line
                line_p_counter = 2  # at least 2 points in a line
                for test_point in points:
                    if test_point == line_point1 or test_point == line_point2:
                        continue
                    line_p_counter += __three_points_in_line(line_point1, line_point2, test_point)
                res = max(res, line_p_counter)

        return res


def main():
    # Example 1: Output: 3
    # points = [[1, 1], [2, 2], [3, 3]]

    # Example 2: Output: 4
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxPoints(points)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
