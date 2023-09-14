#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1222-Queens-That-Can-Attack-the-King.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-14
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 1222 - (Medium) Queens That Can Attack the King
https://leetcode.com/problems/queens-that-can-attack-the-king/

Description & Requirement:
    On a 0-indexed 8 x 8 chessboard, there can be multiple black queens ad one white king.

    You are given a 2D integer array queens where queens[i] = [xQueen_i, yQueen_i] 
    represents the position of the ith black queen on the chessboard. 
    You are also given an integer array king of length 2 where king = [xKing, yKing] 
    represents the position of the white king.

    Return the coordinates of the black queens that can directly attack the king. 
    You may return the answer in any order.

Example 1:
    Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
    Output: [[0,1],[1,0],[3,3]]
    Explanation: The diagram above shows the three queens that can directly 
        attack the king and the three queens that cannot attack the king 
        (i.e., marked with red dashes).
Example 2:
    Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
    Output: [[2,2],[3,4],[4,4]]
    Explanation: The diagram above shows the three queens that can directly 
        attack the king and the three queens that cannot attack the king 
        (i.e., marked with red dashes).

Constraints:
    1 <= queens.length < 64
    queens[i].length == king.length == 2
    0 <= xQueen_i, yQueen_i, xKing, yKing < 8
    All the given positions are unique.
"""


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # exception case
        assert isinstance(queens, list) and len(queens) >= 1
        assert isinstance(king, list) and len(king) == 2
        # main method: (searching from the king or queen)
        return self._queensAttacktheKing(queens, king)

    def _queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        assert isinstance(queens, list) and len(queens) >= 1
        assert isinstance(king, list) and len(king) == 2

        queen_pos = set((x, y) for x, y in queens)

        res = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue

                kx, ky = king[0] + dx, king[1] + dy
                while 0 <= kx < 8 and 0 <= ky < 8:
                    if (kx, ky) in queen_pos:
                        res.append([kx, ky])
                        break
                    kx += dx
                    ky += dy

        return res


def main():
    # Example 1: Output: [[0,1],[1,0],[3,3]]
    # queens = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
    # king = [0, 0]

    # Example 2: Output: [[2,2],[3,4],[4,4]]
    queens = [[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]]
    king = [3, 3]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.queensAttacktheKing(queens, king)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
