#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0130-Surrounded-Regions.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-21
=================================================================="""

import sys
import time
from typing import List
import collections

"""
LeetCode - 0130 - (Medium) - Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

Description & Requirement:
    Given an m x n matrix board containing 'X' and 'O', 
    capture all regions that are 4-directionally surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
    Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    Explanation: Surrounded regions should not be on the border, 
        which means that any 'O' on the border of the board are not flipped to 'X'. 
        Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
        Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:
    Input: board = [["X"]]
    Output: [["X"]]

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # exception case
        if not isinstance(board, list) or len(board) <= 0 or not isinstance(board[0], list) or len(board[0]) <= 0:
            return  # Error input type
        col = len(board[0])
        for row in board:
            if len(row) != col:
                return  # Error input type
        if len(board) == 1 or col == 1:
            return  # no need to change
        # main method: (bfs for each "O", if the current "O" region is 4-directionally surrounded by 'X', flip them)
        self._solve(board)

    def _solve(self, board: List[List[str]]) -> None:
        max_row = len(board)
        assert max_row > 1
        max_col = len(board[0])
        assert max_col > 1

        done_bfs_board = [[False for _ in range(max_col)] for _ in range(max_row)]  # avoid repeat search

        def __bfs(start_row: int, start_col: int):
            if not (0 <= start_row < max_row and 0 <= start_col < max_col):
                return
            if board[start_row][start_col] != "O":  # not an uncharted island
                return
            bfs_queue = collections.deque()
            bfs_queue.append((start_row, start_col))
            done_bfs_board[start_row][start_col] = True  # mark, avoid repeat search

            todo_flip = []  # all points in this region
            surround_flag = True  # if this region is surrounded by "X"

            while len(bfs_queue) > 0:
                _row, _col = bfs_queue.popleft()
                todo_flip.append((_row, _col))

                # if this region touch the border of the board, then it won't be surrounded by "X"
                if _row == 0 or _row == max_row - 1 or _col == 0 or _col == max_col - 1:
                    surround_flag = False
                    # break  # don't break the loop, keep bfs till find all points in this cannot-be-flip region

                if _col + 1 < max_col and board[_row][_col + 1] == "O" and not done_bfs_board[_row][_col + 1]:  # east
                    done_bfs_board[_row][_col + 1] = True
                    bfs_queue.append((_row, _col + 1))
                if _row + 1 < max_row and board[_row + 1][_col] == "O" and not done_bfs_board[_row + 1][_col]:  # south
                    done_bfs_board[_row + 1][_col] = True
                    bfs_queue.append((_row + 1, _col))
                if 0 <= _col - 1 and board[_row][_col - 1] == "O" and not done_bfs_board[_row][_col - 1]:  # west
                    done_bfs_board[_row][_col - 1] = True
                    bfs_queue.append((_row, _col - 1))
                if 0 <= _row - 1 and board[_row - 1][_col] == "O" and not done_bfs_board[_row - 1][_col]:  # north
                    done_bfs_board[_row - 1][_col] = True
                    bfs_queue.append((_row - 1, _col))

            if surround_flag:  # if this region is surrounded by "X", then flip them all
                for point in todo_flip:
                    board[point[0]][point[1]] = "X"

        # bfs for each "O", if the current "O" region is 4-directionally surrounded by 'X', flip them
        for cur_row in range(max_row):
            for cur_col in range(max_col):
                if board[cur_row][cur_col] == "O" and not done_bfs_board[cur_row][cur_col]:
                    __bfs(cur_row, cur_col)


def main():
    # Example 1: Output: [
    #     ["X","X","X","X"],
    #     ["X","X","X","X"],
    #     ["X","X","X","X"],
    #     ["X","O","X","X"]
    # ]
    # board = [
    #     ["X", "X", "X", "X"],
    #     ["X", "O", "O", "X"],
    #     ["X", "X", "O", "X"],
    #     ["X", "O", "X", "X"]
    # ]

    # Example 2: Output: [["X"]]
    # board = [["X"]]

    # Example 3: Output: [
    #     ["X","O","X","O","O","O","O"],
    #     ["X","O","O","O","O","O","O"],
    #     ["X","O","O","O","O","X","O"],
    #     ["O","O","O","O","X","O","X"],
    #     ["O","X","O","O","O","O","O"],
    #     ["O","O","O","O","O","O","O"],
    #     ["O","X","O","O","O","O","O"]
    # ]
    board = [
        ["X", "O", "X", "O", "O", "O", "O"],
        ["X", "O", "O", "O", "O", "O", "O"],
        ["X", "O", "O", "O", "O", "X", "O"],
        ["O", "O", "O", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O"],
        ["O", "X", "O", "O", "O", "O", "O"]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    # ans = solution.numIslands(board)
    solution.solve(board)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    for row in board:
        print(row)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
