#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0322-Coin-Change.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-31
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0322 - (Medium) - Coin Change
https://leetcode.com/problems/coin-change/

Description & Requirement:
    You are given an integer array coins representing coins of different denominations 
    and an integer amount representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount. 
    If that amount of money cannot be made up by any combination of the coins, return -1.

    You may assume that you have an infinite number of each kind of coin.

Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
Example 2:
    Input: coins = [2], amount = 3
    Output: -1
Example 3:
    Input: coins = [1], amount = 0
    Output: 0

Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 2^31 - 1
    0 <= amount <= 10^4

Related Problem:
    LC-0518-Coin-Change-2
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # exception case
        if not isinstance(amount, int) or amount <= 0:
            return 0  # amount == 0, no change is needed
        if not isinstance(coins, list) or len(coins) <= 0:
            return -1  # Error input type (now amount >= 1)
        # main method: (Knapsack problem - Dynamic Programming)
        #     dp[i] is minimum number of coins to get total amount i (i = 0, 1, 2, ..., amount)
        #     dp equation: dp[i] = min(1 + dp[i-j]), where j in coins (i - j >= 0), means a valid coin denomination
        #     dp init: dp[0] == 0.
        #     dp aim: get dp[-1]
        return self._coinChange(coins, amount)

    def _coinChange(self, coins: List[int], amount: int) -> int:
        len_coins = len(coins)
        assert len_coins >= 1 and amount >= 1

        # default list coins is sorted. if not, sort it first (and remove duplicated denominations)
        # coins.sort()

        # dp[i] is minimum number of coins to get total amount i (i = 0, 1, 2, ..., amount)
        dp = [-1 for _ in range(amount + 1)]  # -1 means can't get this total coin amount
        dp[0] = 0  # need no coin to get amount 0

        for i in range(1, amount + 1):
            for j in coins:
                if i - j < 0 or dp[i - j] == -1:  # index out of range, or dp[i - j] itself can't be reached
                    continue
                if dp[i] == -1:  # the state of dp[i] change from "can't reach" to "can reach"
                    dp[i] = dp[i - j] + 1
                else:  # update dp[i] if dp[i - j] + 1 is smaller
                    dp[i] = min(dp[i], dp[i - j] + 1)

        return dp[-1]


def main():
    # Example 1: Output: 3
    #     Explanation: 11 = 5 + 5 + 1
    coins = [1, 2, 5]
    amount = 11

    # Example 2: Output: -1
    # coins = [2]
    # amount = 3

    # Example 3: Output: 0
    # coins = [1]
    # amount = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.coinChange(coins, amount)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
