#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2373-Largest-Local-Values-in-a-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-01
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2373 - (Easy) - Largest Local Values in a Matrix
https://leetcode.com/problems/largest-local-values-in-a-matrix/

Description & Requirement:
    You are given an n x n integer matrix grid.

    Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
    maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.

    In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

    Return the generated matrix.

Example 1:
    Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    Output: [[9,9],[8,6]]
    Explanation: The diagram above shows the original matrix and the generated matrix.
        Notice that each value in the generated matrix corresponds to 
        the largest value of a contiguous 3 x 3 matrix in grid.
Example 2:
    Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    Output: [[2,2,2],[2,2,2],[2,2,2]]
    Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.

Constraints:
    n == grid.length == grid[i].length
    3 <= n <= 100
    1 <= grid[i][j] <= 100
"""


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 3
        # main method: (scan the grid)
        return self._largestLocal(grid)

    def _largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        assert isinstance(grid, list) and len(grid) >= 3

        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                res[i][j] = max(grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3))

        return res


def main():
    # Example 1: Output: [[9,9],[8,6]]
    # grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]

    # Example 2: Output: [[2,2,2],[2,2,2],[2,2,2]]
    grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.largestLocal(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
