#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1033-Moving-Stones-Until-Consecutive.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-30
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1033 - (Medium) - Moving Stones Until Consecutive
https://leetcode.com/problems/moving-stones-until-consecutive/

Description & Requirement:
    There are three stones in different positions on the X-axis. 
    You are given three integers a, b, and c, the positions of the stones.

    In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), 
    and move it to an unoccupied position between those endpoints. Formally, let's say the stones are 
    currently at positions x, y, and z with x < y < z. You pick up the stone at either position x or position z, 
    and move that stone to an integer position k, with x < k < z and k != y.

    The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).

    Return an integer array answer of length 2 where:
        answer[0] is the minimum number of moves you can play, and
        answer[1] is the maximum number of moves you can play.

Example 1:
    Input: a = 1, b = 2, c = 5
    Output: [1,2]
    Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.
Example 2:
    Input: a = 4, b = 3, c = 2
    Output: [0,0]
    Explanation: We cannot make any moves.
Example 3:
    Input: a = 3, b = 5, c = 1
    Output: [1,2]
    Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.

Constraints:
    1 <= a, b, c <= 100
    a, b, and c have different values.
"""


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        # exception case
        assert isinstance(a, int) and a >= 1
        assert isinstance(b, int) and 1 <= b != a
        assert isinstance(c, int) and 1 <= c != a and c != b
        # main method: (greedy, sorting)
        return self._numMovesStones(a, b, c)

    def _numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        assert isinstance(a, int) and a >= 1
        assert isinstance(b, int) and 1 <= b != a
        assert isinstance(c, int) and 1 <= c != a and c != b

        x, y, z = sorted([a, b, c])
        res = [2, z - x - 2]
        if (z - y) == 1 and (y - x) == 1:
            res[0] = 0
        elif (z - y) <= 2 or (y - x) <= 2:
            res[0] = 1

        return res


def main():
    # Example 1: Output: [1,2]
    # a = 1
    # b = 2
    # c = 5

    # Example 2: Output: [0,0]
    # a = 4
    # b = 3
    # c = 2

    # Example 3: Output: [1,2]
    a = 3
    b = 5
    c = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numMovesStones(a, b, c)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
