#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1260-Shift-2D-Grid.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-11
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1260 - (Easy) - Shift 2D Grid
https://leetcode.com/problems/shift-2d-grid/

Description & Requirement:
    Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

    In one shift operation:
        Element at grid[i][j] moves to grid[i][j + 1].
        Element at grid[i][n - 1] moves to grid[i + 1][0].
        Element at grid[m - 1][n - 1] moves to grid[0][0].

    Return the 2D grid after applying shift operation k times.

Example 1:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:
    Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
    Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
    Output: [[1,2,3],[4,5,6],[7,8,9]]

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m <= 50
    1 <= n <= 50
    -1000 <= grid[i][j] <= 1000
    0 <= k <= 100
"""


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # exception case
        assert isinstance(k, int) and k >= 0
        assert isinstance(grid, list) and len(grid) >= 1
        assert isinstance(grid[0], list) and len(grid[0]) >= 1
        total_number = len(grid) * len(grid[0])
        # check the validity of the grid matrix
        n = len(grid[0])
        for row in grid:
            assert isinstance(row, list) and len(row) == n
        # main method: (convert the grid to 1-dim list, then shift and recover)
        return self._shiftGrid(grid, k)

    def _shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        Runtime: 156 ms, faster than 99.72% of Python3 online submissions for Shift 2D Grid.
        Memory Usage: 14.4 MB, less than 13.09% of Python3 online submissions for Shift 2D Grid.
        """
        assert isinstance(grid, list) and len(grid) >= 1
        assert isinstance(grid[0], list) and len(grid[0]) >= 1
        m, n = len(grid), len(grid[0])

        total_number = m * n
        if k % total_number == 0:  # no need to shift
            return grid

        grid_1_dim = []
        for row in grid:  # convert the grid to 1-dim list
            grid_1_dim.extend(row)

        k %= total_number
        grid_1_dim = grid_1_dim[total_number - k:] + grid_1_dim[0: total_number - k]  # shift

        res = []
        for row_idx in range(m):  # recover
            res.append(grid_1_dim[row_idx * n: (row_idx + 1) * n])

        return res


def main():
    # Example 1: Output: [[9,1,2],[3,4,5],[6,7,8]]
    # grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # k = 1

    # Example 2: Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
    # grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    # k = 4

    # Example 3: Output: [[1,2,3],[4,5,6],[7,8,9]]
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 9

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.shiftGrid(grid, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
