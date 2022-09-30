#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0218-The-Skyline-Problem.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-30
=================================================================="""

import sys
import time
from typing import List
import heapq
# import collections
# import functools

"""
LeetCode - 0218 - (Hard) - The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/

Description & Requirement:
    A city's skyline is the outer contour of the silhouette formed by all the buildings in that city 
    when viewed from a distance. Given the locations and heights of all the buildings, 
    return the skyline formed by these buildings collectively.

    The geometric information of each building is given in the array buildings 
    where buildings[i] = [left_i, right_i, height_i]:
        left_i is the x coordinate of the left edge of the i-th building.
        right_i is the x coordinate of the right edge of the i-th building.
        height_i is the height of the ith building.

    You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

    The skyline should be represented as a list of "key points" 
    sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. 
    Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, 
    which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends.
    Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

    Note: There must be no consecutive horizontal lines of equal height in the output skyline. 
    For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; 
    the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

Example 1:
    Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    Explanation:
    Figure A shows the buildings of the input.
    Figure B shows the skyline formed by those buildings. 
        The red points in figure B represent the key points in the output list.
Example 2:
    Input: buildings = [[0,2,3],[2,5,3]]
    Output: [[0,3],[5,0]]

Constraints:
    1 <= buildings.length <= 10^4
    0 <= left_i < right_i <= 2^31 - 1
    1 <= height_i <= 2^31 - 1
    buildings is sorted by left_i in non-decreasing order.
"""


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(buildings, list) and len(buildings) >= 1
        for building in buildings:
            assert isinstance(building, list) and len(building) == 3
            assert building[1] >= building[0] >= 0 and building[2] >= 1
        # main method: (heap)
        return self._getSkyline(buildings)

    def _getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        assert isinstance(buildings, list) and len(buildings) >= 1

        b_lhr = [(_l, -_h, _r) for _l, _r, _h in buildings]
        b_lhr += [(_r, 0, 0) for _l, _r, _h in buildings]
        b_lhr.sort()

        res = [[0, 0]]
        queue = [(0, float('inf'))]
        for left, minus_h, right in b_lhr:
            height = -minus_h
            while left >= queue[0][1]:
                heapq.heappop(queue)
            if height > 0:
                heapq.heappush(queue, (-height, right))
            if res[-1][1] != -queue[0][0]:
                res.append([left, -queue[0][0]])

        return res[1:]


def main():
    # Example 1: Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]

    # Example 2: Output: [[0,3],[5,0]]
    # buildings = [[0, 2, 3], [2, 5, 3]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getSkyline(buildings)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
