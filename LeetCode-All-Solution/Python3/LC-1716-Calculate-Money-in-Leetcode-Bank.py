#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1716-Calculate-Money-in-Leetcode-Bank.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-15
=================================================================="""

import sys
import time
# from typing import List

"""
LeetCode - 1716 - (Easy) - Calculate Money in Leetcode Bank
https://leetcode.com/problems/calculate-money-in-leetcode-bank/

Description & Requirement:
    Henry wants to save money for his first car. He puts money in the Leetcode bank every day.

    He starts by putting in $1 on Monday, the first day. 
    Every day from Tuesday to Sunday, he will put in $1 more than the day before. 
    On every subsequent Monday, he will put in $1 more than the previous Monday.

    Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example 1:
    Input: n = 4
    Output: 10
    Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:
    Input: n = 10
    Output: 37
    Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:
    Input: n = 20
    Output: 96
    Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.

Constraints:
    1 <= n <= 1000
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        # exception case
        if not isinstance(n, int) or n <= 0:
            return 0  # Error input type
        if n == 1:
            return 1
        # main method: (Mathematics formula)
        # each day of week0:     1+0,       2+0,       3+0,       4+0,        5+0,        6+0,        7+0
        # each day of week1:     1+1,       2+1,       3+1,       4+1,        5+1,        6+1,        7+1
        # each day of week2:     1+2,       2+2,       3+2,       4+2,        5+2,        6+2,        7+2
        # each day of week(n%7): 1+(n%7),   2+(n%7),   3+(n%7),   4+(n%7),    5+(n%7),    6+(n%7),    7+(n%7)
        # sum of cur  week0:     1+0,       3+0,       6+0,       10+0,       15+0,       21+0,       28+0
        # sum of cur  week1:     1+1,       3+2,       6+3,       10+4,       15+5,       21+6,       28+7
        # sum of cur  week2:     1+2,       3+4,       6+6,       10+8,       15+10,      21+12,      28+14
        # sum of cur  week(n%7): 1+(n%7)*1, 3+(n%7)*2, 6+(n%7)*3, 10+(n%7)*4, 15+(n%7)*5, 21+(n%7)*6, 28+(n%7)*7
        return self._totalMoney(n)

    def _totalMoney(self, n: int) -> int:
        """
        Runtime: 28 ms, faster than 90.76% of Python3 online submissions for Calculate Money in Leetcode Bank.
        Memory Usage: 14.2 MB, less than 39.01% of Python3 online submissions for Calculate Money in Leetcode Bank.
        """
        cur_week = int(n / 7)
        cur_weekday = n % 7

        cumulate_former_week = sum([(28 + _week * 7) for _week in range(cur_week)])
        cumulate_this_week = sum([(_day + cur_week) for _day in range(1, cur_weekday + 1)])

        return cumulate_former_week + cumulate_this_week


def main():
    # Example 1: Output: 10
    # n = 4

    # Example 2: Output: 37
    # n = 10

    # Example 3: Output: 96
    # n = 20

    # Example 4: Output: 74926
    n = 1000

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.totalMoney(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
