#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1605-Find-Valid-Matrix-Given-Row-and-Column-Sums.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-14
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1605 - (Medium) - Find Valid Matrix Given Row and Column Sums
https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

Description & Requirement:
    You are given two arrays rowSum and colSum of non-negative integers where 
    rowSum[i] is the sum of the elements in the i-th row and 
    colSum[j] is the sum of the elements of the j-th column of a 2D matrix. 
    In other words, you do not know the elements of the matrix, 
    but you do know the sums of each row and column.

    Find any matrix of non-negative integers of size rowSum.length x colSum.length that 
    satisfies the rowSum and colSum requirements.

    Return a 2D array representing any matrix that fulfills the requirements. 
    It's guaranteed that at least one matrix that fulfills the requirements exists.

Example 1:
    Input: rowSum = [3,8], colSum = [4,7]
    Output: [[3,0],
             [1,7]]
    Explanation: 
        0th row: 3 + 0 = 3 == rowSum[0]
        1st row: 1 + 7 = 8 == rowSum[1]
        0th column: 3 + 1 = 4 == colSum[0]
        1st column: 0 + 7 = 7 == colSum[1]
        The row and column sums match, and all matrix elements are non-negative.
        Another possible matrix is: [[1,2],
                                     [3,5]]
Example 2:
    Input: rowSum = [5,7,10], colSum = [8,6,8]
    Output: [[0,5,0],
             [6,1,0],
             [2,0,8]]

Constraints:
    1 <= rowSum.length, colSum.length <= 500
    0 <= rowSum[i], colSum[i] <= 10^8
    sum(rowSum) == sum(colSum)
"""


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # exception case
        assert isinstance(rowSum, list) and len(rowSum) >= 1
        assert isinstance(colSum, list) and len(colSum) >= 1
        # main method: (greedily scan the matrix)
        return self._restoreMatrix(rowSum, colSum)

    def _restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        assert isinstance(rowSum, list) and len(rowSum) >= 1
        assert isinstance(colSum, list) and len(colSum) >= 1

        len_row, len_col = len(rowSum), len(colSum)
        matrix = [[0] * len_col for _ in range(len_row)]

        i = j = 0
        while i < len_row and j < len_col:
            min_value = min(rowSum[i], colSum[j])

            matrix[i][j] = min_value
            rowSum[i] -= min_value
            colSum[j] -= min_value

            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1

        return matrix


def main():
    # Example 1: Output: [[3,0], [1,7]]
    # rowSum = [3, 8]
    # colSum = [4, 7]

    # Example 2: Output: [[0,5,0], [6,1,0], [2,0,8]]
    rowSum = [5, 7, 10]
    colSum = [8, 6, 8]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.restoreMatrix(rowSum, colSum)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
