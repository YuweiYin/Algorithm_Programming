#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0688-Knight-Probability-in-Chessboard.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-17
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0688 - (Medium) - Knight Probability in Chessboard
https://leetcode.com/problems/knight-probability-in-chessboard/

Description & Requirement:
    On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. 
    The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

    A chess knight has eight possible moves it can make, as illustrated below. 
    Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

    Each time the knight is to move, it chooses one of eight possible moves uniformly at random 
    (even if the piece would go off the chessboard) and moves there.

    The knight continues moving until it has made exactly k moves or has moved off the chessboard.

    Return the probability that the knight remains on the board after it has stopped moving.

Example 1:
    Input: n = 3, k = 2, row = 0, column = 0
    Output: 0.06250
    Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
        From each of those positions, there are also two moves that will keep the knight on the board.
        The total probability the knight stays on the board is 0.0625.
Example 2:
    Input: n = 1, k = 0, row = 0, column = 0
    Output: 1.00000

Constraints:
    1 <= n <= 25
    0 <= k <= 100
    0 <= row, column <= n
"""


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # exception case
        assert isinstance(n, int) and n > 0 and isinstance(k, int) and k >= 0
        assert isinstance(row, int) and 0 <= row <= n and isinstance(column, int) and 0 <= column <= n
        # main method: (Dynamic Programming)
        #     DFS idea: each step, 8 possible moves, the total probability of staying in the chessboard is 8-fold sum.
        #         recursively compute until reaching k steps or going off the chessboard (stay prob = 0)
        #     optimize: DP: dp[i][j][k] is the stay probability when the knight moves to (i, j) and has k+1 steps left
        #     dp equation: dp[i][j][k] = sum(0.125 * dp[last_i][last_j][k-1] for all 8 valid (last_i, last_j) pairs)
        #     dp init: dp[i][j][0], consider each point, 1 step left, calculate stay_prob
        #     dp aim: get dp[row][col][k - 1]
        # return self._knightProbabilityDfs(n, k, row, column)
        return self._knightProbabilityDp(n, k, row, column)

    def _knightProbabilityDfs(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:  # no moves, just check the start position
            return float(1.0) if (0 <= row < n and 0 <= column < n) else float(0.0)
        if row < 0 or row >= n or column < 0 or column >= n:  # start position is out of the chessboard
            return float(0.0)

        # 8 moves
        moves = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

        # stimulate the knight moving process (dfs, correct but TLE)
        def __dfs(r: int, c: int, step: int) -> float:
            if not(0 <= r < n and 0 <= c < n):  # already out of chessboard, so stay_prob == 0
                return float(0.0)
            if step == k:  # in chessboard, and step == k, won't move again, so stay_prob == 1
                return float(1.0)

            # consider all 8 moves, each one weights 0.125
            stay_p = float(0.0)
            for move in moves:
                stay_p += float(0.125) * __dfs(r + move[0], c + move[1], step + 1)

            return stay_p
        return __dfs(row, column, 0)

    def _knightProbabilityDp(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:  # no moves, just check the start position
            return float(1.0) if (0 <= row < n and 0 <= column < n) else float(0.0)
        if row < 0 or row >= n or column < 0 or column >= n:  # start position is out of the chessboard
            return float(0.0)

        # 8 moves
        moves = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

        def __stay_or_out(r: int, c: int) -> float:
            stay_p = float(0.0)
            for _move in moves:
                if 0 <= r + _move[0] < n and 0 <= c + _move[1] < n:  # a valid move, gain 0.125
                    stay_p += float(0.125)
            return stay_p

        # dp[i][j][k] is the stay probability when the knight moves to (i, j) and has k+1 steps left
        dp = [[[float(0.0) for _ in range(k)] for _ in range(n)] for _ in range(n)]

        # dp init: dp[i][j][0], consider each point, 1 step left, calculate stay_prob
        for r_idx in range(n):
            for c_idx in range(n):
                dp[r_idx][c_idx][0] = __stay_or_out(r_idx, c_idx)

        # dp equation: dp[i][j][k] = 0.125 * sum(dp[last_i][last_j][k-1] for all 8 valid (last_i, last_j) pairs)
        for step in range(1, k):  # left (k-1) steps
            for cur_r in range(n):
                for cur_c in range(n):
                    for move in moves:
                        last_r, last_c = cur_r - move[0], cur_c - move[1]
                        if 0 <= last_r < n and 0 <= last_c < n:
                            dp[cur_r][cur_c][step] += dp[last_r][last_c][step - 1]
                    dp[cur_r][cur_c][step] *= float(0.125)

        # dp aim: get dp[row][col][k - 1]
        return dp[row][column][-1]


def main():
    # Example 1: Output: 0.06250
    # n = 3
    # k = 2
    # row = 0
    # column = 0

    # Example 2: Output: 1.00000
    # n = 1
    # k = 0
    # row = 0
    # column = 0

    # Example 3: Output: 0.00019
    n = 8
    k = 30
    row = 6
    column = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.knightProbability(n, k, row, column)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
