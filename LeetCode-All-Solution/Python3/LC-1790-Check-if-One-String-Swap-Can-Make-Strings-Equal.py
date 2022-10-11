#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1790-Check-if-One-String-Swap-Can-Make-Strings-Equal.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-11
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1790 - (Easy) - Check if One String Swap Can Make Strings Equal
https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

Description & Requirement:
    You are given two strings s1 and s2 of equal length. A string swap is an operation where 
    you choose two indices in a string (not necessarily different) and swap the characters at these indices.

    Return true if it is possible to make both strings equal 
    by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:
    Input: s1 = "bank", s2 = "kanb"
    Output: true
    Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:
    Input: s1 = "attack", s2 = "defend"
    Output: false
    Explanation: It is impossible to make them equal with one string swap.
Example 3:
    Input: s1 = "kelb", s2 = "kelb"
    Output: true
    Explanation: The two strings are already equal, so no string swap operation is required.

Constraints:
    1 <= s1.length, s2.length <= 100
    s1.length == s2.length
    s1 and s2 consist of only lowercase English letters.
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # exception case
        assert isinstance(s1, str) and len(s1) >= 1
        assert isinstance(s2, str) and len(s1) == len(s2)
        # main method: (check the mismatched chars)
        return self._areAlmostEqual(s1, s2)

    def _areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Runtime: 34 ms, faster than 91.62% of submissions for Check if One String Swap Can Make Strings Equal.
        Memory Usage: 13.9 MB, less than 20.11% of submissions for Check if One String Swap Can Make Strings Equal.
        """
        assert isinstance(s1, str) and len(s1) >= 1
        assert isinstance(s2, str) and len(s1) == len(s2)

        n = len(s1)
        mismatch_1 = set()
        mismatch_2 = set()
        cnt = 0

        for idx in range(n):
            ch_1, ch_2 = s1[idx], s2[idx]
            if ch_1 != ch_2:
                mismatch_1.add(ch_1)
                mismatch_2.add(ch_2)
                cnt += 1
                if cnt > 2:
                    return False

        if mismatch_1 == mismatch_2:
            return len(mismatch_1) == 0 or len(mismatch_1) == 2
        else:
            return False


def main():
    # Example 1: Output: true
    # s1, s2 = "bank", "kanb"

    # Example 2: Output: false
    # s1, s2 = "attack", "defend"

    # Example 3: Output: true
    # s1, s2 = "kelb", "kelb"

    # Example 4: Output: false
    s1, s2 = "qgqeg", "gqgeq"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.areAlmostEqual(s1, s2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
