#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1240-Tiling-a-Rectangle-with-the-Fewest-Squares.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-08
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1240 - (Hard) - Tiling a Rectangle with the Fewest Squares
https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

Description & Requirement:
    Given a rectangle of size n x m, 
    return the minimum number of integer-sided squares that tile the rectangle.

Example 1:
    Input: n = 2, m = 3
    Output: 3
    Explanation: 3 squares are necessary to cover the rectangle.
        2 (squares of 1x1)
        1 (square of 2x2)
Example 2:
    Input: n = 5, m = 8
    Output: 5
Example 3:
    Input: n = 11, m = 13
    Output: 6

Constraints:
    1 <= n, m <= 13
"""


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(m, int) and m >= 1
        # main method: (backtrace)
        return self._tilingRectangle(n, m)

    def _tilingRectangle(self, n: int, m: int) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(m, int) and m >= 1

        def __dfs(x: int, y: int, cnt: int) -> None:
            nonlocal res
            if cnt >= res:
                return
            if x >= n:
                res = cnt
                return

            if y >= m:
                __dfs(x + 1, 0, cnt)
                return

            if rect[x][y]:
                __dfs(x, y + 1, cnt)
                return

            k = min(n - x, m - y)
            while k >= 1 and __is_available(x, y, k):
                __fill_up(x, y, k, True)
                __dfs(x, y + k, cnt + 1)
                __fill_up(x, y, k, False)
                k -= 1

        def __is_available(x: int, y: int, k: int) -> bool:
            for i in range(k):
                for j in range(k):
                    if rect[x + i][y + j]:
                        return False
            return True

        def __fill_up(x: int, y: int, k: int, val: bool) -> None:
            for i in range(k):
                for j in range(k):
                    rect[x + i][y + j] = val

        res = max(n, m)
        rect = [[False] * m for _ in range(n)]
        __dfs(0, 0, 0)

        return res


def main():
    # Example 1: Output: 3
    # n = 2
    # m = 3

    # Example 2: Output: 5
    # n = 5
    # m = 8

    # Example 3: Output: 6
    n = 11
    m = 13

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.tilingRectangle(n, m)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
