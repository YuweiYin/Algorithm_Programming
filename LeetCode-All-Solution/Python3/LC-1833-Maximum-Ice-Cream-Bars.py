#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1833-Maximum-Ice-Cream-Bars.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-06
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1833 - (Medium) - Maximum Ice Cream Bars
https://leetcode.com/problems/maximum-ice-cream-bars/

Description & Requirement:
    It is a sweltering summer day, and a boy wants to buy some ice cream bars.

    At the store, there are n ice cream bars. You are given an array costs of length n, 
    where costs[i] is the price of the ith ice cream bar in coins. 
    The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

    Return the maximum number of ice cream bars the boy can buy with coins coins.

    Note: The boy can buy the ice cream bars in any order.

Example 1:
    Input: costs = [1,3,2,4,1], coins = 7
    Output: 4
    Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
Example 2:
    Input: costs = [10,6,8,7,7,8], coins = 5
    Output: 0
    Explanation: The boy cannot afford any of the ice cream bars.
Example 3:
    Input: costs = [1,6,3,1,2,5], coins = 20
    Output: 6
    Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.

Constraints:
    costs.length == n
    1 <= n <= 10^5
    1 <= costs[i] <= 10^5
    1 <= coins <= 10^8
"""


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # exception case
        assert isinstance(costs, list) and len(costs) >= 1
        assert isinstance(coins, int) and coins >= 1
        # main method: (sorting & greedy)
        return self._maxIceCream(costs, coins)

    def _maxIceCream(self, costs: List[int], coins: int) -> int:
        assert isinstance(costs, list) and len(costs) >= 1
        assert isinstance(coins, int) and coins >= 1

        costs.sort()
        res = 0
        for cost in costs:
            if cost <= coins:
                coins -= cost
                res += 1
            else:
                break

        return res


def main():
    # Example 1: Output: 4
    # costs = [1, 3, 2, 4, 1]
    # coins = 7

    # Example 2: Output: 0
    costs = [10, 6, 8, 7, 7, 8]
    coins = 5

    # Example 3: Output: 6
    # costs = [1, 6, 3, 1, 2, 5]
    # coins = 20

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxIceCream(costs, coins)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
