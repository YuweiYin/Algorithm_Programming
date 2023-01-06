#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2180-Count-Integers-With-Even-Digit-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-06
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2180 - (Easy) - Count Integers With Even Digit Sum
https://leetcode.com/problems/count-integers-with-even-digit-sum/

Description & Requirement:
    Given a positive integer num, 
    return the number of positive integers less than or equal to num whose digit sums are even.

    The digit sum of a positive integer is the sum of all its digits.

Example 1:
    Input: num = 4
    Output: 2
    Explanation:
        The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    
Example 2:
    Input: num = 30
    Output: 14
    Explanation:
        The 14 integers less than or equal to 30 whose digit sums are even are
        2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.

Constraints:
    1 <= num <= 1000
"""


class Solution:
    def countEven(self, num: int) -> int:
        # exception case
        assert isinstance(num, int) and num >= 1
        # main method: (mathematics)
        return self._countEven(num)

    def _countEven(self, num: int) -> int:
        assert isinstance(num, int) and num >= 1

        y, x = divmod(num, 10)
        res = y * 5
        y_sum = 0
        while y > 0:
            y_sum += y % 10
            y //= 10

        if y_sum & 0x01 == 1:
            return res - 1 + ((x + 1) >> 1)
        else:
            return res + (x >> 1)


def main():
    # Example 1: Output: 2
    # num = 4

    # Example 2: Output: 14
    num = 30

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countEven(num)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
