#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2483-Minimum-Penalty-for-a-Shop.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-29
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2483 - (Medium) Minimum Penalty for a Shop
https://leetcode.com/problems/minimum-penalty-for-a-shop/

Description & Requirement:
    You are given the customer visit log of a shop represented by a 0-indexed string customers 
    consisting only of characters 'N' and 'Y':
        if the i-th character is 'Y', it means that customers come at the i-th hour
        whereas 'N' indicates that no customers come at the i-th hour.

    If the shop closes at the j-th hour (0 <= j <= n), the penalty is calculated as follows:
        For every hour when the shop is open and no customers come, the penalty increases by 1.
        For every hour when the shop is closed and customers come, the penalty increases by 1.

    Return the earliest hour at which the shop must be closed to incur a minimum penalty.

    Note that if a shop closes at the j-th hour, it means the shop is closed at the hour j.

Example 1:
    Input: customers = "YYNY"
    Output: 2
    Explanation: 
        - Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
        - Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
        - Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
        - Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
        - Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
        Closing the shop at 2nd or 4th hour gives a minimum penalty. 
        Since 2 is earlier, the optimal closing time is 2.
Example 2:
    Input: customers = "NNNNN"
    Output: 0
    Explanation: It is best to close the shop at the 0th hour as no customers arrive.
Example 3:
    Input: customers = "YYYY"
    Output: 4
    Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.

Constraints:
    1 <= customers.length <= 10^5
    customers consists only of characters 'Y' and 'N'.
"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # exception case
        assert isinstance(customers, str) and len(customers) >= 1
        # main method: (counter)
        return self._bestClosingTime(customers)

    def _bestClosingTime(self, customers: str) -> int:
        assert isinstance(customers, str) and len(customers) >= 1

        res = 0
        min_cost = cost = customers.count("Y")

        for i, c in enumerate(customers, 1):
            if c == "N":
                cost += 1
            else:
                cost -= 1
                if cost < min_cost:
                    cost = min_cost
                    res = i

        return res


def main():
    # Example 1: Output: 2
    customers = "YYNY"

    # Example 2: Output: 0
    # customers = "NNNNN"

    # Example 3: Output: 4
    # customers = "YYYY"

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.bestClosingTime(customers)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
