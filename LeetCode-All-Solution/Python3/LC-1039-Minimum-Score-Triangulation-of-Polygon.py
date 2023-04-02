#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1039-Minimum-Score-Triangulation-of-Polygon.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-02
=================================================================="""

import sys
import time
from typing import List
# import collections
import functools

"""
LeetCode - 1039 - (Medium) - Minimum Score Triangulation of Polygon
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

Description & Requirement:
    You have a convex n-sided polygon where each vertex has an integer value. 
    You are given an integer array values where values[i] is the value of the ith vertex (i.e., clockwise order).

    You will triangulate the polygon into n - 2 triangles. For each triangle, 
    the value of that triangle is the product of the values of its vertices, and 
    the total score of the triangulation is the sum of these values over all n - 2 triangles in the triangulation.

    Return the smallest possible total score that you can achieve with some triangulation of the polygon.

Example 1:
    Input: values = [1,2,3]
    Output: 6
    Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
Example 2:
    Input: values = [3,7,4,5]
    Output: 144
    Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
        The minimum score is 144.
Example 3:
    Input: values = [1,3,1,4,1,5]
    Output: 13
    Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.

Constraints:
    n == values.length
    3 <= n <= 50
    1 <= values[i] <= 100
"""


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # exception case
        assert isinstance(values, list) and len(values) >= 3
        # main method: (dynamic programming)
        return self._minScoreTriangulation(values)

    def _minScoreTriangulation(self, values: List[int]) -> int:
        assert isinstance(values, list) and len(values) >= 3

        @functools.lru_cache(maxsize=None)
        def __dp(i, j):
            if i + 2 > j:
                return 0

            if i + 2 == j:
                return values[i] * values[i + 1] * values[j]

            return min((values[i] * values[k] * values[j] + __dp(i, k) + __dp(k, j)) for k in range(i + 1, j))

        return __dp(0, len(values) - 1)


def main():
    # Example 1: Output: 6
    values = [1, 2, 3]

    # Example 2: Output: 144
    # values = [3, 7, 4, 5]

    # Example 3: Output: 13
    # values = [1, 3, 1, 4, 1, 5]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minScoreTriangulation(values)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
