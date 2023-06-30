#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1253-Reconstruct-a-2-Row-Binary-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-29
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 1253 - (Medium) - Reconstruct a 2-Row Binary Matrix
https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

Description & Requirement:
    Given the following details of a matrix with n columns and 2 rows:
        The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
        The sum of elements of the 0-th(upper) row is given as upper.
        The sum of elements of the 1-st(lower) row is given as lower.
        The sum of elements in the i-th column(0-indexed) is colsum[i], 
            where colsum is given as an integer array with length n.

    Your task is to reconstruct the matrix with upper, lower and colsum.

    Return it as a 2-D integer array.

    If there are more than one valid solution, any of them will be accepted.

    If no valid solution exists, return an empty 2-D array.

Example 1:
    Input: upper = 2, lower = 1, colsum = [1,1,1]
    Output: [[1,1,0],[0,0,1]]
    Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
Example 2:
    Input: upper = 2, lower = 3, colsum = [2,2,1,1]
    Output: []
Example 3:
    Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
    Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]

Constraints:
    1 <= colsum.length <= 10^5
    0 <= upper, lower <= colsum.length
    0 <= colsum[i] <= 2
"""


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        # exception case
        assert isinstance(upper, int) and upper >= 0
        assert isinstance(lower, int) and lower >= 0
        assert isinstance(colsum, list) and len(colsum) >= 1 and all([0 <= cs <= 2 for cs in colsum])
        # main method: (simulation)
        return self._reconstructMatrix(upper, lower, colsum)

    def _reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        assert isinstance(upper, int) and upper >= 0
        assert isinstance(lower, int) and lower >= 0
        assert isinstance(colsum, list) and len(colsum) >= 1 and all([0 <= cs <= 2 for cs in colsum])

        n = len(colsum)
        sum_val = 0
        two_num = 0
        for i in range(n):
            if colsum[i] == 2:
                two_num += 1
            sum_val += colsum[i]

        if sum_val != upper + lower or min(upper, lower) < two_num:
            return []

        upper -= two_num
        lower -= two_num
        res = [[0] * n for _ in range(2)]
        for i in range(n):
            if colsum[i] == 2:
                res[0][i] = res[1][i] = 1
            elif colsum[i] == 1:
                if upper > 0:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1

        return res


def main():
    # Example 1: Output: [[1,1,0],[0,0,1]]
    # upper = 2
    # lower = 1
    # colsum = [1, 1, 1]

    # Example 2: Output: []
    # upper = 2
    # lower = 3
    # colsum = [2, 2, 1, 1]

    # Example 3: Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
    upper = 5
    lower = 5
    colsum = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reconstructMatrix(upper, lower, colsum)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
