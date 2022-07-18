#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0749-Contain-Virus.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-18
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0749 - (Hard) - Contain Virus
https://leetcode.com/problems/contain-virus/

Description & Requirement:
    A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

    The world is modeled as an m x n binary grid isInfected, where isInfected[i][j] == 0 represents uninfected cells, 
    and isInfected[i][j] == 1 represents cells contaminated with the virus. 
    A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

    Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. 
    Resources are limited. Each day, you can install walls around only one region 
    (i.e., the affected area (continuous block of infected cells) 
    that threatens the most uninfected cells the following night). There will never be a tie.

    Return the number of walls used to quarantine all the infected regions. 
    If the world will become fully infected, return the number of walls used.

Example 1:
    Input: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
    Output: 10
    Explanation: There are 2 contaminated regions.
        On the first day, add 5 walls to quarantine the viral region on the left.
        On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.
Example 2:
    Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
    Output: 4
    Explanation: Even though there is only one cell saved, there are 4 walls built.
        Notice that walls are only built on the shared boundary of two different cells.
Example 3:
    Input: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
    Output: 13
    Explanation: The region on the left only builds two new walls.

Constraints:
    m == isInfected.length
    n == isInfected[i].length
    1 <= m, n <= 50
    isInfected[i][j] is either 0 or 1.
    There is always a contiguous viral region throughout the described process 
    that will infect strictly more uncontaminated squares in the next round.
"""


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        # exception case
        assert isinstance(isInfected, list) and len(isInfected) >= 1 and len(isInfected[0]) >= 1
        max_col = len(isInfected[0])
        for row in isInfected:
            assert isinstance(row, list) and len(row) == max_col
            for item in row:
                assert isinstance(item, int) and (item == 0 or item == 1)
        # main method: (multi-source BFS)
        return self._containVirus(isInfected)

    def _containVirus(self, isInfected: List[List[int]]) -> int:
        """
        Runtime: 80 ms, faster than 95.56% of Python3 online submissions for Contain Virus.
        Memory Usage: 14.4 MB, less than 98.48% of Python3 online submissions for Contain Virus.
        """
        assert isinstance(isInfected, list) and len(isInfected) >= 1 and len(isInfected[0]) >= 1
        max_row, max_col = len(isInfected), len(isInfected[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0

        while True:
            # each day and night is one while loop
            neighbors, wall_list = [], []
            for row in range(max_row):
                for col in range(max_col):
                    if isInfected[row][col] == 1:
                        bfs_queue = collections.deque([(row, col)])
                        neighbor = set()
                        wall, idx = 0, len(neighbors) + 1
                        isInfected[row][col] = -idx

                        while len(bfs_queue) > 0:
                            x, y = bfs_queue.popleft()
                            for di in directions:
                                x_next, y_next = x + di[0], y + di[1]
                                if 0 <= x_next < max_row and 0 <= y_next < max_col:
                                    if isInfected[x_next][y_next] == 1:
                                        bfs_queue.append((x_next, y_next))
                                        isInfected[x_next][y_next] = -idx
                                    elif isInfected[x_next][y_next] == 0:
                                        wall += 1
                                        neighbor.add((x_next, y_next))

                        neighbors.append(neighbor)
                        wall_list.append(wall)

            if not neighbors:
                break

            idx = 0
            for i in range(1, len(neighbors)):
                if len(neighbors[i]) > len(neighbors[idx]):
                    idx = i

            res += wall_list[idx]
            for i in range(max_row):
                for j in range(max_col):
                    if isInfected[i][j] < 0:
                        if isInfected[i][j] != -idx - 1:
                            isInfected[i][j] = 1
                        else:
                            isInfected[i][j] = 2

            for i, neighbor in enumerate(neighbors):
                if i != idx:
                    for x, y in neighbor:
                        isInfected[x][y] = 1

            if len(neighbors) == 1:
                break

        return res


def main():
    # Example 1: Output: 10
    # isInfected = [
    #     [0, 1, 0, 0, 0, 0, 0, 1],
    #     [0, 1, 0, 0, 0, 0, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 0, 0]
    # ]

    # Example 2: Output: 4
    # isInfected = [
    #     [1, 1, 1],
    #     [1, 0, 1],
    #     [1, 1, 1]
    # ]

    # Example 3: Output: 13
    isInfected = [
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.containVirus(isInfected)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
