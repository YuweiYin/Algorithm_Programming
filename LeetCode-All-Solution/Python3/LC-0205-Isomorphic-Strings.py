#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0205-Isomorphic-Strings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-30
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0205 - (Easy) - Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/

Description & Requirement:
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. 
    No two characters may map to the same character, but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: true
Example 2:
    Input: s = "foo", t = "bar"
    Output: false
Example 3:
    Input: s = "paper", t = "title"
    Output: true

Constraints:
    1 <= s.length <= 5 * 10^4
    t.length == s.length
    s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(t, str) and len(t) == len(s)
        # main method: (hash dict. bijection)
        return self._isIsomorphic(s, t)

    def _isIsomorphic(self, s: str, t: str) -> bool:
        """
        Runtime: 45 ms, faster than 77.80% of Python3 online submissions for Isomorphic Strings.
        Memory Usage: 14.2 MB, less than 89.48% of Python3 online submissions for Isomorphic Strings.
        """
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(t, str) and len(t) == len(s)
        len_s = len(s)

        hash_dict = dict({})
        for idx in range(len_s):
            ch_s = s[idx]
            ch_t = t[idx]
            if ch_s not in hash_dict:  # mapping
                hash_dict[ch_s] = ch_t
            else:
                if hash_dict[ch_s] != ch_t:  # conflict
                    return False

        # reversely check
        hash_dict = dict({})
        for idx in range(len_s):
            ch_s = s[idx]
            ch_t = t[idx]
            if ch_t not in hash_dict:  # mapping
                hash_dict[ch_t] = ch_s
            else:
                if hash_dict[ch_t] != ch_s:  # conflict
                    return False

        return True


def main():
    # Example 1: Output: true
    s = "egg"
    t = "add"

    # Example 2: Output: false
    # s = "foo"
    # t = "bar"

    # Example 3: Output: true
    # s = "paper"
    # t = "title"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isIsomorphic(s, t)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
