#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0036-Valid-Sudoku.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-01
=================================================================="""

import sys
import time
from typing import List, Tuple, Union
# import functools

"""
LeetCode - 0036 - (Medium) - Valid Sudoku
https://leetcode.com/problems/valid-sudoku/

Description & Requirement:
    Determine if a 9 x 9 Sudoku board is valid. 
    Only the filled cells need to be validated according to the following rules:
        1. Each row must contain the digits 1-9 without repetition.
        2. Each column must contain the digits 1-9 without repetition.
        3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    Note:
        - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        - Only the filled cells need to be validated according to the mentioned rules.

Example 1:
    Input: board = 
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    Output: true
Example 2:
    Input: board = 
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
        Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # exception case
        if not isinstance(board, list) or len(board) != 9:
            return False
        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return False
        # main method: (just check each row and col and (3 * 3) square)
        #     note that only nine (3 * 3) squares are needed to be checked
        return self._isValidSudoku(board)

    def _isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku_number = 9

        def __check_sudoku(number_list: Union[List[str], Tuple[str]]) -> bool:
            indicator = set()
            for number_str in number_list:
                if number_str == ".":
                    continue
                if number_str not in indicator:  # no a repetition
                    indicator.add(number_str)
                else:  # repeated number
                    return False
            return True

        # check nine rows
        for row in board:
            if not __check_sudoku(row):
                return False

        # check nine cols
        col_idx = 0
        while col_idx < sudoku_number:
            col = [board[row_idx][col_idx] for row_idx in range(sudoku_number)]
            if not __check_sudoku(col):
                return False
            col_idx += 1

        # check nine (3 * 3) squares
        square_row = 0  # the left-up corner index
        square_col = 0  # the left-up corner index
        while square_row < sudoku_number:
            row_1 = board[square_row][square_col: square_col + 3]
            row_2 = board[square_row + 1][square_col: square_col + 3]
            row_3 = board[square_row + 2][square_col: square_col + 3]
            if not __check_sudoku(row_1 + row_2 + row_3):
                return False
            if square_col + 3 >= sudoku_number:  # change row
                square_row += 3
                square_col = (square_col + 3) % sudoku_number
            else:  # change col
                square_col += 3

        return True


def main():
    # Example 1: Output: true
    # board = [
    #     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    # ]

    # Example 2: Output: false
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
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
    ans = solution.isValidSudoku(board)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
