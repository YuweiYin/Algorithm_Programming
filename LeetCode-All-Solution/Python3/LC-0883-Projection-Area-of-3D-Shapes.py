#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0883-Projection-Area-of-3D-Shapes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-26
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0883 - (Easy) - Projection Area of 3D Shapes
https://leetcode.com/problems/projection-area-of-3d-shapes/

Description & Requirement:
    You are given an n x n grid where we place some 1 x 1 x 1 cubes 
    that are axis-aligned with the x, y, and z axes.

    Each value v = grid[i][j] represents a tower of v cubes placed on top of the cell (i, j).

    We view the projection of these cubes onto the xy, yz, and zx planes.

    A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane. 
    We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

    Return the total area of all three projections.

Example 1:
    Input: grid = [[1,2],[3,4]]
    Output: 17
    Explanation: Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
Example 2:
    Input: grid = [[2]]
    Output: 5
Example 3:
    Input: grid = [[1,0],[0,2]]
    Output: 8

Constraints:
    n == grid.length == grid[i].length
    1 <= n <= 50
    0 <= grid[i][j] <= 50
"""


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and 1 <= len(grid) == len(grid[0])
        # main method: (convert integer n into string, then scan it)
        return self._projectionArea(grid)

    def _projectionArea(self, grid: List[List[int]]) -> int:
        assert isinstance(grid, list) and 1 <= len(grid) == len(grid[0])
        n = len(grid)

        res = 0
        max_val_of_row = [0 for _ in range(n)]  # the highest val of each row (for yz plane)
        max_val_of_col = [0 for _ in range(n)]  # the highest val of each col (for zx plane)

        for row in range(n):
            for col in range(n):
                cur_val = grid[row][col]
                if cur_val > 0:
                    res += 1  # xy plane (aerial view)
                if cur_val > max_val_of_row[row]:
                    max_val_of_row[row] = cur_val
                if cur_val > max_val_of_col[col]:
                    max_val_of_col[col] = cur_val

        return res + sum(max_val_of_row) + sum(max_val_of_col)


def main():
    # Example 1: Output: 17
    # grid = [[1, 2], [3, 4]]

    # Example 2: Output: 5
    # grid = [[2]]

    # Example 3: Output: 8
    grid = [[1, 0], [0, 2]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.projectionArea(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
