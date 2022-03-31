#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0973-K-Closest-Points-to-Origin.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-31
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0973 - (Medium) - K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

Description & Requirement:
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
    return the k closest points to the origin (0, 0).

    The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

    You may return the answer in any order. 
    The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation:
        The distance between (1, 3) and the origin is sqrt(10).
        The distance between (-2, 2) and the origin is sqrt(8).
        Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
        We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:
    Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]
    Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
    1 <= k <= points.length <= 10^4
    -10^4 < xi, yi < 10^4
"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # exception case
        assert isinstance(k, int) and k >= 1
        assert isinstance(points, list) and len(points) >= k
        # main method: (record the distance and sort)
        return self._kClosest(points, k)

    def _kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_dict = dict({})
        for point in points:
            if not isinstance(point, list) or len(point) != 2:
                continue
            cur_dist_square = point[0] * point[0] + point[1] * point[1]
            if cur_dist_square not in dist_dict:
                dist_dict[cur_dist_square] = [point]
            else:
                dist_dict[cur_dist_square].append(point)

        dist_point = list(dist_dict.items())
        dist_point.sort(key=lambda x: x[0])

        res = []
        cur_order = 0
        for dist, point_list in dist_point:
            cur_order += len(point_list)
            if len(res) < k:
                res.extend(point_list)
                if len(res) >= k:
                    break
            else:
                break

        return res


def main():
    # Example 1: Output: [[-2,2]]
    # points = [[1, 3], [-2, 2]]
    # k = 1

    # Example 2: Output: [[3,3],[-2,4]]
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.kClosest(points, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
