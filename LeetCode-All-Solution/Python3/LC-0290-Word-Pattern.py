#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0290-Word-Pattern.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-17
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0290 - (Easy) - Word Pattern
https://leetcode.com/problems/word-pattern/

Description & Requirement:
    Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection 
    between a letter in pattern and a non-empty word in s.

Example 1:
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true
Example 2:
    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false
Example 3:
    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false

Constraints:
    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # exception case
        if not isinstance(pattern, str):
            return False  # Error input type
        if not isinstance(s, str):
            return False  # Error input type
        if pattern == '' and s == '':
            return True
        if len(pattern) <= 0 or len(s) <= 0:
            return False  # only one of pattern/s is '', can't match
        # main method: (double dict (bijection), per char/word matching)
        return self._wordPattern(pattern, s)

    def _wordPattern(self, pattern: str, s: str) -> bool:
        pattern = pattern.strip()
        s = s.strip()
        len_pattern = len(pattern)
        w_list = s.split()
        len_w_list = len(w_list)
        assert len_pattern > 0 and len_w_list > 0

        if len_pattern != len_w_list:
            return False

        dict_pw = dict({})  # key: pattern char, value: word in s
        dict_wp = dict({})  # key: word in s, value: pattern char

        for idx, cur_word in enumerate(w_list):
            cur_p = pattern[idx]
            # pattern -> word injection
            if cur_p in dict_pw:
                if dict_pw[cur_p] != cur_word:
                    return False
            else:
                dict_pw[cur_p] = cur_word
            # word -> pattern injection
            if cur_word in dict_wp:
                if dict_wp[cur_word] != cur_p:
                    return False
            else:
                dict_wp[cur_word] = cur_p

        return True


def main():
    # Example 1: Output: true
    # pattern = "abba"
    # s = "dog cat cat dog"

    # Example 2: Output: false
    # pattern = "abba"
    # s = "dog cat cat fish"

    # Example 3: Output: false
    pattern = "aaaa"
    s = "dog cat cat dog"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.wordPattern(pattern, s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
