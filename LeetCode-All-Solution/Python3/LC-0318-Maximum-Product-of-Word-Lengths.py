#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0318-Maximum-Product-of-Word-Lengths.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-29
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0318 - (Medium) - Maximum Product of Word Lengths
https://leetcode.com/problems/maximum-product-of-word-lengths/

Description & Requirement:
    Given a string array words, return the maximum value of length(word[i]) * length(word[j]) 
    where the two words do not share common letters. 
    If no such two words exist, return 0.

Example 1:
    Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    Output: 16
    Explanation: The two words can be "abcw", "xtfn".
Example 2:
    Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
    Output: 4
    Explanation: The two words can be "ab", "cd".
Example 3:
    Input: words = ["a","aa","aaa","aaaa"]
    Output: 0
    Explanation: No such pair of words.

Constraints:
    2 <= words.length <= 1000
    1 <= words[i].length <= 1000
    words[i] consists only of lowercase English letters.
"""


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # exception case
        assert isinstance(words, list) and len(words) >= 2
        for word in words:
            assert isinstance(word, str) and len(word) >= 1 and word.islower()
        # main method: (represent each word as 26-bit integer, 2 loop scan)
        return self._maxProduct(words)

    def _maxProduct(self, words: List[str]) -> int:
        """
        Runtime: 585 ms, faster than 76.27% of Python3 online submissions for Maximum Product of Word Lengths.
        Memory Usage: 14.6 MB, less than 29.91% of Python3 online submissions for Maximum Product of Word Lengths.
        """
        assert isinstance(words, list) and len(words) >= 2
        len_words = len(words)

        ord_a = ord("a")
        words_bin = []
        for word in words:
            word_bin = 0
            for ch in word:
                word_bin |= 1 << (ord(ch) - ord_a)  # record each letter
            words_bin.append((len(word), word_bin))

        res = 0
        words_bin.sort(reverse=True)
        for i in range(len_words):
            for j in range(i + 1, len_words):
                if words_bin[i][1] & words_bin[j][1] == 0:  # no overlapping letters
                    res = max(res, words_bin[i][0] * words_bin[j][0])

        return res


def main():
    # Example 1: Output: 16
    # words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]

    # Example 2: Output: 4
    # words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]

    # Example 3: Output: 0
    words = ["a", "aa", "aaa", "aaaa"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxProduct(words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
