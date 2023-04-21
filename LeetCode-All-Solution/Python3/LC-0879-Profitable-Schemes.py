#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0879-Profitable-Schemes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-21
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0879 - (Hard) - Profitable Schemes
https://leetcode.com/problems/profitable-schemes/

Description & Requirement:
    There is a group of n members, and a list of various crimes they could commit. 
    The ith crime generates a profit[i] and requires group[i] members to participate in it. 
    If a member participates in one crime, that member can't participate in another crime.

    Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, 
    and the total number of members participating in that subset of crimes is at most n.

    Return the number of schemes that can be chosen. Since the answer may be very large, 
    return it modulo 10^9 + 7.

Example 1:
    Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
    Output: 2
    Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
        In total, there are 2 schemes.
Example 2:
    Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
    Output: 7
    Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
        There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).

Constraints:
    1 <= n <= 100
    0 <= minProfit <= 100
    1 <= group.length <= 100
    1 <= group[i] <= 100
    profit.length == group.length
    0 <= profit[i] <= 100
"""


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(minProfit, int) and minProfit >= 0
        assert isinstance(group, list) and len(group) >= 1
        assert isinstance(profit, list) and len(profit) == len(group)
        # main method: (dynamic programming)
        return self._profitableSchemes(n, minProfit, group, profit)

    def _profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(minProfit, int) and minProfit >= 0
        assert isinstance(group, list) and len(group) >= 1
        assert isinstance(profit, list) and len(profit) == len(group)

        MOD = int(1e9+7)

        length = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        for i in range(1, length + 1):
            members, earn = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < members:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - members][max(0, k - earn)]) % MOD

        return sum(dp[length][j][minProfit] for j in range(n + 1)) % MOD


def main():
    # Example 1: Output: 2
    # n = 5
    # minProfit = 3
    # group = [2, 2]
    # profit = [2, 3]

    # Example 2: Output: 7
    n = 10
    minProfit = 5
    group = [2, 3, 5]
    profit = [6, 7, 8]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.profitableSchemes(n, minProfit, group, profit)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
