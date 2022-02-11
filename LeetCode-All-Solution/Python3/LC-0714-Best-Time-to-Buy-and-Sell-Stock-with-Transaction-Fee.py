#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0714-Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-11
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0714 - (Medium) - Best Time to Buy and Sell Stock with Transaction Fee
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

Description & Requirement:
    You are given an array prices where prices[i] is the price of a given stock on the ith day, 
    and an integer fee representing a transaction fee.

    Find the maximum profit you can achieve. 
    You may complete as many transactions as you like, 
    but you need to pay the transaction fee for each transaction.

    Note: You may not engage in multiple transactions simultaneously 
        (i.e., you must sell the stock before you buy again).

Example 1:
    Input: prices = [1,3,2,8,4,9], fee = 2
    Output: 8
    Explanation: The maximum profit can be achieved by:
        - Buying at prices[0] = 1
        - Selling at prices[3] = 8
        - Buying at prices[4] = 4
        - Selling at prices[5] = 9
        The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:
    Input: prices = [1,3,7,5,10,3], fee = 3
    Output: 6

Constraints:
    1 <= prices.length <= 5 * 10^4
    1 <= prices[i] < 5 * 10^4
    0 <= fee < 5 * 10^4

Related Problems:
    (Easy)   121. Best Time to Buy and Sell Stock
    (Medium) 122. Best Time to Buy and Sell Stock II
    (Hard)   123. Best Time to Buy and Sell Stock III
    (Hard)   188. Best Time to Buy and Sell Stock IV
    (Medium) 309. Best Time to Buy and Sell Stock with Cooldown
    (Medium) 714. Best Time to Buy and Sell Stock with Transaction Fee
"""


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # exception case
        if not isinstance(prices, list) or len(prices) <= 0:
            return 0  # Error input type
        if len(prices) == 1:
            return 0  # only one day, do nothing, no net profit
        assert isinstance(fee, int) and fee >= 0
        # main method: (Dynamic Programming)
        #     dp[i][0] is the max profit using prices[0: i+1], when there's a bought stock in hand (holding state)
        #     dp[i][1] is the max profit using prices[0: i+1], when there's no bought stock in hand (empty state)
        #     dp equation: dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])  # buying don't need transaction fee
        #         explanation: dp[i][0] holding state, either day i-1 is holding or day i-1 is empty and day_i do buying
        #                  dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)  # selling needs transaction fee
        #         explanation: dp[i][1] empty state, either day i-1 is empty or day i-1 is holding and day_i do selling
        #     dp init: dp[i][0] = - prices[0] (first day buying), dp[i][1] = 0
        #     dp aim: get max(dp[-1])
        return self._maxProfit(prices, fee)

    def _maxProfit(self, prices: List[int], fee: int) -> int:
        len_prices = len(prices)
        assert len_prices >= 2 and fee >= 0

        dp = [[0, 0] for _ in range(len_prices)]
        dp[0][0] = - prices[0]

        for day_i in range(1, len_prices):
            dp[day_i][0] = max(dp[day_i - 1][0], dp[day_i - 1][1] - prices[day_i])  # buying don't need transaction fee
            dp[day_i][1] = max(dp[day_i - 1][1], dp[day_i - 1][0] + prices[day_i] - fee)  # selling needs trans fee

        return max(dp[-1])


def main():
    # Example 1: Output: 8
    #     Explanation: The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2

    # Example 2: Output: 6
    # prices = [1, 3, 7, 5, 10, 3]
    # fee = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxProfit(prices, fee)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
