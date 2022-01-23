#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2034-Stock-Price-Fluctuation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-23
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 2034 - (Medium) - Stock Price Fluctuation
https://leetcode.com/problems/stock-price-fluctuation/

Description & Requirement:
    You are given a stream of records about a particular stock. 
    Each record contains a timestamp and the corresponding price of the stock at that timestamp.

    Unfortunately due to the volatile nature of the stock market, 
    the records do not come in order. Even worse, some records may be incorrect. 
    Another record with the same timestamp may appear later in the stream 
    correcting the price of the previous wrong record.

    Design an algorithm that:
        Updates the price of the stock at a particular timestamp, 
            correcting the price from any previous records at the timestamp.
        Finds the latest price of the stock based on the current records. 
            The latest price is the price at the latest timestamp recorded.
        Finds the maximum price the stock has been based on the current records.
        Finds the minimum price the stock has been based on the current records.

    Implement the StockPrice class:
        StockPrice() Initializes the object with no price records.
        void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
        int current() Returns the latest price of the stock.
        int maximum() Returns the maximum price of the stock.
        int minimum() Returns the minimum price of the stock.

Example 1:
    Input
    ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
    [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
    Output
    [null, null, null, 5, 10, null, 5, null, 2]
    Explanation
        StockPrice stockPrice = new StockPrice();
        stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
        stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
        stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
        stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
        stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
                                  // Timestamps are [1,2] with corresponding prices [3,5].
        stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
        stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
        stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.

Constraints:
    1 <= timestamp, price <= 10^9
    At most 105 calls will be made in total to update, current, maximum, and minimum.
    current, maximum, and minimum will be called only after update has been called at least once.
"""


class StockPrice:

    def __init__(self):
        # use SortedList or use two heap to maintain the maximum and minimum
        from sortedcontainers import SortedList

        self.sorted_price = SortedList()  # all prices that are sorted (from the smallest to the biggest)
        self.timestamp2price = dict({})  # key: timestamp; value: price
        self.latest_timestamp = 0  # the latest timestamp

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timestamp2price:
            self.sorted_price.discard(self.timestamp2price[timestamp])  # discard old price
        self.sorted_price.add(price)  # add new price
        self.timestamp2price[timestamp] = price  # new dict map
        self.latest_timestamp = max(self.latest_timestamp, timestamp)  # update the latest timestamp

    def current(self) -> int:
        return self.timestamp2price[self.latest_timestamp]

    def maximum(self) -> int:
        return self.sorted_price[-1]

    def minimum(self) -> int:
        return self.sorted_price[0]


def main():
    # init instance
    # solution = Solution()

    # run & time
    start = time.process_time()
    # ans = solution.subsetsWithDup(nums)
    # Your StockPrice object will be instantiated and called as such:
    # Example 1: Output: [null, null, null, 5, 10, null, 5, null, 2]
    #     timestamp = ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
    #     price = [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
    obj = StockPrice()
    obj.update(1, 10)
    obj.update(2, 5)
    print(obj.current())
    print(obj.maximum())
    obj.update(1, 3)
    print(obj.maximum())
    obj.update(4, 2)
    print(obj.minimum())
    end = time.process_time()

    # show answer
    # print('\nAnswer:')
    # print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
