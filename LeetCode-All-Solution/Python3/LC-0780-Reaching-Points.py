#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0780-Reaching-Points.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-09
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0780 - (Hard) - Reaching Points
https://leetcode.com/problems/reaching-points/

Description & Requirement:
    Given four integers sx, sy, tx, and ty, 
    return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations, 
    or false otherwise.

    The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).

Example 1:
    Input: sx = 1, sy = 1, tx = 3, ty = 5
    Output: true
    Explanation:
        One series of moves that transforms the starting point to the target is:
        (1, 1) -> (1, 2)
        (1, 2) -> (3, 2)
        (3, 2) -> (3, 5)
Example 2:
    Input: sx = 1, sy = 1, tx = 2, ty = 2
    Output: false
Example 3:
    Input: sx = 1, sy = 1, tx = 1, ty = 1
    Output: true

Constraints:
    1 <= sx, sy, tx, ty <= 10^9
"""


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # exception case
        assert isinstance(sx, int) and sx >= 1 and isinstance(sy, int) and sy >= 1
        assert isinstance(tx, int) and tx >= 1 and isinstance(ty, int) and ty >= 1
        # main method: (convert from (tx, ty) to (sx, sy))
        return self._reachingPoints(sx, sy, tx, ty)

    def _reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # operation 1: sx += sy
        # operation 2: sy += sx
        if sx == tx and sy == ty:
            return True

        # note that 1 <= sx, sy, so (sx + sy) must > sx or sy, which means
        #     if initially (sx, sy) != (tx, ty) and tx == ty, then the (tx, ty) can't be reached
        if tx == ty:
            return False

        while sx < tx != ty and sy < ty:  # subtract the smaller one of (tx, ty) from the bigger one
            if tx > ty:
                tx %= ty  # subtract ty from tx
            else:
                ty %= tx  # subtract tx from ty

        if sx == tx and sy == ty:  # bingo
            return True
        elif sx == tx:  # sy != ty
            return sy < ty and (ty - sy) % tx == 0  # subtract tx from (ty - sy)
        elif sy == ty:  # sx != tx
            return sx < tx and (tx - sx) % ty == 0  # subtract ty from (tx - sx)
        else:
            return False


def main():
    # Example 1: Output: true
    sx = 1
    sy = 1
    tx = 3
    ty = 5

    # Example 2: Output: false
    # sx = 1
    # sy = 1
    # tx = 2
    # ty = 2

    # Example 3: Output: true
    # sx = 1
    # sy = 1
    # tx = 1
    # ty = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reachingPoints(sx, sy, tx, ty)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
