#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2309-Greatest-English-Letter-in-Upper-and-Lower-Case.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-27
=================================================================="""

import sys
import time
import string
# from typing import List
# import collections
# import functools

"""
LeetCode - 2309 - (Easy) - Greatest English Letter in Upper and Lower Case
https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

Description & Requirement:
    Given a string of English letters s, return the greatest English letter which 
    occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. 
    If no such letter exists, return an empty string.

    An English letter b is greater than another letter a if b appears after a in the English alphabet.

Example 1:
    Input: s = "lEeTcOdE"
    Output: "E"
    Explanation:
        The letter 'E' is the only letter to appear in both lower and upper case.
Example 2:
    Input: s = "arRAzFif"
    Output: "R"
    Explanation:
        The letter 'R' is the greatest letter to appear in both lower and upper case.
        Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.
Example 3:
    Input: s = "AbCdEfGhIjK"
    Output: ""
    Explanation:
        There is no letter that appears in both lower and upper case.

Constraints:
    1 <= s.length <= 1000
    s consists of lowercase and uppercase English letters.
"""


class Solution:
    def greatestLetter(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (hash set)
        return self._greatestLetter(s)

    def _greatestLetter(self, s: str) -> str:
        assert isinstance(s, str) and len(s) >= 1

        s = set(s)
        for lower, upper in zip(reversed(string.ascii_lowercase), reversed(string.ascii_uppercase)):
            if lower in s and upper in s:
                return upper

        return ""


def main():
    # Example 1: Output: "E"
    # s = "lEeTcOdE"

    # Example 2: Output: "R"
    # s = "arRAzFif"

    # Example 3: Output: ""
    s = "AbCdEfGhIjK"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.greatestLetter(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
