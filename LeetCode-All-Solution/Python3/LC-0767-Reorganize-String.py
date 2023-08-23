#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0767-Reorganize-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-23
=================================================================="""

import sys
import time
# from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 0767 - (Medium) Reorganize String
https://leetcode.com/problems/reorganize-string/

Description & Requirement:
    Given a string s, rearrange the characters of s so that 
    any two adjacent characters are not the same.

    Return any possible rearrangement of s or return "" if not possible.

Example 1:
    Input: s = "aab"
    Output: "aba"
Example 2:
    Input: s = "aaab"
    Output: ""

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.
"""


class Solution:
    def reorganizeString(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (hash counter)
        return self._reorganizeString(s)

    def _reorganizeString(self, s: str) -> str:
        assert isinstance(s, str) and len(s) >= 1

        if len(s) < 2:
            return s

        n = len(s)
        counts = collections.Counter(s)
        max_count = max(counts.items(), key=lambda x: x[1])[1]
        if max_count > (n + 1) // 2:
            return ""

        reorganize_array = [""] * n
        even_idx, odd_idx = 0, 1
        half_n = n // 2

        for c, count in counts.items():
            while 0 < count <= half_n and odd_idx < n:
                reorganize_array[odd_idx] = c
                count -= 1
                odd_idx += 2
            while count > 0:
                reorganize_array[even_idx] = c
                count -= 1
                even_idx += 2

        return "".join(reorganize_array)


def main():
    # Example 1: Output: "aba"
    s = "aab"

    # Example 2: Output: ""
    # s = "aaab"

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.reorganizeString(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
