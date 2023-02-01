#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1071-Greatest-Common-Divisor-of-Strings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-01
=================================================================="""

import sys
import time
import math
# from typing import List
# import collections
# import functools

"""
LeetCode - 1071 - (Easy) - Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/

Description & Requirement:
    For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
    (i.e., t is concatenated with itself one or more times).

    Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"
Example 2:
    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"
Example 3:
    Input: str1 = "LEET", str2 = "CODE"
    Output: ""

Constraints:
    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # exception case
        assert isinstance(str1, str) and len(str1) >= 1
        assert isinstance(str2, str) and len(str2) >= 1
        # main method: (math gcd)
        return self._gcdOfStrings(str1, str2)

    def _gcdOfStrings(self, str1: str, str2: str) -> str:
        assert isinstance(str1, str) and len(str1) >= 1
        assert isinstance(str2, str) and len(str2) >= 1

        gcd_len = math.gcd(len(str1), len(str2))

        return str1[: gcd_len] if str1 + str2 == str2 + str1 else ""


def main():
    # Example 1: Output: "ABC"
    str1 = "ABCABC"
    str2 = "ABC"

    # Example 2: Output: "AB"
    # str1 = "ABABAB"
    # str2 = "ABAB"

    # Example 3: Output: ""
    # str1 = "LEET"
    # str2 = "CODE"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.gcdOfStrings(str1, str2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
