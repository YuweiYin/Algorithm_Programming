#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0420-Strong-Password-Checker.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-02
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0420 - (Hard) - Strong Password Checker
https://leetcode.com/problems/strong-password-checker/

Description & Requirement:
    Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
    Input: s = "aba"
    Output: true
Example 2:
    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'c'.
Example 3:
    Input: s = "abc"
    Output: false

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (left/right two pointers)
        return self._validPalindrome(s)

    def _validPalindrome(self, s: str) -> bool:
        delete_change = [True]  # delete at most one character from s

        def __check_palin(left_idx: int, right_idx: int) -> bool:
            while left_idx < right_idx:
                if s[left_idx] == s[right_idx]:
                    left_idx += 1
                    right_idx -= 1
                else:
                    if delete_change[0]:
                        delete_change[0] = False
                        return __check_palin(left_idx + 1, right_idx) or __check_palin(left_idx, right_idx - 1)
                    else:  # no chance to delete char
                        return False
            return True

        return __check_palin(0, len(s) - 1)


def main():
    # Example 1: Output: true
    # s = "aba"

    # Example 2: Output: true
    s = "abca"

    # Example 3: Output: false
    # s = "abc"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.validPalindrome(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
