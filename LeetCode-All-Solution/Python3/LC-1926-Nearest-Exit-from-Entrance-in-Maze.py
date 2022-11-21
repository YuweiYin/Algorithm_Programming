#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1926-Nearest-Exit-from-Entrance-in-Maze.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-21
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1926 - (Medium) - Nearest Exit from Entrance in Maze
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

Description & Requirement:
    You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+').
    You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column
    of the cell you are initially standing at.

    In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, 
    and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. 
    An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

    Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Example 1:
    Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
    Output: 1
    Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
        Initially, you are at the entrance cell [1,2].
        - You can reach [1,0] by moving 2 steps left.
        - You can reach [0,2] by moving 1 step up.
        It is impossible to reach [2,3] from the entrance.
        Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:
    Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
    Output: 2
    Explanation: There is 1 exit in this maze at [1,2].
        [1,0] does not count as an exit since it is the entrance cell.
        Initially, you are at the entrance cell [1,0].
        - You can reach [1,2] by moving 2 steps right.
        Thus, the nearest exit is [1,2], which is 2 steps away.
Example 3:
    Input: maze = [[".","+"]], entrance = [0,0]
    Output: -1
    Explanation: There are no exits in this maze.

Constraints:
    maze.length == m
    maze[i].length == n
    1 <= m, n <= 100
    maze[i][j] is either '.' or '+'.
    entrance.length == 2
    0 <= entrance_row < m
    0 <= entrance_col < n
    entrance will always be an empty cell.
"""


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # exception case
        assert isinstance(maze, list) and len(maze) >= 1 and len(maze[0]) >= 1
        assert isinstance(entrance, list) and len(entrance) == 2
        # main method: (BFS)
        return self._nearestExit(maze, entrance)

    def _nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        Runtime: 1140 ms, faster than 76.66% of Python3 online submissions for Nearest Exit from Entrance in Maze.
        Memory Usage: 14.6 MB, less than 68.60% of Python3 online submissions for Nearest Exit from Entrance in Maze.
        """
        assert isinstance(maze, list) and len(maze) >= 1 and len(maze[0]) >= 1
        assert isinstance(entrance, list) and len(entrance) == 2
        m, n = len(maze), len(maze[0])

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        queue = collections.deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        while len(queue) > 0:
            cx, cy, d = queue.popleft()
            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                        return d + 1
                    maze[nx][ny] = '+'
                    queue.append((nx, ny, d + 1))

        # no exit
        return -1


def main():
    # Example 1: Output: 1
    maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
    entrance = [1, 2]

    # Example 2: Output: 2
    # maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    # entrance = [1, 0]

    # Example 3: Output: -1
    # maze = [[".", "+"]]
    # entrance = [0, 0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.nearestExit(maze, entrance)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
