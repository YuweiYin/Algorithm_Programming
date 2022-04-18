#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0030-Substring-with-Concatenation-of-All-Words.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-18
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0030 - (Hard) - Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/

Description & Requirement:
    You are given a string s and an array of strings words of the same length. 
    Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, 
    in any order, and without any intervening characters.

    You can return the answer in any order.

Example 1:
    Input: s = "barfoothefoobarman", words = ["foo","bar"]
    Output: [0,9]
    Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
        The output order does not matter, returning [9,0] is fine too.
Example 2:
    Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
    Output: []
Example 3:
    Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    Output: [6,9,12]

Constraints:
    1 <= s.length <= 10^4
    s consists of lower-case English letters.
    1 <= words.length <= 5000
    1 <= words[i].length <= 30
    words[i] consists of lower-case English letters.
"""


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # exception case
        assert isinstance(s, str) and len(s) >= 1 and s.islower()
        assert isinstance(words, list) and len(words) >= 1
        len_word = len(words[0])
        for word in words:
            assert isinstance(word, str) and len(word) == len_word and word.islower()
        # main method: (sliding window)
        return self._findSubstring(s, words)

    def _findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_s = len(s)
        assert len_s >= 1 and len(words) >= 1
        len_word = len(words[0])  # the length of a single word
        assert len_word >= 1
        len_substr = len_word * len(words)  # the length of the target sub string

        if len_s < len_substr:
            return []

        word_dict = dict({})  # key: word; value: the index of word in list words
        for w_idx, word in enumerate(words):
            if word not in word_dict:
                word_dict[word] = [w_idx]  # may have duplicated words in list words
            else:
                word_dict[word].append(w_idx)

        res = []
        for left_idx in range(len_s - len_substr + 1):
            words_used = [False for _ in range(len(words))]
            right_idx = left_idx + len_substr
            idx = left_idx
            match = True
            while idx < right_idx:
                cur_word = s[idx: idx + len_word]
                if cur_word in word_dict:
                    has_set_true = False
                    for w_idx in word_dict[cur_word]:
                        if not words_used[w_idx]:  # if False, set True
                            words_used[w_idx] = True
                            has_set_true = True
                            break
                    if not has_set_true:  # can't set any bool flag as True, can't match, break
                        match = False
                        break
                else:  # cur_word itself doesn't match
                    match = False
                    break
                idx += len_word
            if match:
                res.append(left_idx)

        return res


def main():
    # Example 1: Output: [0,9]
    # s = "barfoothefoobarman"
    # words = ["foo", "bar"]

    # Example 2: Output: []
    # s = "wordgoodgoodgoodbestword"
    # words = ["word", "good", "best", "word"]

    # Example 3: Output: [6,9,12]
    # s = "barfoofoobarthefoobarman"
    # words = ["bar", "foo", "the"]

    # Example 4: Output: [8]
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findSubstring(s, words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
