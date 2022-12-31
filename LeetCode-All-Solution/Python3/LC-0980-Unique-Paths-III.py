#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0980-Unique-Paths-III.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-31
=================================================================="""

import sys
import time
from typing import List
from functools import lru_cache
# import collections
# import functools

"""
LeetCode - 0980 - (Easy) - Unique Paths III
https://leetcode.com/problems/unique-paths-iii/

Description & Requirement:
    You are given an m x n integer array grid where grid[i][j] could be:
        1 representing the starting square. There is exactly one starting square.
        2 representing the ending square. There is exactly one ending square.
        0 representing empty squares we can walk over.
        -1 representing obstacles that we cannot walk over.

    Return the number of 4-directional walks from the starting square to the ending square, 
    that walk over every non-obstacle square exactly once.

Example 1:
    Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    Output: 2
    Explanation: We have the following two paths: 
        1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
        2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:
    Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    Output: 4
    Explanation: We have the following four paths: 
        1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
        2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
        3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
        4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:
    Input: grid = [[0,1],[2,0]]
    Output: 0
    Explanation: There is no path that walks over every empty square exactly once.
        Note that the starting and ending square can be anywhere in the grid.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 20
    1 <= m * n <= 20
    -1 <= grid[i][j] <= 2
    There is exactly one starting cell and one ending cell.
"""


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1
        n = len(grid[0])
        for row in grid:
            assert isinstance(row, list) and len(row) == n
        # main method: (dynamic programming)
        return self._uniquePathsIII(grid)

    def _uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        Time: beats 85.79%; Space: beats 7.26%
        """
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1
        m, n = len(grid), len(grid[0])

        paths = 0
        r_idx_start, c_idx_start = 0, 0
        r_idx_target, c_idx_target = 0, 0
        for r_idx, row in enumerate(grid):
            for c_idx, val in enumerate(row):
                if val % 2 == 0:
                    paths |= 1 << (r_idx * n + c_idx)
                if val == 1:  # start
                    r_idx_start, c_idx_start = r_idx, c_idx
                if val == 2:  # target
                    r_idx_target, c_idx_target = r_idx, c_idx

        @lru_cache(maxsize=None)
        def dp(cur_r_idx, cur_c_idx, path):
            if cur_r_idx == r_idx_target and cur_c_idx == c_idx_target:
                return int(path == 0)

            res = 0
            for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = cur_r_idx + direction[0], cur_c_idx + direction[1]
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] % 2 == 0 and path & (1 << (nr * n + nc)):
                        res += dp(nr, nc, path ^ (1 << (nr * n + nc)))

            return res

        return dp(r_idx_start, c_idx_start, paths)


def main():
    # Example 1: Output: 2
    # grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]

    # Example 2: Output: 4
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]

    # Example 3: Output: 0
    # grid = [[0, 1], [2, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.uniquePathsIII(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
