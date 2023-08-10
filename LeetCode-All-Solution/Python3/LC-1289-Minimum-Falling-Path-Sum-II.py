#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1289-Minimum-Falling-Path-Sum-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-10
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 1289 - (Hard) - Minimum Falling Path Sum II
https://leetcode.com/problems/minimum-falling-path-sum-ii/

Description & Requirement:
    Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

    A falling path with non-zero shifts is a choice of exactly one element from each row of grid 
    such that no two elements chosen in adjacent rows are in the same column.

Example 1:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
    Output: 13
    Explanation: 
        The possible falling paths are:
        [1,5,9], [1,5,7], [1,6,7], [1,6,8],
        [2,4,8], [2,4,9], [2,6,7], [2,6,8],
        [3,4,8], [3,4,9], [3,5,7], [3,5,9]
        The falling path with the smallest sum is [1,5,7], so the answer is 13.
Example 2:
    Input: grid = [[7]]
    Output: 7

Constraints:
    n == grid.length == grid[i].length
    1 <= n <= 200
    -99 <= grid[i][j] <= 99
"""


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid) == len(grid[0])
        # main method: (dynamic programming)
        return self._minFallingPathSum(grid)

    def _minFallingPathSum(self, grid: List[List[int]]) -> int:
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid) == len(grid[0])

        first_min_sum, second_min_sum = 0, 0
        first_min_index = -1

        for i in range(len(grid)):
            cur_first_min_sum, cur_second_min_sum = int(1e9+7), int(1e9+7)
            cur_first_min_index = -1

            for j in range(len(grid)):
                cur_sum = grid[i][j]
                if j != first_min_index:
                    cur_sum += first_min_sum
                else:
                    cur_sum += second_min_sum
                if cur_sum < cur_first_min_sum:
                    cur_second_min_sum, cur_first_min_sum = cur_first_min_sum, cur_sum
                    cur_first_min_index = j
                elif cur_sum < cur_second_min_sum:
                    cur_second_min_sum = cur_sum

            first_min_sum, second_min_sum = cur_first_min_sum, cur_second_min_sum
            first_min_index = cur_first_min_index

        return first_min_sum


def main():
    # Example 1: Output: 13
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Example 2: Output: 7
    # grid = [[7]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minFallingPathSum(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
