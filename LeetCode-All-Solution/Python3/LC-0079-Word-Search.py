#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0079-Word-Search.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-24
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0079 - (Medium) - Word Search
https://leetcode.com/problems/word-search/

Description & Requirement:
    Given an m x n grid of characters board and a string word, 
    return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, 
    where adjacent cells are horizontally or vertically neighboring. 
    The same letter cell may not be used more than once.

Example 1:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true
Example 2:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true
Example 3:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false

Constraints:
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # exception case
        if not isinstance(board, list) or len(board) <= 0 or not isinstance(board[0], list) or len(board[0]) <= 0:
            return False  # Error input type
        if not isinstance(word, str) or len(word) <= 0:
            return False  # Error input type
        col = len(board[0])
        for row in board:
            if not isinstance(row, list) or len(row) != col:
                return False  # Error input type
        # main method: (dfs & backtrace.)
        return self._exist(board, word)

    def _exist(self, board: List[List[str]], word: str) -> bool:
        max_row = len(board)
        max_col = len(board[0])
        len_word = len(word)
        assert max_row > 0 and max_col > 0 and len_word > 0

        def __dfs(todo_char_index: int, start_row: int, start_col: int, done_point: set) -> bool:
            if todo_char_index < 0 or todo_char_index >= len_word:  # out of index
                return False
            if word[todo_char_index] != board[start_row][start_col]:  # don't match the current char
                return False
            if todo_char_index == len_word - 1:  # match end
                return True
            # not full matched yet, keep dfs
            if start_col + 1 < max_col and (start_row, start_col + 1) not in done_point:  # go east
                done_point.add((start_row, start_col + 1))  # record used point
                if __dfs(todo_char_index + 1, start_row, start_col + 1, done_point):
                    return True  # if found, return True, else keep searching
                done_point.discard((start_row, start_col + 1))  # backtrace
            if start_row + 1 < max_row and (start_row + 1, start_col) not in done_point:  # go south
                done_point.add((start_row + 1, start_col))  # record used point
                if __dfs(todo_char_index + 1, start_row + 1, start_col, done_point):
                    return True  # if found, return True, else keep searching
                done_point.discard((start_row + 1, start_col))  # backtrace
            if start_col - 1 >= 0 and (start_row, start_col - 1) not in done_point:  # go west
                done_point.add((start_row, start_col - 1))  # record used point
                if __dfs(todo_char_index + 1, start_row, start_col - 1, done_point):
                    return True  # if found, return True, else keep searching
                done_point.discard((start_row, start_col - 1))  # backtrace
            if start_row - 1 >= 0 and (start_row - 1, start_col) not in done_point:  # go north
                done_point.add((start_row - 1, start_col))  # record used point
                if __dfs(todo_char_index + 1, start_row - 1, start_col, done_point):
                    return True  # if found, return True, else keep searching
                done_point.discard((start_row - 1, start_col))  # backtrace
            return False  # can't find a valid path in the board to form the target word

        for row_index in range(max_row):
            for col_index in range(max_col):  # consider every char in the board
                if board[row_index][col_index] == word[0]:  # if match word[0], then start dfs
                    done_dfs_point = set()  # to avoid repeat search
                    done_dfs_point.add((row_index, col_index))
                    # if dfs succeed, then return True, else keep searching
                    if __dfs(0, row_index, col_index, done_dfs_point):
                        return True

        return False  # can't find a valid path in the board to form the target word


def main():
    # Example 1: Output: true
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word = "ABCCED"

    # Example 2: Output: true
    # board = [
    #     ["A", "B", "C", "E"],
    #     ["S", "F", "C", "S"],
    #     ["A", "D", "E", "E"]
    # ]
    # word = "SEE"

    # Example 3: Output: false
    # board = [
    #     ["A", "B", "C", "E"],
    #     ["S", "F", "C", "S"],
    #     ["A", "D", "E", "E"]
    # ]
    # word = "ABCB"

    # Example 4: Output: true
    # board = [
    #     ["a", "b"],
    #     ["c", "d"]
    # ]
    # word = "acdb"

    # Example 5: Output: false
    board = [["a", "a"]]
    word = "aaa"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.exist(board, word)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
