#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0459-Repeated-Substring-Pattern.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-21
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 0459 - (Easy) Repeated Substring Pattern
https://leetcode.com/problems/repeated-substring-pattern/

Description & Requirement:
    Given a string s, check if it can be constructed by taking a substring of it 
    and appending multiple copies of the substring together.

Example 1:
    Input: s = "abab"
    Output: true
    Explanation: It is the substring "ab" twice.
Example 2:
    Input: s = "aba"
    Output: false
Example 3:
    Input: s = "abcabcabcabc"
    Output: true
    Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

Constraints:
    1 <= s.length <= 10^4
    s consists of lowercase English letters.
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (string matching)
        return self._repeatedSubstringPattern(s)

    def _repeatedSubstringPattern(self, s: str) -> bool:
        assert isinstance(s, str) and len(s) >= 1

        return (s + s).find(s, 1) != len(s)


def main():
    # Example 1: Output: true
    # s = "abab"

    # Example 2: Output: false
    # s = "aba"

    # Example 3: Output: true
    s = "abcabcabcabc"

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.repeatedSubstringPattern(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
