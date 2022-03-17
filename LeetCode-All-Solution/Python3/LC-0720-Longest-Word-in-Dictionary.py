#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0720-Longest-Word-in-Dictionary.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-17
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0720 - (Medium) - Longest Word in Dictionary
https://leetcode.com/problems/longest-word-in-dictionary/

Description & Requirement:
    Given an array of strings words representing an English Dictionary, 
    return the longest word in words that can be built one character at a time by other words in words.

    If there is more than one possible answer, return the longest word with the smallest lexicographical order. 
    If there is no answer, return the empty string.

Example 1:
    Input: words = ["w","wo","wor","worl","world"]
    Output: "world"
    Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
    Input: words = ["a","banana","app","appl","ap","apply","apple"]
    Output: "apple"
    Explanation: Both "apply" and "apple" can be built from other words in the dictionary. 
        However, "apple" is lexicographically smaller than "apply".

Constraints:
    1 <= words.length <= 1000
    1 <= words[i].length <= 30
    words[i] consists of lowercase English letters.
"""


class Solution:
    def longestWord(self, words: List[str]) -> str:
        # exception case
        assert isinstance(words, list) and len(words) > 0
        for word in words:
            assert isinstance(word, str) and len(word) > 0
        # main method: (sort word list, from left to right, consider if the current word can be built)
        return self._longestWord(words)

    def _longestWord(self, words: List[str]) -> str:
        """
        Runtime: 102 ms, faster than 85.73% of Python3 online submissions for Longest Word in Dictionary.
        Memory Usage: 14.5 MB, less than 76.83% of Python3 online submissions for Longest Word in Dictionary.
        """
        len_words = len(words)
        assert len_words > 0

        words.sort()
        can_build = dict({})
        for word in words:
            if word not in can_build:
                can_build[word] = False

        max_len = 1
        for word in words:
            if len(word) == 1:  # len == 1, can be built
                can_build[word] = True
            else:
                pre_word = word[:-1]
                if pre_word in can_build and can_build[pre_word]:  # pre_word exists and it can be built
                    can_build[word] = True
                    max_len = max(max_len, len(word))  # record the max length

        possible_result = []
        for word, build_flag in can_build.items():
            if build_flag and len(word) == max_len:
                possible_result.append(word)

        # return the longest word with the smallest lexicographical order.
        return min(possible_result) if len(possible_result) > 0 else ""


def main():
    # Example 1: Output: "world"
    # words = ["w", "wo", "wor", "worl", "world"]

    # Example 2: Output: "apple"
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestWord(words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
