#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0363-Max-Sum-of-Rectangle-No-Larger-Than-K.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-27
=================================================================="""

import sys
import time
from typing import List
from sortedcontainers import SortedList
# import collections
# import functools

"""
LeetCode - 0363 - (Hard) - Max Sum of Rectangle No Larger Than K
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

Description & Requirement:
    Given an m x n matrix matrix and an integer k, 
    return the max sum of a rectangle in the matrix such that its sum is no larger than k.

    It is guaranteed that there will be a rectangle with a sum no larger than k.

Example 1:
    Input: matrix = [[1,0,1],[0,-2,3]], k = 2
    Output: 2
    Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, 
        and 2 is the max number no larger than k (k = 2).
Example 2:
    Input: matrix = [[2,2,-1]], k = 3
    Output: 3

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -100 <= matrix[i][j] <= 100
    -10^5 <= k <= 10^5

Follow up:
    What if the number of rows is much larger than the number of columns?
"""


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # exception case
        assert isinstance(k, int)
        assert isinstance(matrix, list) and len(matrix) >= 1 and len(matrix[0]) >= 1
        n = len(matrix[0])
        for row in matrix:
            assert isinstance(row, list) and len(row) == n
        # main method: (sorted list & prefix sum)
        return self._maxSumSubmatrix(matrix, k)

    def _maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        assert isinstance(k, int)
        assert isinstance(matrix, list) and len(matrix) >= 1 and len(matrix[0]) >= 1
        m = len(matrix)
        n = len(matrix[0])

        res = -int(1e9+7)  # -10^5 <= k <= 10^5

        for row_left in range(m):  # the index of the left row
            col_sum = [0 for _ in range(n)]  # col_sum[i] is the sum of the i-th column
            for row_right in range(row_left, m):  # the index of the right row
                # get the sum of each column
                for col in range(n):
                    col_sum[col] += matrix[row_right][col]

                sum_set = SortedList([0])
                rectangle_sum = 0

                for v in col_sum:
                    rectangle_sum += v
                    idx = sum_set.bisect_left(rectangle_sum - k)  # binary search, find a proper
                    if idx != len(sum_set):
                        res = max(res, rectangle_sum - sum_set[idx])
                    sum_set.add(rectangle_sum)

        return res


def main():
    # Example 1: Output: 2
    # matrix = [[1, 0, 1], [0, -2, 3]]
    # k = 2

    # Example 2: Output: 3
    matrix = [[2, 2, -1]]
    k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxSumSubmatrix(matrix, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
