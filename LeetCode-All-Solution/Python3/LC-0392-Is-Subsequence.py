#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0392-Is-Subsequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-22
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0392 - (Easy) - Is Subsequence
https://leetcode.com/problems/is-subsequence/

Description & Requirement:
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string 
    by deleting some (can be none) of the characters without disturbing the relative positions 
    of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true
Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false

Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 10^4
    s and t consist only of lowercase English letters.

Follow up:
    Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, 
    and you want to check one by one to see if t has its subsequence. 
    In this scenario, how would you change your code?
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # exception case
        assert isinstance(s, str) and isinstance(t, str)
        if len(s) == 0:
            return True  # always can find a empty string
        if len(t) == 0:
            return False  # now len(s) > 0, so if len(t) == 0, then can't find s in t
        if len(s) >= len(t):
            return s == t
        # main method: (scan and greedily match each char of s in t)
        return self._isSubsequence(s, t)  # Time: O(len(s) + len(t));  Space: O(1).

    def _isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        assert len_s > 0 and len_t > 0

        s_idx = 0
        t_idx = 0
        while s_idx < len_s and t_idx < len_t:
            if t[t_idx] == s[s_idx]:  # match a char, move s_idx, check the next char of s
                s_idx += 1
            t_idx += 1

        return s_idx == len_s


def main():
    # Example 1: Output: true
    s = "abc"
    t = "ahbgdc"

    # Example 2: Output: false
    # s = "axc"
    # t = "ahbgdc"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isSubsequence(s, t)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
