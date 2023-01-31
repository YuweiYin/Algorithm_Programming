#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2319-Check-if-Matrix-Is-X-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-31
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2319 - (Easy) - Check if Matrix Is X-Matrix
https://leetcode.com/problems/check-if-matrix-is-x-matrix/

Description & Requirement:
    A square matrix is said to be an X-Matrix if both of the following conditions hold:
        All the elements in the diagonals of the matrix are non-zero.
        All other elements are 0.

    Given a 2D integer array grid of size n x n representing a square matrix, 
    return true if grid is an X-Matrix. Otherwise, return false.

Example 1:
    Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
    Output: true
    Explanation: Refer to the diagram above. 
        An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
        Thus, grid is an X-Matrix.
Example 2:
    Input: grid = [[5,7,0],[0,3,1],[0,5,0]]
    Output: false
    Explanation: Refer to the diagram above.
        An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
        Thus, grid is not an X-Matrix.

Constraints:
    n == grid.length == grid[i].length
    3 <= n <= 100
    0 <= grid[i][j] <= 10^5
"""


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 3
        # main method: (mathematics)
        return self._checkXMatrix(grid)

    def _checkXMatrix(self, grid: List[List[int]]) -> bool:
        """
        Time: beats 94.69%; Space: beats 95.15%
        """
        assert isinstance(grid, list) and len(grid) >= 3

        n_row = len(grid)
        for i, row in enumerate(grid):
            for j, ele in enumerate(row):
                if i == j or (i + j) == (n_row - 1):
                    if ele == 0:
                        return False
                elif ele > 0:
                    return False

        return True


def main():
    # Example 1: Output: true
    grid = [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]

    # Example 2: Output: false
    # grid = [[5, 7, 0], [0, 3, 1], [0, 5, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.checkXMatrix(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
