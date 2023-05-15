#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1072-Flip-Columns-For-Maximum-Number-of-Equal-Rows.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-15
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1072 - (Medium) - Flip Columns For Maximum Number of Equal Rows
https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

Description & Requirement:
    You are given an m x n binary matrix matrix.

    You can choose any number of columns in the matrix and flip every cell in that column 
    (i.e., Change the value of the cell from 0 to 1 or vice versa).

    Return the maximum number of rows that have all values equal after some number of flips.

Example 1:
    Input: matrix = [[0,1],[1,1]]
    Output: 1
    Explanation: After flipping no values, 1 row has all values equal.
Example 2:
    Input: matrix = [[0,1],[1,0]]
    Output: 2
    Explanation: After flipping values in the first column, both rows have equal values.
Example 3:
    Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
    Output: 2
    Explanation: After flipping values in the first two columns, the last two rows have equal values.

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] is either 0 or 1.
"""


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # exception case
        assert isinstance(matrix, list) and len(matrix) >= 1 and len(matrix[0]) >= 1
        # main method: (hash counter)
        return self._maxEqualRowsAfterFlips(matrix)

    def _maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        assert isinstance(matrix, list) and len(matrix) >= 1 and len(matrix[0]) >= 1

        m, n = len(matrix), len(matrix[0])
        count = collections.Counter()
        for r_idx in range(m):
            value = 0
            for c_idx in range(n):
                value = value * 10 + (matrix[r_idx][c_idx] ^ matrix[r_idx][0])
            count[value] += 1

        return max(count.values())


def main():
    # Example 1: Output: 1
    # matrix = [[0, 1], [1, 1]]

    # Example 2: Output: 2
    # matrix = [[0, 1], [1, 0]]

    # Example 3: Output: 2
    matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxEqualRowsAfterFlips(matrix)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
