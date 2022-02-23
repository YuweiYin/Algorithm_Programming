#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0518-Coin-Change-2.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-23
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0518 - (Medium) - Coin Change 2
https://leetcode.com/problems/coin-change-2/

Description & Requirement:
    You are given an integer array coins representing coins of 
    different denominations and an integer amount representing a total amount of money.

    Return the number of combinations that make up that amount. 
    If that amount of money cannot be made up by any combination of the coins, return 0.

    You may assume that you have an infinite number of each kind of coin.

    The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
    Input: amount = 5, coins = [1,2,5]
    Output: 4
    Explanation: there are four ways to make up the amount:
        5=5
        5=2+2+1
        5=2+1+1+1
        5=1+1+1+1+1
Example 2:
    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:
    Input: amount = 10, coins = [10]
    Output: 1

Constraints:
    1 <= coins.length <= 300
    1 <= coins[i] <= 5000
    All the values of coins are unique.
    0 <= amount <= 5000

Related Problem:
    LC-0322-Coin-Change
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # exception case
        if not isinstance(amount, int) or amount < 0:
            return 0  # amount == 0, no change is needed
        if not isinstance(coins, list) or len(coins) <= 0:
            return 0  # that amount of money cannot be made up by any combination of the coins
        if amount == 0:
            return 1
        # main method: (Dynamic Programming)
        #     dp[i] is the number of combinations to make up a certain amount i (i = 0, 1, 2, ..., amount)
        #     dp equation: dp[i] = sum(dp[i-j]), where j in coins (i - j >= 0), means a valid coin denomination
        #     dp init: dp[0] == 1
        #     dp aim: get dp[-1]
        return self._change(amount, coins)

    def _change(self, amount: int, coins: List[int]) -> int:
        len_coins = len(coins)
        assert len_coins >= 1 and amount >= 1

        # default list coins is sorted. if not, sort it first (and remove duplicated denominations)
        # coins.sort()

        # dp[i] is the number of combinations to make up a certain amount i (i = 0, 1, 2, ..., amount)
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1  # dp init: dp[0] == 1

        # note that outer loop is valid coin denominations
        for j in coins:
            for i in range(j, amount + 1):
                if dp[i - j] == -1:  # index out of range, or dp[i - j] itself can't be reached
                    continue
                else:  # accumulate dp[i], there are more combination to make up amount i
                    # dp equation: dp[i] = sum(dp[i-j]), where j in coins (i - j >= 0), means a valid coin denomination
                    dp[i] += dp[i - j]

        # dp aim: get dp[-1]
        return dp[-1]


def main():
    # Example 1: Output: 4
    amount = 5
    coins = [1, 2, 5]

    # Example 2: Output: 0
    # amount = 3
    # coins = [2]

    # Example 3: Output: 1
    # amount = 10
    # coins = [10]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.change(amount, coins)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
