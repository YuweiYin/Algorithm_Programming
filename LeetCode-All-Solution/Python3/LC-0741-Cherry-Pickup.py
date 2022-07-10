#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0741-Cherry-Pickup.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-10
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0741 - (Hard) - Cherry Pickup
https://leetcode.com/problems/cherry-pickup/

Description & Requirement:
    You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.
        0 means the cell is empty, so you can pass through,
        1 means the cell contains a cherry that you can pick up and pass through, or
        -1 means the cell contains a thorn that blocks your way.

    Return the maximum number of cherries you can collect by following the rules below:
        Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down 
            through valid path cells (cells with value 0 or 1).
        After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
        When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
        If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.

Example 1:
    Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
    Output: 5
    Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2).
        4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
        Then, the player went left, up, up, left to return home, picking up one more cherry.
        The total number of cherries picked up is 5, and this is the maximum possible.
Example 2:
    Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
    Output: 0

Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 50
    grid[i][j] is -1, 0, or 1.
    grid[0][0] != -1
    grid[n - 1][n - 1] != -1
"""


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1
        max_row = len(grid)
        for row in grid:
            assert isinstance(row, list) and len(row) == max_row
        # main method: (dynamic programming)
        return self._cherryPickup(grid)

    def _cherryPickup(self, grid: List[List[int]]) -> int:
        assert isinstance(grid, list) and len(grid) >= 1

        n = len(grid)

        # dp[i][u][v] means the max sum of cherries when two people start from [u][i-u] and [v][i-v] to [n-1][n-1]
        dp = [[[-int(1e9+7) for _ in range(n)] for _ in range(n)] for _ in range((n << 1) - 1)]
        dp[0][0][0] = grid[0][0]

        for i in range(1, (n << 1) - 1):
            for u_r in range(max(i - n + 1, 0), min(i + 1, n)):  # u_r: the row index of person u
                u_c = i - u_r  # u_c: the col index of person u
                if grid[u_r][u_c] == -1:  # cannot move
                    continue
                for v_r in range(u_r, min(i + 1, n)):  # v_r: the row index of person v
                    v_c = i - v_r  # v_c: the col index of person v
                    if grid[v_r][v_c] == -1:  # cannot move
                        continue
                    res = dp[i - 1][u_r][v_r]  # move towards rightward
                    if u_r > 0:
                        res = max(res, dp[i - 1][u_r - 1][v_r])  # move downward and rightward
                    if v_r > 0:
                        res = max(res, dp[i - 1][u_r][v_r - 1])  # move rightward and downward
                    if u_r > 0 and v_r > 0:
                        res = max(res, dp[i - 1][u_r - 1][v_r - 1])  # both move downward
                    res += grid[u_r][u_c]
                    if u_r != v_r:  # to avoid duplication (pick cherries in the same cell)
                        res += grid[v_r][v_c]
                    dp[i][u_r][v_r] = res

        return max(0, dp[-1][-1][-1])


def main():
    # Example 1: Output: 5
    grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]

    # Example 2: Output: 0
    # grid = [[1, 1, -1], [1, -1, 1], [-1, 1, 1]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.cherryPickup(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
