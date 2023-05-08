#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1263-Minimum-Moves-to-Move-a-Box-to-Their-Target-Location.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-08
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1263 - (Hard) - Minimum Moves to Move a Box to Their Target Location
https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

Description & Requirement:
    A storekeeper is a game in which the player pushes boxes around 
    in a warehouse trying to get them to target locations.

    The game is represented by an m x n grid of characters grid where 
    each element is a wall, floor, or box.

    Your task is to move the box 'B' to the target position 'T' under the following rules:
        The character 'S' represents the player. The player can move up, down, left, right 
            in grid if it is a floor (empty cell).
        The character '.' represents the floor which means a free cell to walk.
        The character '#' represents the wall which means an obstacle (impossible to walk there).
        There is only one box 'B' and one target cell 'T' in the grid.
        The box can be moved to an adjacent free cell by standing next to the box and then 
            moving in the direction of the box. This is a push.
        The player cannot walk through the box.

    Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.

Example 1:
    Input: grid = [["#","#","#","#","#","#"],
                   ["#","T","#","#","#","#"],
                   ["#",".",".","B",".","#"],
                   ["#",".","#","#",".","#"],
                   ["#",".",".",".","S","#"],
                   ["#","#","#","#","#","#"]]
    Output: 3
    Explanation: We return only the number of times the box is pushed.
Example 2:
    Input: grid = [["#","#","#","#","#","#"],
                   ["#","T","#","#","#","#"],
                   ["#",".",".","B",".","#"],
                   ["#","#","#","#",".","#"],
                   ["#",".",".",".","S","#"],
                   ["#","#","#","#","#","#"]]
    Output: -1
Example 3:
    Input: grid = [["#","#","#","#","#","#"],
                   ["#","T",".",".","#","#"],
                   ["#",".","#","B",".","#"],
                   ["#",".",".",".",".","#"],
                   ["#",".",".",".","S","#"],
                   ["#","#","#","#","#","#"]]
    Output: 5
    Explanation: push the box down, left, left, up and up.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 20
    grid contains only characters '.', '#', 'S', 'T', or 'B'.
    There is only one character 'S', 'B', and 'T' in the grid.
"""


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1
        # main method: (BFS and dynamic programming)
        return self._minPushBox(grid)

    def _minPushBox(self, grid: List[List[str]]) -> int:
        assert isinstance(grid, list) and len(grid) >= 1

        m = len(grid)
        n = len(grid[0])
        sx, sy, bx, by = None, None, None, None
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 'S':
                    sx = x
                    sy = y
                elif grid[x][y] == 'B':
                    bx = x
                    by = y

        def __valid(x, y) -> bool:
            return 0 <= x < m and 0 <= y < n and grid[x][y] != "#"

        d = [0, -1, 0, 1, 0]
        dp = [[float("inf")] * (m * n) for _ in range(m * n)]
        dp[sx * n + sy][bx * n + by] = 0
        queue = collections.deque([(sx * n + sy, bx * n + by)])
        while len(queue) > 0:
            queue_new = collections.deque()
            while len(queue) > 0:
                s1, b1 = queue.popleft()
                sx1, sy1 = s1 // n, s1 % n
                bx1, by1 = b1 // n, b1 % n

                if grid[bx1][by1] == "T":
                    return int(dp[s1][b1])

                for i in range(4):
                    sx2, sy2 = sx1 + d[i], sy1 + d[i + 1]
                    s2 = sx2 * n + sy2

                    if not __valid(sx2, sy2):
                        continue

                    if sx2 == bx1 and sy2 == by1:
                        bx2, by2 = bx1 + d[i], by1 + d[i + 1]
                        b2 = bx2 * n + by2

                        if not __valid(bx2, by2) or dp[s2][b2] <= dp[s1][b1] + 1:
                            continue

                        dp[s2][b2] = dp[s1][b1] + 1
                        queue_new.append((s2, b2))
                    else:
                        if dp[s2][b1] <= dp[s1][b1]:
                            continue

                        dp[s2][b1] = dp[s1][b1]
                        queue.append((s2, b1))

            queue, queue_new = queue_new, queue

        return -1


def main():
    # Example 1: Output: 3
    # grid = [["#", "#", "#", "#", "#", "#"],
    #         ["#", "T", "#", "#", "#", "#"],
    #         ["#", ".", ".", "B", ".", "#"],
    #         ["#", ".", "#", "#", ".", "#"],
    #         ["#", ".", ".", ".", "S", "#"],
    #         ["#", "#", "#", "#", "#", "#"]]

    # Example 2: Output: -1
    # grid = [["#", "#", "#", "#", "#", "#"],
    #         ["#", "T", "#", "#", "#", "#"],
    #         ["#", ".", ".", "B", ".", "#"],
    #         ["#", "#", "#", "#", ".", "#"],
    #         ["#", ".", ".", ".", "S", "#"],
    #         ["#", "#", "#", "#", "#", "#"]]

    # Example 3: Output: 5
    grid = [["#", "#", "#", "#", "#", "#"],
            ["#", "T", ".", ".", "#", "#"],
            ["#", ".", "#", "B", ".", "#"],
            ["#", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", "S", "#"],
            ["#", "#", "#", "#", "#", "#"]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minPushBox(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
