#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0824-Goat-Latin.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-21
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0824 - (Easy) - Goat Latin
https://leetcode.com/problems/goat-latin/

Description & Requirement:
    You are given a string sentence that consist of words separated by spaces. 
    Each word consists of lowercase and uppercase letters only.

    We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) 
    The rules of Goat Latin are as follows:
        If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
            For example, the word "apple" becomes "applema".
        If a word begins with a consonant (i.e., not a vowel), 
        remove the first letter and append it to the end, then add "ma".
            For example, the word "goat" becomes "oatgma".
        Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
            For example, the first word gets "a" added to the end, 
            the second word gets "aa" added to the end, and so on.

    Return the final sentence representing the conversion from sentence to Goat Latin.

Example 1:
    Input: sentence = "I speak Goat Latin"
    Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:
    Input: sentence = "The quick brown fox jumped over the lazy dog"
    Output: 
        "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

Constraints:
    1 <= sentence.length <= 150
    sentence consists of English letters and spaces.
    sentence has no leading or trailing spaces.
    All the words in sentence are separated by a single space.
"""


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # exception case
        assert isinstance(sentence, str) and len(sentence) >= 1
        # main method: (deal with each word)
        return self._toGoatLatin(sentence)

    def _toGoatLatin(self, sentence: str) -> str:
        assert isinstance(sentence, str) and len(sentence) >= 1

        vowel = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        word_list = sentence.strip().split()
        for idx, word in enumerate(word_list):
            assert isinstance(word, str) and len(word) >= 1
            if word[0] in vowel:
                goat_latin_word = word + "ma"
            else:
                goat_latin_word = word[1:] + word[0] + "ma"
            goat_latin_word += "a" * (idx + 1)
            word_list[idx] = goat_latin_word
        return " ".join(word_list)


def main():
    # Example 1: Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    sentence = "I speak Goat Latin"

    # Example 2: Output:
    #    "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    # sentence = "The quick brown fox jumped over the lazy dog"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.toGoatLatin(sentence)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
