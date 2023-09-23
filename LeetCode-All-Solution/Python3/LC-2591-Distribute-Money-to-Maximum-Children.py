#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2591-Distribute-Money-to-Maximum-Children.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-23
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2591 - (Easy) Distribute Money to Maximum Children
https://leetcode.com/problems/distribute-money-to-maximum-children/

Description & Requirement:
    You are given an integer money denoting the amount of money (in dollars) that 
    you have and another integer children denoting the number of children 
    that you must distribute the money to.

    You have to distribute the money according to the following rules:
        - All money must be distributed.
        - Everyone must receive at least 1 dollar.
        - Nobody receives 4 dollars.

    Return the maximum number of children who may receive exactly 8 dollars 
    if you distribute the money according to the aforementioned rules. 
    If there is no way to distribute the money, return -1.

Example 1:
    Input: money = 20, children = 3
    Output: 1
    Explanation: 
        The maximum number of children with 8 dollars will be 1. 
        One of the ways to distribute the money is:
        - 8 dollars to the first child.
        - 9 dollars to the second child. 
        - 3 dollars to the third child.
        It can be proven that no distribution exists such that number of children 
        getting 8 dollars is greater than 1.
Example 2:
    Input: money = 16, children = 2
    Output: 2
    Explanation: Each child can be given 8 dollars.

Constraints:
    1 <= money <= 200
    2 <= children <= 30
"""


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # exception case
        assert isinstance(money, int) and money >= 1
        assert isinstance(children, int) and children >= 2
        # main method: (greedy)
        return self._distMoney(money, children)

    def _distMoney(self, money: int, children: int) -> int:
        assert isinstance(money, int) and money >= 1
        assert isinstance(children, int) and children >= 2

        if money < children:
            return -1

        money -= children
        res = min(money // 7, children)  # counter
        money -= res * 7
        children -= res

        if (children == 0 and money > 0) or (children == 1 and money == 3):
            res -= 1

        return res


def main():
    # Example 1: Output: 1
    # money = 20
    # children = 3

    # Example 2: Output: 2
    money = 16
    children = 2

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.distMoney(money, children)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
