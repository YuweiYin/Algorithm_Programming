#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1254-Number-of-Closed-Islandss.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-06
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1254 - (Medium) - Number of Closed Islands
https://leetcode.com/problems/number-of-closed-islands/

Description & Requirement:
    Given a 2D grid consists of 0s (land) and 1s (water). 
    An island is a maximal 4-directionally connected group of 0s and a closed island 
    is an island totally (all left, top, right, bottom) surrounded by 1s.

    Return the number of closed islands.

Example 1:
    Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    Output: 2
    Explanation: 
        Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:
    Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    Output: 1
Example 3:
    Input: grid = [[1,1,1,1,1,1,1],
                   [1,0,0,0,0,0,1],
                   [1,0,1,1,1,0,1],
                   [1,0,1,0,1,0,1],
                   [1,0,1,1,1,0,1],
                   [1,0,0,0,0,0,1],
                   [1,1,1,1,1,1,1]]
    Output: 2

Constraints:
    1 <= grid.length, grid[0].length <= 100
    0 <= grid[i][j] <=1
"""


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1
        # main method: (DFS)
        return self._closedIsland(grid)

    def _closedIsland(self, grid: List[List[int]]) -> int:
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0),)
        m, n = len(grid), len(grid[0])

        def __dfs(r, c):
            if not (-1 < r < m and -1 < c < n and grid[r][c] == 0):
                return
            grid[r][c] = 1
            for d in directions:
                __dfs(r + d[0], c + d[1])

        for i in range(m):
            __dfs(i, 0)
            __dfs(i, n - 1)

        for j in range(n):
            __dfs(0, j)
            __dfs(m - 1, j)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    __dfs(i, j)
                    res += 1

        return res


def main():
    # Example 1: Output: 2
    # grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0],
    #         [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]

    # Example 2: Output: 1
    # grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]

    # Example 3: Output: 2
    grid = [[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.closedIsland(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
