#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0063-Unique-Paths-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-18
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0063 - (Medium) - Unique Paths II
https://leetcode.com/problems/unique-paths-ii/

Description & Requirement:
    A robot is located at the top-left corner of a m x n grid.

    The robot can only move either down or right at any point in time. 
    The robot is trying to reach the bottom-right corner of the grid.

    Now consider if some obstacles are added to the grids. 
    How many unique paths would there be?

    An obstacle and space is marked as 1 and 0 respectively in the grid.

Example 1:
    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation: There is one obstacle in the middle of the 3x3 grid above.
        There are two ways to reach the bottom-right corner:
        1. Right -> Right -> Down -> Down
        2. Down -> Down -> Right -> Right
Example 2:
    Input: obstacleGrid = [[0,1],[0,0]]
    Output: 1

Constraints:
    m == obstacleGrid.length
    n == obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] is 0 or 1.

Related Problem:
    LC-0062-Unique-Paths
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # exception case
        if not isinstance(obstacleGrid, list) or len(obstacleGrid) <= 0:
            return 0  # Error input type
        if not isinstance(obstacleGrid[0], list) or len(obstacleGrid[0]) <= 0:
            return 0  # Error input type
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0  # the start/target position is blocked
        # main method: (Dynamic Programming)
        #     dp[i][j] is the number of unique paths form (0, 0) to (i, j)
        #     dp equation: dp[i][j] = dp[i-1][j] + dp[i][j-1] if grid[i][j] == 0 else 0
        #     dp init: dp[0: i][0] = 1 when all dp[0: i][0] is 0, later all dp[i+1: ][0] = 0 (encounter obstacle)
        #              dp[0][0: j] = 1 when all dp[0][0: j] is 0, later all dp[0][j+1: ] = 0 (encounter obstacle)
        #     dp aim: get dp[-1][-1]
        return self._uniquePathsWithObstacles(obstacleGrid)

    def _uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        max_row = len(obstacleGrid)
        assert max_row > 0
        max_col = len(obstacleGrid[0])
        assert max_col > 0

        # if there's no obstacle, the same solution as LC-0062-Unique-Paths
        num_obstacle = sum([sum(row) for row in obstacleGrid])
        if max_row == 1 or max_col == 1:  # only one row or one col, at most 1 path. if exist obstacle, then 0 path.
            return 1 if num_obstacle == 0 else 0
        if num_obstacle == 0:
            return self._uniquePathsWithoutObstacles(max_row, max_col)

        # dp[i][j] is the number of unique paths form (0, 0) to (i, j)
        dp = [[0 for _ in range(max_col)] for _ in range(max_row)]

        # dp init: dp[0: i][0] = 1 when all dp[0: i][0] is 0, later all dp[i+1: ][0] = 0 (encounter obstacle)
        #          dp[0][0: j] = 1 when all dp[0][0: j] is 0, later all dp[0][j+1: ] = 0 (encounter obstacle)
        for row_idx in range(max_row):
            if obstacleGrid[row_idx][0] == 0:
                dp[row_idx][0] = 1
            else:
                break

        for col_idx in range(max_col):
            if obstacleGrid[0][col_idx] == 0:
                dp[0][col_idx] = 1
            else:
                break

        # dp equation: dp[i][j] = dp[i-1][j] + dp[i][j-1] if grid[i][j] == 0 else 0
        for row_idx in range(1, max_row):
            for col_idx in range(1, max_col):
                if obstacleGrid[row_idx][col_idx] == 0:
                    dp[row_idx][col_idx] = dp[row_idx - 1][col_idx] + dp[row_idx][col_idx - 1]

        # dp aim: get dp[-1][-1]
        return dp[-1][-1]

    def _uniquePathsWithoutObstacles(self, m: int, n: int) -> int:
        assert isinstance(m, int) and m > 1 and isinstance(n, int) and n > 1

        def __combination_number(x: int, y: int) -> int:
            if x < y:  # swap, guarantee that x >= y
                x, y = y, x
            if y == 0 or y == x:
                return 1
            if y == 1 or y == x - 1:
                return x
            combo = float(1.0)

            x_nums = [i for i in range(x - y + 1, x + 1)]  # x-y+1, x-y+2, ..., x
            y_nums = [i for i in range(1, y + 1)]  # 1, 2, ..., y
            assert len(x_nums) == len(y_nums) == y
            cur_index = 0
            while cur_index < y:
                combo *= x_nums[cur_index] / y_nums[cur_index]  # more likely to overflow if Prod all x_num in x_nums
                cur_index += 1

            return int(round(combo, ndigits=0))

        return __combination_number(m + n - 2, n - 1) if m >= n else __combination_number(m + n - 2, m - 1)


def main():
    # Example 1: Output: 2
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    # Example 2: Output: 1
    # obstacleGrid = [
    #     [0, 1],
    #     [0, 0]
    # ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.uniquePathsWithObstacles(obstacleGrid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
