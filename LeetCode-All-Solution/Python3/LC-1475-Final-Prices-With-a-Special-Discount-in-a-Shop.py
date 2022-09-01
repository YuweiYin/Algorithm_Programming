#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1475-Final-Prices-With-a-Special-Discount-in-a-Shop.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-01
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1475 - (Easy) - Final Prices With a Special Discount in a Shop
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

Description & Requirement:
    Given the array prices where prices[i] is the price of the ith item in a shop. 
    There is a special discount for items in the shop, if you buy the ith item, 
    then you will receive a discount equivalent to prices[j] where j is the minimum index such that 
    j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

    Return an array where the i-th element is the final price you will pay 
    for the i-th item of the shop considering the special discount.

Example 1:
    Input: prices = [8,4,6,2,3]
    Output: [4,2,4,2,3]
    Explanation: 
        For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, 
            therefore, the final price you will pay is 8 - 4 = 4. 
        For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, 
            therefore, the final price you will pay is 4 - 2 = 2. 
        For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, 
            therefore, the final price you will pay is 6 - 2 = 4. 
        For items 3 and 4 you will not receive any discount at all.
Example 2:
    Input: prices = [1,2,3,4,5]
    Output: [1,2,3,4,5]
    Explanation: In this case, for all items, you will not receive any discount at all.
Example 3:
    Input: prices = [10,1,1,6]
    Output: [9,0,1,6]

Constraints:
    1 <= prices.length <= 500
    1 <= prices[i] <= 10^3
"""


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # exception case
        assert isinstance(prices, list) and len(prices) >= 1
        # main method: (simulate the process OR monotonous stack)
        return self._finalPrices(prices)

    def _finalPrices(self, prices: List[int]) -> List[int]:
        assert isinstance(prices, list) and len(prices) >= 1
        n = len(prices)

        # res = []
        # for i, price in enumerate(prices):
        #     price_after_discount = price
        #     for j in range(i + 1, n):
        #         if prices[j] <= price:
        #             price_after_discount -= prices[j]
        #             break
        #     res.append(price_after_discount)
        #
        # return res

        # monotonous stack
        res = [0 for _ in range(n)]
        stack = [0]
        for i in range(n - 1, -1, -1):
            price_after_discount = prices[i]
            while len(stack) > 1 and stack[-1] > price_after_discount:
                stack.pop()
            res[i] = price_after_discount - stack[-1]
            stack.append(price_after_discount)

        return res


def main():
    # Example 1: Output: [4,2,4,2,3]
    prices = [8, 4, 6, 2, 3]

    # Example 2: Output: [1,2,3,4,5]
    # prices = [1, 2, 3, 4, 5]

    # Example 3: Output: [9,0,1,6]
    # prices = [10, 1, 1, 6]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.finalPrices(prices)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
