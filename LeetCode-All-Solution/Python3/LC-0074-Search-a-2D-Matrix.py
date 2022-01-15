#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0074-Search-a-2D-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-15
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0074 - (Medium) - Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/

Description & Requirement:
    Write an efficient algorithm that searches for a value in an m x n matrix. 
    This matrix has the following properties:
        1. Integers in each row are sorted from left to right.
        2. The first integer of each row is greater than the last integer of the previous row.

Example 1:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true
Example 2:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10^4 <= matrix[i][j], target <= 10^4
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # exception case
        if not isinstance(matrix, list) or len(matrix) <= 0:
            return False  # Error input type
        if not isinstance(matrix[0], list) or len(matrix[0]) <= 0:
            return False  # Error input type
        col = len(matrix[0])
        for row in matrix:
            if not isinstance(row, list) or len(row) != col:
                return False
        # main method: (Strategy & Binary Search)
        #    idea: from matrix[0][max_col - 1], if this number >= target, then the target must be in this row
        #        else if this number < target, then the target must be in one of the following rows,
        #        so test matrix[1][max_col - 1], ..., till matrix[max_row - 1][max_col - 1]
        return self._searchMatrix(matrix, target)

    def _searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        assert isinstance(matrix, list) and len(matrix) > 0
        max_row = len(matrix)
        max_col = len(matrix[0])

        cur_row = 0
        cur_col = max_col - 1

        def __binary_search(nums: list, left_idx: int, right_idx: int):
            if left_idx > right_idx:
                return -1

            mid_idx = (left_idx + right_idx) >> 1
            mid_num = nums[mid_idx]
            if target == mid_num:  # bingo
                return mid_idx
            elif target < mid_num:  # go left
                return __binary_search(nums, left_idx, mid_idx - 1)
            else:  # go right
                return __binary_search(nums, mid_idx + 1, right_idx)

        while cur_row < max_row:  # scan to find the right row (follow up: can be optimized using binary search)
            if matrix[cur_row][cur_col] == target:  # bingo
                return True
            elif matrix[cur_row][cur_col] > target:  # the targe is either in this row or not exist
                find_idx = __binary_search(matrix[cur_row], 0, max_col)
                return True if 0 <= find_idx < max_col else False
            else:  # consider the next row
                cur_row += 1

        return False


def main():
    # Example 1: Output: true
    # matrix = [
    #     [1, 3, 5, 7],
    #     [10, 11, 16, 20],
    #     [23, 30, 34, 60]
    # ]
    # target = 3

    # Example 2: Output: false
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 13

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
