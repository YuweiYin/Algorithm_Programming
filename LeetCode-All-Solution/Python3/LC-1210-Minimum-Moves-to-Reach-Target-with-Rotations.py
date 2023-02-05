#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1210-Minimum-Moves-to-Reach-Target-with-Rotations.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-05
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1210 - (Hard) - Minimum Moves to Reach Target with Rotations
https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

Description & Requirement:
    In an n*n grid, there is a snake that spans 2 cells and starts moving from the top left corner at (0, 0) and (0, 1).
    The grid has empty cells represented by zeros and blocked cells represented by ones. 
    The snake wants to reach the lower right corner at (n-1, n-2) and (n-1, n-1).

    In one move the snake can:
        Move one cell to the right if there are no blocked cells there. 
            This move keeps the horizontal/vertical position of the snake as it is.
        Move down one cell if there are no blocked cells there. 
            This move keeps the horizontal/vertical position of the snake as it is.
        Rotate clockwise if it's in a horizontal position and the two cells under it are both empty. 
            In that case the snake moves from (r, c) and (r, c+1) to (r, c) and (r+1, c).
        Rotate counterclockwise if it's in a vertical position and the two cells to its right are both empty. 
            In that case the snake moves from (r, c) and (r+1, c) to (r, c) and (r, c+1).

    Return the minimum number of moves to reach the target.

    If there is no way to reach the target, return -1.

Example 1:
    Input: grid = [[0,0,0,0,0,1],
                   [1,1,0,0,1,0],
                   [0,0,0,0,1,1],
                   [0,0,1,0,1,0],
                   [0,1,1,0,0,0],
                   [0,1,1,0,0,0]]
    Output: 11
    Explanation:
        One possible solution is [right, right, rotate clockwise, right, 
        down, down, down, down, rotate counterclockwise, right, down].
Example 2:
    Input: grid = [[0,0,1,1,1,1],
                   [0,0,0,0,1,1],
                   [1,1,0,0,0,1],
                   [1,1,1,0,0,1],
                   [1,1,1,0,0,1],
                   [1,1,1,0,0,0]]
    Output: 9

Constraints:
    2 <= n <= 100
    0 <= grid[i][j] <= 1
    It is guaranteed that the snake starts at empty cells.
"""


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 2 and len(grid[0]) >= 2
        n = len(grid)
        for row in grid:
            assert isinstance(row, list) and len(row) == n and all([num >= 0 for num in row])
        # main method: (BFS)
        return self._minimumMoves(grid)

    def _minimumMoves(self, grid: List[List[int]]) -> int:
        """
        Time: beats 100%; Space: beats 57.89%
        """
        assert isinstance(grid, list) and len(grid) >= 2 and len(grid[0]) >= 2
        n = len(grid)

        dist = {(0, 0, 0): 0}
        queue = collections.deque([(0, 0, 0)])

        while len(queue) > 0:
            x, y, status = queue.popleft()
            if status == 0:
                # right
                if y + 2 < n and (x, y + 1, 0) not in dist and grid[x][y + 2] == 0:
                    dist[(x, y + 1, 0)] = dist[(x, y, 0)] + 1
                    queue.append((x, y + 1, 0))

                # down
                if x + 1 < n and (x + 1, y, 0) not in dist and grid[x + 1][y] == grid[x + 1][y + 1] == 0:
                    dist[(x + 1, y, 0)] = dist[(x, y, 0)] + 1
                    queue.append((x + 1, y, 0))

                # clockwise rotate 90 degree
                if x + 1 < n and y + 1 < n and (x, y, 1) not in dist and grid[x + 1][y] == grid[x + 1][y + 1] == 0:
                    dist[(x, y, 1)] = dist[(x, y, 0)] + 1
                    queue.append((x, y, 1))
            else:
                # right
                if y + 1 < n and (x, y + 1, 1) not in dist and grid[x][y + 1] == grid[x + 1][y + 1] == 0:
                    dist[(x, y + 1, 1)] = dist[(x, y, 1)] + 1
                    queue.append((x, y + 1, 1))

                # down
                if x + 2 < n and (x + 1, y, 1) not in dist and grid[x + 2][y] == 0:
                    dist[(x + 1, y, 1)] = dist[(x, y, 1)] + 1
                    queue.append((x + 1, y, 1))

                # anticlockwise rotate 90 degree
                if x + 1 < n and y + 1 < n and (x, y, 0) not in dist and grid[x][y + 1] == grid[x + 1][y + 1] == 0:
                    dist[(x, y, 0)] = dist[(x, y, 1)] + 1
                    queue.append((x, y, 0))

        return dist.get((n - 1, n - 2, 0), -1)


def main():
    # Example 1: Output: 11
    grid = [[0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0]]

    # Example 2: Output: 9
    # grid = [[0, 0, 1, 1, 1, 1],
    #         [0, 0, 0, 0, 1, 1],
    #         [1, 1, 0, 0, 0, 1],
    #         [1, 1, 1, 0, 0, 1],
    #         [1, 1, 1, 0, 0, 1],
    #         [1, 1, 1, 0, 0, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumMoves(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
