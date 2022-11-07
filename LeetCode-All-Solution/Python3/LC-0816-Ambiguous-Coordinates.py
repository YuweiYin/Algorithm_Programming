#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0816-Ambiguous-Coordinates.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-07
=================================================================="""

import sys
import time
from typing import List
from itertools import product
# import collections
# import functools

"""
LeetCode - 0816 - (Medium) - Ambiguous Coordinates
https://leetcode.com/problems/ambiguous-coordinates/

Description & Requirement:
    We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". 
    Then, we removed all commas, decimal points, and spaces and ended up with the string s.
        For example, "(1, 3)" becomes s = "(13)" and "(2, 0.5)" becomes s = "(205)".

    Return a list of strings representing all possibilities for what our original coordinates could have been.

    Our original representation never had extraneous zeroes, so we never started with numbers like 
    "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with fewer digits. 
    Also, a decimal point within a number never occurs without at least one digit occurring before it, 
    so we never started with numbers like ".1".

    The final answer list can be returned in any order. 
    All coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
    Input: s = "(123)"
    Output: ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]
Example 2:
    Input: s = "(0123)"
    Output: ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]
    Explanation: 0.0, 00, 0001 or 00.01 are not allowed.
Example 3:
    Input: s = "(00011)"
    Output: ["(0, 0.011)","(0.001, 1)"]

Constraints:
    4 <= s.length <= 12
    s[0] == '(' and s[s.length - 1] == ')'.
    The rest of s are digits.
"""


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        # exception case
        assert isinstance(s, str) and len(s) >= 4 and s[0] == "(" and s[-1] == ")" and s[1:-1].isdigit()
        # main method: (enumerate all possibilities)
        return self._ambiguousCoordinates(s)

    def _ambiguousCoordinates(self, s: str) -> List[str]:
        assert isinstance(s, str) and len(s) >= 4 and s[0] == "(" and s[-1] == ")" and s[1:-1].isdigit()
        n = len(s) - 2
        s = s[1: len(s) - 1]

        res = []

        def __get_pos(s: str) -> List[str]:
            pos = []
            if s[0] != '0' or s == '0':
                pos.append(s)
            for p in range(1, len(s)):
                if p != 1 and s[0] == '0' or s[-1] == '0':
                    continue
                pos.append(s[:p] + '.' + s[p:])
            return pos

        for idx in range(1, n):
            left = __get_pos(s[:idx])
            if len(left) == 0:
                continue
            right = __get_pos(s[idx:])
            if len(right) == 0:
                continue
            for i, j in product(left, right):
                res.append('(' + i + ', ' + j + ')')

        return res


def main():
    # Example 1: Output: ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]
    # s = "(123)"

    # Example 2: Output: ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]
    s = "(0123)"

    # Example 3: Output: ["(0, 0.011)","(0.001, 1)"]
    # s = "(00011)"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.ambiguousCoordinates(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
