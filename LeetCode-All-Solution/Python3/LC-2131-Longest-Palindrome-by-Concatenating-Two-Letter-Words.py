#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2131-Longest-Palindrome-by-Concatenating-Two-Letter-Words.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-03
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 2131 - (Medium) - Longest Palindrome by Concatenating Two Letter Words
https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

Description & Requirement:
    You are given an array of strings words. Each element of words consists of two lowercase English letters.

    Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. 
    Each element can be selected at most once.

    Return the length of the longest palindrome that you can create. 
    If it is impossible to create any palindrome, return 0.

    A palindrome is a string that reads the same forward and backward.

Example 1:
    Input: words = ["lc","cl","gg"]
    Output: 6
    Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
        Note that "clgglc" is another longest palindrome that can be created.
Example 2:
    Input: words = ["ab","ty","yt","lc","cl","ab"]
    Output: 8
    Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
        Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:
    Input: words = ["cc","ll","xx"]
    Output: 2
    Explanation: One longest palindrome is "cc", of length 2.
        Note that "ll" is another longest palindrome that can be created, and so is "xx".

Constraints:
    1 <= words.length <= 10^5
    words[i].length == 2
    words[i] consists of lowercase English letters.
"""


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        for word in words:
            assert isinstance(word, str) and word.islower() and len(word) == 2
        # main method: (deal with pairs "xy" and "yx")
        return self._longestPalindrome(words)

    def _longestPalindrome(self, words: List[str]) -> int:
        assert isinstance(words, list) and len(words) >= 1

        freq = collections.Counter(words)
        res = 0
        has_mid = False  # if there is a word in the middle
        for word, cnt in freq.items():
            rev = word[1] + word[0]
            if word == rev:
                if cnt & 0x01 == 1:
                    has_mid = True
                res += (cnt >> 1) << 2
            elif word > rev:
                res += min(freq[word], freq[rev]) << 2
        if has_mid:  # has the middle word "xx"
            res += 2

        return res


def main():
    # Example 1: Output: 6
    # words = ["lc", "cl", "gg"]

    # Example 2: Output: 8
    # words = ["ab", "ty", "yt", "lc", "cl", "ab"]

    # Example 3: Output: 2
    words = ["cc", "ll", "xx"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestPalindrome(words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
