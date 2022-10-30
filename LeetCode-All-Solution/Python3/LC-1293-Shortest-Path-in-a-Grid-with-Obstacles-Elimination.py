#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1293-Shortest-Path-in-a-Grid-with-Obstacles-Elimination.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-30
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1293 - (Hard) - Shortest Path in a Grid with Obstacles Elimination
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

Description & Requirement:
    You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
    You can move up, down, left, or right from and to an empty cell in one step.

    Return the minimum number of steps to walk from the upper left corner (0, 0) 
    to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. 
    If it is not possible to find such walk return -1.

Example 1:
    Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
    Output: 6
    Explanation: 
        The shortest path without eliminating any obstacle is 10.
        The shortest path with one obstacle elimination at position (3,2) is 6. 
        Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:
    Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
    Output: -1
    Explanation: We need to eliminate at least two obstacles to find such a walk.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 40
    1 <= k <= m * n
    grid[i][j] is either 0 or 1.
    grid[0][0] == grid[m - 1][n - 1] == 0
"""


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1
        m = len(grid)
        n = len(grid[0])
        assert isinstance(k, int) and 1 <= k <= m * n
        for row in grid:
            assert isinstance(row, list) and len(row) == n
        # main method: (BFS)
        return self._shortestPath(grid, k)

    def _shortestPath(self, grid: List[List[int]], k: int) -> int:
        assert isinstance(grid, list) and len(grid) >= 1
        m = len(grid)
        n = len(grid[0])
        assert isinstance(k, int) and 1 <= k <= m * n

        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0

        k = min(k, m + n - 3)
        visited = set()
        visited.add((0, 0, k))
        q = collections.deque([(0, 0, k)])

        step = 0
        # max_step = m + n - 2
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while len(q) > 0:
            step += 1
            cnt = len(q)
            for _ in range(cnt):
                x, y, rest = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 0 and (nx, ny, rest) not in visited:
                            if nx == m - 1 and ny == n - 1:
                                return step
                            q.append((nx, ny, rest))
                            visited.add((nx, ny, rest))
                        elif grid[nx][ny] == 1 and rest > 0 and (nx, ny, rest - 1) not in visited:
                            q.append((nx, ny, rest - 1))
                            visited.add((nx, ny, rest - 1))

        return -1


def main():
    # Example 1: Output: 6
    grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
    k = 1

    # Example 2: Output: -1
    # grid = [[0, 1, 1], [1, 1, 1], [1, 0, 0]]
    # k = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.shortestPath(grid, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
