#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1499-Max-Value-of-Equation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-21
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 1499 - (Hard) - Max Value of Equation
https://leetcode.com/problems/max-value-of-equation/

Description & Requirement:
    You are given an array points containing the coordinates of points on a 2D plane, 
    sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for 
    all 1 <= i < j <= points.length. You are also given an integer k.

    Return the maximum value of the equation yi + yj + |xi - xj| where 
    |xi - xj| <= k and 1 <= i < j <= points.length.

    It is guaranteed that there exists at least one pair of points 
    that satisfy the constraint |xi - xj| <= k.

Example 1:
    Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
    Output: 4
    Explanation: The first two points satisfy the condition |xi - xj| <= 1 and 
        if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points 
        also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
        No other pairs satisfy the condition, so we return the max of 4 and 1.
Example 2:
    Input: points = [[0,0],[3,0],[9,2]], k = 3
    Output: 3
    Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, 
        and give the value of 0 + 0 + |0 - 3| = 3.

Constraints:
    2 <= points.length <= 10^5
    points[i].length == 2
    -10^8 <= xi, yi <= 10^8
    0 <= k <= 2 * 10^8
    xi < xj for all 1 <= i < j <= points.length
    xi form a strictly increasing sequence.
"""


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # exception case
        assert isinstance(points, list) and len(points) >= 2
        assert isinstance(k, int) and k >= 0
        # main method: (deque)
        return self._findMaxValueOfEquation(points, k)

    def _findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        assert isinstance(points, list) and len(points) >= 2
        assert isinstance(k, int) and k >= 0

        res = -int(1e9+7)
        queue = collections.deque()
        for x, y in points:
            while queue and x - queue[0][1] > k:
                queue.popleft()
            if queue:
                res = max(res, x + y + queue[0][0])
            while queue and y - x >= queue[-1][0]:
                queue.pop()
            queue.append([y - x, x])

        return res


def main():
    # Example 1: Output: 4
    points = [[1, 3], [2, 0], [5, 10], [6, -10]]
    k = 1

    # Example 2: Output: 3
    # points = [[0, 0], [3, 0], [9, 2]]
    # k = 3

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.findMaxValueOfEquation(points, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
