#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0761-Special-Binary-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-08
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0761 - (Hard) - Special Binary String
https://leetcode.com/problems/special-binary-string/

Description & Requirement:
    Special binary strings are binary strings with the following two properties:
        The number of 0's is equal to the number of 1's.
        Every prefix of the binary string has at least as many 1's as 0's.

    You are given a special binary string s.

    A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. 
    Two strings are consecutive if the last character of the first string is exactly one index before 
    the first character of the second string.

    Return the lexicographically largest resulting string possible 
    after applying the mentioned operations on the string.

Example 1:
    Input: s = "11011000"
    Output: "11100100"
    Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
    This is the lexicographically largest string possible after some number of swaps.
Example 2:
    Input: s = "10"
    Output: "10"

Constraints:
    1 <= s.length <= 50
    s[i] is either '0' or '1'.
    s is a special binary string.
"""


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        for ch in s:
            assert ch == "0" or ch == "1"
        # main method: (divide and conquer)
        return self._makeLargestSpecial(s)

    def _makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s

        substr = list()
        counter = 0
        left = 0

        for idx, ch in enumerate(s):
            if ch == "1":
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    substr.append("1" + self._makeLargestSpecial(s[left + 1: idx]) + "0")
                    left = idx + 1

        substr.sort(reverse=True)
        return "".join(substr)


def main():
    # Example 1: Output: "11100100"
    s = "11011000"

    # Example 2: Output: "10"
    # s = "10"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.makeLargestSpecial(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
