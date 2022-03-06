#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1359-Count-All-Valid-Pickup-and-Delivery-Options.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-06
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 1359 - (Hard) - Count All Valid Pickup and Delivery Options
https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

Description & Requirement:
    Given n orders, each order consist in pickup and delivery services. 

    Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

    Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
    Input: n = 1
    Output: 1
    Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
Example 2:
    Input: n = 2
    Output: 6
    Explanation: All possible orders: 
        (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
        This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
Example 3:
    Input: n = 3
    Output: 90

Constraints:
    1 <= n <= 500
"""


class Solution:
    def countOrders(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n > 0
        if n == 1:
            return 1
        # main method: (Combinatorics: the only limit is delivery(i) > pickup(i), and count all combinations)
        #     first, consider the number of combinations of all p_i (i = 1, 2, ..., n) in 2n slots
        #         there must be a p_i in the first slot, and other p_j (j != i) can be freely placed to anywhere
        #         except the last slot, so the number of combinations for p_i is (C_{n}^{1} * A_{2n-2}^{n-1}) in total
        #         explanation: (C_{n}^{1}) is the choice of first slot,
        #             (A_{2n-2}^{n-1}) is the choice of (n-1) slots out of (2n-2) slots with order considered
        #     second, assume n = 3 and now the order of p_i is p_2 < p_3 < p_1,
        #         if p_2, p_3, p_1, ___, ___, ___, the number of possible slots is 3!
        #         if p_2, p_3, ___, p_1, ___, ___, the number of possible slots is C_{2}^{1} * 2!
        #         if p_2, p_3, ___, ___, p_1, ___, the number of possible slots is C_{1}^{1} * 2!
        #         if p_2, ___, p_3, ___, p_1, ___, the number of possible slots is C_{1}^{1} * C_{1}^{1} * C_{1}^{1}
        #         so the total number of possible slots now is 3! + 2^2 * 2! + 2^0 * 1!
        #         thus the total number of combinations in second stage is ... TODO
        # other method:
        #     if spare the constraint of delivery(i) > pickup(i), then the total number of combinations is (2n)!
        #     among the (2n)! combinations, there are all possible (d_i, p_i) pairs,
        #     for each pair (d_i, p_i), either d_i < p_i or d_i > p_i, 2 cases,
        #         so the all (d_i, p_i) pair relations are 2^n,
        #     but only one case out of 2^n cases is valid, e.g., d_1 > p_1 && d_2 > p_2 && ... && d_n > p_n
        #     so the result is  (2n)! / 2^n = (2n-1)!! * (2n)!! / 2^n = (2n-1)!! * n!
        return self._countOrders(n)

    def _countOrders(self, n: int) -> int:
        """
        the result is  (2n)! / 2^n = (2n-1)!! * (2n)!! / 2^n = (2n-1)!! * n!
        """
        res = 1
        MOD = int(1e9+7)

        for i in range(1, n + 1):
            res = (res * i * ((i << 1) - 1)) % MOD

        return res


def main():
    # Example 1: Output: 1
    # n = 1

    # Example 2: Output: 6
    # n = 2

    # Example 3: Output: 90
    # n = 3

    # Example 4: Output: 764678010
    n = 500

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countOrders(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
