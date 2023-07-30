#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0664-Strange-Printer.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-30
=================================================================="""

import sys
import time
# from typing import List
# import functools
# import itertools

"""
LeetCode - 0664 - (Hard) - Strange Printer
https://leetcode.com/problems/strange-printer/

Description & Requirement:
    There is a strange printer with the following two special properties:
        The printer can only print a sequence of the same character each time.
        At each turn, the printer can print new characters starting from and ending at any place and 
            will cover the original existing characters.

    Given a string s, return the minimum number of turns the printer needed to print it.

Example 1:
    Input: s = "aaabbb"
    Output: 2
    Explanation: Print "aaa" first and then print "bbb".
Example 2:
    Input: s = "aba"
    Output: 2
    Explanation: Print "aaa" first and then print "b" from the second place of the string, 
        which will cover the existing character 'a'.

Constraints:
    1 <= s.length <= 100
    s consists of lowercase English letters.
"""


class Solution:
    def strangePrinter(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (interval DP)
        return self._strangePrinter(s)

    def _strangePrinter(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1

        n = len(s)
        dp = [[n] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

        return dp[0][-1]


def main():
    # Example 1: Output: 2
    s = "aaabbb"

    # Example 2: Output: 2
    # s = "aba"

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.strangePrinter(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
