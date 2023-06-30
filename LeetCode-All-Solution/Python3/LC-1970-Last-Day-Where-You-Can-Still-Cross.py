#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1970-Last-Day-Where-You-Can-Still-Cross.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-30
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 1970 - (Hard) - Last Day Where You Can Still Cross
https://leetcode.com/problems/last-day-where-you-can-still-cross/

Description & Requirement:
    There is a 1-based binary matrix where 0 represents land and 1 represents water. 
    You are given integers row and col representing the number of rows and columns in the matrix, respectively.

    Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. 
    You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, 
    the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

    You want to find the last day that it is possible to walk from the top to the bottom by 
    only walking on land cells. You can start from any cell in the top row and end at any cell 
    in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

    Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

Example 1:
    Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
    Output: 2
    Explanation: The above image depicts how the matrix changes each day starting from day 0.
        The last day where it is possible to cross from top to bottom is on day 2.
Example 2:
    Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
    Output: 1
    Explanation: The above image depicts how the matrix changes each day starting from day 0.
        The last day where it is possible to cross from top to bottom is on day 1.
Example 3:
    Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
    Output: 3
    Explanation: The above image depicts how the matrix changes each day starting from day 0.
        The last day where it is possible to cross from top to bottom is on day 3.

Constraints:
    2 <= row, col <= 2 * 10^4
    4 <= row * col <= 2 * 10^4
    cells.length == row * col
    1 <= ri <= row
    1 <= ci <= col
    All the values of cells are unique.
"""


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # exception case
        assert isinstance(row, int) and row >= 2
        assert isinstance(col, int) and col >= 2
        assert isinstance(cells, list) and len(cells) == row * col
        # main method: (binary search + BFS)
        return self._latestDayToCross(row, col, cells)

    def _latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        assert isinstance(row, int) and row >= 2
        assert isinstance(col, int) and col >= 2
        assert isinstance(cells, list) and len(cells) == row * col

        left, right, res = 0, row * col, 0
        while left <= right:
            mid = (left + right) >> 1

            grid = [[1] * col for _ in range(row)]
            for x, y in cells[:mid]:
                grid[x - 1][y - 1] = 0

            queue = collections.deque()
            for i in range(col):
                if grid[0][i]:
                    queue.append((0, i))
                    grid[0][i] = 0

            found = False
            while queue:
                x, y = queue.popleft()
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny]:
                        if nx == row - 1:
                            found = True
                            break
                        queue.append((nx, ny))
                        grid[nx][ny] = 0

            if found:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res


def main():
    # Example 1: Output: 2
    # row = 2
    # col = 2
    # cells = [[1, 1], [2, 1], [1, 2], [2, 2]]

    # Example 2: Output: 1
    # row = 2
    # col = 2
    # cells = [[1, 1], [1, 2], [2, 1], [2, 2]]

    # Example 3: Output: 3
    row = 3
    col = 3
    cells = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.latestDayToCross(row, col, cells)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
