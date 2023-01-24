#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1828-Queries-on-Number-of-Points-Inside-a-Circle.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-24
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1828 - (Medium) - Queries on Number of Points Inside a Circle
https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

Description & Requirement:
    You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. 
    Multiple points can have the same coordinates.

    You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle 
    centered at (xj, yj) with a radius of rj.

    For each query queries[j], compute the number of points inside the jth circle. 
    Points on the border of the circle are considered inside.

    Return an array answer, where answer[j] is the answer to the jth query.

Example 1:
    Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
    Output: [3,2,2]
    Explanation: The points and circles are shown above.
        queries[0] is the green circle, queries[1] is the red circle, and queries[2] is the blue circle.
Example 2:
    Input: points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
    Output: [2,3,2,4]
    Explanation: The points and circles are shown above.
        queries[0] is green, queries[1] is red, queries[2] is blue, and queries[3] is purple.

Constraints:
    1 <= points.length <= 500
    points[i].length == 2
    0 <= xi, yi <= 500
    1 <= queries.length <= 500
    queries[j].length == 3
    0 <= xj, yj <= 500
    1 <= rj <= 500
    All coordinates are integers.

Follow up:
    Could you find the answer for each query in better complexity than O(n)?
"""


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(points, list) and len(points) >= 1
        for point in points:
            assert isinstance(point, list) and len(point) == 2
        assert isinstance(queries, list) and len(queries) >= 1
        for query in queries:
            assert isinstance(query, list) and len(query) == 3
        # main method: (deal with each query)
        return self._countPoints(points, queries)

    def _countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        Time: beats %; Space: beats %
        """
        assert isinstance(points, list) and len(points) >= 1
        assert isinstance(queries, list) and len(queries) >= 1

        res = [0] * len(queries)

        for idx, (qx, qy, qr) in enumerate(queries):
            for (px, py) in points:
                if (qx - px) ** 2 + (qy - py) ** 2 <= qr ** 2:
                    res[idx] += 1

        return res


def main():
    # Example 1: Output: [3,2,2]
    # points = [[1, 3], [3, 3], [5, 3], [2, 2]]
    # queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]

    # Example 2: Output: [2,3,2,4]
    points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countPoints(points, queries)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
