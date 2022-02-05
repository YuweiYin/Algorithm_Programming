#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1219-Path-with-Maximum-Gold.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-05
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1219 - (Medium) - Path with Maximum Gold
https://leetcode.com/problems/path-with-maximum-gold/

Description & Requirement:
    In a gold mine grid of size m x n, each cell in this mine has an integer 
    representing the amount of gold in that cell, 0 if it is empty.

    Return the maximum amount of gold you can collect under the conditions:
        Every time you are located in a cell you will collect all the gold in that cell.
        From your position, you can walk one step to the left, right, up, or down.
        You can't visit the same cell more than once.
        Never visit a cell with 0 gold.
        You can start and stop collecting gold from any position in the grid that has some gold.

Example 1:
    Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
    Output: 24
    Explanation:
        [[0,6,0],
         [5,8,7],
         [0,9,0]]
        Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:
    Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    Output: 28
    Explanation:
        [[1,0,7],
         [2,0,6],
         [3,4,5],
         [0,3,0],
         [9,0,20]]
        Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 15
    0 <= grid[i][j] <= 100
    There are at most 25 cells containing gold.
"""


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # exception case
        if not isinstance(grid, list) or len(grid) <= 0 or not isinstance(grid[0], list) or len(grid[0]) <= 0:
            return 0  # Error input type
        len_col = len(grid[0])
        for row in grid:
            if not isinstance(row, list) or len(row) != len_col:
                return 0  # Error input type
        # main method: (DFS from each non-zero gold point, search until no way to go, then get one gold result)
        return self._getMaximumGold(grid)

    def _getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        Runtime: 1430 ms, faster than 74.27% of Python3 online submissions for Path with Maximum Gold.
        Memory Usage: 14.1 MB, less than 79.33% of Python3 online submissions for Path with Maximum Gold.
        """
        max_row = len(grid)
        assert max_row > 0
        max_col = len(grid[0])
        assert max_col > 0

        dfs_visit_map = [[False for _ in range(max_col)] for _ in range(max_row)]

        def __dfs(cur_row: int, cur_col: int, cur_gold: int) -> int:
            # dfs_visit_map[cur_row][cur_col] = True
            cur_gold += grid[cur_row][cur_col]

            # east
            if cur_col + 1 < max_col and grid[cur_row][cur_col + 1] > 0 and not dfs_visit_map[cur_row][cur_col + 1]:
                dfs_visit_map[cur_row][cur_col + 1] = True
                gain_east = __dfs(cur_row, cur_col + 1, cur_gold)
                dfs_visit_map[cur_row][cur_col + 1] = False  # backtrace / unlock point
            else:
                gain_east = cur_gold

            # south
            if cur_row + 1 < max_row and grid[cur_row + 1][cur_col] > 0 and not dfs_visit_map[cur_row + 1][cur_col]:
                dfs_visit_map[cur_row + 1][cur_col] = True
                gain_south = __dfs(cur_row + 1, cur_col, cur_gold)
                dfs_visit_map[cur_row + 1][cur_col] = False  # backtrace / unlock point
            else:
                gain_south = cur_gold

            # west
            if cur_col - 1 >= 0 and grid[cur_row][cur_col - 1] > 0 and not dfs_visit_map[cur_row][cur_col - 1]:
                dfs_visit_map[cur_row][cur_col - 1] = True
                gain_west = __dfs(cur_row, cur_col - 1, cur_gold)
                dfs_visit_map[cur_row][cur_col - 1] = False  # backtrace / unlock point
            else:
                gain_west = cur_gold

            # north
            if cur_row - 1 >= 0 and grid[cur_row - 1][cur_col] > 0 and not dfs_visit_map[cur_row - 1][cur_col]:
                dfs_visit_map[cur_row - 1][cur_col] = True
                gain_north = __dfs(cur_row - 1, cur_col, cur_gold)
                dfs_visit_map[cur_row - 1][cur_col] = False  # backtrace / unlock point
            else:
                gain_north = cur_gold

            # get the max gold path
            return max(gain_east, gain_south, gain_west, gain_north)

        res = 0
        for row_index in range(max_row):
            for col_index in range(max_col):
                # DFS from each non-zero gold point, search until no way to go, then get one gold result
                if grid[row_index][col_index] > 0:
                    # optimize: start from a corner point will be the optimal, because the miner can't go back
                    # form corner point, if it can go east, then can NOT go west, vice versa. so do north and south.
                    # test if this point is a corner point (NO!!! This limit sometimes is not correct!)
                    # if col_index + 1 < max_col and grid[row_index][col_index + 1] > 0:  # east
                    #     can_go_east = True
                    # else:
                    #     can_go_east = False
                    #
                    # if row_index + 1 < max_row and grid[row_index + 1][col_index] > 0:  # south
                    #     can_go_south = True
                    # else:
                    #     can_go_south = False
                    #
                    # if col_index - 1 >= 0 and grid[row_index][col_index - 1] > 0:  # west
                    #     can_go_west = True
                    # else:
                    #     can_go_west = False
                    #
                    # if row_index - 1 >= 0 and grid[row_index - 1][col_index] > 0:  # north
                    #     can_go_north = True
                    # else:
                    #     can_go_north = False
                    #
                    # # only go from the corner point
                    # if (can_go_east and can_go_west) or (can_go_south and can_go_north):
                    #     continue

                    dfs_visit_map = [[False for _ in range(max_col)] for _ in range(max_row)]  # reset visit map
                    dfs_visit_map[row_index][col_index] = True
                    res = max(res, __dfs(row_index, col_index, 0))

        return res


def main():
    # Example 1: Output: 24
    # grid = [
    #     [0, 6, 0],
    #     [5, 8, 7],
    #     [0, 9, 0]
    # ]

    # Example 2: Output: 28
    # grid = [
    #     [1, 0, 7],
    #     [2, 0, 6],
    #     [3, 4, 5],
    #     [0, 3, 0],
    #     [9, 0, 20]
    # ]

    # Example 3: Output: 77
    # grid = [
    #     [0, 0, 19, 5, 8],
    #     [11, 20, 14, 1, 0],
    #     [0, 0, 1, 1, 1],
    #     [0, 2, 0, 2, 0]
    # ]

    # Example 4: Output: 19
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getMaximumGold(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
