#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1337-The-K-Weakest-Rows-in-a-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-27
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1337 - (Easy) - The K Weakest Rows in a Matrix
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

Description & Requirement:
    You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). 
    The soldiers are positioned in front of the civilians. 
    That is, all the 1's will appear to the left of all the 0's in each row.

    A row i is weaker than a row j if one of the following is true:
        The number of soldiers in row i is less than the number of soldiers in row j.
        Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Example 1:
    Input: mat = 
        [[1,1,0,0,0],
         [1,1,1,1,0],
         [1,0,0,0,0],
         [1,1,0,0,0],
         [1,1,1,1,1]], 
        k = 3
    Output: [2,0,3]
    Explanation: 
        The number of soldiers in each row is: 
        - Row 0: 2 
        - Row 1: 4 
        - Row 2: 1 
        - Row 3: 2 
        - Row 4: 5 
        The rows ordered from weakest to strongest are [2,0,3,1,4].
Example 2:
    Input: mat = 
        [[1,0,0,0],
         [1,1,1,1],
         [1,0,0,0],
         [1,0,0,0]], 
        k = 2
    Output: [0,2]
    Explanation: 
        The number of soldiers in each row is: 
        - Row 0: 1 
        - Row 1: 4 
        - Row 2: 1 
        - Row 3: 1 
        The rows ordered from weakest to strongest are [0,2,3,1].

Constraints:
    m == mat.length
    n == mat[i].length
    2 <= n, m <= 100
    1 <= k <= m
    matrix[i][j] is either 0 or 1.
"""


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # exception case
        assert isinstance(mat, list) and len(mat) >= 2
        max_col = len(mat[0])
        for row in mat:
            assert isinstance(row, list) and len(row) == max_col
        # main method: (record: (row_idx, sum_row), and then sort)
        return self._kWeakestRows(mat, k)

    def _kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        Runtime: 130 ms, faster than 72.03% of Python3 online submissions for The K Weakest Rows in a Matrix.
        Memory Usage: 14.2 MB, less than 90.64% of Python3 online submissions for The K Weakest Rows in a Matrix.
        """
        strength = []
        for idx, row in enumerate(mat):
            strength.append((idx, sum(row)))

        strength.sort(key=lambda x: (x[1], x[0]))
        res = []
        for item in strength[:k]:
            res.append(item[0])

        return res


def main():
    # Example 1: Output: [2,0,3]
    # mat = [
    #     [1, 1, 0, 0, 0],
    #     [1, 1, 1, 1, 0],
    #     [1, 0, 0, 0, 0],
    #     [1, 1, 0, 0, 0],
    #     [1, 1, 1, 1, 1]
    # ]
    # k = 3

    # Example 2: Output: [0,2]
    mat = [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0]
    ]
    k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.kWeakestRows(mat, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
