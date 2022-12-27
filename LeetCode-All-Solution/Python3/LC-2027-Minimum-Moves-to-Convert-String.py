#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2027-Minimum-Moves-to-Convert-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-27
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2027 - (Easy) - Minimum Moves to Convert String
https://leetcode.com/problems/minimum-moves-to-convert-string/

Description & Requirement:
    You are given a string s consisting of n characters which are either 'X' or 'O'.

    A move is defined as selecting three consecutive characters of s and converting them to 'O'. 
    Note that if a move is applied to the character 'O', it will stay the same.

    Return the minimum number of moves required so that all the characters of s are converted to 'O'.

Example 1:
    Input: s = "XXX"
    Output: 1
    Explanation: XXX -> OOO
    We select all the 3 characters and convert them in one move.
Example 2:
    Input: s = "XXOX"
    Output: 2
    Explanation: XXOX -> OOOX -> OOOO
    We select the first 3 characters in the first move, and convert them to 'O'.
    Then we select the last 3 characters and convert them so that the final string contains all 'O's.
Example 3:
    Input: s = "OOOO"
    Output: 0
    Explanation: There are no 'X's in s to convert.

Constraints:
    3 <= s.length <= 1000
    s[i] is either 'X' or 'O'.
"""


class Solution:
    def minimumMoves(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 3
        # main method: (greedy)
        return self._minimumMoves(s)

    def _minimumMoves(self, s: str) -> int:
        """
        Time: beats 83.95%; Space: beats 15.38%
        """
        assert isinstance(s, str) and len(s) >= 3

        visited = -1
        res = 0
        for idx, ch in enumerate(s):
            if ch == 'X' and idx > visited:
                res += 1
                visited = idx + 2

        return res


def main():
    # Example 1: Output: 1
    # s = "XXX"

    # Example 2: Output: 2
    # s = "XXOX"

    # Example 3: Output: 0
    s = "OOOO"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumMoves(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
