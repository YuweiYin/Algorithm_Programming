#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0504-Base-7.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-07
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0504 - (Easy) - Base 7
https://leetcode.com/problems/base-7/

Description & Requirement:
    Given an integer num, return a string of its base 7 representation.

Example 1:
    Input: num = 100
    Output: "202"
Example 2:
    Input: num = -7
    Output: "-10"

Constraints:
    -10^7 <= num <= 10^7
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        # exception case
        assert isinstance(num, int)
        # main method: (stack stimulate)
        return self._convertToBase7(num)

    def _convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        res = ""
        sign = False
        if num < 0:  # get rid of the sign
            num = - num
            sign = True

        BASE = 7
        while num > 0:
            residual = num % BASE
            num = int(num / BASE)
            res = str(residual) + res

        return res if not sign else "-" + res


def main():
    # Example 1: Output: "202"
    # num = 100

    # Example 2: Output: "-10"
    # num = -7

    # Example 3: Output: "150666343"
    # num = int(1e7)

    # Example 4: Output: "-150666343"
    num = - int(1e7)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.convertToBase7(num)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
