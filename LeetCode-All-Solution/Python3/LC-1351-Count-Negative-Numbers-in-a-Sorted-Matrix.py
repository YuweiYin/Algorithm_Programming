#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1351-Count-Negative-Numbers-in-a-Sorted-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-08
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1351 - (Easy) - Count Negative Numbers in a Sorted Matrix
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

Description & Requirement:
    Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
    return the number of negative numbers in grid.

Example 1:
    Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    Output: 8
    Explanation: There are 8 negatives number in the matrix.
Example 2:
    Input: grid = [[3,2],[1,0]]
    Output: 0

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100
"""


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1
        # main method: (binary search)
        return self._countNegatives(grid)

    def _countNegatives(self, grid: List[List[int]]) -> int:
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1

        m, n = len(grid[0]), len(grid)
        res, j = 0, m
        for i in range(n):
            if j == 0:
                break
            if grid[i][j - 1] >= 0:
                continue

            left, right = 0, j
            while left < right:
                mid = (right + left) >> 1
                if grid[i][mid] >= 0:
                    left = mid + 1
                else:
                    right = mid

            res += (j - left) * (n - i)
            j = left

        return res


def main():
    # Example 1: Output: 8
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

    # Example 2: Output: 0
    # grid = [[3, 2], [1, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countNegatives(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
