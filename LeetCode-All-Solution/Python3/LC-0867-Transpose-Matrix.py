#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0867-Transpose-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-02
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0867 - (Easy) - Transpose Matrix
https://leetcode.com/problems/transpose-matrix/

Description & Requirement:
    Given a 2D integer array matrix, return the transpose of matrix.

    The transpose of a matrix is the matrix flipped over its main diagonal, 
    switching the matrix's row and column indices.

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:
    Input: matrix = [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 1000
    1 <= m * n <= 10^5
    -10^9 <= matrix[i][j] <= 10^9
"""


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(matrix, list) and len(matrix) >= 1 and len(matrix[0]) >= 1
        max_col = len(matrix[0])
        for row in matrix:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (vertically traverse)
        return self._transpose(matrix)

    def _transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        max_row, max_col = len(matrix), len(matrix[0])

        res_list = []
        for c_idx in range(max_col):
            new_row = []
            for r_idx in range(max_row):
                new_row.append(matrix[r_idx][c_idx])
            res_list.append(new_row)

        return res_list


def main():
    # Example 1: Output: [[1,4,7],[2,5,8],[3,6,9]]
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Example 2: Output: [[1,4],[2,5],[3,6]]
    matrix = [[1, 2, 3], [4, 5, 6]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.transpose(matrix)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
