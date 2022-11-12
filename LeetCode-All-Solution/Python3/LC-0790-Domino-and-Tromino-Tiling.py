#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0790-Domino-and-Tromino-Tiling.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-12
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0790 - (Medium) - Domino and Tromino Tiling
https://leetcode.com/problems/domino-and-tromino-tiling/

Description & Requirement:
    You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

    Given an integer n, return the number of ways to tile an 2 x n board. 
    Since the answer may be very large, return it modulo 10^9 + 7.

    In a tiling, every square must be covered by a tile. 
    Two tilings are different if and only if there are two 4-directionally adjacent cells on the board 
    such that exactly one of the tilings has both squares occupied by a tile.

Example 1:
    Input: n = 3
    Output: 5
    Explanation: The five different ways are show above.
Example 2:
    Input: n = 1
    Output: 1

Constraints:
    1 <= n <= 1000
"""


class Solution:
    def numTilings(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (dynamic programming)
        return self._numTilings(n)

    def _numTilings(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1

        MOD = int(1e9+7)
        dp = [[0 for _ in range(4)] for _ in range(n + 1)]
        dp[0][3] = 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][3]
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            dp[i][3] = (((dp[i - 1][0] + dp[i - 1][1]) % MOD + dp[i - 1][2]) % MOD + dp[i - 1][3]) % MOD

        return dp[n][3]


def main():
    # Example 1: Output: 5
    n = 3

    # Example 2: Output: 1
    # n = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numTilings(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
