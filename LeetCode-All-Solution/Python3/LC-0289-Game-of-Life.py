#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0289-Game-of-Life.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-12
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0289 - (Medium) - Game of Life
https://leetcode.com/problems/game-of-life/

Description & Requirement:
    According to Wikipedia's article: "The Game of Life, also known simply as Life, 
    is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

    The board is made up of an m x n grid of cells, where each cell has an initial state: 
    live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors 
    (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
        Any live cell with fewer than two live neighbors dies as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population.
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    The next state is created by applying the above rules simultaneously to every cell in the current state, 
    where births and deaths occur simultaneously. 
    Given the current state of the m x n grid board, return the next state.

Example 1:
    Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:
    Input: board = [[1,1],[1,0]]
    Output: [[1,1],[1,1]]

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 25
    board[i][j] is 0 or 1.

Follow up:
    Could you solve it in-place? Remember that the board needs to be updated simultaneously: 
        You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite, 
        which would cause problems when the active area encroaches upon the border of the array 
        (i.e., live cells reach the border). How would you address these problems?
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # exception case
        assert isinstance(board, list) and len(board) >= 1
        assert isinstance(board[0], list) and len(board[0]) >= 1
        n = len(board[0])
        for row in board:
            assert isinstance(row, list) and len(row) == n
        # main method: (check 8 neighbors of each cell and determine its next state)
        #     for in-place modification, use numbers -1, 0, 1, 2 to indicate the state change
        #     -1: dead -> live; 0: dead -> dead; 1: live -> live; 2: live -> dead.
        self._gameOfLife(board)

    def _gameOfLife(self, board: List[List[int]]) -> None:
        assert isinstance(board, list) and len(board) >= 1
        assert isinstance(board[0], list) and len(board[0]) >= 1
        m, n = len(board), len(board[0])

        direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def __count_live_neighbors(_r: int, _c: int) -> int:
            counter = 0
            for nei in direction:
                nei_row = _r + nei[0]
                nei_col = _c + nei[1]
                if 0 <= nei_row < m and 0 <= nei_col < n and board[nei_row][nei_col] > 0:
                    counter += 1
            return counter

        for row_idx in range(m):
            for col_idx in range(n):
                # Any live cell with fewer than two live neighbors dies as if caused by under-population.
                # Any live cell with two or three live neighbors lives on to the next generation.
                # Any live cell with more than three live neighbors dies, as if by over-population.
                # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                cur_state = board[row_idx][col_idx]
                live_neighbor_counter = __count_live_neighbors(row_idx, col_idx)
                # -1: dead -> live; 0: dead -> dead; 1: live -> live; 2: live -> dead.
                if cur_state == 1:
                    if live_neighbor_counter < 2:
                        board[row_idx][col_idx] = 2  # live -> dead
                    elif live_neighbor_counter > 3:
                        board[row_idx][col_idx] = 2  # live -> dead
                    else:
                        pass  # live -> live
                else:
                    if live_neighbor_counter == 3:
                        board[row_idx][col_idx] = -1  # dead -> live
                    else:
                        pass  # dead -> dead

        # recover: -1 -> 1; 2 -> 0
        for row_idx in range(m):
            for col_idx in range(n):
                if board[row_idx][col_idx] == -1:
                    board[row_idx][col_idx] = 1
                elif board[row_idx][col_idx] == 2:
                    board[row_idx][col_idx] = 0


def main():
    # Example 1: Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    # board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]

    # Example 2: Output: [[1,1],[1,1]]
    board = [[1, 1], [1, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.gameOfLife(board)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(board)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
