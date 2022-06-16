#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0037-Sudoku-Solver.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-16
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0037 - (Hard) - Valid Sudoku
https://leetcode.com/problems/valid-sudoku/

Description & Requirement:
    Write a program to solve a Sudoku puzzle by filling the empty cells.

    A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    The '.' character indicates empty cells.

Example 1:
    Input: board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    Output: [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
    ]

Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit or '.'.
    It is guaranteed that the input board has only one solution.
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # exception case
        assert isinstance(board, list) and len(board) == 9
        for row in board:
            assert isinstance(row, list) and len(row) == 9
        # main method: (recursion + backtrace + bit manipulation)
        self._solveSudoku(board)

    def _solveSudoku(self, board: List[List[str]]) -> None:
        """
        Runtime: 78 ms, faster than 94.91% of Python3 online submissions for Sudoku Solver.
        Memory Usage: 14.2 MB, less than 21.93% of Python3 online submissions for Sudoku Solver.
        """
        N = 9
        line = [0 for _ in range(N)]
        column = [0 for _ in range(N)]
        block = [[0 for _ in range(3)] for _ in range(3)]
        valid = False
        spaces = list()  # unfilled spaces

        def __flip(_row: int, _col: int, _digit: int):
            line[_row] ^= (1 << _digit)
            column[_col] ^= (1 << _digit)
            block[_row // 3][_col // 3] ^= (1 << _digit)

        def __dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return

            _row, _col = spaces[pos]
            _mask = ~(line[_row] | column[_col] | block[_row // 3][_col // 3]) & 0x1ff
            while _mask:
                digitMask = _mask & (-_mask)
                digit = bin(digitMask).count("0") - 1
                __flip(_row, _col, digit)
                board[_row][_col] = str(digit + 1)
                __dfs(pos + 1)
                __flip(_row, _col, digit)
                _mask &= (_mask - 1)
                if valid:
                    return

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    digit = int(board[row][col]) - 1
                    __flip(row, col, digit)

        while True:
            modified = False
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        mask = ~(line[row] | column[col] | block[row // 3][col // 3]) & 0x1ff
                        if not (mask & (mask - 1)):
                            digit = bin(mask).count("0") - 1
                            __flip(row, col, digit)
                            board[row][col] = str(digit + 1)
                            modified = True
            if not modified:
                break

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    spaces.append((row, col))

        __dfs(0)


def main():
    # Example 1: Output: [
    #     ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    #     ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    #     ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    #     ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    #     ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    #     ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    #     ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    #     ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    #     ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
    # ]
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.solveSudoku(board)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    for row in board:
        print(row)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
