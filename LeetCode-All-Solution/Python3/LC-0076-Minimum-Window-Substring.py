#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0076-Minimum-Window-Substring.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-22
=================================================================="""

import sys
import time
import collections
# from typing import List
# import functools

"""
LeetCode - 0076 - (Hard) - Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Description & Requirement:
    Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that 
    every character in t (including duplicates) is included in the window. 
    If there is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.

    A substring is a contiguous sequence of characters within the string.

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.
Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
        Since the largest window of s only has one 'a', return empty string.

Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 10^5
    s and t consist of uppercase and lowercase English letters.

Follow up:
    Could you find an algorithm that runs in O(m + n) time?
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1 and s.isalpha()
        assert isinstance(t, str) and len(t) >= 1 and t.isalpha()
        # main method: (sliding window)
        return self._minWindow(s, t)

    def _minWindow(self, s: str, t: str) -> str:
        """
        Runtime: 70 ms, faster than 99.95% of Python3 online submissions for Minimum Window Substring.
        Memory Usage: 14.7 MB, less than 83.90% of Python3 online submissions for Minimum Window Substring.
        """
        assert isinstance(s, str) and len(s) >= 1 and s.isalpha()
        assert isinstance(t, str) and len(t) >= 1 and t.isalpha()

        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        need_counter = len(t)

        i = 0
        res = (0, float('inf'))

        for j, c in enumerate(s):
            if need[c] > 0:
                need_counter -= 1
            need[c] -= 1
            if need_counter == 0:
                while True:
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:
                    res = (i, j)
                need[s[i]] += 1
                need_counter += 1
                i += 1

        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]


def main():
    # Example 1: Output: "BANC"
    s = "ADOBECODEBANC"
    t = "ABC"

    # Example 2: Output: "a"
    # s = "a"
    # t = "a"

    # Example 3: Output: ""
    # s = "a"
    # t = "aa"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minWindow(s, t)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
