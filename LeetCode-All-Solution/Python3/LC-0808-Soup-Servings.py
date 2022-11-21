#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0808-Soup-Servings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-21
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0808 - (Medium) - Soup Servings
https://leetcode.com/problems/soup-servings/

Description & Requirement:
    There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. 
    There are four kinds of operations:
        Serve 100 ml of soup A and 0 ml of soup B,
        Serve 75 ml of soup A and 25 ml of soup B,
        Serve 50 ml of soup A and 50 ml of soup B, and
        Serve 25 ml of soup A and 75 ml of soup B.

    When we serve some soup, we give it to someone, and we no longer have it. 
    Each turn, we will choose from the four operations with an equal probability 0.25. 
    If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. 
    We stop once we no longer have some quantity of both types of soup.

    Note that we do not have an operation where all 100 ml's of soup B are used first.

    Return the probability that soup A will be empty first, plus half the probability that A and B become empty 
    at the same time. Answers within 10-5 of the actual answer will be accepted.

Example 1:
    Input: n = 50
    Output: 0.62500
    Explanation: If we choose the first two operations, A will become empty first.
        For the third operation, A and B will become empty at the same time.
        For the fourth operation, B will become empty first.
        So the total probability of A becoming empty first plus half the probability that A and B 
        become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
Example 2:
    Input: n = 100
    Output: 0.71875

Constraints:
    0 <= n <= 10^9
"""


class Solution:
    def soupServings(self, n: int) -> float:
        # exception case
        assert isinstance(n, int) and n >= 0
        # main method: (dynamic programming)
        return self._soupServings(n)

    def _soupServings(self, n: int) -> float:
        assert isinstance(n, int) and n >= 0

        n = (n + 24) // 25
        if n >= 179:
            return 1.0
        dp = [[0.0 for _ in range(n + 1)] for _ in range(n + 1)]
        dp[0] = [0.5] + [1.0  for _ in range(n)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][max(0, j - 1)] +
                            dp[max(0, i - 2)][max(0, j - 2)] + dp[max(0, i - 1)][max(0, j - 3)]) / 4

        return dp[-1][-1]


def main():
    # Example 1: Output: 0.62500
    # n = 50

    # Example 2: Output: 0.71875
    n = 100

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.soupServings(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
