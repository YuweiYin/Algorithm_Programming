#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0782-Transform-to-Chessboard.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-23
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0782 - (Hard) - Transform to Chessboard
https://leetcode.com/problems/transform-to-chessboard/

Description & Requirement:
    You are given an n x n binary grid board. 
    In each move, you can swap any two rows with each other, or any two columns with each other.

    Return the minimum number of moves to transform the board into a chessboard board. 
    If the task is impossible, return -1.

    A chessboard board is a board where no 0's and no 1's are 4-directionally adjacent.

Example 1:
    Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
    Output: 2
    Explanation: One potential sequence of moves is shown.
        The first move swaps the first and second column.
        The second move swaps the second and third row.
Example 2:
    Input: board = [[0,1],[1,0]]
    Output: 0
    Explanation: Also note that the board with 0 in the top left corner, is also a valid chessboard.
Example 3:
    Input: board = [[1,0],[1,0]]
    Output: -1
    Explanation: No matter what sequence of moves you make, you cannot end with a valid chessboard.

Constraints:
    n == board.length
    n == board[i].length
    2 <= n <= 30
    board[i][j] is either 0 or 1.
"""


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        # exception case
        assert isinstance(board, list) and len(board) >= 2
        n = len(board)
        for row in board:
            assert isinstance(row, list) and len(row) == n
        # main method: (bit manipulation)
        return self._movesToChessboard(board)

    def _movesToChessboard(self, board: List[List[int]]) -> int:
        assert isinstance(board, list) and len(board) >= 2
        n = len(board)

        # the first row and col
        mask_row, mask_col = 0, 0
        for i in range(n):
            mask_row |= board[0][i] << i
            mask_col |= board[i][0] << i
        mask_row_reverse = ((1 << n) - 1) ^ mask_row
        mask_col_reverse = ((1 << n) - 1) ^ mask_col
        row_counter, col_counter = 0, 0
        for i in range(n):
            cur_mask_row, cur_mask_col = 0, 0
            for j in range(n):
                cur_mask_row |= board[i][j] << j
                cur_mask_col |= board[j][i] << j
            # check if each row and col are valid
            if cur_mask_row != mask_row and cur_mask_row != mask_row_reverse or \
                    cur_mask_col != mask_col and cur_mask_col != mask_col_reverse:
                return -1
            row_counter += cur_mask_row == mask_row  # record the number of rows that is same with the first row
            col_counter += cur_mask_col == mask_col  # record the number of cols that is same with the first col

        def __bit_count(integer: int):
            return bin(integer).count("1")

        def getMoves(mask: int, count: int) -> int:
            ones = __bit_count(mask)
            n_half = n >> 1
            if n & 1:
                # if n is odd, then the difference between the number of "1" and "0" in each line is 1
                if abs(n - (ones << 1)) != 1 or abs(n - (count << 1)) != 1:
                    return -1
                if ones == n_half:
                    # the least swap operations that change all the even bits to "1"
                    return n_half - __bit_count(mask & 0xAAAAAAAA)
                else:
                    # the least swap operations that change all the odd bits to "1"
                    return ((n + 1) >> 1) - __bit_count(mask & 0x55555555)
            else:
                # if n is even, then the number of "1" and "0" in each line is equal
                if ones != n_half or count != n_half:
                    return -1
                # the least swap operations that change all the even bits to "1"
                count_even = n_half - __bit_count(mask & 0xAAAAAAAA)
                # the least swap operations that change all the odd bits to "1"
                count_odd = n_half - __bit_count(mask & 0x55555555)
                return min(count_even, count_odd)

        row_moves = getMoves(mask_row, row_counter)
        col_moves = getMoves(mask_col, col_counter)

        return -1 if row_moves == -1 or col_moves == -1 else row_moves + col_moves


def main():
    # Example 1: Output: 2
    board = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]

    # Example 2: Output: 0
    # board = [[0, 1], [1, 0]]

    # Example 3: Output: -1
    # board = [[1, 0], [1, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.movesToChessboard(board)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
