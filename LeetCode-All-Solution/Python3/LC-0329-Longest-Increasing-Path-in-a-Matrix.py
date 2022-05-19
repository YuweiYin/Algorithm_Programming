#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0329-Longest-Increasing-Path-in-a-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-19
=================================================================="""

import sys
import time
from typing import List
import functools

"""
LeetCode - 0329 - (Hard) - Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Description & Requirement:
    Given an m x n integers matrix, return the length of the longest increasing path in matrix.

    From each cell, you can either move in four directions: left, right, up, or down. 
    You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
    Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:
    Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:
    Input: matrix = [[1]]
    Output: 1

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    0 <= matrix[i][j] <= 2^31 - 1
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # exception case
        assert isinstance(matrix, list) and len(matrix) >= 1
        assert isinstance(matrix[0], list) and len(matrix[0]) >= 1
        max_col = len(matrix[0])
        for row in matrix:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (DFS with memo)
        return self._longestIncreasingPath(matrix)

    def _longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        assert isinstance(matrix, list) and len(matrix) >= 1
        assert isinstance(matrix[0], list) and len(matrix[0]) >= 1
        max_row, max_col = len(matrix), len(matrix[0])

        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        @functools.lru_cache(maxsize=None)
        def __dfs(_r: int, _c: int) -> int:
            max_path_len = 1
            for dx, dy in DIRS:
                next_r, next_c = _r + dx, _c + dy
                if 0 <= next_r < max_row and 0 <= next_c < max_col and matrix[_r][_c] < matrix[next_r][next_c]:
                    max_path_len = max(max_path_len, __dfs(next_r, next_c) + 1)
            return max_path_len

        res = 1
        for cur_row in range(max_row):
            for cur_col in range(max_col):
                res = max(res, __dfs(cur_row, cur_col))  # start from every point

        return res


def main():
    # Example 1: Output: 4
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]

    # Example 2: Output: 4
    # matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]

    # Example 3: Output: 1
    # matrix = [[1]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestIncreasingPath(matrix)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
