#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0576-Out-of-Boundary-Paths.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-16
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0576 - (Medium) - Out of Boundary Paths
https://leetcode.com/problems/out-of-boundary-paths/

Description & Requirement:
    There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. 
    You are allowed to move the ball to one of the four adjacent cells in the grid 
    (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

    Given the five integers m, n, maxMove, startRow, startColumn, 
    return the number of paths to move the ball out of the grid boundary. 
    Since the answer can be very large, return it modulo 109 + 7.

Example 1:
    Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
    Output: 6
Example 2:
    Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
    Output: 12

Constraints:
    1 <= m, n <= 50
    0 <= maxMove <= 50
    0 <= startRow < m
    0 <= startColumn < n
"""


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # exception case
        assert isinstance(m, int) and m >= 1
        assert isinstance(n, int) and n >= 1
        assert isinstance(maxMove, int) and maxMove >= 0
        assert isinstance(startRow, int) and 0 <= startRow < m
        assert isinstance(startColumn, int) and 0 <= startColumn < n
        # main method: (dynamic programming)
        return self._findPaths(m, n, maxMove, startRow, startColumn)

    def _findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        assert isinstance(m, int) and m >= 1
        assert isinstance(n, int) and n >= 1
        assert isinstance(maxMove, int) and maxMove >= 0
        assert isinstance(startRow, int) and 0 <= startRow < m
        assert isinstance(startColumn, int) and 0 <= startColumn < n

        MOD = int(1e9+7)
        res = 0

        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1

        for i in range(maxMove):
            for j in range(m):
                for k in range(n):
                    if dp[i][j][k] > 0:
                        for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                            if 0 <= j1 < m and 0 <= k1 < n:
                                dp[i + 1][j1][k1] = (dp[i + 1][j1][k1] + dp[i][j][k]) % MOD
                            else:
                                res = (res + dp[i][j][k]) % MOD

        return res


def main():
    # Example 1: Output: 6
    # m, n, maxMove, startRow, startColumn = 2, 2, 2, 0, 0

    # Example 2: Output: 12
    m, n, maxMove, startRow, startColumn = 1, 3, 3, 0, 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findPaths(m, n, maxMove, startRow, startColumn)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
