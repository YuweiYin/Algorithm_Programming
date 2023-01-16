#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1813-Sentence-Similarity-III.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-16
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1813 - (Medium) - Sentence Similarity III
https://leetcode.com/problems/sentence-similarity-iii/

Description & Requirement:
    A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
    For example, "Hello World", "HELLO", "hello world hello world" are all sentences. 
    Words consist of only uppercase and lowercase English letters.

    Two sentences sentence1 and sentence2 are similar if it is possible to insert an arbitrary sentence 
    (possibly empty) inside one of these sentences such that the two sentences become equal. 
    For example, sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" can be made equal 
    by inserting "my name is" between "Hello" and "Jane" in sentence2.

    Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. 
    Otherwise, return false.

Example 1:
    Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
    Output: true
    Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
Example 2:
    Input: sentence1 = "of", sentence2 = "A lot of words"
    Output: false
    Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.
Example 3:
    Input: sentence1 = "Eating right now", sentence2 = "Eating"
    Output: true
    Explanation: sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.

Constraints:
    1 <= sentence1.length, sentence2.length <= 100
    sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
    The words in sentence1 and sentence2 are separated by a single space.
"""


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # exception case
        assert isinstance(sentence1, str) and len(sentence1) >= 1
        assert isinstance(sentence2, str) and len(sentence2) >= 1
        # main method: (two pointers)
        return self._areSentencesSimilar(sentence1, sentence2)

    def _areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        Time: beats 85.59%; Space: beats 81.8%
        """
        assert isinstance(sentence1, str) and len(sentence1) >= 1
        assert isinstance(sentence2, str) and len(sentence2) >= 1

        words1 = sentence1.split()
        words2 = sentence2.split()

        i, j = 0, 0
        while i < len(words1) and i < len(words2) and words1[i] == words2[i]:
            i += 1

        while j < len(words1) - i and j < len(words2) - i and words1[-j - 1] == words2[-j - 1]:
            j += 1

        return i + j == min(len(words1), len(words2))


def main():
    # Example 1: Output: true
    # sentence1 = "My name is Haley"
    # sentence2 = "My Haley"

    # Example 2: Output: false
    # sentence1 = "of"
    # sentence2 = "A lot of words"

    # Example 3: Output: true
    sentence1 = "Eating right now"
    sentence2 = "Eating"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.areSentencesSimilar(sentence1, sentence2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
