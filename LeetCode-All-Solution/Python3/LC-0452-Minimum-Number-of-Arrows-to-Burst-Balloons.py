#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0452-Minimum-Number-of-Arrows-to-Burst-Balloons.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-13
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0452 - (Medium) - Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

Description:
    There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
    The balloons are represented as a 2D integer array `points` where `points[i] = [x_start, x_end]` 
    denotes a balloon whose horizontal diameter stretches between `x_start` and `x_end`. 
    You do not know the exact y-coordinates of the balloons.

    Arrows can be shot up directly vertically (in the positive y-direction) 
    from different points along the x-axis. 
    A balloon with `x_start` and `x_end` is burst by an arrow shot at `x` if `x_start <= x <= x_end`. 
    There is no limit to the number of arrows that can be shot. 
    A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Requirement:
    Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:
    Input: points = [[10,16],[2,8],[1,6],[7,12]]
    Output: 2
    Explanation: The balloons can be burst by 2 arrows:
        - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
        - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
Example 2:
    Input: points = [[1,2],[3,4],[5,6],[7,8]]
    Output: 4
    Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:
    Input: points = [[1,2],[2,3],[3,4],[4,5]]
    Output: 2
    Explanation: The balloons can be burst by 2 arrows:
        - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
        - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:
    1 <= points.length <= 10^5
    points[i].length == 2
    -2^31 <= x_start < x_end <= 2^31 - 1
"""


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # exception case
        if not isinstance(points, list) or len(points) <= 0:
            return 0  # Error input type
        for point in points:
            if not isinstance(point, list) or len(point) != 2:
                return 0  # Error input type
        if len(points) == 1:  # only one balloon, just one shot
            return 1
        # main method: (greedily shot from the max-gain position, i.e., the most overlapped point)
        #     before greedy search, sort the x_end to avoid double loop O(n^2) time
        return self._findMinArrowShots(points)

    def _findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Time: beats 84.86%; Space: beats 70.29%
        """
        len_points = len(points)
        assert len_points > 1

        points.sort(key=lambda x: x[1])
        pre_end = points[0][1]  # the x_end of the first balloon
        arrow_counter = 1  # at least one shot

        for point in points:
            # if the current balloon's x_end > previous balloon's x_start
            # then the previous balloon is burst by one arrow and won't be considered anymore
            if point[0] > pre_end:
                pre_end = point[1]  # change x_end
                arrow_counter += 1  # need a new arrow shot

        return arrow_counter


def main():
    # Example 1: Output: 2
    #     Explanation: The balloons can be burst by 2 arrows:
    #         - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
    #         - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
    # points = [[10, 16], [2, 8], [1, 6], [7, 12]]

    # Example 2: Output: 4
    #     Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
    # points = [[1, 2], [3, 4], [5, 6], [7, 8]]

    # Example 3: Output: 2
    #     Explanation: The balloons can be burst by 2 arrows:
    #         - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
    #         - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
    points = [[1, 2], [2, 3], [3, 4], [4, 5]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findMinArrowShots(points)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
