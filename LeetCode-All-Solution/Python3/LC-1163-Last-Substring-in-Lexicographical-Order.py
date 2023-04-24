#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1163-Last-Substring-in-Lexicographical-Order.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-24
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1163 - (Hard) - Last Substring in Lexicographical Order
https://leetcode.com/problems/last-substring-in-lexicographical-order/

Description & Requirement:
    Given a string s, return the last substring of s in lexicographical order.

Example 1:
    Input: s = "abab"
    Output: "bab"
    Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. 
        The lexicographically maximum substring is "bab".
Example 2:
    Input: s = "leetcode"
    Output: "tcode"

Constraints:
    1 <= s.length <= 4 * 10^5
    s contains only lowercase English letters.
"""


class Solution:
    def lastSubstring(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (two pointers)
        return self._lastSubstring(s)

    def _lastSubstring(self, s: str) -> str:
        assert isinstance(s, str) and len(s) >= 1

        i, j, n = 0, 1, len(s)
        while j < n:
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j = j + k + 1

        return s[i:]


def main():
    # Example 1: Output: "bab"
    # s = "abab"

    # Example 2: Output: "tcode"
    s = "leetcode"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.lastSubstring(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
