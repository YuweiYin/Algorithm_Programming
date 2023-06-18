#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2328-Number-of-Increasing-Paths-in-a-Grid.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-18
=================================================================="""

import sys
import time
from typing import List
# import collections
import functools

"""
LeetCode - 2328 - (Hard) - Number of Increasing Paths in a Grid
https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

Description & Requirement:
    You are given an m x n integer matrix grid, 
    where you can move from a cell to any adjacent cell in all 4 directions.

    Return the number of strictly increasing paths in the grid such that 
    you can start from any cell and end at any cell. 
    Since the answer may be very large, return it modulo 109 + 7.

    Two paths are considered different if 
    they do not have exactly the same sequence of visited cells.

Example 1:
    Input: grid = [[1,1],[3,4]]
    Output: 8
    Explanation: The strictly increasing paths are:
        - Paths with length 1: [1], [1], [3], [4].
        - Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
        - Paths with length 3: [1 -> 3 -> 4].
        The total number of paths is 4 + 3 + 1 = 8.
Example 2:
    Input: grid = [[1],[2]]
    Output: 3
    Explanation: The strictly increasing paths are:
        - Paths with length 1: [1], [2].
        - Paths with length 2: [1 -> 2].
        The total number of paths is 2 + 1 = 3.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 1000
    1 <= m * n <= 10^5
    1 <= grid[i][j] <= 10^5
"""


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1
        # main method: (memorized search)
        return self._countPaths(grid)

    def _countPaths(self, grid: List[List[int]]) -> int:
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1

        MOD = int(1e9+7)
        m, n = len(grid), len(grid[0])

        @functools.lru_cache(maxsize=None)
        def __dfs(i: int, j: int) -> int:
            res = 1
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j]:
                    res += __dfs(x, y)
            return res % MOD

        return sum(__dfs(i, j) for i in range(m) for j in range(n)) % MOD


def main():
    # Example 1: Output: 8
    grid = [[1, 1], [3, 4]]

    # Example 2: Output: 3
    # grid = [[1], [2]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countPaths(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
