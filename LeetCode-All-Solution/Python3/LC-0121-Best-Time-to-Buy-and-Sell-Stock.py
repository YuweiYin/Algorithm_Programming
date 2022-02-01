#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0121-Best-Time-to-Buy-and-Sell-Stock.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-01
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0121 - (Easy) - Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Description & Requirement:
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and 
    choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. 
    If you cannot achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4

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
            return 0  # Error word1 input type
        if len(prices) == 1:
            return 0  # only one day, buy and sell, no net profit
        # main method: (scan, consider diff between prices)
        #     idea: buy on the current lowest price day X, then consider how many profit can get on other day Y (Y > X)
        return self._maxProfit(prices)

    def _maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        assert len_prices >= 2

        res = 0  # default profit is 0

        # buy on the current lowest price day X, then consider how many profit can get on other day Y (Y > X)
        min_price = prices[0]  # the current lowest price

        for price in prices:
            res = max(res, price - min_price)  # update the max profit
            min_price = min(min_price, price)  # update the min price

        return res


def main():
    # Example 1: Output: 5
    prices = [7, 1, 5, 3, 6, 4]

    # Example 2: Output: 0
    # prices = [7, 6, 4, 3, 1]

    # Example 3: Output: 2
    # prices = [2, 4, 1]

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
