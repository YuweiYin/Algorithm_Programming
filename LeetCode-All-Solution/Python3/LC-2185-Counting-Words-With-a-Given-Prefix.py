#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2185-Counting-Words-With-a-Given-Prefix.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-08
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2185 - (Easy) - Counting Words With a Given Prefix
https://leetcode.com/problems/counting-words-with-a-given-prefix/

Description & Requirement:
    You are given an array of strings words and a string pref.

    Return the number of strings in words that contain pref as a prefix.

    A prefix of a string s is any leading contiguous substring of s.

Example 1:
    Input: words = ["pay","attention","practice","attend"], pref = "at"
    Output: 2
    Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:
    Input: words = ["leetcode","win","loops","success"], pref = "code"
    Output: 0
    Explanation: There are no strings that contain "code" as a prefix.

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length, pref.length <= 100
    words[i] and pref consist of lowercase English letters.
"""


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(pref, str) and len(pref) >= 1
        # main method: (scan the list and match the prefix)
        return self._prefixCount(words, pref)

    def _prefixCount(self, words: List[str], pref: str) -> int:
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(pref, str) and len(pref) >= 1

        len_pre = len(pref)
        res = 0
        for word in words:
            if word[:len_pre] == pref:
                res += 1

        return res


def main():
    # Example 1: Output: 2
    # words = ["pay", "attention", "practice", "attend"]
    # pref = "at"

    # Example 2: Output: 0
    words = ["leetcode", "win", "loops", "success"]
    pref = "code"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.prefixCount(words, pref)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
