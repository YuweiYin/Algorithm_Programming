#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0240-Search-a-2D-Matrix-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-14
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0240 - (Medium) - Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/

Description & Requirement:
    Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
    This matrix has the following properties:
        Integers in each row are sorted in ascending from left to right.
        Integers in each column are sorted in ascending from top to bottom.

Example 1:
    Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
    Output: true
Example 2:
    Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
    Output: false

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= n, m <= 300
    -10^9 <= matrix[i][j] <= 10^9
    All the integers in each row are sorted in ascending order.
    All the integers in each column are sorted in ascending order.
    -10^9 <= target <= 10^9
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # exception case
        assert isinstance(matrix, list) and len(matrix) > 0
        max_col = len(matrix[0])
        for row in matrix:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (if row[0] <= target <= row[-1] and __binary_search(row, 0, max_col - 1, target) return True)
        # other idea: from (i, j) == (0, max_col - 1)
        #     if target == matrix[i][j], return True
        #     if target < matrix[i][j], j -= 1
        #     if target > matrix[i][j], i += 1
        return self._searchMatrix(matrix, target)

    def _searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Runtime: 168 ms, faster than 91.78% of Python3 online submissions for Search a 2D Matrix II.
        Memory Usage: 20.5 MB, less than 30.50% of Python3 online submissions for Search a 2D Matrix II.
        """
        max_row = len(matrix)
        assert max_row > 0
        max_col = len(matrix[0])
        assert max_col > 0

        def __binary_search(array: list, left: int, right: int, tgt: int) -> bool:
            if left > right:
                return False
            if left == right:
                return array[left] == tgt
            mid = (left + right) >> 1
            if tgt == array[mid]:
                return True
            elif tgt < array[mid]:
                return __binary_search(array, left, mid - 1, tgt)
            else:
                return __binary_search(array, mid + 1, right, tgt)

        for row in matrix:
            if row[0] <= target <= row[-1] and __binary_search(row, 0, max_col - 1, target):
                return True
        return False


def main():
    # Example 1: Output: true
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 5

    # Example 2: Output: false
    # matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    # target = 20

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.searchMatrix(matrix, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
