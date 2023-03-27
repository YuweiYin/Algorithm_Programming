#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1638-Count-Substrings-That-Differ-by-One-Character.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-27
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1638 - (Medium) - Count Substrings That Differ by One Character
https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

Description & Requirement:
    Given two strings s and t, find the number of ways you can choose a non-empty substring of s and 
    replace a single character by a different character such that the resulting substring is a substring of t. 
    In other words, find the number of substrings in s that differ from some substring in t by exactly one character.

    For example, the underlined substrings in "computer" and "computation" 
    only differ by the 'e'/'a', so this is a valid way.

    Return the number of substrings that satisfy the condition above.

    A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "aba", t = "baba"
    Output: 6
    Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
        ("aba", "baba")
        ("aba", "baba")
        ("aba", "baba")
        ("aba", "baba")
        ("aba", "baba")
        ("aba", "baba")
        The underlined portions are the substrings that are chosen from s and t.
Example 2:
    Input: s = "ab", t = "bb"
    Output: 3
    Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
        ("ab", "bb")
        ("ab", "bb")
        ("ab", "bb")
        The underlined portions are the substrings that are chosen from s and t.

Constraints:
    1 <= s.length, t.length <= 100
    s and t consist of lowercase English letters only.
"""


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(t, str) and len(t) >= 1
        # main method: (enumerate or DP)
        return self._countSubstrings(s, t)

    def _countSubstrings(self, s: str, t: str) -> int:
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(t, str) and len(t) >= 1

        res = 0

        for idx_s in range(len(s)):
            for idx_t in range(len(t)):
                diff = 0
                ptr = 0
                while idx_s + ptr < len(s) and idx_t + ptr < len(t):
                    if s[idx_s + ptr] != t[idx_t + ptr]:
                        diff += 1
                    if diff == 1:
                        res += 1
                    elif diff > 1:
                        break
                    ptr += 1

        return res


def main():
    # Example 1: Output: 6
    s = "aba"
    t = "baba"

    # Example 2: Output: 3
    # s = "ab"
    # t = "bb"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countSubstrings(s, t)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
