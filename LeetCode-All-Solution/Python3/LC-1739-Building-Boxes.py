#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1739-Building-Boxes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-25
=================================================================="""

import sys
import time
import math
# from typing import List
# import collections
# import functools

"""
LeetCode - 1739 - (Hard) - Building Boxes
https://leetcode.com/problems/building-boxes/

Description & Requirement:
    You have a cubic storeroom where the width, length, and height of the room are all equal to n units. 
    You are asked to place n boxes in this room where each box is a cube of unit side length. 
    There are however some rules to placing the boxes:
        You can place the boxes anywhere on the floor.
        If box x is placed on top of the box y, then each side of the four vertical sides of the box y must 
            either be adjacent to another box or to a wall.

    Given an integer n, return the minimum possible number of boxes touching the floor.

Example 1:
    Input: n = 3
    Output: 3
    Explanation: The figure above is for the placement of the three boxes.
        These boxes are placed in the corner of the room, where the corner is on the left side.
Example 2:
    Input: n = 4
    Output: 3
    Explanation: The figure above is for the placement of the four boxes.
        These boxes are placed in the corner of the room, where the corner is on the left side.
Example 3:
    Input: n = 10
    Output: 6
    Explanation: The figure above is for the placement of the ten boxes.
        These boxes are placed in the corner of the room, where the corner is on the back side.

Constraints:
    1 <= n <= 10^9
"""


class Solution:
    def minimumBoxes(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (find the pattern, mathematics)
        return self._minimumBoxes(n)

    def _minimumBoxes(self, n: int) -> int:
        """
        Time: beats 98.33%; Space: beats 72.73%
        """
        assert isinstance(n, int) and n >= 1

        def __g(x: int):
            return int(x * (x + 1) * (x + 2) / 6)

        i = int((6 * n) ** (1.0 / 3))
        if __g(i) < n:
            i += 1
        n -= __g(i - 1)
        j = math.ceil((math.sqrt(8 * n + 1) - 1) / 2)

        return int((i - 1) * i / 2) + j


def main():
    # Example 1: Output: 3
    # n = 3

    # Example 2: Output: 3
    # n = 4

    # Example 3: Output: 6
    n = 10

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumBoxes(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
