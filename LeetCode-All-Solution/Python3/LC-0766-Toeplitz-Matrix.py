#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0766-Toeplitz-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-31
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0766 - (Easy) - Toeplitz Matrix
https://leetcode.com/problems/toeplitz-matrix/

Description & Requirement:
    Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

    A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:
    Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    Output: true
    Explanation:
        In the above grid, the diagonals are:
        "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
        In each diagonal all elements are the same, so the answer is True.
Example 2:
    Input: matrix = [[1,2],[2,2]]
    Output: false
    Explanation:
        The diagonal "[1, 2]" has different elements.

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 20
    0 <= matrix[i][j] <= 99

Follow up:
    What if the matrix is stored on disk, and the memory is limited such that 
        you can only load at most one row of the matrix into the memory at once?
    What if the matrix is so large that you can only load up a partial row into the memory at once?
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # exception case
        assert isinstance(matrix, list) and len(matrix) >= 1 and len(matrix[0]) >= 1
        n = len(matrix[0])
        for row in matrix:
            assert isinstance(row, list) and len(row) == n
            for item in row:
                assert isinstance(item, int) and item >= 0
        # main method: (scan and check every diagonal)
        return self._isToeplitzMatrix(matrix)

    def _isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Runtime: 121 ms, faster than 78.44% of Python3 online submissions for Toeplitz Matrix.
        Memory Usage: 13.9 MB, less than 78.65% of Python3 online submissions for Toeplitz Matrix.
        """
        assert isinstance(matrix, list) and len(matrix) >= 1 and len(matrix[0]) >= 1
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 or n == 1:
            return True

        def __check_diagonal(start_r, start_c) -> bool:
            value = matrix[start_r][start_c]
            while start_r + 1 < m and start_c + 1 < n:
                next_val = matrix[start_r + 1][start_c + 1]
                if value != next_val:
                    return False
                start_r += 1
                start_c += 1
            return True

        for cur_r in range(m):
            if not __check_diagonal(cur_r, 0):
                return False

        for cur_c in range(n):
            if not __check_diagonal(0, cur_c):
                return False

        return True


def main():
    # Example 1: Output: true
    # matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]

    # Example 2: Output: false
    # matrix = [[1, 2], [2, 2]]

    # Example 3: Output: false
    matrix = [[11, 74, 0, 93], [40, 11, 74, 7]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isToeplitzMatrix(matrix)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
