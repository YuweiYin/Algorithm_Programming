#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1003-Check-If-Word-Is-Valid-After-Substitutions.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-03
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1003 - (Medium) - Check If Word Is Valid After Substitutions
https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

Description & Requirement:
    Given a string s, determine if it is valid.

    A string s is valid if, starting with an empty string t = "", you can transform t into s 
    after performing the following operation any number of times:

        Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, 
        where t == tleft + tright. Note that tleft and tright may be empty.

    Return true if s is a valid string, otherwise, return false.

Example 1:
    Input: s = "aabcbc"
    Output: true
    Explanation:
        "" -> "abc" -> "aabcbc"
        Thus, "aabcbc" is valid.
Example 2:
    Input: s = "abcabcababcc"
    Output: true
    Explanation:
        "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
        Thus, "abcabcababcc" is valid.
Example 3:
    Input: s = "abccba"
    Output: false
    Explanation: It is impossible to get "abccba" using the operation.

Constraints:
    1 <= s.length <= 2 * 10^4
    s consists of letters 'a', 'b', and 'c'
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (stack)
        return self._isValid(s)

    def _isValid(self, s: str) -> bool:
        assert isinstance(s, str) and len(s) >= 1

        stack = []
        for ch in s:
            stack.append(ch)
            if "".join(stack[-3:]) == "abc":
                stack[-3:] = []

        return len(stack) == 0


def main():
    # Example 1: Output: true
    # s = "aabcbc"

    # Example 2: Output: true
    s = "abcabcababcc"

    # Example 3: Output: false
    # s = "abccba"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isValid(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
