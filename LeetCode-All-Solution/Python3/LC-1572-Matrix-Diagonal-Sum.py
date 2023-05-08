#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1572-Matrix-Diagonal-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-08
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1572 - (Easy) - Matrix Diagonal Sum
https://leetcode.com/problems/matrix-diagonal-sum/

Description & Requirement:
    Given a square matrix mat, return the sum of the matrix diagonals.

    Only include the sum of all the elements on the primary diagonal and 
    all the elements on the secondary diagonal that are not part of the primary diagonal.

Example 1:
    Input: mat = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
    Output: 25
    Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
        Notice that element mat[1][1] = 5 is counted only once.
Example 2:
    Input: mat = [[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]]
    Output: 8
Example 3:
    Input: mat = [[5]]
    Output: 5

Constraints:
    n == mat.length == mat[i].length
    1 <= n <= 100
    1 <= mat[i][j] <= 100
"""


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # exception case
        assert isinstance(mat, list) and len(mat) >= 1 and len(mat) == len(mat[0])
        # main method: (subtract the central value)
        return self._diagonalSum(mat)

    def _diagonalSum(self, mat: List[List[int]]) -> int:
        assert isinstance(mat, list) and len(mat) >= 1 and len(mat) == len(mat[0])

        n = len(mat)
        val_sum = 0
        mid_idx = n >> 1
        for i in range(n):
            val_sum += mat[i][i] + mat[i][n - 1 - i]

        return val_sum - mat[mid_idx][mid_idx] * (n & 0x01)


def main():
    # Example 1: Output: 25
    # mat = [[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]]

    # Example 2: Output: 8
    mat = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]

    # Example 3: Output: 5
    # mat = [[5]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.diagonalSum(mat)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
