#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2218-Maximum-Value-of-K-Coins-From-Piles.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-15
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2218 - (Hard) - Maximum Value of K Coins From Piles
https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

Description & Requirement:
    There are n piles of coins on a table. 
    Each pile consists of a positive number of coins of assorted denominations.

    In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

    Given a list piles, where piles[i] is a list of integers denoting 
    the composition of the i-th pile from top to bottom, and a positive integer k, 
    return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

Example 1:
    Input: piles = [[1,100,3],[7,8,9]], k = 2
    Output: 101
    Explanation:
        The above diagram shows the different ways we can choose k coins.
        The maximum total we can obtain is 101.
Example 2:
    Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
    Output: 706
    Explanation:
        The maximum total can be obtained if we choose all coins from the last pile.

Constraints:
    n == piles.length
    1 <= n <= 1000
    1 <= piles[i][j] <= 10^5
    1 <= k <= sum(piles[i].length) <= 2000
"""


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # exception case
        assert isinstance(piles, list) and len(piles) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (dynamic programming)
        return self._maxValueOfCoins(piles, k)

    def _maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        assert isinstance(piles, list) and len(piles) >= 1
        assert isinstance(k, int) and k >= 1

        dp = [0] * (k + 1)
        sum_n = 0
        for pile in piles:
            n = len(pile)
            for i in range(1, n):
                pile[i] += pile[i - 1]
            sum_n = min(sum_n + n, k)
            for j in range(sum_n, 0, -1):
                dp[j] = max(dp[j], max(dp[j - w - 1] + pile[w] for w in range(min(n, j))))

        return dp[-1]


def main():
    # Example 1: Output: 101
    piles = [[1, 100, 3], [7, 8, 9]]
    k = 2

    # Example 2: Output: 706
    # piles = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]]
    # k = 7

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxValueOfCoins(piles, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
