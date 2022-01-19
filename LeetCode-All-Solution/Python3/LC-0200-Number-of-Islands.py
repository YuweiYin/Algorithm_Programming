#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0200-Number-of-Islands.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-19
=================================================================="""

import sys
import time
from typing import List
import collections

"""
LeetCode - 0200 - (Medium) - Number of Islands
https://leetcode.com/problems/number-of-islands/

Description & Requirement:
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
    return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.

Example 1:
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1
Example 2:
    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # exception case
        if not isinstance(grid, list) or len(grid) <= 0 or not isinstance(grid[0], list) or len(grid[0]) <= 0:
            return 0  # Error input type
        col = len(grid[0])
        for row in grid:
            if len(row) != col:
                return 0  # Error input type
        # main method: (bfs for each uncharted map dot)
        return self._numIslands(grid)

    def _numIslands(self, grid: List[List[str]]) -> int:
        max_row = len(grid)
        assert max_row > 0
        max_col = len(grid[0])
        assert max_col > 0

        def __bfs(start_row: int, start_col: int) -> int:
            if not (0 <= start_row < max_row and 0 <= start_col < max_col):
                return 0
            if grid[start_row][start_col] != "1":  # not an uncharted island
                return 0
            bfs_queue = collections.deque()
            bfs_queue.append((start_row, start_col))
            grid[start_row][start_col] = "2"  # mark as charted island
            while len(bfs_queue) > 0:
                _row, _col = bfs_queue.popleft()
                if _col + 1 < max_col and grid[_row][_col + 1] == "1":  # east
                    grid[_row][_col + 1] = "2"
                    bfs_queue.append((_row, _col + 1))
                if _row + 1 < max_row and grid[_row + 1][_col] == "1":  # south
                    grid[_row + 1][_col] = "2"
                    bfs_queue.append((_row + 1, _col))
                if 0 <= _col - 1 and grid[_row][_col - 1] == "1":  # west
                    grid[_row][_col - 1] = "2"
                    bfs_queue.append((_row, _col - 1))
                if 0 <= _row - 1 and grid[_row - 1][_col] == "1":  # north
                    grid[_row - 1][_col] = "2"
                    bfs_queue.append((_row - 1, _col))
            return 1  # find one whole island

        island_counter = 0
        for cur_row in range(max_row):
            for cur_col in range(max_col):
                island_counter += __bfs(cur_row, cur_col)  # bfs for each uncharted map dot

        return island_counter


def main():
    # Example 1: Output: 1
    # grid = [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]

    # Example 2: Output: 3
    # grid = [
    #     ["1", "1", "0", "0", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "1", "0", "0"],
    #     ["0", "0", "0", "1", "1"]
    # ]

    # Example 3: Output: 3
    grid = [
        ["1", "0", "1", "1", "0", "1", "1"]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numIslands(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
