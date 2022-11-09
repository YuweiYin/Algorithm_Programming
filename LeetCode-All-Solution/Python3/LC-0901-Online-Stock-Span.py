#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0901-Online-Stock-Span.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-21
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0901 - (Medium) - Online Stock Span
https://leetcode.com/problems/online-stock-span/

Description & Requirement:
    Design an algorithm that collects daily price quotes for some stock and 
    returns the span of that stock's price for the current day.

    The span of the stock's price today is defined as the maximum number of consecutive days 
    (starting from today and going backward) for which the stock price was less than or equal to today's price.

        For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], 
        then the stock spans would be [1,1,1,2,1,4,6].

    Implement the StockSpanner class:
        StockSpanner() Initializes the object of the class.
        int next(int price) Returns the span of the stock's price given that today's price is price.

Example 1:
    Input
        ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
        [[], [100], [80], [60], [70], [60], [75], [85]]
    Output
        [null, 1, 1, 1, 2, 1, 4, 6]
    Explanation
        StockSpanner stockSpanner = new StockSpanner();
        stockSpanner.next(100); // return 1
        stockSpanner.next(80);  // return 1
        stockSpanner.next(60);  // return 1
        stockSpanner.next(70);  // return 2
        stockSpanner.next(60);  // return 1
        stockSpanner.next(75);  // return 4, because the last 4 prices 
            (including today's price of 75) were less than or equal to today's price.
        stockSpanner.next(85);  // return 6

Constraints:
    1 <= price <= 10^5
    At most 10^4 calls will be made to next.
"""


class StockSpanner:

    def __init__(self):
        self.stack = [(-1, int(1e9+7))]
        self.idx = -1

    def next(self, price: int) -> int:
        """
        Runtime: 416 ms, faster than 96.84% of Python3 online submissions for Online Stock Span.
        Memory Usage: 19.5 MB, less than 70.93% of Python3 online submissions for Online Stock Span.
        """
        # method: monotonous stack
        self.idx += 1
        while price >= self.stack[-1][1]:
            self.stack.pop()
        self.stack.append((self.idx, price))
        return self.idx - self.stack[-2][0]


def main():
    # Example 1: Output: [null, 1, 1, 1, 2, 1, 4, 6]
    command_list = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    param_list = [[], [100], [80], [60], [70], [60], [75], [85]]

    # init instance
    # solution = Solution()
    obj = StockSpanner()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "next" and isinstance(param, list) and len(param) == 1:
            ans.append(obj.next(param[0]))
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
