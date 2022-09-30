#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-INTERVIEW-0108-Zero-Matrix-LCCI.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-30
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - INTERVIEW-0108 - (Medium) - Zero Matrix
https://leetcode.cn/problems/zero-matrix-lcci/

Description & Requirement:
    Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

Example 1:
    Input: 
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    Output: 
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]
Example 2:
    Input: 
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    Output: 
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # exception case
        assert isinstance(matrix, list) and len(matrix) > 0
        # main method: (use only one variable to record the modification)
        self._setZeroes(matrix)

    def _setZeroes(self, matrix: List[List[int]]) -> None:
        assert isinstance(matrix, list) and len(matrix) > 0

        m, n = len(matrix), len(matrix[0])
        is_col0_zero = False

        for i in range(m):
            if matrix[i][0] == 0:
                is_col0_zero = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if is_col0_zero:
                matrix[i][0] = 0


def main():
    # Example 1:
    # Output:
    # [
    #   [1,0,1],
    #   [0,0,0],
    #   [1,0,1]
    # ]
    # matrix = [
    #     [1, 1, 1],
    #     [1, 0, 1],
    #     [1, 1, 1]
    # ]

    # Example 2:
    # Output:
    # [
    #   [0,0,0,0],
    #   [0,4,5,0],
    #   [0,3,1,0]
    # ]
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.setZeroes(matrix)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    for row in matrix:
        print(row)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
