#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0777-Swap-Adjacent-in-LR-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-02
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0777 - (Medium) - Swap Adjacent in LR String
https://leetcode.com/problems/swap-adjacent-in-lr-string/

Description & Requirement:
    In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", 
    a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR".

    Given the starting string start and the ending string end, return True if and only if 
    there exists a sequence of moves to transform one string to the other.

Example 1:
    Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
    Output: true
    Explanation: We can transform start to end following these steps:
        RXXLRXRXL ->
        XRXLRXRXL ->
        XRLXRXRXL ->
        XRLXXRRXL ->
        XRLXXRRLX
Example 2:
    Input: start = "X", end = "L"
    Output: false

Constraints:
    1 <= start.length <= 10^4
    start.length == end.length
    Both start and end will only consist of characters in 'L', 'R', and 'X'.
"""


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # exception case
        assert isinstance(start, str) and isinstance(end, str) and len(start) == len(end) >= 1
        # main method: (process simulation)
        return self._canTransform(start, end)

    def _canTransform(self, start: str, end: str) -> bool:
        assert isinstance(start, str) and isinstance(end, str) and len(start) == len(end) >= 1

        n = len(start)
        i = j = 0
        while i < n and j < n:
            # skip "X" first
            while i < n and start[i] == "X":
                i += 1
            while j < n and end[j] == "X":
                j += 1
            if i < n and j < n:
                if start[i] != end[j]:
                    return False
                c = start[i]
                if (c == "L" and i < j) or (c == "R" and i > j):
                    return False
                i += 1
                j += 1

        # match the rest chars
        while i < n:
            if start[i] != "X":
                return False
            i += 1

        while j < n:
            if end[j] != "X":
                return False
            j += 1

        return True


def main():
    # Example 1: Output: true
    _start = "RXXLRXRXL"
    _end = "XRLXXRRLX"

    # Example 2: Output: false
    # _start = "X"
    # _end = "L"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canTransform(_start, _end)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
