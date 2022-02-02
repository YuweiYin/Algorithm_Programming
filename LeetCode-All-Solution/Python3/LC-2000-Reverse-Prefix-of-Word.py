#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2000-Reverse-Prefix-of-Word.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-02
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 2000 - (Easy) - Reverse Prefix of Word
https://leetcode.com/problems/reverse-prefix-of-word/

Description & Requirement:
    Given a 0-indexed string word and a character ch, 
    reverse the segment of word that starts at index 0 and 
    ends at the index of the first occurrence of ch (inclusive). 
    If the character ch does not exist in word, do nothing.

    For example, if word = "abcdefd" and ch = "d", 
    then you should reverse the segment that starts at 0 and ends at 3 (inclusive). 
    The resulting string will be "dcbaefd".

    Return the resulting string.

Example 1:
    Input: word = "abcdefd", ch = "d"
    Output: "dcbaefd"
    Explanation: The first occurrence of "d" is at index 3. 
        Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
Example 2:
    Input: word = "xyxzxe", ch = "z"
    Output: "zxyxxe"
    Explanation: The first and only occurrence of "z" is at index 3.
        Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".
Example 3:
    Input: word = "abcd", ch = "z"
    Output: "abcd"
    Explanation: "z" does not exist in word.
        You should not do any reverse operation, the resulting string is "abcd".

Constraints:
    1 <= word.length <= 250
    word consists of lowercase English letters.
    ch is a lowercase English letter.
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # exception case
        if not isinstance(word, str) or len(word) <= 0:
            return ""  # Error word1 input type
        if not isinstance(ch, str) or len(ch) <= 0 or len(ch) > len(word):
            return word  # do nothing
        # main method: (just find the first ch in word, then reverse this part. if no ch, return original word)
        return self._reversePrefix(word, ch)

    def _reversePrefix(self, word: str, ch: str) -> str:
        len_word = len(word)
        len_ch = len(ch)
        assert len_word >= 1 and 1 <= len_ch <= len_word

        match_index = word.find(ch)  # find the first ch in word
        if match_index == -1:  # if no ch, return original word
            return word
        else:  # reverse this part, form the answer
            return word[0: match_index + len_ch][::-1] + word[match_index + len_ch:]


def main():
    # Example 1: Output: "dcbaefd"
    word = "abcdefd"
    ch = "d"

    # Example 2: Output: "zxyxxe"
    # word = "xyxzxe"
    # ch = "z"

    # Example 3: Output: "abcd"
    # word = "abcd"
    # ch = "z"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reversePrefix(word, ch)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
