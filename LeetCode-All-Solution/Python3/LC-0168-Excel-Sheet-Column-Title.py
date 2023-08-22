#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0168-Excel-Sheet-Column-Title.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-22
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 0168 - (Easy) Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/

Description & Requirement:
    Given an integer columnNumber, 
    return its corresponding column title as it appears in an Excel sheet.

    For example:
        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28
        ...

Example 1:
    Input: columnNumber = 1
    Output: "A"
Example 2:
    Input: columnNumber = 28
    Output: "AB"
Example 3:
    Input: columnNumber = 701
    Output: "ZY"

Constraints:
    1 <= columnNumber <= 2^31 - 1
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # exception case
        assert isinstance(columnNumber, int) and columnNumber >= 1
        # main method: (simulation)
        return self._convertToTitle(columnNumber)

    def _convertToTitle(self, columnNumber: int) -> str:
        assert isinstance(columnNumber, int) and columnNumber >= 1

        res = []
        while columnNumber > 0:
            ch = ((columnNumber - 1) % 26) + 1
            res.append(chr(ch - 1 + ord("A")))
            columnNumber = (columnNumber - ch) // 26

        return "".join(res[::-1])


def main():
    # Example 1: Output: "A"
    # columnNumber = 1

    # Example 2: Output: "AB"
    # columnNumber = 28

    # Example 3: Output: "ZY"
    columnNumber = 701

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.convertToTitle(columnNumber)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
