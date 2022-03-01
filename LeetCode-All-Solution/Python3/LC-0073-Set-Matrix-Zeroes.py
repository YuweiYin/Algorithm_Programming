#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0073-Set-Matrix-Zeroes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-01
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0073 - (Medium) - Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/

Description & Requirement:
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

    You must do it [in place](https://en.wikipedia.org/wiki/In-place_algorithm).

Example 1:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1

Follow up:
    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # exception case
        assert isinstance(matrix, list) and len(matrix) > 0
        assert isinstance(matrix[0], list) and len(matrix[0]) > 0
        max_col = len(matrix[0])
        for row in matrix:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (if use space O(m+n), just use O(m) and O(n) lists to indicate whether a row/col need to be set)
        #     O(1) optimize: use the first row and first col of the given matrix to replace aforementioned two lists.
        self._setZeroes(matrix)

    def _setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Runtime: 195 ms, faster than 44.19% of Python3 online submissions for Set Matrix Zeroes.
        Memory Usage: 14.3 MB, less than 99.94% of Python3 online submissions for Set Matrix Zeroes.
        """
        max_row = len(matrix)
        assert max_row > 0
        max_col = len(matrix[0])
        assert max_col > 0

        # since first row and first col is used to indicate the situations of other rows and cols
        # whether first row and first col should be set zeros no not need to be marked by another two variable
        set_first_row = any(num == 0 for num in matrix[0])
        set_first_col = any(matrix[row_idx][0] == 0 for row_idx in range(max_row))

        # check each number in the matrix
        for row_idx in range(1, max_row):
            for col_idx in range(1, max_col):
                if matrix[row_idx][col_idx] == 0:
                    # first row and first col is used to indicate the situations of other rows and cols
                    matrix[row_idx][0] = 0  # this row should be set 0
                    matrix[0][col_idx] = 0  # this col should be set 0

        # do setting (except first row and first col themselves)
        for row_idx in range(1, max_row):
            for col_idx in range(1, max_col):
                if matrix[row_idx][0] == 0 or matrix[0][col_idx] == 0:
                    matrix[row_idx][col_idx] = 0

        # set first row
        if set_first_row:
            for col_idx in range(max_col):
                matrix[0][col_idx] = 0

        # set first col
        if set_first_col:
            for row_idx in range(max_row):
                matrix[row_idx][0] = 0


def main():
    # Example 1: Output: [[1,0,1],[0,0,0],[1,0,1]]
    # matrix = [
    #     [1, 1, 1],
    #     [1, 0, 1],
    #     [1, 1, 1]
    # ]

    # Example 2: Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    # ans = solution.setZeroes(matrix)
    solution.setZeroes(matrix)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    # print(ans)
    print(matrix)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
