#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0792-Number-of-Matching-Subsequences.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-20
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0792 - (Medium) - Number of Matching Subsequences
https://leetcode.com/problems/number-of-matching-subsequences/

Description & Requirement:
    Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

    A subsequence of a string is a new string generated from the original string with some characters (can be none) 
    deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

Example 1:
    Input: s = "abcde", words = ["a","bb","acd","ace"]
    Output: 3
    Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:
    Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
    Output: 2

Constraints:
    1 <= s.length <= 5 * 10^4
    1 <= words.length <= 5000
    1 <= words[i].length <= 50
    s and words[i] consist of only lowercase English letters.
"""


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1 and s.isalpha() and s.islower()
        assert isinstance(words, list) and len(words) >= 1
        for word in words:
            assert isinstance(word, str) and len(word) >= 1 and word.isalpha() and word.islower()
        # main method: (hash bucket)
        return self._numMatchingSubseq(s, words)

    def _numMatchingSubseq(self, s: str, words: List[str]) -> int:
        assert isinstance(s, str) and len(s) >= 1 and s.isalpha() and s.islower()
        assert isinstance(words, list) and len(words) >= 1

        res = 0
        bucket = [[] for _ in range(26)]
        ord_a = ord('a')

        for word in words:
            it = iter(word)
            bucket[ord(next(it)) - ord_a].append(it)

        for ch in s:
            ch_idx = ord(ch) - ord_a
            old_bucket = bucket[ch_idx]
            bucket[ch_idx] = []

            while old_bucket:
                it = old_bucket.pop()
                it_next = next(it, None)
                if it_next:
                    bucket[ord(it_next) - ord('a')].append(it)
                else:
                    res += 1

        return res

    def _isSubsequence(self, sub: str, t: str) -> bool:
        # LC-0392-Is-Subsequence
        assert isinstance(sub, str) and isinstance(t, str)
        len_s = len(sub)
        len_t = len(t)
        if len_s == 0:
            return True  # always can find a empty string
        if len_t == 0:
            return False  # now len(s) > 0, so if len(t) == 0, then can't find s in t
        if len_s >= len_t:
            return sub == t

        # main method: (scan and greedily match each char of s in t)
        s_idx = 0
        t_idx = 0
        while s_idx < len_s and t_idx < len_t:
            if t[t_idx] == sub[s_idx]:  # match a char, move s_idx, check the next char of s
                s_idx += 1
            t_idx += 1

        return s_idx == len_s


def main():
    # Example 1: Output: 3
    # s = "abcde"
    # words = ["a", "bb", "acd", "ace"]

    # Example 2: Output: 2
    s = "dsahjpjauf"
    words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numMatchingSubseq(s, words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
