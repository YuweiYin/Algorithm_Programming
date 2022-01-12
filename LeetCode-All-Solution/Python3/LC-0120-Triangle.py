#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0120-Triangle.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-12
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0120 - (Medium) - Triangle
https://leetcode.com/problems/triangle/

Description & Requirement:
    Given a triangle array, return the minimum path sum from top to bottom.

    For each step, you may move to an adjacent number of the row below. 
    More formally, if you are on index i on the current row, 
    you may move to either index i or index i + 1 on the next row.

Example 1:
    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11
    Explanation: The triangle looks like:
       2
      3 4
     6 5 7
    4 1 8 3
    The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.
Example 2:
    Input: triangle = [[-10]]
    Output: -10

Constraints:
    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -10^4 <= triangle[i][j] <= 10^4
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # exception case
        if not isinstance(triangle, list) or len(triangle) <= 0:
            return 0  # Error input type
        if len(triangle) == 1:
            return 0 if len(triangle[0]) <= 0 else triangle[0][0]
        valid_len = 1
        for tri in triangle:
            assert isinstance(tri, list) and len(tri) == valid_len
            valid_len += 1
        # main method: (1. one-dimension dynamic programming  2. dfs & backtrack)
        #     dp equation: dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])  i = 1, 2, ...
        #     explanation: when reach (i, j), it can only come from either (i-1, j-1) or (i-1, j)
        return self._minimumTotal(triangle)

    def _minimumTotal(self, triangle: List[List[int]]) -> int:
        max_layer_index = len(triangle)
        assert max_layer_index > 1
        INF = sys.maxsize

        dp = []
        for tri in triangle:
            dp.append([INF for _ in range(len(tri))])

        dp[0][0] = triangle[0][0]  # the top one
        cur_layer_index = 1
        while cur_layer_index < max_layer_index:
            cur_layer_nums = triangle[cur_layer_index]
            len_cur_layer = len(cur_layer_nums)
            assert isinstance(cur_layer_nums, list)
            cur_num_index = 1
            # the middle ones of the current layer can come from their left-up or right-up
            while cur_num_index < len_cur_layer - 1:
                dp[cur_layer_index][cur_num_index] = triangle[cur_layer_index][cur_num_index] + \
                                                     min(dp[cur_layer_index - 1][cur_num_index - 1],
                                                         dp[cur_layer_index - 1][cur_num_index])
                cur_num_index += 1  # move right to the next number of the same layer
            # the first one of the current layer must come from the right-up one
            dp[cur_layer_index][0] = triangle[cur_layer_index][0] + dp[cur_layer_index - 1][0]
            # the last one of the current layer must come from the left-up one
            dp[cur_layer_index][len_cur_layer - 1] = triangle[cur_layer_index][len_cur_layer - 1] + \
                                                     dp[cur_layer_index - 1][len_cur_layer - 2]
            cur_layer_index += 1  # move down to the next layer

        # return the minimum of the bottom layer
        return min(dp[max_layer_index - 1])


def main():
    # Example 1: Output: 11
    #     Explanation: The triangle looks like:
    #        2
    #       3 4
    #      6 5 7
    #     4 1 8 3
    #     The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

    # Example 2: Output: -10
    # triangle = [[-10]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumTotal(triangle)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
