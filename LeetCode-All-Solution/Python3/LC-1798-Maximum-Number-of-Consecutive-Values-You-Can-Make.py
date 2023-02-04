#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1798-Maximum-Number-of-Consecutive-Values-You-Can-Make.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-04
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1798 - (Medium) - Maximum Number of Consecutive Values You Can Make
https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

Description & Requirement:
    You are given an integer array coins of length n which represents the n coins that you own. 
    The value of the ith coin is coins[i]. You can make some value x 
    if you can choose some of your n coins such that their values sum up to x.

    Return the maximum number of consecutive integer values that 
    you can make with your coins starting from and including 0.

    Note that you may have multiple coins of the same value.

Example 1:
    Input: coins = [1,3]
    Output: 2
    Explanation: You can make the following values:
        - 0: take []
        - 1: take [1]
        You can make 2 consecutive integer values starting from 0.
Example 2:
    Input: coins = [1,1,1,4]
    Output: 8
    Explanation: You can make the following values:
        - 0: take []
        - 1: take [1]
        - 2: take [1,1]
        - 3: take [1,1,1]
        - 4: take [4]
        - 5: take [4,1]
        - 6: take [4,1,1]
        - 7: take [4,1,1,1]
        You can make 8 consecutive integer values starting from 0.
Example 3:
    Input: coins = [1,4,10,3,1]
    Output: 20

Constraints:
    coins.length == n
    1 <= n <= 4 * 10^4
    1 <= coins[i] <= 4 * 10^4
"""


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # exception case
        assert isinstance(coins, list) and len(coins) >= 1
        # main method: (sorting and greedy)
        return self._getMaximumConsecutive(coins)

    def _getMaximumConsecutive(self, coins: List[int]) -> int:
        assert isinstance(coins, list) and len(coins) >= 1

        res = 1
        coins.sort()

        for coin in coins:
            if coin > res:
                break
            res += coin

        return res


def main():
    # Example 1: Output: 2
    # coins = [1, 3]

    # Example 2: Output: 8
    # coins = [1, 1, 1, 4]

    # Example 3: Output: 20
    coins = [1, 4, 10, 3, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getMaximumConsecutive(coins)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
