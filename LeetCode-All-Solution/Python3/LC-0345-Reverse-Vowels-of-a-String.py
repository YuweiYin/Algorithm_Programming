#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0345-Reverse-Vowels-of-a-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-04
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0345 - (Easy) - Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/

Description & Requirement:
    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
    Input: s = "hello"
    Output: "holle"
Example 2:
    Input: s = "leetcode"
    Output: "leotcede"

Constraints:
    1 <= s.length <= 3 * 10^5
    s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (two pointers coming from leftmost and rightmost to meet each other)
        return self._reverseVowels(s)

    def _reverseVowels(self, s: str) -> str:
        assert isinstance(s, str) and len(s) >= 1

        vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        n = len(s)
        s = [ch for ch in s]
        i, j = 0, n - 1
        while i < j:
            while i < n and s[i] not in vowel_set:
                i += 1
            while j > 0 and s[j] not in vowel_set:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)


def main():
    # Example 1: Output: "holle"
    # s = "hello"

    # Example 2: Output: "leotcede"
    s = "leetcode"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reverseVowels(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
