#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0188-Best-Time-to-Buy-and-Sell-Stock-IV.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-10
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0188 - (Hard) - Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Description & Requirement:
    You are given an integer array prices 
    where prices[i] is the price of a given stock on the ith day, and an integer k.

    Find the maximum profit you can achieve. You may complete at most k transactions.

    Note: You may not engage in multiple transactions simultaneously 
        (i.e., you must sell the stock before you buy again).

Example 1:
    Input: k = 2, prices = [2,4,1]
    Output: 2
    Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:
    Input: k = 2, prices = [3,2,6,5,0,3]
    Output: 7
    Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. 
        Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:
    0 <= k <= 100
    0 <= prices.length <= 1000
    0 <= prices[i] <= 1000
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # exception case
        assert isinstance(k, int) and k >= 0
        assert isinstance(prices, list)
        for price in prices:
            assert isinstance(price, int) and price >= 0
        # main method: (dynamic programming)
        return self._maxProfit(k , prices)

    def _maxProfit(self, k: int, prices: List[int]) -> int:
        assert isinstance(k, int) and k >= 0 and isinstance(prices, list)

        if len(prices) < 1:
            return 0

        n = len(prices)
        k = min(k, n >> 1)

        # dp_buy[i][j] the max profit for prices[0:i] when j transactions have been done and there's a stock in hand
        dp_buy = [[0 for _ in range(k + 1)] for _ in range(n)]
        # dp_buy[i][j] the max profit for prices[0:i] when j transactions have been done and there's no stocks in hand
        dp_sell = [[0 for _ in range(k + 1)] for _ in range(n)]

        dp_buy[0][0], dp_sell[0][0] = -prices[0], 0
        for i in range(1, k + 1):
            dp_buy[0][i] = - int(1e9+7)
            dp_sell[0][i] = - int(1e9+7)

        for i in range(1, n):
            dp_buy[i][0] = max(dp_buy[i - 1][0], dp_sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                dp_buy[i][j] = max(dp_buy[i - 1][j], dp_sell[i - 1][j] - prices[i])
                dp_sell[i][j] = max(dp_sell[i - 1][j], dp_buy[i - 1][j - 1] + prices[i])

        return max(dp_sell[n - 1])


def main():
    # Example 1: Output: 2
    # k = 2
    # prices = [2, 4, 1]

    # Example 2: Output: 7
    k = 2
    prices = [3, 2, 6, 5, 0, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxProfit(k, prices)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
