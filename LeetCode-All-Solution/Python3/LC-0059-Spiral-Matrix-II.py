#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0059-Spiral-Matrix-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-13
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0059 - (Medium) - Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/

Description & Requirement:
    Given a positive integer n, 
    generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
    Input: n = 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:
    Input: n = 1
    Output: [[1]]

Constraints:
    1 <= n <= 20
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # exception case
        assert isinstance(n, int) and n > 0
        # main method: (stimulate spiral process)
        return self._generateMatrix(n)

    def _generateMatrix(self, n: int) -> List[List[int]]:
        """
        Runtime: 23 ms, faster than 99.14% of Python3 online submissions for Spiral Matrix II.
        Memory Usage: 14 MB, less than 9.09% of Python3 online submissions for Spiral Matrix II.
        """
        assert isinstance(n, int) and n > 0
        res = [[0 for _ in range(n)] for _ in range(n)]

        row, col = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        di = 0  # directions[di] is the current direction
        cur_num = 1
        max_num = n * n

        while cur_num <= max_num:
            if res[row][col] == 0:
                res[row][col] = cur_num
                cur_num += 1
            new_row, new_col = row + directions[di][0], col + directions[di][1]
            if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n or res[new_row][new_col] != 0:
                di = (di + 1) % len(directions)
                new_row, new_col = row + directions[di][0], col + directions[di][1]
            row, col = new_row, new_col

        return res


def main():
    # Example 1: Output: [[1,2,3],[8,9,4],[7,6,5]]
    n = 3

    # Example 2: Output: [[1]]
    # n = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.generateMatrix(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
