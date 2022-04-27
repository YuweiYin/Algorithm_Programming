#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0417-Pacific-Atlantic-Water-Flow.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-27
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0417 - (Medium) - Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/

Description & Requirement:
    There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
    The Pacific Ocean touches the island's left and top edges, 
    and the Atlantic Ocean touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights 
    where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

    The island receives a lot of rain, and the rain water can flow to neighboring cells directly 
    north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. 
    Water can flow from any cell adjacent to an ocean into the ocean.

    Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that 
    rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
    Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:
    Input: heights = [[2,1],[1,2]]
    Output: [[0,0],[0,1],[1,0],[1,1]]

Constraints:
    m == heights.length
    n == heights[r].length
    1 <= m, n <= 200
    0 <= heights[r][c] <= 10^5
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(heights, list) and len(heights) >= 1 and len(heights[0]) >= 1
        # main method: (multi-source BFS from left/top edge (Pacific) and from right/bottom edge (Atlantic))
        return self._pacificAtlantic(heights)

    def _pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Runtime: 289 ms, faster than 90.40% of Python3 online submissions for Pacific Atlantic Water Flow.
        Memory Usage: 15.8 MB, less than 22.98% of Python3 online submissions for Pacific Atlantic Water Flow.
        """
        assert isinstance(heights, list) and len(heights) >= 1 and len(heights[0]) >= 1
        max_row = len(heights)
        max_col = len(heights[0])

        bfs_queue = collections.deque()

        # multi-source BFS from left/top edge (Pacific)
        pacific_grid = [[False for _ in range(max_col)] for _ in range(max_row)]
        visit_grid = [[False for _ in range(max_col)] for _ in range(max_row)]
        bfs_queue.append((0, 0))
        visit_grid[0][0] = True
        for r in range(1, max_row):  # left edge
            bfs_queue.append((r, 0))
            visit_grid[r][0] = True
        for c in range(1, max_col):  # top edge
            bfs_queue.append((0, c))
            visit_grid[0][c] = True
        while len(bfs_queue) > 0:
            row, col = bfs_queue.popleft()
            pacific_grid[row][col] = True
            cur_h = heights[row][col]
            if col - 1 >= 0 and not visit_grid[row][col - 1] and cur_h <= heights[row][col - 1]:  # west
                bfs_queue.append((row, col - 1))
                visit_grid[row][col - 1] = True
            if col + 1 < max_col and not visit_grid[row][col + 1] and cur_h <= heights[row][col + 1]:  # east
                bfs_queue.append((row, col + 1))
                visit_grid[row][col + 1] = True
            if row - 1 >= 0 and not visit_grid[row - 1][col] and cur_h <= heights[row - 1][col]:  # north
                bfs_queue.append((row - 1, col))
                visit_grid[row - 1][col] = True
            if row + 1 < max_row and not visit_grid[row + 1][col] and cur_h <= heights[row + 1][col]:  # south
                bfs_queue.append((row + 1, col))
                visit_grid[row + 1][col] = True

        # multi-source BFS from right/bottom edge (Atlantic)
        atlantic_grid = [[False for _ in range(max_col)] for _ in range(max_row)]
        visit_grid = [[False for _ in range(max_col)] for _ in range(max_row)]
        bfs_queue.append((max_row - 1, max_col - 1))
        visit_grid[max_row - 1][max_col - 1] = True
        for r in range(0, max_row - 1):  # right edge
            bfs_queue.append((r, max_col - 1))
            visit_grid[r][max_col - 1] = True
        for c in range(0, max_col - 1):  # bottom edge
            bfs_queue.append((max_row - 1, c))
            visit_grid[max_row - 1][c] = True
        while len(bfs_queue) > 0:
            row, col = bfs_queue.popleft()
            atlantic_grid[row][col] = True
            cur_h = heights[row][col]
            if col - 1 >= 0 and not visit_grid[row][col - 1] and cur_h <= heights[row][col - 1]:  # west
                bfs_queue.append((row, col - 1))
                visit_grid[row][col - 1] = True
            if col + 1 < max_col and not visit_grid[row][col + 1] and cur_h <= heights[row][col + 1]:  # east
                bfs_queue.append((row, col + 1))
                visit_grid[row][col + 1] = True
            if row - 1 >= 0 and not visit_grid[row - 1][col] and cur_h <= heights[row - 1][col]:  # north
                bfs_queue.append((row - 1, col))
                visit_grid[row - 1][col] = True
            if row + 1 < max_row and not visit_grid[row + 1][col] and cur_h <= heights[row + 1][col]:  # south
                bfs_queue.append((row + 1, col))
                visit_grid[row + 1][col] = True

        res = []
        for row in range(max_row):
            for col in range(max_col):
                if pacific_grid[row][col] and atlantic_grid[row][col]:  # can flow to both oceans
                    res.append([row, col])
        return res


def main():
    # Example 1: Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]

    # Example 2: Output: [[0,0],[0,1],[1,0],[1,1]]
    # heights = [[2, 1], [1, 2]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.pacificAtlantic(heights)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
