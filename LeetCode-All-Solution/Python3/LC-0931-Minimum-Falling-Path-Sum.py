#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0931-Minimum-Falling-Path-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-16
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0931 - (Medium) - Minimum Falling Path Sum
https://leetcode.com/problems/minimum-falling-path-sum/

Description & Requirement:
    Given an n x n array of integers matrix, 
    return the minimum sum of any falling path through matrix.

    A falling path starts at any element in the first row and 
    chooses the element in the next row that is either directly below or diagonally left/right. 
    Specifically, the next element from position (row, col) will be 
    (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:
    Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
    Output: 13
    Explanation: There are two falling paths with a minimum sum.
Example 2:
    Input: matrix = [[-19,57],[-40,-5]]
    Output: -59

Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 100
    -100 <= matrix[i][j] <= 100
"""


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # exception case
        assert isinstance(matrix, list) and len(matrix) > 0 and isinstance(matrix[0], list) and len(matrix[0]) > 0
        n = len(matrix)
        for row in matrix:
            assert isinstance(row, list) and len(row) == n
        # main method: (Dynamic Programming)
        #     dp[i][j] is the minimum sum of falling path from layer 0 to point (i, j)
        #     dp equation: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + matrix[i][j] where 0 <= i, j < n
        #     dp init: dp[0][j] = matrix[0][j]
        #     dp aim: get min(dp[-1])
        return self._minFallingPathSum(matrix)

    def _minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Runtime: 132 ms, faster than 87.38% of Python3 online submissions for Minimum Falling Path Sum.
        Memory Usage: 14.8 MB, less than 76.94% of Python3 online submissions for Minimum Falling Path Sum.
        """
        n = len(matrix)
        assert n > 0 and n == len(matrix[0])

        if n == 1:
            return matrix[0][0]

        dp = matrix.copy()
        for row in range(1, n):
            dp[row][0] = min(dp[row - 1][0], dp[row - 1][1]) + matrix[row][0]  # leftmost
            dp[row][n - 1] = min(dp[row - 1][n - 1], dp[row - 1][n - 2]) + matrix[row][n - 1]  # rightmost
            for col in range(1, n - 1):  # middle
                dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row - 1][col + 1]) + matrix[row][col]

        return min(dp[-1])


def main():
    # Example 1: Output: 13
    matrix = [
        [2, 1, 3],
        [6, 5, 4],
        [7, 8, 9]
    ]

    # Example 2: Output: -59
    # matrix = [
    #     [-19, 57],
    #     [-40, -5]
    # ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minFallingPathSum(matrix)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
