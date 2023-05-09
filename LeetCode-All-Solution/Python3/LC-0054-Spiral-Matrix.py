#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0054-Spiral-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-09
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0054 - (Easy) - Spiral Matrix
https://leetcode.com/problems/spiral-matrix/description/

Description & Requirement:
    Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]
Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(matrix, list) and len(matrix) >= 1 and len(matrix[0]) >= 1
        # main method: (simulate the process)
        return self._spiralOrder(matrix)

    def _spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        assert isinstance(matrix, list) and len(matrix) >= 1 and len(matrix[0]) >= 1

        if not matrix or not matrix[0]:
            return []

        n_row, n_col = len(matrix), len(matrix[0])
        visited = [[False] * n_col for _ in range(n_row)]
        total = n_row * n_col
        order = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_index = 0
        row, col = 0, 0

        for i in range(total):
            order[i] = matrix[row][col]
            visited[row][col] = True
            next_row, next_col = row + directions[direction_index][0], col + directions[direction_index][1]
            if not (0 <= next_row < n_row and 0 <= next_col < n_col and not visited[next_row][next_col]):
                direction_index = (direction_index + 1) % 4
            row += directions[direction_index][0]
            col += directions[direction_index][1]

        return order


def main():
    # Example 1: Output: [1,2,3,6,9,8,7,4,5]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Example 2: Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.spiralOrder(matrix)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
