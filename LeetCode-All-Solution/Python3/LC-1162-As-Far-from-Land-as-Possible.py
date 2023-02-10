#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1162-As-Far-from-Land-as-Possible.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-10
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1162 - (Medium) - As Far from Land as Possible
https://leetcode.com/problems/as-far-from-land-as-possible/

Description & Requirement:
    Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, 
    find a water cell such that its distance to the nearest land cell is maximized, and return the distance. 
    If no land or water exists in the grid, return -1.

    The distance used in this problem is the Manhattan distance: 
    the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Example 1:
    Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
    Output: 2
    Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:
    Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
    Output: 4
    Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 100
    grid[i][j] is 0 or 1
"""


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1
        n = len(grid)
        for row in grid:
            assert isinstance(row, list) and len(row) == n
        # main method: (multi-source BFS)
        return self._maxDistance(grid)

    def _maxDistance(self, grid: List[List[int]]) -> int:
        assert isinstance(grid, list) and len(grid) >= 1
        n = len(grid)

        distance = -1
        queue = collections.deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j])

        if not queue or len(queue) == n * n:
            return -1

        while len(queue) > 0:
            distance += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for r, c in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                        grid[r][c] = 2
                        queue.append([r, c])

        return distance


def main():
    # Example 1: Output: 2
    # grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    # Example 2: Output: 4
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxDistance(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
