#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0028-Implement-strStr.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-14
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0028 - (Easy) - Implement strStr()
https://leetcode.com/problems/implement-strstr/

Description & Requirement:
    Implement strStr().

    Given two strings needle and haystack, 
    return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Clarification:
        What should we return when needle is an empty string? This is a great question to ask during an interview.
        For the purpose of this problem, we will return 0 when needle is an empty string. 
            This is consistent to C's strstr() and Java's indexOf().

Example 1:
    Input: haystack = "hello", needle = "ll"
    Output: 2
Example 2:
    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

Constraints:
    1 <= haystack.length, needle.length <= 10^4
    haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # exception case
        assert isinstance(haystack, str) and len(haystack) >= 1
        assert isinstance(needle, str) and len(needle) >= 1
        # main method: (sub string matching. built-in function: `find`)
        return self._strStr(haystack, needle)

    def _strStr(self, haystack: str, needle: str) -> int:
        """
        Runtime: 40 ms, faster than 81.90% of Python3 online submissions for Implement strStr().
        Memory Usage: 13.9 MB, less than 94.33% of Python3 online submissions for Implement strStr().
        """
        return haystack.find(needle)


def main():
    # Example 1: Output: 2
    # haystack = "hello"
    # needle = "ll"

    # Example 2: Output: -1
    haystack = "aaaaa"
    needle = "bba"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.strStr(haystack, needle)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
