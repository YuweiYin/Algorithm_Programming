#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0051-N-Queens.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-04
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0051 - (Hard) - N Queens
https://leetcode.com/problems/n-queens/

Description & Requirement:
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
    such that no two queens attack each other.

    Given an integer n, return all distinct solutions to the n-queens puzzle. 
    You may return the answer in any order.

    Each solution contains a distinct board configuration of the n-queens' placement, 
    where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
    Input: n = 4
    Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:
    Input: n = 1
    Output: [["Q"]]

Constraints:
    1 <= n <= 9
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (backtrace, based on bit manipulation)
        return self._solveNQueens(n)

    def _solveNQueens(self, n: int) -> List[List[str]]:
        """
        Runtime: 64 ms, faster than 81.46% of Python3 online submissions for N-Queens.
        Memory Usage: 14.4 MB, less than 45.52% of Python3 online submissions for N-Queens.
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
        return res


def main():
    # Example 1: Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    n = 4

    # Example 2: Output: [["Q"]]
    # n = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.solveNQueens(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
