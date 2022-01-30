#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0884-Uncommon-Words-from-Two-Sentences.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-30
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0884 - (Easy) - Uncommon Words from Two Sentences
https://leetcode.com/problems/uncommon-words-from-two-sentences/

Description & Requirement:
    A sentence is a string of single-space separated words where each word consists only of lowercase letters.

    A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

    Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:
    Input: s1 = "this apple is sweet", s2 = "this apple is sour"
    Output: ["sweet","sour"]
Example 2:
    Input: s1 = "apple apple", s2 = "banana"
    Output: ["banana"]

Constraints:
    1 <= s1.length, s2.length <= 200
    s1 and s2 consist of lowercase English letters and spaces.
    s1 and s2 do not have leading or trailing spaces.
    All the words in s1 and s2 are separated by a single space.
"""


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # exception case
        assert isinstance(s1, str) and isinstance(s2, str)
        # main method: (hash dict statistics word frequency)
        return self._uncommonFromSentences(s1, s2)

    def _uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_list1 = s1.strip().split()
        word_list2 = s2.strip().split()

        word_freq = dict({})

        for word in (word_list1 + word_list2):
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1

        res_list = []
        for word, freq in word_freq.items():
            # a word is uncommon if it appears exactly once in one of the sentences,
            #     and does not appear in the other sentence.
            if freq == 1:
                res_list.append(word)

        return res_list


def main():
    # Example 1: Output: ["sweet","sour"]
    # s1 = "this apple is sweet"
    # s2 = "this apple is sour"

    # Example 2: Output: ["banana"]
    s1 = "apple apple"
    s2 = "banana"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.uncommonFromSentences(s1, s2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
