#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-INTERVIEW-0502-Binary-Number-to-String-LCCI.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-02
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - INTERVIEW-0502 - (Medium) - Binary Number to String
https://leetcode.cn/problems/bianry-number-to-string-lcci/

Description & Requirement:
    Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, 
    print the binary representation. If the number cannot be represented accurately in binary 
    with at most 32 characters, print "ERROR".

Example1:
    Input: 0.625
    Output: "0.101"
Example2:
    Input: 0.1
    Output: "ERROR"
    Note: 0.1 cannot be represented accurately in binary.

Note:
    This two characters "0." should be counted into 32 characters.
    The number of decimal places for num is at most 6 digits
"""


class Solution:
    def printBin(self, num: float) -> str:
        # exception case
        assert isinstance(num, float) and 0.0 < num < 1.0
        # main method: (deal with each digit)
        return self._printBin(num)

    def _printBin(self, num: float) -> str:
        assert isinstance(num, float) and 0.0 < num < 1.0

        res = "0."
        while len(res) <= 32 and num != 0:
            num *= 2
            digit = int(num)
            res += str(digit)
            num -= digit

        return res if len(res) <= 32 else "ERROR"


def main():
    # Example1: Output: "0.101"
    num = 0.625

    # Example2: Output: "ERROR"
    # num = 0.1

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.printBin(num)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
