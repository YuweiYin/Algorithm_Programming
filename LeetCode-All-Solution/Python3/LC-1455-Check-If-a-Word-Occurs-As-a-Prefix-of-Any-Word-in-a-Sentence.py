#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1455-Check-If-a-Word-Occurs-As-a-Prefix-of-Any-Word-in-a-Sentence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-21
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1455 - (Easy) - Check If a Word Occurs As a Prefix of Any Word in a Sentence
https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

Description & Requirement:
    Given a sentence that consists of some words separated by a single space, and a searchWord, 
    check if searchWord is a prefix of any word in sentence.

    Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. 
    If searchWord is a prefix of more than one word, return the index of the first word (minimum index). 
    If there is no such word return -1.

    A prefix of a string s is any leading contiguous substring of s.

Example 1:
    Input: sentence = "i love eating burger", searchWord = "burg"
    Output: 4
    Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
Example 2:
    Input: sentence = "this problem is an easy problem", searchWord = "pro"
    Output: 2
    Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, 
        but we return 2 as it's the minimal index.
Example 3:
    Input: sentence = "i am tired", searchWord = "you"
    Output: -1
    Explanation: "you" is not a prefix of any word in the sentence.

Constraints:
    1 <= sentence.length <= 100
    1 <= searchWord.length <= 10
    sentence consists of lowercase English letters and spaces.
    searchWord consists of lowercase English letters.
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # exception case
        assert isinstance(sentence, str) and len(sentence) >= 1
        assert isinstance(searchWord, str) and len(sentence) >= 1 and searchWord.islower()
        # main method: (scan each word from left to right in the sentence)
        return self._isPrefixOfWord(sentence, searchWord)

    def _isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        assert isinstance(sentence, str) and len(sentence) >= 1
        assert isinstance(searchWord, str) and len(sentence) >= 1 and searchWord.islower()
        len_sw = len(searchWord)

        for idx, word in enumerate(sentence.strip().split()):
            if isinstance(word, str) and word[:len_sw] == searchWord:
                return idx + 1  # 1-indexed

        return -1


def main():
    # Example 1: Output: 4
    # sentence = "i love eating burger"
    # searchWord = "burg"

    # Example 2: Output: 2
    # sentence = "this problem is an easy problem"
    # searchWord = "pro"

    # Example 3: Output: -1
    sentence = "i am tired"
    searchWord = "you"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isPrefixOfWord(sentence, searchWord)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
