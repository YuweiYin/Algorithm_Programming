#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1672-Richest-Customer-Wealth.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-31
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1672 - (Easy) - Richest Customer Wealth
https://leetcode.com/problems/richest-customer-wealth/

Description & Requirement:
    You are given an m x n integer grid accounts where 
    accounts[i][j] is the amount of money the i-th customer has in the j-th bank. 
    Return the wealth that the richest customer has.

    A customer's wealth is the amount of money they have in all their bank accounts. 
    The richest customer is the customer that has the maximum wealth.

Example 1:
    Input: accounts = [[1,2,3],[3,2,1]]
    Output: 6
    Explanation:
        1st customer has wealth = 1 + 2 + 3 = 6
        2nd customer has wealth = 3 + 2 + 1 = 6
        Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:
    Input: accounts = [[1,5],[7,3],[3,5]]
    Output: 10
    Explanation: 
        1st customer has wealth = 6
        2nd customer has wealth = 10 
        3rd customer has wealth = 8
        The 2nd customer is the richest with a wealth of 10.
Example 3:
    Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
    Output: 17

Constraints:
    m == accounts.length
    n == accounts[i].length
    1 <= m, n <= 50
    1 <= accounts[i][j] <= 100
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # exception case
        if not isinstance(accounts, list) or len(accounts) <= 0:
            return 0  # Error input type
        for account in accounts:
            assert isinstance(account, list)
        # main method: (sum each inner list and return the max sum)
        return self._maximumWealth(accounts)

    def _maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0

        for account in accounts:
            res = max(res, sum(account))

        return res


def main():
    # Example 1: Output: 6
    # accounts = [[1, 2, 3], [3, 2, 1]]

    # Example 2: Output: 10
    # accounts = [[1, 5], [7, 3], [3, 5]]

    # Example 3: Output: 17
    accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximumWealth(accounts)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
