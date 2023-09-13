#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2596-Check-Knight-Tour-Configuration.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-13
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2596 - (Medium) Check Knight Tour Configuration
https://leetcode.com/problems/check-knight-tour-configuration/

Description & Requirement:
    There is a knight on an n x n chessboard. In a valid configuration, 
    the knight starts at the top-left cell of the board and visits every cell on the board exactly once.

    You are given an n x n integer matrix grid consisting of distinct integers 
    from the range [0, n * n - 1] where grid[row][col] indicates that the cell (row, col) 
    is the grid[row][col]th cell that the knight visited. The moves are 0-indexed.

    Return true if grid represents a valid configuration of the knight's movements or false otherwise.

    Note that a valid knight move consists of moving two squares vertically and one square horizontally, 
    or two squares horizontally and one square vertically. 
    The figure below illustrates all the possible eight moves of a knight from some cell.

Example 1:
    Input: grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
    Output: true
    Explanation: The above diagram represents the grid. 
        It can be shown that it is a valid configuration.
Example 2:
    Input: grid = [[0,3,6],[5,8,1],[2,7,4]]
    Output: false
    Explanation: The above diagram represents the grid. 
        The 8th move of the knight is not valid considering its position after the 7th move.

Constraints:
    n == grid.length == grid[i].length
    3 <= n <= 7
    0 <= grid[row][col] < n * n
    All integers in grid are unique.
"""


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        # exception case
        assert isinstance(grid, list) and len(grid) == len(grid[0]) >= 3
        # main method: (simulation)
        return self._checkValidGrid(grid)

    def _checkValidGrid(self, grid: List[List[int]]) -> bool:
        assert isinstance(grid, list) and len(grid) == len(grid[0]) >= 3

        if grid[0][0] != 0:
            return False

        n = len(grid)
        indices = [[] for _ in range(n * n)]
        for i in range(n):
            for j in range(n):
                indices[grid[i][j]] = [i, j]

        for i in range(1, n * n, 1):
            dx = abs(indices[i][0] - indices[i - 1][0])
            dy = abs(indices[i][1] - indices[i - 1][1])
            if dx * dy != 2:
                return False

        return True


def main():
    # Example 1: Output: true
    grid = [[0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [12, 1, 8, 21, 6], [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]]

    # Example 2: Output: false
    # grid = [[0, 3, 6], [5, 8, 1], [2, 7, 4]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.checkValidGrid(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
