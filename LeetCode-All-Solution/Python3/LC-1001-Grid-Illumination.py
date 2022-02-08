#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1001-Grid-Illumination.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-08
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1001 - (Hard) - Grid Illumination
https://leetcode.com/problems/grid-illumination/

Description & Requirement:
    There is a 2D grid of size n x n where each cell of this grid has a lamp that is initially turned off.

    You are given a 2D array of lamp positions lamps, 
    where lamps[i] = [row_i, col_i] indicates that the lamp at grid[row_i][col_i] is turned on. 
    Even if the same lamp is listed more than once, it is turned on.

    When a lamp is turned on, it illuminates its cell and all other cells in the same row, column, or diagonal.

    You are also given another 2D array queries, where queries[j] = [row_j, col_j]. 
    For the jth query, determine whether grid[row_j][col_j] is illuminated or not. 
    After answering the j-th query, turn off the lamp at grid[row_j][col_j] and its 8 adjacent lamps if they exist. 
    A lamp is adjacent if its cell shares either a side or corner with grid[row_j][col_j].

    Return an array of integers ans, 
    where ans[j] should be 1 if the cell in the j-th query was illuminated, or 0 if the lamp was not.

Example 1:
    Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
    Output: [1,0]
    Explanation: We have the initial grid with all lamps turned off. 
        In the above picture we see the grid after turning on the lamp at grid[0][0] 
        then turning on the lamp at grid[4][4].
        The 0th query asks if the lamp at grid[1][1] is illuminated or not (the blue square). 
        It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in the red square.
        The 1st query asks if the lamp at grid[1][0] is illuminated or not (the blue square). 
        It is not illuminated, so set ans[1] = 0. Then, we turn off all lamps in the red rectangle.
Example 2:
    Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
    Output: [1,1]
Example 3:
    Input: n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
    Output: [1,1,0]

Constraints:
    1 <= n <= 10^9
    0 <= lamps.length <= 20000
    0 <= queries.length <= 20000
    lamps[i].length == 2
    0 <= row_i, col_i < n
    queries[j].length == 2
    0 <= row_j, col_j < n
