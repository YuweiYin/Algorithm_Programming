#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1380-Lucky-Numbers-in-a-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-15
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1380 - (Easy) - Lucky Numbers in a Matrix
https://leetcode.com/problems/lucky-numbers-in-a-matrix/

Description & Requirement:
    Given an m x n matrix of distinct numbers, 
    return all lucky numbers in the matrix in any order.

    A lucky number is an element of the matrix such that 
    it is the minimum element in its row and maximum in its column.

Example 1:
    Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
    Output: [15]
    Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:
    Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    Output: [12]
    Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:
    Input: matrix = [[7,8],[1,2]]
    Output: [7]
    Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= n, m <= 50
    1 <= matrix[i][j] <= 10^5.
    All elements in the matrix are distinct.
"""


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(matrix, list) and len(matrix) > 0 and isinstance(matrix[0], list) and len(matrix[0]) > 0
        max_col = len(matrix[0])
        for row in matrix:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (record the min element of each row and the min element of each row, then scan)
        return self._luckyNumbers(matrix)

    def _luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        max_row = len(matrix)
        assert max_row > 0
        max_col = len(matrix[0])
        assert max_col > 0

        # record the min element of each row
        min_row_element = [min(_row) for _row in matrix]

        # record the max element of each col
        max_col_element = []
        for col_index in range(max_col):
            max_col_element.append(max([_row[col_index] for _row in matrix]))

        res = []
        for row_index in range(max_row):
            for col_index, number in enumerate(matrix[row_index]):
                # a lucky number is the minimum element in its row and maximum in its column.
                if number == min_row_element[row_index] and number == max_col_element[col_index]:
                    res.append(number)
        return res


def main():
    # Example 1: Output: [15]
    # matrix = [
    #     [3, 7, 8],
    #     [9, 11, 13],
    #     [15, 16, 17]
    # ]

    # Example 2: Output: [12]
    # matrix = [
    #     [1, 10, 4, 2],
    #     [9, 3, 8, 7],
    #     [15, 16, 17, 12]
    # ]

    # Example 3: Output: [7]
    matrix = [
        [7, 8],
        [1, 2]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.luckyNumbers(matrix)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
