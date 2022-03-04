#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0799-Champagne-Tower.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-04
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0799 - (Medium) - Champagne Tower
https://leetcode.com/problems/champagne-tower/

Description & Requirement:
    We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, 
    and so on until the 100th row.  Each glass holds one cup of champagne.

    Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, 
    any excess liquid poured will fall equally to the glass immediately to the left and right of it.  
    When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, 
    and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

    For example, after one cup of champagne is poured, the top most glass is full.  
    After two cups of champagne are poured, the two glasses on the second row are half full.  
    After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  
    After four cups of champagne are poured, the third row has the middle glass half full, 
    and the two outside glasses are a quarter full, as pictured below.

    Now after pouring some non-negative integer cups of champagne, 
    return how full the jth glass in the ith row is (both i and j are 0-indexed.)

Example 1:
    Input: poured = 1, query_row = 1, query_glass = 1
    Output: 0.00000
    Explanation: We poured 1 cup of champagne to the top glass of the tower (which is indexed as (0, 0)). 
        There will be no excess liquid so all the glasses under the top glass will remain empty.
Example 2:
    Input: poured = 2, query_row = 1, query_glass = 1
    Output: 0.50000
    Explanation: We poured 2 cups of champagne to the top glass of the tower (which is indexed as (0, 0)). 
        There is one cup of excess liquid. The glass indexed as (1, 0) 
        and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champagne.
Example 3:
    Input: poured = 100000009, query_row = 33, query_glass = 17
    Output: 1.00000

Constraints:
    0 <= poured <= 10^9
    0 <= query_glass <= query_row < 100
"""


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # exception case
        assert isinstance(poured, int) and poured >= 0
        assert isinstance(query_row, int) and query_row >= 0
        assert isinstance(query_glass, int) and query_glass <= query_row
        if poured == 0:  # no champagne, so all cups are empty
            return float(0.0)
        if query_row == 0:  # now poured >= 1, and query for the first cup, so it must be full
            return float(1.0)
        # main method: (simulate the pouring process)
        #     if n cups of champagne are poured into a cup, then (n - 1) / 2 will overflow into its left and right cups
        return self._champagneTower(poured, query_row, query_glass)

    def _champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        max_row = 100
        float_0, float_1, float_2 = float(0.0), float(1.0), float(2.0)

        cup_state = []
        for row_max_cup in range(1, max_row + 2):  # set 101 rows
            cup_state.append([float_0 for _ in range(row_max_cup)])
        cup_state[0][0] = float(poured)

        # if n cups of champagne are poured into a cup, then (n - 1) / 2 will overflow into its left and right cups
        for row_idx in range(query_row):
            for cup_idx in range(row_idx + 1):
                if cup_state[row_idx][cup_idx] > float_1:
                    overflow_half = (cup_state[row_idx][cup_idx] - float_1) / float_2
                    # overflow into its left and right cups
                    cup_state[row_idx + 1][cup_idx] += overflow_half
                    cup_state[row_idx + 1][cup_idx + 1] += overflow_half

        return float_1 if cup_state[query_row][query_glass] >= float_1 else cup_state[query_row][query_glass]


def main():
    # Example 1: Output: 0.00000
    # poured, query_row, query_glass = 1, 1, 1

    # Example 2: Output: 0.50000
    # poured, query_row, query_glass = 2, 1, 1

    # Example 3: Output: 1.00000
    poured, query_row, query_glass = 100000009, 33, 17

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.champagneTower(poured, query_row, query_glass)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
