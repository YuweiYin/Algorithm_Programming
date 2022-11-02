#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1620-Coordinate-With-Maximum-Network-Quality.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-02
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1620 - (Medium) - Coordinate With Maximum Network Quality
https://leetcode.com/problems/coordinate-with-maximum-network-quality/

Description & Requirement:
    You are given an array of network towers towers, where towers[i] = [xi, yi, qi] denotes the i-th network tower 
    with location (xi, yi) and quality factor qi. All the coordinates are integral coordinates on the X-Y plane, 
    and the distance between the two coordinates is the Euclidean distance.

    You are also given an integer radius where a tower is reachable if the distance is less than or equal to radius. 
    Outside that distance, the signal becomes garbled, and the tower is not reachable.

    The signal quality of the ith tower at a coordinate (x, y) is calculated with the formula ⌊qi / (1 + d)⌋, 
    where d is the distance between the tower and the coordinate. The network quality at a coordinate is 
    the sum of the signal qualities from all the reachable towers.

    Return the array [cx, cy] representing the integral coordinate (cx, cy) where the network quality is maximum. 
    If there are multiple coordinates with the same network quality, 
    return the lexicographically minimum non-negative coordinate.

    Note:
        A coordinate (x1, y1) is lexicographically smaller than (x2, y2) if either:
            x1 < x2, or
            x1 == x2 and y1 < y2.
        ⌊val⌋ is the greatest integer less than or equal to val (the floor function).

Example 1:
    Input: towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
    Output: [2,1]
    Explanation: At coordinate (2, 1) the total quality is 13.
        - Quality of 7 from (2, 1) results in ⌊7 / (1 + sqrt(0)⌋ = ⌊7⌋ = 7
        - Quality of 5 from (1, 2) results in ⌊5 / (1 + sqrt(2)⌋ = ⌊2.07⌋ = 2
        - Quality of 9 from (3, 1) results in ⌊9 / (1 + sqrt(1)⌋ = ⌊4.5⌋ = 4
        No other coordinate has a higher network quality.
Example 2:
    Input: towers = [[23,11,21]], radius = 9
    Output: [23,11]
    Explanation: Since there is only one tower, the network quality is highest right at the tower's location.
Example 3:
    Input: towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
    Output: [1,2]
    Explanation: Coordinate (1, 2) has the highest network quality.

Constraints:
    1 <= towers.length <= 50
    towers[i].length == 3
    0 <= xi, yi, qi <= 50
    1 <= radius <= 50
"""


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        # exception case
        assert isinstance(radius, int) and radius >= 1
        assert isinstance(towers, list) and len(towers) >= 1
        for tower in towers:
            assert isinstance(tower, list) and len(tower) == 3
        # main method: (simulation)
        return self._bestCoordinate(towers, radius)

    def _bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        assert isinstance(radius, int) and radius >= 1
        assert isinstance(towers, list) and len(towers) >= 1

        x_max = max(t[0] for t in towers)
        y_max = max(t[1] for t in towers)
        cx = cy = max_quality = 0
        for x in range(x_max + 1):
            for y in range(y_max + 1):
                quality = 0
                for tx, ty, q in towers:
                    d = (x - tx) ** 2 + (y - ty) ** 2
                    if d <= radius ** 2:
                        quality += int(q / (1 + d ** 0.5))
                if quality > max_quality:
                    cx, cy, max_quality = x, y, quality

        return [cx, cy]


def main():
    # Example 1: Output: [2,1]
    # towers = [[1, 2, 5], [2, 1, 7], [3, 1, 9]]
    # radius = 2

    # Example 2: Output: [23,11]
    # towers = [[23, 11, 21]]
    # radius = 9

    # Example 3: Output: [1,2]
    towers = [[1, 2, 13], [2, 1, 7], [0, 1, 9]]
    radius = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.bestCoordinate(towers, radius)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
