#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1252-Cells-with-Odd-Values-in-a-Matrix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-12
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1252 - (Easy) - Cells with Odd Values in a Matrix
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

Description & Requirement:
    There is an m x n matrix that is initialized to all 0's. 
    There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location 
    to perform some increment operations on the matrix.

    For each location indices[i], do both of the following:
        Increment all the cells on row ri.
        Increment all the cells on column ci.

    Given m, n, and indices, 
    return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

Example 1:
    Input: m = 2, n = 3, indices = [[0,1],[1,1]]
    Output: 6
    Explanation: Initial matrix = [[0,0,0],[0,0,0]].
        After applying first increment it becomes [[1,2,1],[0,1,0]].
        The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.
Example 2:
    Input: m = 2, n = 2, indices = [[1,1],[0,0]]
    Output: 0
    Explanation: Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.

Constraints:
    1 <= m, n <= 50
    1 <= indices.length <= 100
    0 <= ri < m
    0 <= ci < n

Follow up:
    Could you solve this in O(n + m + indices.length) time with only O(n + m) extra space?
"""


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # exception case
        assert isinstance(m, int) and m >= 1 and isinstance(n, int) and n >= 1
        assert isinstance(indices, list) and len(indices) >= 1
        for index in indices:
            assert isinstance(index, list) and len(index) == 2 and 0 <= index[0] <= m and 0 <= index[1] <= n
        # main method: (record the number of increment of each row and column, indicating the final states)
        return self._oddCells(m, n, indices)

    def _oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        """
        Runtime: 70 ms, faster than 59.36% of Python3 online submissions for Cells with Odd Values in a Matrix.
        Memory Usage: 13.9 MB, less than 89.79% of Python3 online submissions for Cells with Odd Values in a Matrix.
        """
        assert isinstance(m, int) and m >= 1 and isinstance(n, int) and n >= 1
        assert isinstance(indices, list) and len(indices) >= 1

        row_changes = [0 for _ in range(m)]  # the number of increment of each row
        col_changes = [0 for _ in range(n)]  # the number of increment of each column

        for index in indices:
            row_changes[index[0]] += 1
            col_changes[index[1]] += 1

        res = 0
        odd_row_counter = 0
        for row in row_changes:
            if row & 0x01 == 1:  # odd changes on this row
                odd_row_counter += 1
                res += n

        for col in col_changes:
            if col & 0x01 == 1:  # odd changes on this col
                res += (m - (odd_row_counter << 1))  # double odd -> even

        return res


def main():
    # Example 1: Output: 6
    m = 2
    n = 3
    indices = [[0, 1], [1, 1]]

    # Example 2: Output: 0
    # m = 2
    # n = 2
    # indices = [[1, 1], [0, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.oddCells(m, n, indices)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
