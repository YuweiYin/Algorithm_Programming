#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1444-Number-of-Ways-of-Cutting-a-Pizza.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-31
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1444 - (Hard) - Number of Ways of Cutting a Pizza
https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/

Description & Requirement:
    Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 
    'A' (an apple) and '.' (empty cell) and given the integer k. 
    You have to cut the pizza into k pieces using k-1 cuts. 

    For each cut you choose the direction: vertical or horizontal, 
    then you choose a cut position at the cell boundary and cut the pizza into two pieces. 
    If you cut the pizza vertically, give the left part of the pizza to a person. 
    If you cut the pizza horizontally, give the upper part of the pizza to a person. 
    Give the last piece of pizza to the last person.

    Return the number of ways of cutting the pizza such that each piece contains at least one apple. 
    Since the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:
    Input: pizza = ["A..","AAA","..."], k = 3
    Output: 3 
    Explanation: The figure above shows the three ways to cut the pizza. 
        Note that pieces must contain at least one apple.
Example 2:
    Input: pizza = ["A..","AA.","..."], k = 3
    Output: 1
Example 3:
    Input: pizza = ["A..","A..","..."], k = 1
    Output: 1

Constraints:
    1 <= rows, cols <= 50
    rows == pizza.length
    cols == pizza[i].length
    1 <= k <= 10
    pizza consists of characters 'A' and '.' only.
"""


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # exception case
        assert isinstance(pizza, list) and len(pizza) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (dynamic programming)
        return self._ways(pizza, k)

    def _ways(self, pizza: List[str], k: int) -> int:
        assert isinstance(pizza, list) and len(pizza) >= 1
        assert isinstance(k, int) and k >= 1

        MOD = int(1e9+7)
        m, n = len(pizza), len(pizza[0])

        post = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                post[i][j] = post[i + 1][j] + post[i][j + 1] - post[i + 1][j + 1] + int(pizza[i][j] == "A")

        dp = [[[0] * (k + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j][1] = int(post[i][j] > 0)
                for p in range(2, k + 1):
                    dp[i][j][p] += sum(dp[x][j][p - 1] for x in range(i + 1, m) if p - 1 <= post[x][j] < post[i][j])
                    dp[i][j][p] += sum(dp[i][y][p - 1] for y in range(j + 1, n) if p - 1 <= post[i][y] < post[i][j])
                    dp[i][j][p] %= MOD

        return dp[0][0][k] % MOD


def main():
    # Example 1: Output: 3
    # pizza = ["A..", "AAA", "..."]
    # k = 3

    # Example 2: Output: 1
    # pizza = ["A..", "AA.", "..."]
    # k = 3

    # Example 3: Output: 1
    pizza = ["A..", "A..", "..."]
    k = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.ways(pizza, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