"""


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # exception case
        if not isinstance(queries, list) or len(queries) <= 0:
            return []  # no queries
        if not isinstance(n, int) or n <= 0:
            return [0 for _ in range(len(queries))]  # no grid, all queries are not illuminated
        if not isinstance(lamps, list) or len(lamps) <= 0:
            return [0 for _ in range(len(queries))]  # no lamps, all queries are not illuminated
        # input validation check
        for query in queries:
            assert isinstance(query, list) and len(query) == 2
            assert 0 <= query[0] < n and 0 <= query[1] < n
        for lamp in lamps:
            assert isinstance(lamp, list) and len(lamp) == 2
            assert 0 <= lamp[0] < n and 0 <= lamp[1] < n
        # main method: (hash dict, record if each row/col/diagonal/rev-diagonal is illuminated)
        #     when a lamp is removed, quickly modify all row/col/diagonal/rev-diagonal hash dicts
        return self._gridIllumination(n, lamps, queries)

    def _gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        len_queries = len(queries)
        len_lamps = len(lamps)
        assert n >= 1 and len_queries >= 1 and len_lamps >= 1

        query_answer = []

        # class Lamp:
        #     def __init__(self, row_index: int, col_index: int):
        #         self.row_index = row_index
        #         self.col_index = col_index

        lamp_idx_set = set()

        # row_dict = dict({})  # key: row index; value: lamps that illuminate this row
        # col_dict = dict({})  # key: col index; value: lamps that illuminate this col
        # diagonal_dict = dict({})  # key: diagonal index; value: lamps that illu this diagonal: up-left to down-right
        # rev_diagonal_dict = dict({})  # key: reverse diagonal index; value: lamps illu this r d: up-right to down-left

        row_dict = dict({})  # key: row index; value: how many lamps can illuminate this row
        col_dict = dict({})  # key: col index; value: how many lamps can illuminate this col
        # diagonal_dict: up-left to down-right
        diagonal_dict = dict({})  # key: diagonal index (row - col); value: how many lamps can illuminate this diagonal
        # rev_diagonal_dict: up-right to down-left
        rev_diagonal_dict = dict({})  # key: reverse diagonal index (row + col); value: how many lamps ...

        for r_idx, c_idx in lamps:
            if (r_idx, c_idx) in lamp_idx_set:
                continue
            else:
                lamp_idx_set.add((r_idx, c_idx))

            if r_idx not in row_dict:
                row_dict[r_idx] = 1
            else:
                row_dict[r_idx] += 1

            if c_idx not in col_dict:
                col_dict[c_idx] = 1
            else:
                col_dict[c_idx] += 1

            # here is the optimization of diagonal judgement
            if (r_idx - c_idx) not in diagonal_dict:
                diagonal_dict[r_idx - c_idx] = 1
            else:
                diagonal_dict[r_idx - c_idx] += 1

            if (r_idx + c_idx) not in rev_diagonal_dict:
                rev_diagonal_dict[r_idx + c_idx] = 1
            else:
                rev_diagonal_dict[r_idx + c_idx] += 1

        adjacent_idx_shift = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

        for query in queries:
            q_r_idx, q_c_idx = query

            is_illuminated = False
            if q_r_idx in row_dict and row_dict[q_r_idx] > 0:  # this row has been illuminated
                is_illuminated = True
            elif q_c_idx in col_dict and col_dict[q_c_idx] > 0:  # this col has been illuminated
                is_illuminated = True
            else:  # consider if this diagonal or reverse diagonal has been illuminated
                # diagonal (up-left to down-right):         ..., (i-1, j-1), (i, j), (i+1, j+1), ...
                #     (lamp_row_idx - query_row_idx) == (lamp_col_idx - query_col_idx)
                # reverse diagonal (up-right to down-left): ..., (i-1, j+1), (i, j), (i+1, j-1), ...
                #     (lamp_row_idx + lamp_col_idx) == (query_row_idx + query_col_idx)
                # for lamp_r_idx, lamp_c_idx in lamp_idx_set:  # TODO: can be optimized
                #     if (q_r_idx - lamp_r_idx) == (q_c_idx - lamp_c_idx) or \
                #             (q_r_idx + q_c_idx) == (lamp_r_idx + lamp_c_idx):
                #         is_illuminated = True
                #         break
                if (q_r_idx - q_c_idx) in diagonal_dict and diagonal_dict[q_r_idx - q_c_idx] > 0:
                    is_illuminated = True
                if (q_r_idx + q_c_idx) in rev_diagonal_dict and rev_diagonal_dict[q_r_idx + q_c_idx] > 0:
                    is_illuminated = True
            # answer the query
            if is_illuminated:
                query_answer.append(1)
            else:
                query_answer.append(0)
            # remove lamp and update dict
            for idx_shift in adjacent_idx_shift:
                cur_r_idx, cur_c_idx = q_r_idx + idx_shift[0], q_c_idx + idx_shift[1]
                if not (0 <= cur_r_idx < n and 0 <= cur_c_idx < n):
                    continue
                if (cur_r_idx, cur_c_idx) in lamp_idx_set:
                    # remove lamp
                    lamp_idx_set.discard((cur_r_idx, cur_c_idx))
                    # update dict
                    # if cur_r_idx in row_dict and (cur_r_idx, cur_c_idx) in row_dict[cur_r_idx]:
                    #     row_dict[cur_r_idx].discard((cur_r_idx, cur_c_idx))
                    # if cur_c_idx in col_dict and (cur_r_idx, cur_c_idx) in col_dict[cur_c_idx]:
                    #     col_dict[cur_c_idx].discard((cur_r_idx, cur_c_idx))
                    if cur_r_idx in row_dict:
                        row_dict[cur_r_idx] -= 1
                    if cur_c_idx in col_dict:
                        col_dict[cur_c_idx] -= 1
                    # diagonal
                    if (cur_r_idx - cur_c_idx) in diagonal_dict:
                        diagonal_dict[cur_r_idx - cur_c_idx] -= 1
                    if (cur_r_idx + cur_c_idx) in rev_diagonal_dict:
                        rev_diagonal_dict[cur_r_idx + cur_c_idx] -= 1

        return query_answer


def main():
    # Example 1: Output: [1,0]
    # n = 5
    # lamps = [[0, 0], [4, 4]]
    # queries = [[1, 1], [1, 0]]

    # Example 2: Output: [1,1]
    # n = 5
    # lamps = [[0, 0], [4, 4]]
    # queries = [[1, 1], [1, 1]]

    # Example 3: Output: [1,1,0]
    # n = 5
    # lamps = [[0, 0], [0, 4]]
    # queries = [[0, 4], [0, 1], [1, 4]]

    # Example 4: Output: [1,0]
    n = 6
    lamps = [[1, 1]]
    queries = [[2, 0], [1, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.gridIllumination(n, lamps, queries)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
