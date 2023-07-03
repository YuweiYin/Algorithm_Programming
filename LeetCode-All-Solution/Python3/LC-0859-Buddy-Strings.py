#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0859-Buddy-Strings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-03
=================================================================="""

import sys
import time
# from typing import List
# import functools
# import itertools

"""
LeetCode - 0859 - (Easy) - Buddy Strings
https://leetcode.com/problems/buddy-strings/

Description & Requirement:
    Given two strings s and goal, return true if you can swap two letters in s 
    so the result is equal to goal, otherwise, return false.

    Swapping letters is defined as taking two indices i and j (0-indexed) such that 
    i != j and swapping the characters at s[i] and s[j].

    For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:
    Input: s = "ab", goal = "ba"
    Output: true
    Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:
    Input: s = "ab", goal = "ab"
    Output: false
    Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:
    Input: s = "aa", goal = "aa"
    Output: true
    Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

Constraints:
    1 <= s.length, goal.length <= 2 * 10^4
    s and goal consist of lowercase letters.
"""


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(goal, str) and len(goal) >= 1
        # main method: (enumerate chars)
        return self._buddyStrings(s, goal)

    def _buddyStrings(self, s: str, goal: str) -> bool:
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(goal, str) and len(goal) >= 1

        if len(s) != len(goal):
            return False

        if s == goal:
            if len(set(s)) < len(goal):
                return True
            else:
                return False

        diff = [(ch_s, ch_g) for ch_s, ch_g in zip(s, goal) if ch_s != ch_g]

        return len(diff) == 2 and diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]


def main():
    # Example 1: Output: true
    s = "ab"
    goal = "ba"

    # Example 2: Output: false
    # s = "ab"
    # goal = "ab"

    # Example 3: Output: true
    # s = "aa"
    # goal = "aa"

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.buddyStrings(s, goal)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
