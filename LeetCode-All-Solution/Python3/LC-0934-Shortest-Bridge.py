#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0934-Shortest-Bridge.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-25
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0934 - (Medium) - Shortest Bridge
https://leetcode.com/problems/shortest-bridge/

Description & Requirement:
    You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

    An island is a 4-directionally connected group of 1's not connected to any other 1's. 
    There are exactly two islands in grid.

    You may change 0's to 1's to connect the two islands to form one island.

    Return the smallest number of 0's you must flip to connect the two islands.

Example 1:
    Input: grid = [[0,1],[1,0]]
    Output: 1
Example 2:
    Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
    Output: 2
Example 3:
    Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    Output: 1

Constraints:
    n == grid.length == grid[i].length
    2 <= n <= 100
    grid[i][j] is either 0 or 1.
    There are exactly two islands in grid.
"""


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1
        n = len(grid)
        for row in grid:
            assert isinstance(row, list) and len(row) == n
        # main method: (use BFS to find a island, and then perform BFS until reach the other island)
        return self._shortestBridge(grid)

    def _shortestBridge(self, grid: List[List[int]]) -> int:
        """
        Runtime: 891 ms, faster than 55.44% of Python3 online submissions for Shortest Bridge.
        Memory Usage: 14.4 MB, less than 99.64% of Python3 online submissions for Shortest Bridge.
        """
        assert isinstance(grid, list) and len(grid) >= 1
        n = len(grid)

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != 1:  # find the first "1" land
                    continue
                island = []
                grid[r][c] = -1
                queue = collections.deque([(r, c)])

                # BFS, scan a whole island
                while len(queue) > 0:
                    x, y = queue.popleft()
                    island.append((x, y))
                    for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            grid[nx][ny] = -1
                            queue.append((nx, ny))

                step = 0
                cur_queue = island
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                while True:
                    new_queue = []
                    for x, y in cur_queue:
                        for delta_x, delta_y in directions:
                            cur_x = x + delta_x
                            cur_y = y + delta_y
                            if 0 <= cur_x < n and 0 <= cur_y < n:
                                if grid[cur_x][cur_y] == 1:
                                    return step
                                if grid[cur_x][cur_y] == 0:
                                    grid[cur_x][cur_y] = -1
                                    new_queue.append((cur_x, cur_y))
                    cur_queue = new_queue
                    step += 1

        return 0


def main():
    # Example 1: Output: 1
    # grid = [
    #     [0, 1],
    #     [1, 0]
    # ]

    # Example 2: Output: 2
    # grid = [
    #     [0, 1, 0],
    #     [0, 0, 0],
    #     [0, 0, 1]
    # ]

    # Example 3: Output: 1
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.shortestBridge(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
