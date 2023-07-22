#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0860-Lemonade-Change.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-22
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 0860 - (Easy) - Lemonade Change
https://leetcode.com/problems/lemonade-change/

Description & Requirement:
    At a lemonade stand, each lemonade costs $5. Customers are standing in a queue 
    to buy from you and order one at a time (in the order specified by bills). 
    Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
    You must provide the correct change to each customer so that 
    the net transaction is that the customer pays $5.

    Note that you do not have any change in hand at first.

    Given an integer array bills where bills[i] is the bill the ith customer pays, 
    return true if you can provide every customer with the correct change, or false otherwise.

Example 1:
    Input: bills = [5,5,5,10,20]
    Output: true
    Explanation: 
        From the first 3 customers, we collect three $5 bills in order.
        From the fourth customer, we collect a $10 bill and give back a $5.
        From the fifth customer, we give a $10 bill and a $5 bill.
        Since all customers got correct change, we output true.
Example 2:
    Input: bills = [5,5,10,10,20]
    Output: false
    Explanation: 
        From the first two customers in order, we collect two $5 bills.
        For the next two customers in order, we collect a $10 bill and give back a $5 bill.
        For the last customer, we can not give the change of $15 back because we only have two $10 bills.
        Since not every customer received the correct change, the answer is false.

Constraints:
    1 <= bills.length <= 10^5
    bills[i] is either 5, 10, or 20.
"""


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # exception case
        assert isinstance(bills, list) and len(bills) >= 1
        # main method: (simulate the process)
        return self._lemonadeChange(bills)

    def _lemonadeChange(self, bills: List[int]) -> bool:
        assert isinstance(bills, list) and len(bills) >= 1

        five = ten = 0
        for v in bills:
            if v == 5:
                five += 1
            elif v == 10:
                ten += 1
                five -= 1
            else:
                if ten:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0:
                return False

        return True


def main():
    # Example 1: Output: true
    bills = [5, 5, 5, 10, 20]

    # Example 2: Output: false
    # bills = [5, 5, 10, 10, 20]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.lemonadeChange(bills)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
