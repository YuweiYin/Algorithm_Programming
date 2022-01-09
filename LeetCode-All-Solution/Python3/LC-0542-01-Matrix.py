#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0542-01-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-09
=================================================================="""

import sys
import time
from typing import List
# import functools
# import queue
import collections

"""
LeetCode - 0542 - (Medium) - 01 Matrix
https://leetcode.com/problems/01-matrix/

Description & Requirement:
    Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
    The distance between two adjacent cells is 1.

Example 1:
    Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
    Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:
    Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
    Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 10^4
    1 <= m * n <= 10^4
    mat[i][j] is either 0 or 1.
    There is at least one 0 in mat.
"""


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # exception case
        if not isinstance(mat, list) or len(mat) <= 0 or not isinstance(mat[0], list):
            return []
        len_c = len(mat[0])  # check every row is the same length
        exist_0 = False
        for row in mat:
            if not isinstance(row, list) or len(row) != len_c:
                return []
            if not exist_0:  # find at least one 0
                for num in row:
                    if num == 0:
                        exist_0 = True
                        break
        # main method: multi-source BFS
        return self._updateMatrix(mat)

    def _updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        max_row = len(mat)
        max_col = len(mat[0])

        # INF = sys.maxsize  # max int
        INF = max_row * max_col + 1
        distance_mat = [[INF for _ in range(max_col)] for _ in range(max_row)]

        bfs_queue = collections.deque()
        for row in range(max_row):
            for col in range(max_col):
                if mat[row][col] == 0:  # find all 0
                    distance_mat[row][col] = 0
                    bfs_queue.append([row, col])  # bfs starts from all 0

        while len(bfs_queue) > 0:
            cur_row, cur_col = bfs_queue.popleft()
            cur_dis = distance_mat[cur_row][cur_col]
            if 0 <= cur_col - 1 and distance_mat[cur_row][cur_col - 1] == INF:  # left
                distance_mat[cur_row][cur_col - 1] = cur_dis + 1
                bfs_queue.append([cur_row, cur_col - 1])
            if 0 <= cur_row - 1 and distance_mat[cur_row - 1][cur_col] == INF:  # up
                distance_mat[cur_row - 1][cur_col] = cur_dis + 1
                bfs_queue.append([cur_row - 1, cur_col])
            if cur_col + 1 < max_col and distance_mat[cur_row][cur_col + 1] == INF:  # right
                distance_mat[cur_row][cur_col + 1] = cur_dis + 1
                bfs_queue.append([cur_row, cur_col + 1])
            if cur_row + 1 < max_row and distance_mat[cur_row + 1][cur_col] == INF:  # down
                distance_mat[cur_row + 1][cur_col] = cur_dis + 1
                bfs_queue.append([cur_row + 1, cur_col])

        # DFS error
        # # @functools.lru_cache(maxsize=None)
        # def __dfs(cur_row, cur_col):
        #     if mat[cur_row][cur_col] == 0:  # distance = 0 if cur_num is 0
        #         distance_mat[cur_row][cur_col] = 0
        #         return 0
        #
        #     if distance_mat[cur_row][cur_col] == INF:  # avoid repeat
        #         if 0 <= cur_col - 1:  # left
        #             distance_mat[cur_row][cur_col] = min(
        #                 distance_mat[cur_row][cur_col], __dfs(cur_row, cur_col - 1) + 1)
        #         if 0 <= cur_row - 1:  # up
        #             distance_mat[cur_row][cur_col] = min(
        #                 distance_mat[cur_row][cur_col], __dfs(cur_row - 1, cur_col) + 1)
        #         if cur_col + 1 < max_col:  # right
        #             distance_mat[cur_row][cur_col] = min(
        #                 distance_mat[cur_row][cur_col], __dfs(cur_row, cur_col + 1) + 1)
        #         if cur_row + 1 < max_row:  # down
        #             distance_mat[cur_row][cur_col] = min(
        #                 distance_mat[cur_row][cur_col], __dfs(cur_row + 1, cur_col) + 1)
        #
        #     return distance_mat[cur_row][cur_col]
        #
        # for row in range(max_row):
        #     for col in range(max_col):
        #         __dfs(row, col)  # deal with each item

        return distance_mat


def main():
    # Example 1: Output: [[0,0,0],[0,1,0],[0,0,0]]
    # mat = [
    #     [0, 0, 0],
    #     [0, 1, 0],
    #     [0, 0, 0]
    # ]

    # Example 2: Output: [[0,0,0],[0,1,0],[1,2,1]]
    # mat = [
    #     [0, 0, 0],
    #     [0, 1, 0],
    #     [1, 1, 1]
    # ]

    # Example 3: Output: [
    #       [2,1,0,0,1,0,0,1,1,0],
    #       [1,0,0,1,0,1,1,2,2,1],
    #       [1,1,1,0,0,1,2,2,1,0],
    #       [0,1,2,1,0,1,2,3,2,1],
    #       [0,0,1,2,1,2,1,2,1,0],
    #       [1,1,2,3,2,1,0,1,1,1],
    #       [0,1,2,3,2,1,1,0,0,1],
    #       [1,2,1,2,1,0,0,1,1,2],
    #       [0,1,0,1,1,0,1,2,2,3],
    #       [1,2,1,0,1,0,1,2,3,4]
    #   ]
    mat = [
        [1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
        [1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.updateMatrix(mat)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
