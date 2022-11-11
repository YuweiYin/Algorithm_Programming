#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1704-Determine-if-String-Halves-Are-Alike.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-11
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1704 - (Easy) - Determine if String Halves Are Alike
https://leetcode.com/problems/determine-if-string-halves-are-alike/

Description & Requirement:
    You are given a string s of even length. Split this string into two halves of equal lengths, 
    and let a be the first half and b be the second half.

    Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
    Notice that s contains uppercase and lowercase letters.

    Return true if a and b are alike. Otherwise, return false.

Example 1:
    Input: s = "book"
    Output: true
    Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:
    Input: s = "textbook"
    Output: false
    Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
        Notice that the vowel o is counted twice.

Constraints:
    2 <= s.length <= 1000
    s.length is even.
    s consists of uppercase and lowercase letters.
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # exception case
        assert isinstance(s, str) and len(s) >= 2 and len(s) & 0x01 == 0
        # main method: (hash set, count vowels)
        return self._halvesAreAlike(s)

    def _halvesAreAlike(self, s: str) -> bool:
        """
        Runtime: 56 ms, faster than 72.06% of Python3 online submissions for Determine if String Halves Are Alike.
        Memory Usage: 13.9 MB, less than 78.56% of Python3 online submissions for Determine if String Halves Are Alike.
        """
        assert isinstance(s, str) and len(s) >= 2 and len(s) & 0x01 == 0
        len_s = len(s)

        vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        cnt = 0
        for ch in s[: (len_s >> 1)]:
            if ch in vowel_set:
                cnt += 1

        for ch in s[(len_s >> 1):]:
            if ch in vowel_set:
                cnt -= 1

        return cnt == 0


def main():
    # Example 1: Output: true
    s = "book"

    # Example 2: Output: false
    # s = "textbook"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.halvesAreAlike(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
