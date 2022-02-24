#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1706-Where-Will-the-Ball-Fall.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-24
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1706 - (Medium) - Where Will the Ball Fall
https://leetcode.com/problems/where-will-the-ball-fall/

Description & Requirement:
    You have a 2-D grid of size m x n representing a box, and you have n balls. 
    The box is open on the top and bottom sides.

    Each cell in the box has a diagonal board spanning two corners of the cell 
    that can redirect a ball to the right or to the left.
        A board that redirects the ball to the right spans the top-left corner to the bottom-right corner 
            and is represented in the grid as 1.
        A board that redirects the ball to the left spans the top-right corner to the bottom-left corner 
            and is represented in the grid as -1.

    We drop one ball at the top of each column of the box. 
    Each ball can get stuck in the box or fall out of the bottom. 
    A ball gets stuck if it hits a "V" shaped pattern between two boards or 
    if a board redirects the ball into either wall of the box.

    Return an array answer of size n where answer[i] is the column 
    that the ball falls out of at the bottom after dropping the ball from the ith column at the top, 
    or -1 if the ball gets stuck in the box.

Example 1:
    Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
    Output: [1,-1,-1,-1,-1]
    Explanation: This example is shown in the photo.
        Ball b0 is dropped at column 0 and falls out of the box at column 1.
        Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
        Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
        Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
        Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.
Example 2:
    Input: grid = [[-1]]
    Output: [-1]
    Explanation: The ball gets stuck against the left wall.
Example 3:
    Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
    Output: [0,1,2,3,4,-1]

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    grid[i][j] is 1 or -1.
"""


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(grid, list) and len(grid) > 0 and isinstance(grid[0], list) and len(grid[0]) > 0
        max_col = len(grid[0])
        for row in grid:
            assert isinstance(row, list) and len(row) == max_col
            for item in row:
                assert item == 1 or item == -1
        # main method: (stimulate the falling process)
        return self._findBall(grid)

    def _findBall(self, grid: List[List[int]]) -> List[int]:
        max_row = len(grid)
        assert max_row > 0
        max_col = len(grid[0])
        assert max_col > 0

        # -1 means can't reach the bottom row
        res = [-1 for _ in range(max_col)]

        # simulate the falling process of each ball
        for ball_idx in range(max_col):
            cur_col = ball_idx
            can_fall = True
            for cur_row in range(max_row):
                if grid[cur_row][cur_col] == 1:  # the top-left corner to the bottom-right corner
                    if cur_col == max_col - 1 or grid[cur_row][cur_col + 1] == -1:  # right is wall or form a "V"
                        can_fall = False
                        break
                    else:
                        cur_col += 1  # move right
                else:  # the top-right corner to the bottom-left corner
                    if cur_col == 0 or grid[cur_row][cur_col - 1] == 1:  # left is wall or form a "V"
                        can_fall = False
                        break
                    else:
                        cur_col -= 1  # move left
            if can_fall:
                res[ball_idx] = cur_col

        return res


def main():
    # Example 1: Output: [1,-1,-1,-1,-1]
    # grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]

    # Example 2: Output: [-1]
    # grid = [[-1]]

    # Example 3: Output: [0,1,2,3,4,-1]
    grid = [
        [1, 1, 1, 1, 1, 1],
        [-1, -1, -1, -1, -1, -1],
        [1, 1, 1, 1, 1, 1],
        [-1, -1, -1, -1, -1, -1]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findBall(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
