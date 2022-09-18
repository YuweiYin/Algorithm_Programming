#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0827-Making-A-Large-Island.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-03
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0827 - (Hard) - Making A Large Island
https://leetcode.com/problems/making-a-large-island/

Description & Requirement:
    You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

    Return the size of the largest island in grid after applying this operation.

    An island is a 4-directionally connected group of 1s.

Example 1:
    Input: grid = [[1,0],[0,1]]
    Output: 3
    Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:
    Input: grid = [[1,1],[1,0]]
    Output: 4
    Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:
    Input: grid = [[1,1],[1,1]]
    Output: 4
    Explanation: Can't change any 0 to 1, only one island with area = 4.

Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 500
    grid[i][j] is either 0 or 1.
"""


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1
        n = len(grid)
        for row in grid:
            assert isinstance(row, list) and len(row) == n
        # main method: (try to merge islands)
        return self._largestIsland(grid)

    def _largestIsland(self, grid: List[List[int]]) -> int:
        assert isinstance(grid, list) and len(grid) >= 1
        n = len(grid)

        tag = [[0 for _ in range(n)] for _ in range(n)]
        area = collections.Counter()

        def __dfs(_r: int, _c: int) -> None:
            tag[_r][_c] = t
            area[t] += 1
            for _x, _y in (_r - 1, _c), (_r + 1, _c), (_r, _c - 1), (_r, _c + 1):  # try 4 directions
                if 0 <= _x < n and 0 <= _y < n and grid[_x][_y] > 0 and tag[_x][_y] == 0:
                    __dfs(_x, _y)

        for r_idx, row in enumerate(grid):
            for c_idx, val in enumerate(row):
                if val and tag[r_idx][c_idx] == 0:  # enumerate the lands that have not been visited
                    t = r_idx * n + c_idx + 1
                    __dfs(r_idx, c_idx)

        res = max(area.values(), default=0)

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 0:  # enumerate the lands that can be added
                    new_area = 1
                    connected = {0}
                    for x, y in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):  # try 4 directions
                        if 0 <= x < n and 0 <= y < n and tag[x][y] not in connected:
                            new_area += area[tag[x][y]]
                            connected.add(tag[x][y])
                    res = max(res, new_area)

        return res


def main():
    # Example 1: Output: 3
    grid = [[1, 0], [0, 1]]

    # Example 2: Output: 4
    # grid = [[1, 1], [1, 0]]

    # Example 3: Output: 4
    # grid = [[1, 1], [1, 1]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largestIsland(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
