#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2240-Number-of-Ways-to-Buy-Pens-and-Pencils.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-01
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2240 - (Medium) Number of Ways to Buy Pens and Pencils
https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

Description & Requirement:
    You are given an integer total indicating the amount of money you have. 
    You are also given two integers cost1 and cost2 indicating the price of 
    a pen and pencil respectively. You can spend part or all of your money to 
    buy multiple quantities (or none) of each kind of writing utensil.

    Return the number of distinct ways you can buy some number of pens and pencils.

Example 1:
    Input: total = 20, cost1 = 10, cost2 = 5
    Output: 9
    Explanation: The price of a pen is 10 and the price of a pencil is 5.
        - If you buy 0 pens, you can buy 0, 1, 2, 3, or 4 pencils.
        - If you buy 1 pen, you can buy 0, 1, or 2 pencils.
        - If you buy 2 pens, you cannot buy any pencils.
        The total number of ways to buy pens and pencils is 5 + 3 + 1 = 9.
Example 2:
    Input: total = 5, cost1 = 10, cost2 = 10
    Output: 1
    Explanation: The price of both pens and pencils are 10, 
    which cost more than total, so you cannot buy any writing utensils. 
    Therefore, there is only 1 way: buy 0 pens and 0 pencils.

Constraints:
    1 <= total, cost1, cost2 <= 10^6
"""


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # exception case
        assert isinstance(total, int) and total >= 1
        assert isinstance(cost1, int) and cost1 >= 1
        assert isinstance(cost2, int) and cost2 >= 1
        # main method: (enumeration)
        return self._waysToBuyPensPencils(total, cost1, cost2)

    def _waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        assert isinstance(total, int) and total >= 1
        assert isinstance(cost1, int) and cost1 >= 1
        assert isinstance(cost2, int) and cost2 >= 1

        if cost1 < cost2:
            return self.waysToBuyPensPencils(total, cost2, cost1)

        res, cnt = 0, 0
        while cnt * cost1 <= total:
            res += ((total - cnt * cost1) // cost2) + 1
            cnt += 1

        return res


def main():
    # Example 1: Output: 9
    total = 20
    cost1 = 10
    cost2 = 5

    # Example 2: Output: 1
    # total = 5
    # cost1 = 10
    # cost2 = 10

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.waysToBuyPensPencils(total, cost1, cost2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
