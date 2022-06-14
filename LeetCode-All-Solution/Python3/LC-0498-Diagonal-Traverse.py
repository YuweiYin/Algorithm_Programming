#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0498-Diagonal-Traverse.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-14
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0498 - (Medium) - Diagonal Traverse
https://leetcode.com/problems/diagonal-traverse/

Description & Requirement:
    Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
    Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,4,7,5,3,6,8,9]
Example 2:
    Input: mat = [[1,2],[3,4]]
    Output: [1,2,3,4]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 10^4
    1 <= m * n <= 10^4
    -10^5 <= mat[i][j] <= 10^5
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(mat, list) and len(mat) >= 1 and isinstance(mat[0], list) and len(mat[0]) >= 1
        max_col = len(mat[0])
        for row in mat:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (control the sum of row_index and col_index to traverse the matrix)
        return self._findDiagonalOrder(mat)

    def _findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        assert isinstance(mat, list) and len(mat) >= 1 and isinstance(mat[0], list) and len(mat[0]) >= 1
        max_row = len(mat)
        max_col = len(mat[0])

        res = []
        direction = True  # True: from bottom-left to top-right. False: otherwise.
        for cur_sum in range(max_row + max_col - 1):
            if direction:
                cur_row = cur_sum if cur_sum < max_row else max_row - 1
                cur_col = 0 if cur_sum < max_row else cur_sum - max_row + 1
                while cur_row >= 0 and cur_col < max_col:
                    if 0 <= cur_row < max_row:
                        res.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
            else:
                cur_row = 0 if cur_sum < max_col else cur_sum - max_col + 1
                cur_col = cur_sum if cur_sum < max_col else max_col - 1
                while cur_row < max_row and cur_col >= 0:
                    if 0 <= cur_col < max_col:
                        res.append(mat[cur_row][cur_col])
                    cur_row += 1
                    cur_col -= 1
            direction = not direction

        return res


def main():
    # Example 1: Output: [1,2,4,7,5,3,6,8,9]
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Example 2: Output: [1,2,3,4]
    # mat = [
    #     [1, 2],
    #     [3, 4]
    # ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findDiagonalOrder(mat)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
