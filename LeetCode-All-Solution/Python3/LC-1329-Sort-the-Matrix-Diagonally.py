#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1329-Sort-the-Matrix-Diagonally.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-28
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1329 - (Medium) - Sort the Matrix Diagonally
https://leetcode.com/problems/sort-the-matrix-diagonally/

Description & Requirement:
    A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column 
    and going in the bottom-right direction until reaching the matrix's end. 
    For example, the matrix diagonal starting from mat[2][0], 
    where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

    Given an m x n matrix mat of integers, 
    sort each matrix diagonal in ascending order and return the resulting matrix.

Example 1:
    Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
Example 2:
    Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
    Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    1 <= mat[i][j] <= 100
"""


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(mat, list) and len(mat) >= 1 and len(mat[0]) >= 1
        n = len(mat[0])
        for row in mat:
            assert isinstance(row, list) and len(row) == n
        # main method: (sort each diagonal)
        return self._diagonalSort(mat)

    def _diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Runtime: 90 ms, faster than 90.67% of Python3 online submissions for Sort the Matrix Diagonally.
        Memory Usage: 14.2 MB, less than 95.10% of Python3 online submissions for Sort the Matrix Diagonally.
        """
        assert isinstance(mat, list) and len(mat) >= 1 and len(mat[0]) >= 1
        m, n = len(mat), len(mat[0])

        # enumerate the diagonal points of the first row
        for j in range(n):
            diag_len = m if m < n - j else n - j
            nums = [0 for _ in range(diag_len)]
            for x in range(diag_len):
                nums[x] = mat[x][j + x]
            nums.sort()
            for x in range(diag_len):
                mat[x][j + x] = nums[x]

        # enumerate the diagonal points of the first column
        for i in range(1, m):
            diag_len = n if n < m - i else m - i
            nums = [0 for _ in range(diag_len)]
            for x in range(diag_len):
                nums[x] = mat[i + x][x]
            nums.sort()
            for x in range(diag_len):
                mat[i + x][x] = nums[x]

        return mat


def main():
    # Example 1: Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
    # mat = [
    #     [3, 3, 1, 1],
    #     [2, 2, 1, 2],
    #     [1, 1, 1, 2]
    # ]

    # Example 2: Output: [
    #   [5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
    mat = [
        [11, 25, 66, 1, 69, 7],
        [23, 55, 17, 45, 15, 52],
        [75, 31, 36, 44, 58, 8],
        [22, 27, 33, 25, 68, 4],
        [84, 28, 14, 11, 5, 50]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.diagonalSort(mat)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
