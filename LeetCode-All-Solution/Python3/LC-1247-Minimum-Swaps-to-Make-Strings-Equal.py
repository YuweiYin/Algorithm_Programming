#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1247-Minimum-Swaps-to-Make-Strings-Equal.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-25
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1247 - (Medium) - Minimum Swaps to Make Strings Equal
https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

Description & Requirement:
    You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. 
    Your task is to make these two strings equal to each other. 
    You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

    Return the minimum number of swaps required to make s1 and s2 equal, 
    or return -1 if it is impossible to do so.

Example 1:
    Input: s1 = "xx", s2 = "yy"
    Output: 1
    Explanation: Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
Example 2:
    Input: s1 = "xy", s2 = "yx"
    Output: 2
    Explanation: Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
    Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
    Note that you cannot swap s1[0] and s1[1] to make s1 equal to "yx", 
        cause we can only swap chars in different strings.
Example 3:
    Input: s1 = "xx", s2 = "xy"
    Output: -1

Constraints:
    1 <= s1.length, s2.length <= 1000
    s1, s2 only contain 'x' or 'y'.
"""


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # exception case
        assert isinstance(s1, str) and len(s1) >= 1
        assert isinstance(s2, str) and len(s2) >= 1
        # main method: (just scan the strings)
        return self._minimumSwap(s1, s2)

    def _minimumSwap(self, s1: str, s2: str) -> int:
        assert isinstance(s1, str) and len(s1) >= 1
        assert isinstance(s2, str) and len(s2) >= 1

        xy, yx = 0, 0
        for ch1, ch2 in zip(s1, s2):
            if ch1 == 'x' and ch2 == 'y':
                xy += 1
            if ch1 == 'y' and ch2 == 'x':
                yx += 1

        if (xy + yx) & 0x01 == 1:
            return -1

        return (xy >> 1) + (yx >> 1) + (xy & 0x01) + (yx & 0x01)


def main():
    # Example 1: Output: 1
    s1 = "xx"
    s2 = "yy"

    # Example 2: Output: 2
    # s1 = "xy"
    # s2 = "yx"

    # Example 3: Output: -1
    # s1 = "xx"
    # s2 = "xy"

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minimumSwap(s1, s2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
