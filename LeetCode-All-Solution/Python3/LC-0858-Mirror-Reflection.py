#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0858-Mirror-Reflection.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-04
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0858 - (Medium) - Mirror Reflection
https://leetcode.com/problems/mirror-reflection/

Description & Requirement:
    There is a special square room with mirrors on each of the four walls. 
    Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

    The square room has walls of length p and a laser ray 
    from the southwest corner first meets the east wall at a distance q from the 0th receptor.

    Given the two integers p and q, return the number of the receptor that the ray meets first.

    The test cases are guaranteed so that the ray will meet a receptor eventually.

Example 1:
    Input: p = 2, q = 1
    Output: 2
    Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
Example 2:
    Input: p = 3, q = 1
    Output: 1

Constraints:
    1 <= q <= p <= 1000
"""


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # exception case
        assert isinstance(p, int) and isinstance(q, int) and 1 <= q <= p
        # main method: (simulate the process)
        return self._mirrorReflection(p, q)

    def _mirrorReflection(self, p: int, q: int) -> int:
        assert isinstance(p, int) and isinstance(q, int) and 1 <= q <= p

        from fractions import Fraction as F

        x = y = 0
        rx, ry = p, q
        targets = [(p, 0), (p, p), (0, p)]

        while (x, y) not in targets:
            t = float('inf')
            for v in [F(-x, rx), F(-y, ry), F(p - x, rx), F(p - y, ry)]:
                if v > 0: t = min(t, v)

            x += rx * t
            y += ry * t

            if x == p or x == 0:
                rx *= -1
            if y == p or y == 0:
                ry *= -1

        return 1 if x == y == p else 0 if x == p else 2


def main():
    # Example 1: Output: 2
    p = 2
    q = 1

    # Example 2: Output: 1
    # p = 3
    # q = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.mirrorReflection(p, q)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
