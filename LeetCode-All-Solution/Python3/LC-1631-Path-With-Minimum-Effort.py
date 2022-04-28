#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1631-Path-With-Minimum-Effort.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-28
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1631 - (Medium) - Path With Minimum Effort
https://leetcode.com/problems/path-with-minimum-effort/

Description & Requirement:
    You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, 
    where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), 
    and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). 
    You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

    A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

    Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:
    Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
    Output: 2
    Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
        This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:
    Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
    Output: 1
    Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, 
        which is better than route [1,3,5,3,5].
Example 3:
    Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    Output: 0
    Explanation: This route does not require any effort.

Constraints:
    rows == heights.length
    columns == heights[i].length
    1 <= rows, columns <= 100
    1 <= heights[i][j] <= 10^6
"""


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # exception case
        assert isinstance(heights, list) and len(heights) >= 1 and len(heights[0]) >= 1
        max_col = len(heights[0])
        for row in heights:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (Dynamic Programming: Wrong)
        #     dp equation: dp[i][j] = min(
        #                                 max(dp[i-1][j], abs(heights[i][j] - heights[i-1][j])),
        #                                 max(dp[i][j-1], abs(heights[i][j] - heights[i][j-1]))
        #                             )
        #                  dp[0][0] = 0
        #                  dp[0][j] = max(dp[0][j-1], abs(heights[0][j] - heights[0][j-1]))
        #                  dp[i][0] = max(dp[i-1][0], abs(heights[i][0] - heights[i-1][0]))
        #                  where, 1 <= i < max_row, 1 <= j < max_col
        #     dp aim: get dp[-1][-1]
        # main method: BFS + binary search
        return self._minimumEffortPath(heights)

    def _minimumEffortPathDP(self, heights: List[List[int]]) -> int:
        assert isinstance(heights, list) and len(heights) >= 1 and len(heights[0]) >= 1
        max_row = len(heights)
        max_col = len(heights[0])

        # 1 <= rows, columns <= 100, 1 <= heights[i][j] <= 10^6, so 1e9+7 is INF
        dp = [[int(1e9+7) for _ in range(max_col)] for _ in range(max_row)]
        dp[0][0] = 0
        for j in range(1, max_col):
            dp[0][j] = max(dp[0][j - 1], abs(heights[0][j] - heights[0][j - 1]))
        for i in range(1, max_row):
            dp[i][0] = max(dp[i - 1][0], abs(heights[i][0] - heights[i - 1][0]))

        for i in range(1, max_row):
            for j in range(1, max_col):
                dp[i][j] = min(
                    max(dp[i - 1][j], abs(heights[i][j] - heights[i - 1][j])),
                    max(dp[i][j - 1], abs(heights[i][j] - heights[i][j - 1]))
                )

        return dp[-1][-1]

    def _minimumEffortPath(self, heights: List[List[int]]) -> int:
        assert isinstance(heights, list) and len(heights) >= 1 and len(heights[0]) >= 1
        max_row = len(heights)
        max_col = len(heights[0])

        res = 0
        left = 0  # min res (left border)
        right = int(1e6-1)  # max res (right border), 1 <= heights[i][j] <= 10^6

        while left <= right:  # binary search
            mid = (left + right) >> 1
            bfs_queue = collections.deque()
            bfs_queue.append((0, 0))
            visit_set = {(0, 0)}

            while len(bfs_queue) > 0:  # BFS
                r, c = bfs_queue.popleft()
                if c + 1 < max_col and (r, c + 1) not in visit_set and abs(heights[r][c] - heights[r][c + 1]) <= mid:
                    bfs_queue.append((r, c + 1))
                    visit_set.add((r, c + 1))
                if c - 1 >= 0 and (r, c - 1) not in visit_set and abs(heights[r][c] - heights[r][c - 1]) <= mid:
                    bfs_queue.append((r, c - 1))
                    visit_set.add((r, c - 1))
                if r + 1 < max_row and (r + 1, c) not in visit_set and abs(heights[r][c] - heights[r + 1][c]) <= mid:
                    bfs_queue.append((r + 1, c))
                    visit_set.add((r + 1, c))
                if r - 1 >= 0 and (r - 1, c) not in visit_set and abs(heights[r][c] - heights[r - 1][c]) <= mid:
                    bfs_queue.append((r - 1, c))
                    visit_set.add((r - 1, c))

            if (max_row - 1, max_col - 1) in visit_set:  # can arrive the target cell
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res


def main():
    # Example 1: Output: 2
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]

    # Example 2: Output: 1
    # heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]

    # Example 3: Output: 0
    # heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumEffortPath(heights)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
