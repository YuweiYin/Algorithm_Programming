#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1765-Map-of-Highest-Peak.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-29
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1765 - (Medium) - Map of Highest Peak
https://leetcode.com/problems/map-of-highest-peak/

Description & Requirement:
    You are given an integer matrix isWater of size m x n that represents a map of land and water cells.
        If isWater[i][j] == 0, cell (i, j) is a land cell.
        If isWater[i][j] == 1, cell (i, j) is a water cell.
    You must assign each cell a height in a way that follows these rules:
        The height of each cell must be non-negative.
        If the cell is a water cell, its height must be 0.
        Any two adjacent cells must have an absolute height difference of at most 1. 
            A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter 
            (i.e., their sides are touching).
    Find an assignment of heights such that the maximum height in the matrix is maximized.

    Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. 
    If there are multiple solutions, return any of them.

Example 1:
    Input: isWater = [[0,1],[0,0]]
    Output: [[1,0],[2,1]]
    Explanation: The image shows the assigned heights of each cell.
        The blue cell is the water cell, and the green cells are the land cells.
Example 2:
    Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
    Output: [[1,1,0],[0,1,1],[1,2,2]]
    Explanation: A height of 2 is the maximum possible height of any assignment.
        Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.

Constraints:
    m == isWater.length
    n == isWater[i].length
    1 <= m, n <= 1000
    isWater[i][j] is 0 or 1.
    There is at least one water cell.
"""


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # exception case
        if not isinstance(isWater, list) or len(isWater) <= 0:
            return []  # Error input type
        if not isinstance(isWater[0], list) or len(isWater[0]) <= 0:
            return []  # Error input type
        col = len(isWater[0])
        has_water = False
        for row in isWater:
            assert len(row) == col
            for point in row:
                if point == 0:
                    continue
                elif point == 1:
                    has_water = True
                else:
                    return []  # Error input type
        if not has_water:
            return []  # Error input type
        # main method: (multi-source BFS (Flood Fill), start from all water points, assigning height == 0 to them)
        return self._highestPeak(isWater)

    def _highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        max_row = len(isWater)
        max_col = len(isWater[0])
        assert max_row >= 1 and max_col >= 1

        res = [[-1 for _ in range(max_col)] for _ in range(max_row)]

        # bfs_queue = collections.deque()
        bfs_queue = []  # deal with all adjacent points item at a time, rather than deal points one by one

        # find all source: water point
        for row_index in range(max_row):
            for col_index in range(max_col):
                if isWater[row_index][col_index] == 1:
                    bfs_queue.append((row_index, col_index))  # multi-source
                    res[row_index][col_index] = 0  # water height is 0

        # do BFS process
        while len(bfs_queue) > 0:
            new_bfs_queue = []  # all the points that need to explore for the next step
            for point in bfs_queue:  # deal with all adjacent points item at a time, rather than deal points one by one
                row_index, col_index = point
                cur_point_height = res[row_index][col_index]
                # any two adjacent cells must have an absolute height difference of at most 1.
                if col_index + 1 < max_col and res[row_index][col_index + 1] == -1:  # east
                    res[row_index][col_index + 1] = cur_point_height + 1
                    new_bfs_queue.append((row_index, col_index + 1))
                if row_index + 1 < max_row and res[row_index + 1][col_index] == -1:  # south
                    res[row_index + 1][col_index] = cur_point_height + 1
                    new_bfs_queue.append((row_index + 1, col_index))
                if col_index - 1 >= 0 and res[row_index][col_index - 1] == -1:  # west
                    res[row_index][col_index - 1] = cur_point_height + 1
                    new_bfs_queue.append((row_index, col_index - 1))
                if row_index - 1 >= 0 and res[row_index - 1][col_index] == -1:  # north
                    res[row_index - 1][col_index] = cur_point_height + 1
                    new_bfs_queue.append((row_index - 1, col_index))

            bfs_queue = new_bfs_queue  # to explore all the next points

        return res


def main():
    # Example 1: Output: [
    #     [1, 0],
    #     [2, 1]
    # ]
    # isWater = [
    #     [0, 1],
    #     [0, 0]
    # ]

    # Example 2: Output: [
    #     [1, 1, 0],
    #     [0, 1, 1],
    #     [1, 2, 2]
    # ]
    isWater = [
        [0, 0, 1],
        [1, 0, 0],
        [0, 0, 0]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.highestPeak(isWater)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
