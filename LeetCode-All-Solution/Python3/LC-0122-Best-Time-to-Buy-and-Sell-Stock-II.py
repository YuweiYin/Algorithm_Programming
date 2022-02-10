#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0122-Best-Time-to-Buy-and-Sell-Stock-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-10
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0122 - (Medium) - Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Description & Requirement:
    You are given an integer array prices where prices[i] is the price of a given stock on the i-th day.

    On each day, you may decide to buy and/or sell the stock. 
    You can only hold at most one share of the stock at any time. 
    However, you can buy it then immediately sell it on the same day.

    Find and return the maximum profit you can achieve.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
        Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
        Total profit is 4 + 3 = 7.
Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
        Total profit is 4.
Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

Constraints:
    1 <= prices.length <= 3 * 10^4
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
            return 0  # Error input type
        if len(prices) == 1:
            return 0  # only one day, buy and sell, no net profit
        # main method: (scan, if prices[i] > prices[i-1], just get profit prices[i]-prices[i-1])
        return self._maxProfit(prices)

    def _maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        assert len_prices >= 2

        res = 0

        cur_day = 1
        while cur_day < len_prices:
            if prices[cur_day] > prices[cur_day - 1]:
                res += prices[cur_day] - prices[cur_day - 1]
            cur_day += 1

        return res


def main():
    # Example 1: Output: 7
    # prices = [7, 1, 5, 3, 6, 4]

    # Example 2: Output: 4
    # prices = [1, 2, 3, 4, 5]

    # Example 3: Output: 0
    prices = [7, 6, 4, 3, 1]

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
