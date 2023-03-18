#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1616-Split-Two-Strings-to-Make-Palindrome.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-18
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1616 - (Medium) - Split Two Strings to Make Palindrome
https://leetcode.com/problems/split-two-strings-to-make-palindrome/

Description & Requirement:
    You are given two strings a and b of the same length. Choose an index and split both strings at the same index, 
    splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: 
    bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

    When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. 
    For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

    Return true if it is possible to form a palindrome string, otherwise return false.

    Notice that x + y denotes the concatenation of strings x and y.

Example 1:
    Input: a = "x", b = "y"
    Output: true
    Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
        aprefix = "", asuffix = "x"
        bprefix = "", bsuffix = "y"
        Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
Example 2:
    Input: a = "xbdef", b = "xecab"
    Output: false
Example 3:
    Input: a = "ulacfd", b = "jizalu"
    Output: true
    Explaination: Split them at index 3:
        aprefix = "ula", asuffix = "cfd"
        bprefix = "jiz", bsuffix = "alu"
        Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.

Constraints:
    1 <= a.length, b.length <= 10^5
    a.length == b.length
    a and b consist of lowercase English letters
"""


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        # exception case
        assert isinstance(a, str) and isinstance(b, str) and len(a) == len(b) >= 1
        # main method: (two pointers)
        return self._checkPalindromeFormation(a, b)

    def _checkPalindromeFormation(self, a: str, b: str) -> bool:
        assert isinstance(a, str) and isinstance(b, str) and len(a) == len(b) >= 1

        return self.check_concatenation(a, b) or self.check_concatenation(b, a)

    def check_concatenation(self, a: str, b: str) -> bool:
        left, right = 0, len(a) - 1
        while left < right and a[left] == b[right]:
            left += 1
            right -= 1
        if left >= right:
            return True
        return self.check_self_palindrome(a, left, right) or self.check_self_palindrome(b, left, right)

    @staticmethod
    def check_self_palindrome(a: str, left: int, right: int) -> bool:
        while left < right and a[left] == a[right]:
            left += 1
            right -= 1
        return left >= right


def main():
    # Example 1: Output: true
    # a = "x"
    # b = "y"

    # Example 2: Output: false
    # a = "xbdef"
    # b = "xecab"

    # Example 3: Output: true
    a = "ulacfd"
    b = "jizalu"

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.checkPalindromeFormation(a, b)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
