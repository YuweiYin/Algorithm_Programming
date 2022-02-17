#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0304-Range-Sum-Query-2D-Immutable.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-17
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0304 - (Medium) - Range Sum Query 2D - Immutable
https://leetcode.com/problems/range-sum-query-2d-immutable/

Description & Requirement:
    Given a 2D matrix matrix, handle multiple queries of the following type:
        Calculate the sum of the elements of matrix inside the rectangle 
        defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

    Implement the NumMatrix class:
        NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
        int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix 
            inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example 1:
    Input
        ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
        [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], 
            [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
    Output
        [null, 8, 11, 12]
    Explanation
        NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], 
            [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
        numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
        numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
        numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    -10^5 <= matrix[i][j] <= 10^5
    0 <= row1 <= row2 < m
    0 <= col1 <= col2 < n
    At most 10^4 calls will be made to sumRegion.

Related Problem:
    LC-1314-Matrix-Block-Sum
"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        max_row = len(matrix)
        assert max_row > 0
        max_col = len(matrix[0])
        assert max_col > 0

        self.matrix = matrix

        # get 2-dim prefix sum matrix
        prefix_sum = [[0 for _ in range(max_col + 1)] for _ in range(max_row + 1)]  # first row and col are all 0
        for row_idx in range(1, max_row + 1):  # start from index == 1
            for col_idx in range(1, max_col + 1):
                # pre_sum(i, j) = pre_sum(i-1, j) + pre_sum(i, j-1) - pre_sum(i-1, j-1) + pre_sum(i, j)
                prefix_sum[row_idx][col_idx] = prefix_sum[row_idx - 1][col_idx] + prefix_sum[row_idx][col_idx - 1] - \
                                               prefix_sum[row_idx - 1][col_idx - 1] + matrix[row_idx - 1][col_idx - 1]
        self.prefix_sum = prefix_sum

    def __bounded_prefix_sum(self, r_index: int, c_index: int):
        bounded_r = min(len(self.matrix), max(0, r_index))  # 0 <= bounded_r <= max_row
        bounded_c = min(len(self.matrix[0]), max(0, c_index))  # 0 <= bounded_c <= max_col
        return self.prefix_sum[bounded_r][bounded_c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        assert 0 <= row1 <= row2 < len(self.matrix) and 0 <= col1 <= col2 < len(self.matrix[0])
        return self.__bounded_prefix_sum(row2 + 1, col2 + 1) - self.__bounded_prefix_sum(row1, col2 + 1) - \
            self.__bounded_prefix_sum(row2 + 1, col1) + self.__bounded_prefix_sum(row1, col1)


def main():
    # Example 1: Output: [null, 8, 11, 12]
    #     Explanation
    #         NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1],
    #             [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
    #         numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
    #         numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
    #         numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
    command_list = ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
    param_list = [
        [[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]],
        [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    assert len(command_list) == len(param_list)

    # init instance
    # solution = Solution()

    # run & time
    start = time.process_time()
    obj = NumMatrix(matrix)
    index = 1
    ans = []
    while index < len(param_list):
        row1, col1, row2, col2 = param_list[index]
        ans.append(obj.sumRegion(row1, col1, row2, col2))
        index += 1
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
