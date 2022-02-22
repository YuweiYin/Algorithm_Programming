#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0171-Excel-Sheet-Column-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-22
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0171 - (Easy) - Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/

Description & Requirement:
    Given a string columnTitle that represents the column title as appear in an Excel sheet, 
    return its corresponding column number.

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
    Input: columnTitle = "A"
    Output: 1
Example 2:
    Input: columnTitle = "AB"
    Output: 28
Example 3:
    Input: columnTitle = "ZY"
    Output: 701

Constraints:
    1 <= columnTitle.length <= 7
    columnTitle consists only of uppercase English letters.
    columnTitle is in the range ["A", "FXSHRXW"].
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # exception case
        if not isinstance(columnTitle, str) or len(columnTitle) <= 0:
            return 0  # Error input type
        if not columnTitle.isalpha() or not columnTitle.isupper():
            return 0  # Error input type
        # main method: (base is 26, from right to left scan columnTitle and accumulate numbers)
        return self._titleToNumber(columnTitle)  # Time: O(n log n);  Space: O(n).

    def _titleToNumber(self, columnTitle: str) -> int:
        len_columnTitle = len(columnTitle)
        assert len_columnTitle > 0

        char_to_int = dict({
            "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
            "K": 11, "L": 12,"M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
            "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26
        })
        # other method: ord(upper_letter) - ord("A") + 1,  the inverse function of ord() is chr()

        res = 0
        base = 26
        multiplier = 1

        char_idx = len_columnTitle - 1
        while char_idx >= 0:
            res += multiplier * char_to_int[columnTitle[char_idx]]
            multiplier *= base
            char_idx -= 1

        return res


def main():
    # Example 1: Output: 1
    # columnTitle = "A"

    # Example 2: Output: 28
    # columnTitle = "AB"

    # Example 3: Output: 701
    columnTitle = "ZY"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.titleToNumber(columnTitle)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
