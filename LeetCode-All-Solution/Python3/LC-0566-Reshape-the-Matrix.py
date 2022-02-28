#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0566-Reshape-the-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-28
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0566 - (Easy) - Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/

Description & Requirement:
    In MATLAB, there is a handy function called reshape which 
    can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

    You are given an m x n matrix mat and two integers r and c 
    representing the number of rows and the number of columns of the wanted reshaped matrix.

    The reshaped matrix should be filled with all the elements of the original matrix 
    in the same row-traversing order as they were.

    If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; 
    Otherwise, output the original matrix.

Example 1:
    Input: mat = [[1,2],[3,4]], r = 1, c = 4
    Output: [[1,2,3,4]]
Example 2:
    Input: mat = [[1,2],[3,4]], r = 2, c = 4
    Output: [[1,2],[3,4]]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    -1000 <= mat[i][j] <= 1000
    1 <= r, c <= 300
"""


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # exception case
        assert isinstance(mat, list) and len(mat) > 0
        assert isinstance(mat[0], list) and len(mat[0]) > 0
        max_col = len(mat[0])
        for row in mat:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (if r and c is valid, then row-wise scan all element to a new (r * c) matrix.)
        return self._matrixReshape(mat, r, c)

    def _matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        max_row = len(mat)
        assert max_row > 0
        max_col = len(mat[0])
        assert max_col > 0

        total_element = max_row * max_col
        if total_element != r * c:  # not valid
            return mat

        res = [[0 for _ in range(c)] for _ in range(r)]

        row_mat, col_mat = 0, 0
        row_res, col_res = 0, 0
        while row_mat < max_row:
            res[row_res][col_res] = mat[row_mat][col_mat]
            # move res matrix cursor
            col_res += 1
            if col_res == c:
                col_res = 0
                row_res += 1
            # move mat matrix cursor
            col_mat += 1
            if col_mat == max_col:
                col_mat = 0
                row_mat += 1

        return res


def main():
    # Example 1: Output: [[1,2,3,4]]
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4

    # Example 2: Output: [[1,2],[3,4]]
    # mat = [[1, 2], [3, 4]]
    # r = 2
    # c = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.matrixReshape(mat, r, c)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
