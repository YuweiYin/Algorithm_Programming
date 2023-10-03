#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0123-Best-Time-to-Buy-and-Sell-Stock-III.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-10-03
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 0123 - (Hard) Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Description & Requirement:
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    Find the maximum profit you can achieve. You may complete at most two transactions.

    Note: You may not engage in multiple transactions simultaneously 
    (i.e., you must sell the stock before you buy again).

Example 1:
    Input: prices = [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
        Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
        Note that you cannot buy on day 1, buy on day 2 and sell them later, 
        as you are engaging multiple transactions at the same time. 
        You must sell before buying again.
Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^5
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # exception case
        assert isinstance(prices, list) and len(prices) >= 1
        # main method: (dynamic programming)
        return self._maxProfit(prices)

    def _maxProfit(self, prices: List[int]) -> int:
        assert isinstance(prices, list) and len(prices) >= 1

        n = len(prices)

        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0

        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])

        return sell2


def main():
    # Example 1: Output: 6
    prices = [3, 3, 5, 0, 0, 3, 1, 4]

    # Example 2: Output: 4
    # prices = [1, 2, 3, 4, 5]

    # Example 3: Output: 0
    # prices = [7, 6, 4, 3, 1]

    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.maxProfit(prices)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
