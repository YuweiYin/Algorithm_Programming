#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0983-Minimum-Cost-For-Tickets.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-28
=================================================================="""

import sys
import time
from typing import List
import functools
# import collections

"""
LeetCode - 0983 - (Medium) - Minimum Cost For Tickets
https://leetcode.com/problems/minimum-cost-for-tickets/

Description & Requirement:
    You have planned some train traveling one year in advance. The days of the year in which 
    you will travel are given as an integer array days. Each day is an integer from 1 to 365.

    Train tickets are sold in three different ways:
        a 1-day pass is sold for costs[0] dollars,
        a 7-day pass is sold for costs[1] dollars, and
        a 30-day pass is sold for costs[2] dollars.
        The passes allow that many days of consecutive travel.

    For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

    Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:
    Input: days = [1,4,6,7,8,20], costs = [2,7,15]
    Output: 11
    Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
        On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
        On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
        On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
        In total, you spent $11 and covered all the days of your travel.
Example 2:
    Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
    Output: 17
    Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
        On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
        On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
        In total, you spent $17 and covered all the days of your travel.

Constraints:
    1 <= days.length <= 365
    1 <= days[i] <= 365
    days is in strictly increasing order.
    costs.length == 3
    1 <= costs[i] <= 1000
"""


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # exception case
        assert isinstance(days, list) and len(days) >= 1
        assert isinstance(costs, list) and len(costs) == 3
        # main method: (dynamic programming)
        return self._mincostTickets(days, costs)

    def _mincostTickets(self, days: List[int], costs: List[int]) -> int:
        assert isinstance(days, list) and len(days) >= 1
        assert isinstance(costs, list) and len(costs) == 3

        day_set = set(days)
        durations = [1, 7, 30]

        @functools.lru_cache(maxsize=None)
        def __dp(i):
            if i > 365:
                return 0
            elif i in day_set:
                return min(__dp(i + d) + c for c, d in zip(costs, durations))
            else:
                return __dp(i + 1)

        return __dp(1)


def main():
    # Example 1: Output: 11
    # days = [1, 4, 6, 7, 8, 20]
    # costs = [2, 7, 15]

    # Example 2: Output: 17
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2, 7, 15]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.mincostTickets(days, costs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
