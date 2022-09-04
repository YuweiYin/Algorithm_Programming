#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1582-Special-Positions-in-a-Binary-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-04
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1582 - (Easy) - Special Positions in a Binary Matrix
https://leetcode.com/problems/special-positions-in-a-binary-matrix/

Description & Requirement:
    Given an m x n binary matrix mat, return the number of special positions in mat.

    A position (i, j) is called special if mat[i][j] == 1 and 
    all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:
    Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
    Output: 1
    Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:
    Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3
    Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    mat[i][j] is either 0 or 1.
"""


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # exception case
        assert isinstance(mat, list) and len(mat) >= 1 and len(mat[0]) >= 1
        n = len(mat[0])
        for row in mat:
            assert isinstance(row, list) and len(row) == n
        # main method: (calculate the sum of each row and col)
        return self._numSpecial(mat)

    def _numSpecial(self, mat: List[List[int]]) -> int:
        """
        Runtime: 338 ms, faster than 22.84% of Python3 online submissions for Special Positions in a Binary Matrix.
        Memory Usage: 14.2 MB, less than 91.35% of Python3 online submissions for Special Positions in a Binary Matrix.
        """
        assert isinstance(mat, list) and len(mat) >= 1 and len(mat[0]) >= 1
        # m, n = len(mat), len(mat[0])

        row_sum = [sum(row) for row in mat]
        col_sum = [sum(col) for col in zip(*mat)]

        res = 0
        for i, row in enumerate(mat):
            for j, num in enumerate(row):
                if num == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    res += 1

        return res


def main():
    # Example 1: Output: 1
    mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]

    # Example 2: Output: 3
    # mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numSpecial(mat)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
