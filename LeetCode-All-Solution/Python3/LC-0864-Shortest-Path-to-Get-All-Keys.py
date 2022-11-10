#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0864-Shortest-Path-to-Get-All-Keys.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-10
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0864 - (Hard) - Shortest Path to Get All Keys
https://leetcode.com/problems/shortest-path-to-get-all-keys/

Description & Requirement:
You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
    You start at the starting point and one move consists of walking one space in one of the four cardinal directions. 
    You cannot walk outside the grid, or walk into a wall.

    If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

    For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters 
    of the English alphabet in the grid. This means that there is exactly one key for each lock, 
    and one lock for each key; and also that the letters used to represent the keys and locks were chosen 
    in the same order as the English alphabet.

    Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

Example 1:
    Input: grid = ["@.a..","###.#","b.A.B"]
    Output: 8
    Explanation: Note that the goal is to obtain all the keys not to open all the locks.
Example 2:
    Input: grid = ["@..aA","..B#.","....b"]
    Output: 6
Example 3:
    Input: grid = ["@Aa"]
    Output: -1

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 30
    grid[i][j] is either an English letter, '.', '#', or '@'.
    The number of keys in the grid is in the range [1, 6].
    Each key in the grid is unique.
    Each key in the grid has a matching lock.
"""


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1
        n = len(grid[0])
        for row in grid:
            assert isinstance(row, str) and len(row) == n
        # main method: (BFS)
        return self._shortestPathAllKeys(grid)

    def _shortestPathAllKeys(self, grid: List[str]) -> int:
        """
        Runtime: 705 ms, faster than 71.71% of Python3 online submissions for Shortest Path to Get All Keys.
        Memory Usage: 18.8 MB, less than 72.49% of Python3 online submissions for Shortest Path to Get All Keys.
        """
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1
        m = len(grid)
        n = len(grid[0])

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        sx = sy = 0
        key_to_idx = dict()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    sx, sy = i, j
                elif grid[i][j].islower():
                    if grid[i][j] not in key_to_idx:
                        idx = len(key_to_idx)
                        key_to_idx[grid[i][j]] = idx

        queue = collections.deque([(sx, sy, 0)])
        dist = dict()
        dist[(sx, sy, 0)] = 0
        while len(queue) > 0:
            x, y, mask = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
                    if grid[nx][ny] == "." or grid[nx][ny] == "@":
                        if (nx, ny, mask) not in dist:
                            dist[(nx, ny, mask)] = dist[(x, y, mask)] + 1
                            queue.append((nx, ny, mask))
                    elif grid[nx][ny].islower():
                        idx = key_to_idx[grid[nx][ny]]
                        if (nx, ny, mask | (1 << idx)) not in dist:
                            dist[(nx, ny, mask | (1 << idx))] = dist[(x, y, mask)] + 1
                            if (mask | (1 << idx)) == (1 << len(key_to_idx)) - 1:
                                return dist[(nx, ny, mask | (1 << idx))]
                            queue.append((nx, ny, mask | (1 << idx)))
                    else:
                        idx = key_to_idx[grid[nx][ny].lower()]
                        if (mask & (1 << idx)) and (nx, ny, mask) not in dist:
                            dist[(nx, ny, mask)] = dist[(x, y, mask)] + 1
                            queue.append((nx, ny, mask))

        return -1


def main():
    # Example 1: Output: 8
    # grid = ["@.a..", "###.#", "b.A.B"]

    # Example 2: Output: 6
    grid = ["@..aA", "..B#.", "....b"]

    # Example 3: Output: -1
    # grid = ["@Aa"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.shortestPathAllKeys(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
