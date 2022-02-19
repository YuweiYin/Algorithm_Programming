#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1314-Matrix-Block-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-17
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1314 - (Medium) - Matrix Block Sum
https://leetcode.com/problems/matrix-block-sum/

Description & Requirement:
    Given a m x n matrix mat and an integer k, return a matrix answer where 
    each answer[i][j] is the sum of all elements mat[r][c] for:
        i - k <= r <= i + k,
        j - k <= c <= j + k, and
        (r, c) is a valid position in the matrix.

Example 1:
    Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:
    Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
    Output: [[45,45,45],[45,45,45],[45,45,45]]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n, k <= 100
    1 <= mat[i][j] <= 100

Related Problem:
    LC-0304-Range-Sum-Query-2D-Immutable
"""


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # exception case
        assert isinstance(mat, list) and len(mat) > 0 and isinstance(mat[0], list) and len(mat[0]) > 0
        assert isinstance(k, int) and k > 0
        max_col = len(mat[0])
        for row in mat:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (2-dim prefix sum)
        #     record prefix sum of matrix (0, 0) (0, j) (i, 0) (i, j),
        #         where (i, j) from (0, 0) to (max_row-1, max_col-1)
        #     pre_sum(i, j) = pre_sum(i-1, j) + pre_sum(i, j-1) - pre_sum(i-1, j-1) + matrix(i, j)
        #         - pre_sum(i-1, j-1) to remove redundant part, + matrix(i, j) to add up the current square
        #         0 <= i < max_row, 0 <= j < max_col, pre_sum(-1, ?) = 0, pre_sum(?, -1) = 0
        #     res(i, j) = pre_sum(i+k, j+k) - pre_sum(i+k, j-k-1) - pre_sum(i-k-1, j+k) + pre_sum(i-k-1, j-k-1)
        return self._matrixBlockSum(mat, k)

    def _matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # assert len(mat) > 0 and len(mat[0]) > 0
        max_row = len(mat)
        assert max_row > 0
        max_col = len(mat[0])
        assert max_col > 0

        # get 2-dim prefix sum matrix
        prefix_sum = [[0 for _ in range(max_col + 1)] for _ in range(max_row + 1)]  # first row and col are all 0
        for row_idx in range(1, max_row + 1):  # start from index == 1
            for col_idx in range(1, max_col + 1):
                # pre_sum(i, j) = pre_sum(i-1, j) + pre_sum(i, j-1) - pre_sum(i-1, j-1) + matrix(i, j)
                prefix_sum[row_idx][col_idx] = prefix_sum[row_idx - 1][col_idx] + prefix_sum[row_idx][col_idx - 1] - \
                                               prefix_sum[row_idx - 1][col_idx - 1] + mat[row_idx - 1][col_idx - 1]

        def __bounded_prefix_sum(r_index: int, c_index: int):
            bounded_r = min(max_row, max(0, r_index))  # 0 <= bounded_r <= max_row
            bounded_c = min(max_col, max(0, c_index))  # 0 <= bounded_c <= max_col
            return prefix_sum[bounded_r][bounded_c]

        # calculate res based on the prefix sum matrix
        res = [[0 for _ in range(max_col)] for _ in range(max_row)]
        for row_idx in range(max_row):  # start from index == 0
            for col_idx in range(max_col):
                # res(i, j) = pre_sum(i+k, j+k) - pre_sum(i+k, j-k-1) - pre_sum(i-k-1, j+k) + pre_sum(i-k-1, j-k-1)
                res[row_idx][col_idx] = __bounded_prefix_sum(row_idx + k + 1, col_idx + k + 1) - \
                                        __bounded_prefix_sum(row_idx - k, col_idx + k + 1) - \
                                        __bounded_prefix_sum(row_idx + k + 1, col_idx - k) + \
                                        __bounded_prefix_sum(row_idx - k, col_idx - k)

        return res


def main():
    # Example 1: Output: [
    #     [12,21,16],
    #     [27,45,33],
    #     [24,39,28]
    # ]
    # mat = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]
    # k = 1

    # Example 2: Output: [
    #     [45,45,45],
    #     [45,45,45],
    #     [45,45,45]
    # ]
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.matrixBlockSum(mat, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
