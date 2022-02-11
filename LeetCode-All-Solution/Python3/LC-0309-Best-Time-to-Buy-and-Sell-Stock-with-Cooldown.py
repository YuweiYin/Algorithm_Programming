#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0309-Best-Time-to-Buy-and-Sell-Stock-with-Cooldown.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-11
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0309 - (Medium) - Best Time to Buy and Sell Stock with Cooldown
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Description & Requirement:
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    Find the maximum profit you can achieve. 
    You may complete as many transactions as you like 
    (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
    Note: You may not engage in multiple transactions simultaneously 
        (i.e., you must sell the stock before you buy again).

Example 1:
    Input: prices = [1,2,3,0,2]
    Output: 3
    Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:
    Input: prices = [1]
    Output: 0

Constraints:
    1 <= prices.length <= 5000
    0 <= prices[i] <= 1000

Related Problems:
    (Easy)   121. Best Time to Buy and Sell Stock
    (Medium) 122. Best Time to Buy and Sell Stock II
    (Hard)   123. Best Time to Buy and Sell Stock III
    (Hard)   188. Best Time to Buy and Sell Stock IV
    (Medium) 309. Best Time to Buy and Sell Stock with Cooldown
    (Medium) 714. Best Time to Buy and Sell Stock with Transaction Fee
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # exception case
        if not isinstance(prices, list) or len(prices) <= 0:
            return 0  # Error input type
        if len(prices) == 1:
            return 0  # only one day, buy and sell, no net profit
        # main method: (Dynamic Programming)
        #     dp[i][0] is the max profit using prices[0: i+1], when there's a bought stock in hand (holding state)
        #     dp[i][1] is the max profit using prices[0: i+1], when there's no bought stock in hand, and is frozen
        #     dp[i][2] is the max profit using prices[0: i+1], when there's no bought stock in hand, and is not frozen
        #     dp equation: dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
        #         explanation: (dp[i-1][2] - prices[i]) means buy a stock on day i (from a not frozen state dp[i-1][2])
        #                  dp[i][1] = dp[i-1][0] + prices[i]
        #         explanation: (dp[i-1][0] + prices[i]) means sell a stock on day i (from a holding state dp[i-1][0])
        #                  dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        #         explanation: dp[i][2] means day_i neither buy nor sell a stock, the max profit inherit dp[i-1][1/2]
        #     dp init: dp[i][0] = - prices[0] (first day buying), dp[i][1] = 0, dp[i][2] = 0
        #     dp aim: get max(dp[-1])
        return self._maxProfit(prices)

    def _maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        assert len_prices >= 2

        dp = [[0, 0, 0] for _ in range(len_prices)]
        dp[0][0] = - prices[0]

        for day_i in range(1, len_prices):
            dp[day_i][0] = max(dp[day_i - 1][0], dp[day_i - 1][2] - prices[day_i])
            dp[day_i][1] = dp[day_i - 1][0] + prices[day_i]
            dp[day_i][2] = max(dp[day_i - 1][1], dp[day_i - 1][2])

        return max(dp[-1])


def main():
    # Example 1: Output: 3
    #     Explanation: transactions = [buy, sell, cooldown, buy, sell]
    prices = [1, 2, 3, 0, 2]

    # Example 2: Output: 0
    # prices = [1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxProfit(prices)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
