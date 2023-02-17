#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1139-Largest-1-Bordered-Square.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-17
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1139 - (Medium) - Largest 1-Bordered Square
https://leetcode.com/problems/largest-1-bordered-square/

Description & Requirement:
    Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid 
    that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

Example 1:
    Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
    Output: 9
Example 2:
    Input: grid = [[1,1,0,0]]
    Output: 1

Constraints:
    1 <= grid.length <= 100
    1 <= grid[0].length <= 100
    grid[i][j] is 0 or 1
"""


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1
        n_col = len(grid[0])
        for row in grid:
            assert isinstance(row, list) and len(row) == n_col
        # main method: (dynamic programming)
        return self._largest1BorderedSquare(grid)

    def _largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1
        n_row, n_col = len(grid), len(grid[0])

        dp_left = [[0] * (n_col + 1) for _ in range(n_row + 1)]
        dp_up = [[0] * (n_col + 1) for _ in range(n_row + 1)]

        max_border = 0

        for i in range(1, n_row + 1):
            for j in range(1, n_col + 1):
                if grid[i - 1][j - 1]:
                    dp_left[i][j] = dp_left[i][j - 1] + 1
                    dp_up[i][j] = dp_up[i - 1][j] + 1
                    border = min(dp_left[i][j], dp_up[i][j])

                    while dp_left[i - border + 1][j] < border or dp_up[i][j - border + 1] < border:
                        border -= 1

                    max_border = max(max_border, border)

        return max_border ** 2


def main():
    # Example 1: Output: 9
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    # Example 2: Output: 1
    # grid = [[1, 1, 0, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largest1BorderedSquare(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
