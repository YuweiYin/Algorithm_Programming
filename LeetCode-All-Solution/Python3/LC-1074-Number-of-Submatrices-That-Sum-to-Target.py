#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1074-Number-of-Submatrices-That-Sum-to-Target.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-18
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1074 - (Hard) - Number of Submatrices That Sum to Target
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

Description & Requirement:
    Given a matrix and a target, return the number of non-empty sub-matrices that sum to target.

    A sub-matrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

    Two sub-matrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different 
    if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:
    Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
    Output: 4
    Explanation: The four 1x1 sub-matrices that only contain 0.
Example 2:
    Input: matrix = [[1,-1],[-1,1]], target = 0
    Output: 5
    Explanation: The two 1x2 sub-matrices, plus the two 2x1 sub-matrices, plus the 2x2 submatrix.
Example 3:
    Input: matrix = [[904]], target = 0
    Output: 0

Constraints:
    1 <= matrix.length <= 100
    1 <= matrix[0].length <= 100
    -1000 <= matrix[i] <= 1000
    -10^8 <= target <= 10^8
"""


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # exception case
        assert isinstance(target, int)
        assert isinstance(matrix, list) and len(matrix) >= 1 and len(matrix[0]) >= 1
        max_col = len(matrix[0])
        for row in matrix:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (2-dim prefix sum)
        return self._numSubmatrixSumTarget(matrix, target)

    def _numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        Runtime: 1056 ms, faster than 83.41% of Python3 submissions for Number of Submatrices That Sum to Target.
        Memory Usage: 14.9 MB, less than 47.39% of Python3 submissions for Number of Submatrices That Sum to Target.
        """
        assert isinstance(target, int)
        assert isinstance(matrix, list) and len(matrix) >= 1 and len(matrix[0]) >= 1
        max_row, max_col = len(matrix), len(matrix[0])
        res = 0

        def __count_target_sum(prefix_array: List[int], tgt: int) -> int:
            cnt = collections.Counter([0])
            counter = prefix = 0
            for prefix_sum in prefix_array:
                prefix += prefix_sum
                if prefix - tgt in cnt:
                    counter += cnt[prefix - tgt]
                cnt[prefix] += 1
            return counter

        # enumerate the upper bound of rows
        for row_i in range(max_row):
            row_prefix_array = [0 for _ in range(max_col)]
            # enumerate the lower bound of rows
            for row_j in range(row_i, max_row):
                # update the sum of each column
                for col in range(max_col):
                    row_prefix_array[col] += matrix[row_j][col]
                res += __count_target_sum(row_prefix_array, target)

        return res


def main():
    # Example 1: Output: 4
    matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    target = 0

    # Example 2: Output: 5
    # matrix = [[1, -1], [-1, 1]]
    # target = 0

    # Example 3: Output: 0
    # matrix = [[904]]
    # target = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numSubmatrixSumTarget(matrix, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
