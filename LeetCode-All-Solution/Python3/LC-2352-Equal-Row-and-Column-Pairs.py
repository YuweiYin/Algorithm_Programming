#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2352-Equal-Row-and-Column-Pairs.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-06
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 2352 - (Medium) - Equal Row and Column Pairs
https://leetcode.com/problems/equal-row-and-column-pairs/

Description & Requirement:
    Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) 
    such that row ri and column cj are equal.

    A row and column pair is considered equal if they contain the same elements 
    in the same order (i.e., an equal array).

Example 1:
    Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
    Output: 1
    Explanation: There is 1 equal row and column pair:
        - (Row 2, Column 1): [2,7,7]
Example 2:
    Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    Output: 3
    Explanation: There are 3 equal row and column pairs:
        - (Row 0, Column 0): [3,1,2,2]
        - (Row 2, Column 2): [2,4,2,2]
        - (Row 3, Column 2): [2,4,2,2]

Constraints:
    n == grid.length == grid[i].length
    1 <= n <= 200
    1 <= grid[i][j] <= 10^5
"""


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1
        # main method: (hash counter)
        return self._equalPairs(grid)

    def _equalPairs(self, grid: List[List[int]]) -> int:
        assert isinstance(grid, list) and len(grid) >= 1

        res = 0
        n = len(grid)
        cnt = collections.Counter(tuple(row) for row in grid)

        for j in range(n):
            res += cnt[tuple([grid[i][j] for i in range(n)])]

        return res


def main():
    # Example 1: Output: 1
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]

    # Example 2: Output: 3
    # grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.equalPairs(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
