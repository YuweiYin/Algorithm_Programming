#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0221-Maximal-Square.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-19
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0221 - (Medium) - Maximal Square
https://leetcode.com/problems/maximal-square/

Description & Requirement:
    Given an m x n binary matrix filled with 0's and 1's, 
    find the largest square containing only 1's and return its area.

Example 1:
    Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 4
Example 2:
    Input: matrix = [["0","1"],["1","0"]]
    Output: 1
Example 3:
    Input: matrix = [["0"]]
    Output: 0

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] is '0' or '1'.
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # exception case
        if not isinstance(matrix, list) or len(matrix) <= 0:
            return 0  # Error input type
        if not isinstance(matrix[0], list) or len(matrix[0]) <= 0:
            return 0  # Error input type
        max_col = len(matrix[0])
        for row in matrix:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (Dynamic Programming)
        #     dp[i][j] is the max square area using (i, j) as the right-bottom corner when matrix[i][j] == 1
        #     dp equation: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) if matrix[i][j] == 1 else 0
        #     dp init: dp[i][0] = 1 if matrix[i][0] == 1 else 0; dp[0][j] = 1 if matrix[0][j] == 1 else 0
        #     dp aim: get max square area (record in a variable)
        return self._maximalSquare(matrix)

    def _maximalSquare(self, matrix: List[List[str]]) -> int:
        max_row = len(matrix)
        assert max_row > 0
        max_col = len(matrix[0])
        assert max_col > 0

        # only one row or col, return 1 if "1" exists else 0
        if max_row == 1 or max_col == 1:
            for row in matrix:
                for item in row:
                    if item == "1":
                        return 1
            return 0

        # dp[i][j] is the max square area using (i, j) as the right-bottom corner when matrix[i][j] == 1
        dp = [[0 for _ in range(max_col)] for _ in range(max_row)]

        # dp init: dp[i][0] = 1 if matrix[i][0] == 1 else 0; dp[0][j] = 1 if matrix[0][j] == 1 else 0
        for row_idx in range(max_row):
            if matrix[row_idx][0] == "1":
                dp[row_idx][0] = 1
            else:
                dp[row_idx][0] = 0
        for col_idx in range(max_col):
            if matrix[0][col_idx] == "1":
                dp[0][col_idx] = 1
            else:
                dp[0][col_idx] = 0

        # square area = side_length * side_length
        max_side_length = 0
        for row_idx in range(max_row):
            if matrix[row_idx][0] == "1":
                max_side_length = 1
                break
        if max_side_length == 0:
            for col_idx in range(max_col):
                if matrix[0][col_idx] == "1":
                    max_side_length = 1
                    break

        # dp equation: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) if matrix[i][j] == 1 else 0
        for row_idx in range(1, max_row):
            for col_idx in range(1, max_col):
                if matrix[row_idx][col_idx] == "1":
                    dp[row_idx][col_idx] = 1 + min(
                        dp[row_idx - 1][col_idx], dp[row_idx][col_idx - 1], dp[row_idx - 1][col_idx - 1])
                    max_side_length = max(max_side_length, dp[row_idx][col_idx])

        # dp aim: get max square area (record in a variable)
        return max_side_length * max_side_length


def main():
    # Example 1: Output: 4
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]

    # Example 2: Output: 1
    # matrix = [
    #     ["0", "1"],
    #     ["1", "0"]
    # ]

    # Example 3: Output: 0
    # matrix = [["0"]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximalSquare(matrix)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
