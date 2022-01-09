#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0994-Rotting-Oranges.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-09
=================================================================="""

import sys
import time
from typing import List
# import queue
# import collections

"""
LeetCode - 0994 - (Medium) - Rotting Oranges
https://leetcode.com/problems/rotting-oranges/

Description:
    You are given an m x n grid where each cell can have one of three values:
        0 representing an empty cell,
        1 representing a fresh orange, or
        2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Requirement:
    Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
    If this is impossible, return -1.

Example 1:
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4
Example 2:
    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, 
        because rotting only happens 4-directionally.
Example 3:
    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # exception case
        if not isinstance(grid, list) or len(grid) <= 0 or not isinstance(grid[0], list):
            return -1  # error grid
        len_c = len(grid[0])  # check every row is the same length
        exist_2 = False  # if there's no rotten origin at first, then must return -1
        for row in grid:
            if not isinstance(row, list) or len(row) != len_c:
                return -1  # error grid
            if not exist_2:  # find at least one 2
                for num in row:
                    if num == 2:
                        exist_2 = True
                        break
        # main method: multi-source BFS
        return self._orangesRotting(grid)

    def _orangesRotting(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        max_col = len(grid[0])

        # INF = sys.maxsize  # max int
        INF = max_row * max_col + 1  # rotten minute
        rot_minute_grid = [[INF for _ in range(max_col)] for _ in range(max_row)]
        not_rotten_counter = 0  # the number of not rotten oranges
        elapse_minute = 0

        # bfs_queue = collections.deque()
        bfs_queue = []  # each minute, deal with all current oranges, so needn't use real FIFO queue
        for row in range(max_row):
            for col in range(max_col):
                if grid[row][col] == 2:  # find all rotten oranges 2
                    rot_minute_grid[row][col] = 0  # rotten at the first time
                    bfs_queue.append([row, col])  # bfs starts from all 2
                elif grid[row][col] == 1:
                    not_rotten_counter += 1  # record the number of 1

        while len(bfs_queue) > 0:
            new_queue = []
            # deal with all neighbors of all rotten oranges at this minute
            for index in bfs_queue:
                cur_row, cur_col = index
                cur_rot_minute = rot_minute_grid[cur_row][cur_col]
                if 0 <= cur_col - 1 and grid[cur_row][cur_col - 1] == 1 and \
                        rot_minute_grid[cur_row][cur_col - 1] == INF:  # left
                    rot_minute_grid[cur_row][cur_col - 1] = cur_rot_minute + 1
                    not_rotten_counter -= 1
                    new_queue.append([cur_row, cur_col - 1])
                if 0 <= cur_row - 1 and grid[cur_row - 1][cur_col] == 1 and \
                        rot_minute_grid[cur_row - 1][cur_col] == INF:  # up
                    rot_minute_grid[cur_row - 1][cur_col] = cur_rot_minute + 1
                    not_rotten_counter -= 1
                    new_queue.append([cur_row - 1, cur_col])
                if cur_col + 1 < max_col and grid[cur_row][cur_col + 1] == 1 and \
                        rot_minute_grid[cur_row][cur_col + 1] == INF:  # right
                    rot_minute_grid[cur_row][cur_col + 1] = cur_rot_minute + 1
                    not_rotten_counter -= 1
                    new_queue.append([cur_row, cur_col + 1])
                if cur_row + 1 < max_row and grid[cur_row + 1][cur_col] == 1 and \
                        rot_minute_grid[cur_row + 1][cur_col] == INF:  # down
                    rot_minute_grid[cur_row + 1][cur_col] = cur_rot_minute + 1
                    not_rotten_counter -= 1
                    new_queue.append([cur_row + 1, cur_col])
            bfs_queue = new_queue  # update new queue, deal with newly rotten oranges in the next loop
            if len(new_queue) == 0:  # no new rotten orange in this loop, stop
                break
            elapse_minute += 1  # time flies... tick tick tick...

        assert not_rotten_counter >= 0
        return -1 if not_rotten_counter > 0 else elapse_minute


def main():
    # Example 1: Output: 4
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]

    # Example 2: Output: -1
    # grid = [
    #     [2, 1, 1],
    #     [0, 1, 1],
    #     [1, 0, 1]
    # ]

    # Example 3: Output: 0
    # grid = [[0, 2]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.orangesRotting(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
