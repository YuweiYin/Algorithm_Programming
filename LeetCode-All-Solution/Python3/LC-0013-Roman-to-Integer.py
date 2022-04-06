#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0013-Roman-to-Integer.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-06
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0013 - (Easy) - Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Description & Requirement:
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    For example, 2 is written as II in Roman numeral, just two one's added together. 
    12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. 
    However, the numeral for four is not IIII. 
    Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
    The same principle applies to the number nine, which is written as IX. 
    There are six instances where subtraction is used:
        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.

    Given a roman numeral, convert it to an integer.

Example 1:
    Input: s = "III"
    Output: 3
    Explanation: III = 3.
Example 2:
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
Example 3:
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (greedily convert, from bigger Roman number to smaller ones)
        return self._romanToInt(s)

    def _romanToInt(self, s: str) -> int:
        # num_to_roman = [
        #     (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
        #     (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
        #     (5, "V"), (4, "IV"), (1, "I")
        # ]
        # roman_to_num = [
        #     ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100),
        #     ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9),
        #     ("V", 5), ("IV", 4), ("I", 1)
        # ]
        roman_to_num_dict = dict({
            "M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
            "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9,
            "V": 5, "IV": 4, "I": 1
        })

        res = 0
        len_s = len(s)
        s_idx = 0
        while s_idx < len_s:
            if s_idx < len_s - 1 and s[s_idx: s_idx + 2] in roman_to_num_dict:  # match 2 chars Roman number first
                res += roman_to_num_dict[s[s_idx: s_idx + 2]]
                s_idx += 2
            elif s[s_idx] in roman_to_num_dict:  # them match 1 char Roman number
                res += roman_to_num_dict[s[s_idx]]
                s_idx += 1
            else:  # smaller Roman numbers
                s_idx += 1
        return res


def main():
    # Example 1: Output: 3
    s = "III"

    # Example 2: Output: 58
    # s = "LVIII"

    # Example 3: Output: 1994
    # s = "MCMXCIV"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.romanToInt(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
