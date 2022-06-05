#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0052-N-Queens-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-05
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0052 - (Hard) - N Queens II
https://leetcode.com/problems/n-queens-ii/

Description & Requirement:
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
    such that no two queens attack each other.

    Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
    Input: n = 4
    Output: 2
    Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:
    Input: n = 1
    Output: 1

Constraints:
    1 <= n <= 9
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (backtrace, based on bit manipulation)
        return self._totalNQueens(n)

    def _totalNQueens(self, n: int) -> int:
        """
        Runtime: 32 ms, faster than 99.85% of Python3 online submissions for N-Queens II.
        Memory Usage: 14.2 MB, less than 5.13% of Python3 online submissions for N-Queens II.
        """
        assert isinstance(n, int) and n >= 1

        res = []
        queens = [-1 for _ in range(n)]
        row = ["." for _ in range(n)]

        def __get_board():
            board = []
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def __solve_n_queens(cur_row: int, cur_col: int, diagonal: int, diagonal_rev: int):
            if cur_row == n:
                board = __get_board()
                res.append(board)
            else:
                available_pos = ((1 << n) - 1) & (~(cur_col | diagonal | diagonal_rev))
                while available_pos:
                    pos = available_pos & (-available_pos)
                    available_pos = available_pos & (available_pos - 1)
                    queens[cur_row] = bin(pos - 1).count("1")
                    __solve_n_queens(
                        cur_row + 1, cur_col | pos, (diagonal | pos) << 1, (diagonal_rev | pos) >> 1)

        __solve_n_queens(0, 0, 0, 0)
        return len(res)


def main():
    # Example 1: Output: 2
    n = 4

    # Example 2: Output: 1
    # n = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.totalNQueens(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
