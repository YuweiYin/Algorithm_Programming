#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0064-Minimum-Path-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-19
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0064 - (Medium) - Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

Description & Requirement:
    Given a m x n grid filled with non-negative numbers, 
    find a path from top left to bottom right, 
    which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.

Example 1:
    Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
    Output: 7
    Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:
    Input: grid = [[1,2,3],[4,5,6]]
    Output: 12

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 100
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # exception case
        if not isinstance(grid, list) or len(grid) <= 0:
            return 0  # Error input type
        if not isinstance(grid[0], list) or len(grid[0]) <= 0:
            return 0  # Error input type
        max_col = len(grid[0])
        for row in grid:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (Dynamic Programming)
        #     dp[i][j] is the minimal sum of path form (0, 0) to (i, j)
        #     dp equation: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        #     dp init: dp[0: i][0] = sum(dp[0: i][0]); dp[0][0: j] = sum(dp[0][0: j])
        #     dp aim: get dp[-1][-1]
        return self._minPathSum(grid)

    def _minPathSum(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        assert max_row > 0
        max_col = len(grid[0])
        assert max_col > 0

        # only one row or col, just sum all numbers
        if max_row == 1 or max_col == 1:
            return sum([sum(row) for row in grid])

        # dp[i][j] is the minimal sum of path form (0, 0) to (i, j)
        dp = [[0 for _ in range(max_col)] for _ in range(max_row)]

        # dp init: dp[0: i][0] = sum(dp[0: i][0]), dp[0][0: j] = sum(dp[0][0: j])
        dp[0][0] = grid[0][0]
        for row_idx in range(1, max_row):
            dp[row_idx][0] = dp[row_idx - 1][0] + grid[row_idx][0]
        for col_idx in range(1, max_col):
            dp[0][col_idx] = dp[0][col_idx - 1] + grid[0][col_idx]

        # dp equation: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        for row_idx in range(1, max_row):
            for col_idx in range(1, max_col):
                dp[row_idx][col_idx] = grid[row_idx][col_idx] + min(dp[row_idx - 1][col_idx], dp[row_idx][col_idx - 1])

        # dp aim: get dp[-1][-1]
        return dp[-1][-1]


def main():
    # Example 1: Output: 7
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    # Example 2: Output: 12
    # grid = [
    #     [1, 2, 3],
    #     [4, 5, 6]
    # ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minPathSum(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
