#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1812-Determine-Color-of-a-Chessboard-Square.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-08
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1812 - (Easy) - Determine Color of a Chessboard Square
https://leetcode.com/problems/determine-color-of-a-chessboard-square/

Description & Requirement:
    You are given coordinates, a string that represents the coordinates of a square of the chessboard. 
    Below is a chessboard for your reference.

    Return true if the square is white, and false if the square is black.

    The coordinate will always represent a valid chessboard square. 
    The coordinate will always have the letter first, and the number second.

Example 1:
    Input: coordinates = "a1"
    Output: false
    Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
Example 2:
    Input: coordinates = "h3"
    Output: true
    Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
Example 3:
    Input: coordinates = "c7"
    Output: false

Constraints:
    coordinates.length == 2
    'a' <= coordinates[0] <= 'h'
    '1' <= coordinates[1] <= '8'
"""


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # exception case
        assert isinstance(coordinates, str) and len(coordinates) == 2
        # main method: (the square is white if x + y is an odd number)
        return self._squareIsWhite(coordinates)

    def _squareIsWhite(self, coordinates: str) -> bool:
        assert isinstance(coordinates, str) and len(coordinates) == 2

        x = ord(coordinates[0]) - ord("a") + 1
        y = int(coordinates[1])

        return (x + y) & 0x01 == 1


def main():
    # Example 1: Output: false
    coordinates = "a1"

    # Example 2: Output: true
    # coordinates = "h3"

    # Example 3: Output: false
    # coordinates = "c7"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.squareIsWhite(coordinates)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
