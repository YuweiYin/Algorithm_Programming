#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1184-Distance-Between-Bus-Stops.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-24
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1184 - (Easy) - Distance Between Bus Stops
https://leetcode.com/problems/distance-between-bus-stops/

Description & Requirement:
    A bus has n stops numbered from 0 to n - 1 that form a circle. 
    We know the distance between all pairs of neighboring stops where distance[i] is 
    the distance between the stops number i and (i + 1) % n.

    The bus goes along both directions i.e. clockwise and counterclockwise.

    Return the shortest distance between the given start and destination stops.

Example 1:
    Input: distance = [1,2,3,4], start = 0, destination = 1
    Output: 1
    Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.
Example 2:
    Input: distance = [1,2,3,4], start = 0, destination = 2
    Output: 3
    Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.
Example 3:
    Input: distance = [1,2,3,4], start = 0, destination = 3
    Output: 4
    Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.

Constraints:
    1 <= n <= 10^4
    distance.length == n
    0 <= start, destination < n
    0 <= distance[i] <= 10^4
"""


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # exception case
        assert isinstance(start, int) and start >= 0
        assert isinstance(destination, int) and destination >= 0
        assert isinstance(distance, list) and len(distance) >= 1
        for dist in distance:
            assert isinstance(dist, int) and dist >= 0
        # main method: (only two paths, try both)
        return self._distanceBetweenBusStops(distance, start, destination)

    def _distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        assert isinstance(start, int) and start >= 0
        assert isinstance(destination, int) and destination >= 0
        assert isinstance(distance, list) and len(distance) >= 1

        if start == destination:
            return 0

        # distance[i] is the distance between the stops number i and (i + 1) % n
        if start > destination:  # make sure start has a lower index
            start, destination = destination, start

        dist_1 = sum(distance[start: destination])
        dist_2 = sum(distance) - dist_1

        return min(dist_1, dist_2)


def main():
    # Example 1: Output: 1
    # distance = [1, 2, 3, 4]
    # start = 0
    # destination = 1

    # Example 2: Output: 3
    # distance = [1, 2, 3, 4]
    # start = 0
    # destination = 2

    # Example 3: Output: 4
    distance = [1, 2, 3, 4]
    start = 0
    destination = 3

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.distanceBetweenBusStops(distance, start, destination)
    _end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((_end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
