#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0048-Rotate-Image.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-13
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0048 - (Medium) - Rotate Image
https://leetcode.com/problems/rotate-image/

Description & Requirement:
    You are given an n x n 2D matrix representing an image, 
    rotate the image by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
    DO NOT allocate another 2D matrix and do the rotation.

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # exception case
        assert isinstance(matrix, list) and len(matrix) > 0
        n = len(matrix)
        for row in matrix:
            assert isinstance(row, list) and len(row) == n
        # main method: (rotate 4 items at a time)
        self._rotate(matrix)

    def _rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        assert n > 0
        if n == 1:
            return

        for row in range(n >> 1):
            for col in range(row, n - 1 - row):
                temp = matrix[row][col]
                matrix[row][col] = matrix[n - 1 - col][row]
                matrix[n - 1 - col][row] = matrix[n - 1 - row][n - 1 - col]
                matrix[n - 1 - row][n - 1 - col] = matrix[col][n - 1 - row]
                matrix[col][n - 1 - row] = temp


def main():
    # Example 1: Output: [[7,4,1],[8,5,2],[9,6,3]]
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Example 2: Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.rotate(matrix)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(matrix)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
