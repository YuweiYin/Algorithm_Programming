#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1328-Break-a-Palindrome.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-10
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1328 - (Medium) - Break a Palindrome
https://leetcode.com/problems/break-a-palindrome/

Description & Requirement:
    Given a palindromic string of lowercase English letters palindrome, 
    replace exactly one character with any lowercase English letter so that 
    the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

    Return the resulting string. 
    If there is no way to replace a character to make it not a palindrome, return an empty string.

    A string a is lexicographically smaller than a string b (of the same length) if in the first position 
    where a and b differ, a has a character strictly smaller than the corresponding character in b. 
    For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is 
    at the fourth character, and 'c' is smaller than 'd'.

Example 1:
    Input: palindrome = "abccba"
    Output: "aaccba"
    Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
        Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:
    Input: palindrome = "a"
    Output: ""
    Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

Constraints:
    1 <= palindrome.length <= 1000
    palindrome consists of only lowercase English letters.
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # exception case
        assert isinstance(palindrome, str) and len(palindrome) >= 1
        # main method: (greedily replace the first character that is not "a" to "a")
        return self._breakPalindrome(palindrome)

    def _breakPalindrome(self, palindrome: str) -> str:
        """
        Runtime: 31 ms, faster than 93.59% of Python3 online submissions for Break a Palindrome.
        Memory Usage: 14 MB, less than 13.13% of Python3 online submissions for Break a Palindrome.
        """
        assert isinstance(palindrome, str) and len(palindrome) >= 1

        n = len(palindrome)
        if n <= 1:
            return ""

        for idx in range(n >> 1):
            if palindrome[idx] != "a":
                return palindrome[:idx] + "a" + palindrome[idx + 1:]

        return palindrome[:-1] + "b"


def main():
    # Example 1: Output: "aaccba"
    palindrome = "abccba"

    # Example 2: Output: ""
    # palindrome = "a"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.breakPalindrome(palindrome)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
