#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1091-Shortest-Path-in-Binary-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-21
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1091 - (Medium) - Shortest Path in Binary Matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/

Description & Requirement:
    Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. 
    If there is no clear path, return -1.

    A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) 
    to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
        All the visited cells of the path are 0.
        All the adjacent cells of the path are 8-directionally connected 
            (i.e., they are different and they share an edge or a corner).
    The length of a clear path is the number of visited cells of this path.

Example 1:
    Input: grid = [[0,1],[1,0]]
    Output: 2
Example 2:
    Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4
Example 3:
    Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
    Output: -1

Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 100
    grid[i][j] is 0 or 1
"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # exception case
        if not isinstance(grid, list) or len(grid) <= 0 or not isinstance(grid[0], list) or len(grid[0]) <= 0:
            return -1  # Error input type
        n = len(grid)
        for row in grid:
            if len(row) != n:
                return -1  # Error input type (need n * n)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1  # start or end is not "clear"
        # main method: (bfs, each time step search all possible path)
        return self._shortestPathBinaryMatrix(grid)

    def _shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Runtime: 484 ms, faster than 99.48% of Python3 online submissions for Shortest Path in Binary Matrix.
        Memory Usage: 14.9 MB, less than 59.43% of Python3 online submissions for Shortest Path in Binary Matrix.
        """
        n = len(grid)
        assert n > 0
        for row in grid:
            assert len(row) == n
        assert grid[0][0] == 0 or grid[n - 1][n - 1] == 0

        time_step = 0
        bfs_queue = [(0, 0)]  # each time step search all possible path, and then set a new queue
        # done_bfs_grid = [[False for _ in range(n)] for _ in range(n)]
        grid[0][0] = 2
        find_flag = False

        while len(bfs_queue) > 0:
            time_step += 1
            new_queue = []
            for point in bfs_queue:
                _row, _col = point
                if _row == n - 1 and _col == n - 1:  # find the destination, done all
                    find_flag = True
                    break
                # if done_bfs_grid[_row][_col]:  # avoid repeat search
                #     continue
                # done_bfs_grid[_row][_col] = True
                # search for valid (val=0) 8-directionally connected neighbors
                if _row + 1 < n and _col + 1 < n and grid[_row + 1][_col + 1] == 0:  # southeast
                    grid[_row + 1][_col + 1] = 2  # avoid repeat search
                    new_queue.append((_row + 1, _col + 1))  # next bfs point
                if _col + 1 < n and grid[_row][_col + 1] == 0:  # east
                    grid[_row][_col + 1] = 2
                    new_queue.append((_row, _col + 1))
                if _row + 1 < n and grid[_row + 1][_col] == 0:  # south
                    grid[_row + 1][_col] = 2
                    new_queue.append((_row + 1, _col))
                if _row - 1 >= 0 and _col + 1 < n and grid[_row - 1][_col + 1] == 0:  # northeast
                    grid[_row - 1][_col + 1] = 2
                    new_queue.append((_row - 1, _col + 1))
                if _row + 1 < n and _col - 1 >= 0 and grid[_row + 1][_col - 1] == 0:  # southwest
                    grid[_row + 1][_col - 1] = 2
                    new_queue.append((_row + 1, _col - 1))
                if _row - 1 >= 0 and grid[_row - 1][_col] == 0:  # north
                    grid[_row - 1][_col] = 2
                    new_queue.append((_row - 1, _col))
                if _col - 1 >= 0 and grid[_row][_col - 1] == 0:  # west
                    grid[_row][_col - 1] = 2
                    new_queue.append((_row, _col - 1))
                if _row - 1 >= 0 and _col - 1 >= 0 and grid[_row - 1][_col - 1] == 0:  # northwest
                    grid[_row - 1][_col - 1] = 2
                    new_queue.append((_row - 1, _col - 1))
            bfs_queue = new_queue

        return time_step if find_flag else -1


def main():
    # Example 1: Output: 2
    # grid = [
    #     [0, 1],
    #     [1, 0]
    # ]

    # Example 2: Output: 4
    # grid = [
    #     [0, 0, 0],
    #     [1, 1, 0],
    #     [1, 1, 0]
    # ]

    # Example 3: Output: -1
    # grid = [
    #     [1, 0, 0],
    #     [1, 1, 0],
    #     [1, 1, 0]
    # ]

    # Example 4: Output: -1
    grid = [
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.shortestPathBinaryMatrix(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
