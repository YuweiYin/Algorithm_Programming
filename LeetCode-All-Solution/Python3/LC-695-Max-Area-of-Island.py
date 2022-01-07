#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-695-Max-Area-of-Island.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-07
=================================================================="""

import sys
import time
from typing import List
import queue

"""
LeetCode - 695 - (Medium) - Max Area of Island
https://leetcode.com/problems/max-area-of-island/

Description:
    You are given an m x n binary matrix grid. 
    An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
    You may assume all four edges of the grid are surrounded by water.

    The area of an island is the number of cells with a value 1 in the island.

Requirement:
    Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
    Input: grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:
    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # exception case
        if not isinstance(grid, list) or len(grid) <= 0 or not isinstance(grid[0], list):
            return 0
        len_c = len(grid[0])  # check every row is the same length
        for row in grid:
            if not isinstance(row, list) or len(row) != len_c:
                return 0
        # main method: BFS or DFS
        return self._maxAreaOfIsland(grid)

    def _maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        # cur_area = 0

        len_r = len(grid)
        len_c = len(grid[0])

        sea_number = 0
        land_number = 1
        # fill_land_number = 2  # mark the searched lands, avoid repeat search on the same land
        fill_land_number = sea_number  # for this problem, 0 is ok

        for r_index in range(len_r):  # consider every pixel
            for c_index in range(len_c):
                if grid[r_index][c_index] == land_number:  # count the area of every land
                    cur_area = self._countAreaBFS(grid, r_index, c_index, land_number, fill_land_number)  # BFS
                    # cur_area = self._countAreaDFS(grid, r_index, c_index, land_number, fill_land_number)  # DFS
                    max_area = max(max_area, cur_area)

        return max_area

    def _countAreaBFS(self, grid: List[List[int]], r_idx: int, c_idx: int,
                      land_number: int, fill_land_number: int) -> int:
        area_counter = 0
        len_r = len(grid)
        len_c = len(grid[0])

        # next_queue = collections.deque()  # BFS queue
        next_queue = queue.Queue()  # BFS queue
        next_queue.put([r_idx, c_idx])

        while not next_queue.empty():
            cur_r, cur_c = next_queue.get()  # get current block to be drawn
            if grid[cur_r][cur_c] == land_number:  # avoid repeated land pixel
                grid[cur_r][cur_c] = fill_land_number  # fill this land
                area_counter += 1  # counter plus 1
                # find valid neighbors (4 directions) and add them into the queue
                if cur_r + 1 < len_r and grid[cur_r + 1][cur_c] == land_number:
                    next_queue.put([cur_r + 1, cur_c])
                if cur_r - 1 >= 0 and grid[cur_r - 1][cur_c] == land_number:
                    next_queue.put([cur_r - 1, cur_c])
                if cur_c + 1 < len_c and grid[cur_r][cur_c + 1] == land_number:
                    next_queue.put([cur_r, cur_c + 1])
                if cur_c - 1 >= 0 and grid[cur_r][cur_c - 1] == land_number:
                    next_queue.put([cur_r, cur_c - 1])

        return area_counter

    def _countAreaDFS(self, grid: List[List[int]], r_idx: int, c_idx: int,
                      land_number: int, fill_land_number: int) -> int:
        len_r = len(grid)
        len_c = len(grid[0])

        def __dfs(cur_r: int, cur_c: int) -> int:
            grid[cur_r][cur_c] = fill_land_number  # fill this land
            cur_counter = 1
            # find valid neighbors (4 directions) and perform dfs
            if cur_r + 1 < len_r and grid[cur_r + 1][cur_c] == land_number:
                cur_counter += __dfs(cur_r + 1, cur_c)
            if cur_r - 1 >= 0 and grid[cur_r - 1][cur_c] == land_number:
                cur_counter += __dfs(cur_r - 1, cur_c)
            if cur_c + 1 < len_c and grid[cur_r][cur_c + 1] == land_number:
                cur_counter += __dfs(cur_r, cur_c + 1)
            if cur_c - 1 >= 0 and grid[cur_r][cur_c - 1] == land_number:
                cur_counter += __dfs(cur_r, cur_c - 1)
            return cur_counter

        return __dfs(r_idx, c_idx)


def main():
    # Example 1: Output: 6
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]

    # Example 2: Output: 0
    # grid = [[0, 0, 0, 0, 0, 0, 0, 0]]

    # Example 3: Output: 4
    # grid = [
    #     [1, 1, 0, 0, 0],
    #     [1, 1, 0, 0, 0],
    #     [0, 0, 0, 1, 1],
    #     [0, 0, 0, 1, 1]
    # ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxAreaOfIsland(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
