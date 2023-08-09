#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1281-Subtract-the-Product-and-Sum-of-Digits-of-an-Integer.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-09
=================================================================="""

import sys
import time
# from typing import List
# import functools
# import itertools

"""
LeetCode - 1281 - (Easy) - Subtract the Product and Sum of Digits of an Integer
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

Description & Requirement:
    Given an integer number n, return the difference 
    between the product of its digits and the sum of its digits.

Example 1:
    Input: n = 234
    Output: 15 
    Explanation: 
        Product of digits = 2 * 3 * 4 = 24 
        Sum of digits = 2 + 3 + 4 = 9 
        Result = 24 - 9 = 15
Example 2:
    Input: n = 4421
    Output: 21
    Explanation: 
        Product of digits = 4 * 4 * 2 * 1 = 32 
        Sum of digits = 4 + 4 + 2 + 1 = 11 
        Result = 32 - 11 = 21

Constraints:
    1 <= n <= 10^5
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (simulation)
        return self._subtractProductAndSum(n)

    def _subtractProductAndSum(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1

        m, s = 1, 0
        while n != 0:
            x, n = n % 10, n // 10
            m *= x
            s += x

        return m - s


def main():
    # Example 1: Output: 15
    n = 234

    # Example 2: Output: 21
    # n = 4421

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.subtractProductAndSum(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
