#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1668-Maximum-Repeating-Substring.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-03
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1668 - (Easy) - Maximum Repeating Substring
https://leetcode.com/problems/maximum-repeating-substring/

Description & Requirement:
    For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. 
    The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. 
    If word is not a substring of sequence, word's maximum k-repeating value is 0.

    Given strings sequence and word, return the maximum k-repeating value of word in sequence.

Example 1:
    Input: sequence = "ababc", word = "ab"
    Output: 2
    Explanation: "abab" is a substring in "ababc".
Example 2:
    Input: sequence = "ababc", word = "ba"
    Output: 1
    Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
Example 3:
    Input: sequence = "ababc", word = "ac"
    Output: 0
    Explanation: "ac" is not a substring in "ababc".

Constraints:
    1 <= sequence.length <= 100
    1 <= word.length <= 100
    sequence and word contains only lowercase English letters.
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # exception case
        assert isinstance(sequence, str) and sequence.islower() and len(sequence) >= 1
        assert isinstance(word, str) and word.islower() and len(word) >= 1
        # main method: (KMP + Dynamic Programming)
        return self._maxRepeating(sequence, word)

    def _maxRepeating(self, sequence: str, word: str) -> int:
        assert isinstance(sequence, str) and sequence.islower() and len(sequence) >= 1
        assert isinstance(word, str) and word.islower() and len(word) >= 1

        len_seq = len(sequence)
        len_w = len(word)

        if len_seq < len_w:
            return 0

        fail = [-1 for _ in range(len_w)]
        for i in range(1, len_w):
            j = fail[i - 1]
            while j != -1 and word[j + 1] != word[i]:
                j = fail[j]
            if word[j + 1] == word[i]:
                fail[i] = j + 1

        dp = [0 for _ in range(len_seq)]
        j = -1
        for i in range(len_seq):
            while j != -1 and word[j + 1] != sequence[i]:
                j = fail[j]
            if word[j + 1] == sequence[i]:
                j += 1
                if j == len_w - 1:
                    dp[i] = (0 if i == len_w - 1 else dp[i - len_w]) + 1
                    j = fail[j]

        return max(dp)


def main():
    # Example 1: Output: 2
    # sequence = "ababc"
    # word = "ab"

    # Example 2: Output: 1
    # sequence = "ababc"
    # word = "ba"

    # Example 3: Output: 0
    # sequence = "ababc"
    # word = "ac"

    # Example 4: Output: 5
    sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    word = "aaaba"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxRepeating(sequence, word)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
