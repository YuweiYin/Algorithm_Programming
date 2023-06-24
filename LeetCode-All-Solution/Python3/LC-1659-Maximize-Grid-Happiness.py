#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1659-Maximize-Grid-Happiness.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-24
=================================================================="""

import sys
import time
from typing import List
# import collections
import functools
# import itertools

"""
LeetCode - 1659 - (Hard) - Maximize Grid Happiness
https://leetcode.com/problems/maximize-grid-happiness/

Description & Requirement:
    You are given four integers, m, n, introvertsCount, and extrovertsCount. 
    You have an m x n grid, and there are two types of people: introverts and extroverts. 
    There are introvertsCount introverts and extrovertsCount extroverts.

    You should decide how many people you want to live in the grid and assign each of them one grid cell. 
    Note that you do not have to have all the people living in the grid.

    The happiness of each person is calculated as follows:
        Introverts start with 120 happiness and lose 30 happiness for each neighbor (introvert or extrovert).
        Extroverts start with 40 happiness and gain 20 happiness for each neighbor (introvert or extrovert).

    Neighbors live in the directly adjacent cells north, east, south, and west of a person's cell.

    The grid happiness is the sum of each person's happiness. Return the maximum possible grid happiness.

Example 1:
    Input: m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
    Output: 240
    Explanation: Assume the grid is 1-indexed with coordinates (row, column).
        We can put the introvert in cell (1,1) and put the extroverts in cells (1,3) and (2,3).
        - Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0 neighbors) = 120
        - Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
        - Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
        The grid happiness is 120 + 60 + 60 = 240.
        The above figure shows the grid in this example with each person's happiness. 
        The introvert stays in the light green cell while the extroverts live on the light purple cells.
Example 2:
    Input: m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
    Output: 260
    Explanation: Place the two introverts in (1,1) and (3,1) and the extrovert at (2,1).
        - Introvert at (1,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
        - Extrovert at (2,1) happiness: 40 (starting happiness) + (2 * 20) (2 neighbors) = 80
        - Introvert at (3,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
        The grid happiness is 90 + 80 + 90 = 260.
Example 3:
    Input: m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
    Output: 240

Constraints:
    1 <= m, n <= 5
    0 <= introvertsCount, extrovertsCount <= min(m * n, 6)
"""


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        # exception case
        assert isinstance(m, int) and m >= 1
        assert isinstance(n, int) and n >= 1
        assert isinstance(introvertsCount, int) and introvertsCount >= 0
        assert isinstance(extrovertsCount, int) and extrovertsCount >= 0
        # main method: (dynamic programming)
        return self._getMaxGridHappiness(m, n, introvertsCount, extrovertsCount)

    def _getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        assert isinstance(m, int) and m >= 1
        assert isinstance(n, int) and n >= 1
        assert isinstance(introvertsCount, int) and introvertsCount >= 0
        assert isinstance(extrovertsCount, int) and extrovertsCount >= 0

        T, N, M = 243, 5, 6
        score = [
            [0, 0, 0],
            [0, -60, -10],
            [0, -10, 40],
        ]

        tot = 3 ** n
        mask_bits = [[0] * N for _ in range(T)]
        iv_count, ev_count = [0] * T, [0] * T
        inner_score = [0] * T
        inter_score = [[0] * T for _ in range(T)]

        # Init
        for mask in range(tot):
            mask_tmp = mask
            for i in range(n):
                x = mask_tmp % 3
                mask_bits[mask][i] = x
                mask_tmp //= 3
                if x == 1:
                    iv_count[mask] += 1
                    inner_score[mask] += 120
                elif x == 2:
                    ev_count[mask] += 1
                    inner_score[mask] += 40
                if i > 0:
                    inner_score[mask] += score[x][mask_bits[mask][i - 1]]

        for i in range(tot):
            for j in range(tot):
                for k in range(n):
                    inter_score[i][j] += score[mask_bits[i][k]][mask_bits[j][k]]

        @functools.lru_cache(maxsize=None)
        def dfs(row: int, pre_mask: int, iv: int, ev: int) -> int:
            if row == m or (iv == 0 and ev == 0):
                return 0
            res = 0
            for mask in range(tot):
                if iv_count[mask] > iv or ev_count[mask] > ev:
                    continue
                res = max(res, dfs(row + 1, mask, iv - iv_count[mask], ev - ev_count[mask]) + inner_score[mask] +
                          inter_score[pre_mask][mask])
            return res

        return dfs(0, 0, introvertsCount, extrovertsCount)


def main():
    # Example 1: Output: 240
    m = 2
    n = 3
    introvertsCount = 1
    extrovertsCount = 2

    # Example 2: Output: 260
    # m = 3
    # n = 1
    # introvertsCount = 2
    # extrovertsCount = 1

    # Example 3: Output: 240
    # m = 2
    # n = 2
    # introvertsCount = 4
    # extrovertsCount = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getMaxGridHappiness(m, n, introvertsCount, extrovertsCount)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
