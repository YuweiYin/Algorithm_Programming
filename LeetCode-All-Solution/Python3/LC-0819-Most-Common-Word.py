#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0819-Most-Common-Word.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-17
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0819 - (Easy) - Most Common Word
https://leetcode.com/problems/most-common-word/

Description & Requirement:
    Given a string paragraph and a string array of the banned words banned, 
    return the most frequent word that is not banned. 
    It is guaranteed there is at least one word that is not banned, and that the answer is unique.

    The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Example 1:
    Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
    Output: "ball"
    Explanation: 
        "hit" occurs 3 times, but it is a banned word.
        "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
        Note that words in the paragraph are not case sensitive,
        that punctuation is ignored (even if adjacent to words, such as "ball,"), 
        and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:
    Input: paragraph = "a.", banned = []
    Output: "a"

Constraints:
    1 <= paragraph.length <= 1000
    paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
    0 <= banned.length <= 100
    1 <= banned[i].length <= 10
    banned[i] consists of only lowercase English letters.
"""


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # exception case
        assert isinstance(paragraph, str) and len(paragraph) >= 1
        assert isinstance(banned, list)
        # main method: (hash dict, record counter)
        return self._mostCommonWord(paragraph, banned)

    def _mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
        # for symbol in ["!", "?", "'", ",", ";", "."]:
        #     paragraph = paragraph.replace(symbol, " ")
        symbol_set = {"!", "?", "'", ",", ";", "."}
        new_paragraph = ""
        for ch in paragraph:
            if ch in symbol_set:
                new_paragraph += " "
            else:
                new_paragraph += ch
        word_list = new_paragraph.strip().split()

        banned_set = set()
        for ban_word in banned:
            banned_set.add(ban_word.lower())
        banned_set.add(" ")

        word_counter = dict({})
        for word in word_list:
            word = word.lower()
            if word not in banned_set:
                if word not in word_counter:
                    word_counter[word] = 1
                else:
                    word_counter[word] += 1

        max_counter = max(list(word_counter.values()))
        for k, v in word_counter.items():
            if v == max_counter:
                return k

        return word_list[0] if len(word_list) > 0 else ""  # won't reach here


def main():
    # Example 1: Output: "ball"
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    # Example 2: Output: "a"
    # paragraph = "a."
    # banned = []

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.mostCommonWord(paragraph, banned)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
