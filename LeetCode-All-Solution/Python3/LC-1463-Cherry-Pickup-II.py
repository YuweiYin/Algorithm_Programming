#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1463-Cherry-Pickup-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-08
=================================================================="""
# import collections
import sys
import time
from typing import List
import functools

"""
LeetCode - 1463 - (Hard) - Cherry Pickup II
https://leetcode.com/problems/cherry-pickup-ii/

Description:
    You are given a rows x cols matrix grid representing a field of cherries 
    where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

    You have two robots that can collect cherries for you:
        Robot #1 is located at the top-left corner (0, 0), and
        Robot #2 is located at the top-right corner (0, cols - 1).

Requirement:
    Return the maximum number of cherries collection using both robots by following the rules below:
        From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
        When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
        When both robots stay in the same cell, only one takes the cherries.
        Both robots cannot move outside of the grid at any moment.
        Both robots should reach the bottom row in grid.

Example 1:
    Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
    Output: 24
    Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
        Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
        Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
        Total of cherries: 12 + 12 = 24.
Example 2:
    Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
    Output: 28
    Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
        Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
        Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
        Total of cherries: 17 + 11 = 28.

Constraints:
    rows == grid.length
    cols == grid[i].length
    2 <= rows, cols <= 70
    0 <= grid[i][j] <= 100
"""


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # exception case
        if not isinstance(grid, list) or len(grid) <= 0 or not isinstance(grid[0], list):
            return 0
        len_col = len(grid[0])  # check every row is the same length
        if len_col <= 0:
            return 0
        for row in grid:
            if not isinstance(row, list) or len(row) != len_col:
                return 0
        # main method: Dynamic Programming (Top-Down Memorized Search)
        return self._cherryPickup(grid)

    def _cherryPickup(self, grid: List[List[int]]) -> int:
        max_row= len(grid)
        max_col = len(grid[0])

        def __collect_cherry(row, col1, col2):
            # both robots collect cherries now
            if col1 == col2:  # if they are in the same block, don't collect twice
                return grid[row][col1]
            else:
                return grid[row][col1] + grid[row][col2]

        @functools.lru_cache(maxsize=None)
        def __dfs(row, col1, col2):
            if row == max_row - 1:  # end recursion condition: both robots have reached the last row
                return __collect_cherry(row, col1, col2)  # collect the cherries in the last row

            max_next_cherry = 0  # optimization objective (cherry number) of the next step
            for next_col1 in [col1 - 1, col1, col1 + 1]:  # there are 3 block for robot1 to go next
                for next_col2 in [col2 - 1, col2, col2 + 1]:  # there are also 3 block for robot1 to go next
                    # maximum 9 cases in total, choose the optimal one as the current choice and update max_cherry
                    if 0 <= next_col1 < max_col and 0 <= next_col2 < max_col:  # needless to go out of boundary
                        max_next_cherry = max(max_next_cherry, __dfs(row + 1, next_col1, next_col2))  # next step

            # return: the best result of next step + the current result
            return max_next_cherry + __collect_cherry(row, col1, col2)

        # robot1 starts from [0, 0] and robot2 starts from [0, max_col - 1]
        return __dfs(0, 0, max_col - 1)


def main():
    # Example 1: Output: 24
    grid = [
        [3, 1, 1],
        [2, 5, 1],
        [1, 5, 5],
        [2, 1, 1]
    ]

    # Example 2: Output: 28
    # grid = [
    #     [1, 0, 0, 0, 0, 0, 1],
    #     [2, 0, 0, 0, 0, 3, 0],
    #     [2, 0, 9, 0, 0, 0, 0],
    #     [0, 3, 0, 5, 4, 0, 0],
    #     [1, 0, 2, 3, 0, 0, 6]
    # ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.cherryPickup(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
