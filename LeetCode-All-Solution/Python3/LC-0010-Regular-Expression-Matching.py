#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0010-Regular-Expression-Matching.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-04
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0010 - (Hard) - Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/

Description & Requirement:
    Given an input string s and a pattern p, 
    implement regular expression matching with support for '.' and '*' where:
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).

Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
Example 2:
    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:
    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:
    1 <= s.length <= 20
    1 <= p.length <= 30
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
    It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # exception case
        assert isinstance(s, str) and isinstance(p, str) and len(s) >= 1 and len(p) >= 1
        if s == p:
            return True
        if p == ".*":
            return True
        # main method: (Dynamic Programming, match s[s_idx] and p[p_idx] from s_idx == p_idx == 0)
        return self._isMatch(s, p)

    def _isMatch(self, s: str, p: str) -> bool:
        dp = dict({})  # key: Tuple(s_idx, p_idx); value: True if match(s[0: s_idx], p[0: p_idx]) else False

        def __dp(s_idx: int, p_idx: int) -> bool:
            if (s_idx, p_idx) in dp:  # use the recorded result in the dp table
                return dp[(s_idx, p_idx)]

            if p_idx == len(p):  # p reaches the end
                return s_idx == len(s)

            # match s[s_idx] and p[p_idx]
            first_match = s_idx < len(s) and p_idx < len(p) and ((s[s_idx] == p[p_idx]) or (p[p_idx] == "."))

            # if p[p_idx + 1] is "*"
            if p_idx < len(p) - 1 and p[p_idx + 1] == "*":
                if first_match:
                    res = __dp(s_idx + 1, p_idx) or __dp(s_idx, p_idx + 2)
                else:
                    # if first chars do not match, consider p[p_idx + 1], "*" means p[p_idx] and be skipped
                    res = __dp(s_idx, p_idx + 2)
            else:
                # match first and recursively match the next
                res = first_match and __dp(s_idx + 1, p_idx + 1)

            # record dp table
            if (s_idx, p_idx) not in dp:
                dp[(s_idx, p_idx)] = res

            return res

        return __dp(0, 0)


def main():
    # Example 1: Output: false
    # s = "aa"
    # p = "a"

    # Example 2: Output: true
    # s = "aa"
    # p = "a*"

    # Example 3: Output: true
    s = "ab"
    p = ".*"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isMatch(s, p)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
