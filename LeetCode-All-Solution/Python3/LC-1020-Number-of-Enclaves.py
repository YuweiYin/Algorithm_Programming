#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1020-Number-of-Enclaves.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-12
=================================================================="""

import sys
import time
from typing import List
import collections

"""
LeetCode - 1020 - (Medium) - Number of Enclaves
https://leetcode.com/problems/number-of-enclaves/

Description & Requirement:
    You are given an m x n binary matrix grid, 
    where 0 represents a sea cell and 1 represents a land cell.

    A move consists of walking from one land cell to another adjacent (4-directionally) land cell 
    or walking off the boundary of the grid.

    Return the number of land cells in grid for which 
    we cannot walk off the boundary of the grid in any number of moves.

Example 1:
    Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    Output: 3
    Explanation: There are three 1s that are enclosed by 0s, 
        and one 1 that is not enclosed because its on the boundary.
Example 2:
    Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    Output: 0
    Explanation: All 1s are either on the boundary or can reach the boundary.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 500
    grid[i][j] is either 0 or 1.
"""


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # exception case
        if not isinstance(grid, list) or len(grid) <= 0 or not isinstance(grid[0], list) or len(grid[0]) <= 0:
            return 0  # Error input type
        max_col = len(grid[0])
        for row in grid:
            if not isinstance(row, list) or len(row) != max_col:
                return 0  # Error input type
        # main method: (bfs, detect grid border)
        return self._numEnclaves(grid)

    def _numEnclaves(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        assert max_row >= 1
        max_col = len(grid[0])
        assert max_col >= 1

        move_direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # east, south, west, north

        def __bfs(_row, _col) -> int:
            # if is enclave, return its area, else return 0
            # once visited, change the value of grip[i][j] to 2
            visited_enclave = set()
            is_enclave = True

            bfs_queue = collections.deque()
            bfs_queue.append((_row, _col))
            visited_enclave.add((_row, _col))

            while len(bfs_queue) > 0:
                cur_row, cur_col = bfs_queue.popleft()
                grid[cur_row][cur_col] = 2

                # if encounter the border, then this area is not an enclave (but still keep the bfs process)
                if cur_row == 0 or cur_row == max_row - 1 or cur_col == 0 or cur_col == max_col - 1:
                    is_enclave = False

                # go east, south, west, north
                for direction in move_direction:
                    row_move, col_move = direction
                    next_row, next_col = cur_row + row_move, cur_col + col_move
                    if 0 <= next_row < max_row and 0 <= next_col < max_col and grid[next_row][next_col] == 1 and \
                            (next_row, next_col) not in visited_enclave:
                        visited_enclave.add((next_row, next_col))
                        bfs_queue.append((next_row, next_col))

            return len(visited_enclave) if is_enclave else 0

        enclave_area = 0
        for row in range(1, max_row - 1):  # don't consider border
            for col in range(1, max_col - 1):  # don't consider border
                if grid[row][col] == 1:
                    enclave_area += __bfs(row, col)

        return enclave_area


def main():
    # Example 1: Output: 3
    # grid = [
    #     [0, 0, 0, 0],
    #     [1, 0, 1, 0],
    #     [0, 1, 1, 0],
    #     [0, 0, 0, 0]
    # ]

    # Example 2: Output: 0
    # grid = [
    #     [0, 1, 1, 0],
    #     [0, 0, 1, 0],
    #     [0, 0, 1, 0],
    #     [0, 0, 0, 0]
    # ]

    # Example 3: Output: 3
    # grid = [
    #     [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    #     [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    #     [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    #     [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    #     [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    #     [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    #     [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    #     [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    #     [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]
    # ]

    # Example 4: Output: 27
    grid = [
        [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numEnclaves(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
