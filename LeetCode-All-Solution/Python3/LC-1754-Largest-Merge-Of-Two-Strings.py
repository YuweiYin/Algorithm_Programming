#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1754-Largest-Merge-Of-Two-Strings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-24
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1754 - (Medium) - Largest Merge Of Two Strings
https://leetcode.com/problems/largest-merge-of-two-strings/

Description & Requirement:
    You are given two strings word1 and word2. You want to construct a string merge in the following way: 
    while either word1 or word2 are non-empty, choose one of the following options:
        If word1 is non-empty, append the first character in word1 to merge and delete it from word1.
            For example, if word1 = "abc" and merge = "dv", 
            then after choosing this operation, word1 = "bc" and merge = "dva".
        If word2 is non-empty, append the first character in word2 to merge and delete it from word2.
            For example, if word2 = "abc" and merge = "", 
            then after choosing this operation, word2 = "bc" and merge = "a".

    Return the lexicographically largest merge you can construct.

    A string a is lexicographically larger than a string b (of the same length) if in the first position 
    where a and b differ, a has a character strictly larger than the corresponding character in b. 
    For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is 
    at the fourth character, and d is greater than c.

Example 1:
    Input: word1 = "cabaa", word2 = "bcaaa"
    Output: "cbcabaaaaa"
    Explanation: One way to get the lexicographically largest merge is:
        - Take from word1: merge = "c", word1 = "abaa", word2 = "bcaaa"
        - Take from word2: merge = "cb", word1 = "abaa", word2 = "caaa"
        - Take from word2: merge = "cbc", word1 = "abaa", word2 = "aaa"
        - Take from word1: merge = "cbca", word1 = "baa", word2 = "aaa"
        - Take from word1: merge = "cbcab", word1 = "aa", word2 = "aaa"
        - Append the remaining 5 a's from word1 and word2 at the end of merge.
Example 2:
    Input: word1 = "abcabc", word2 = "abdcaba"
    Output: "abdcabcabcaba"

Constraints:
    1 <= word1.length, word2.length <= 3000
    word1 and word2 consist only of lowercase English letters.
"""


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        # exception case
        assert isinstance(word1, str) and len(word1) >= 1 and word1.lower()
        assert isinstance(word2, str) and len(word2) >= 1 and word2.lower()
        # main method: (greedy)
        return self._largestMerge(word1, word2)

    def _largestMerge(self, word1: str, word2: str) -> str:
        """
        Time: beats 92.42%; Space: beats 91.67%
        """
        assert isinstance(word1, str) and len(word1) >= 1 and word1.lower()
        assert isinstance(word2, str) and len(word2) >= 1 and word2.lower()

        len_1, len_2 = len(word1), len(word2)

        merge_word = []
        idx_1, idx_2 = 0, 0
        while idx_1 < len_1 or idx_2 < len_2:
            if idx_1 < len_1 and word1[idx_1:] > word2[idx_2:]:
                merge_word.append(word1[idx_1])
                idx_1 += 1
            else:
                merge_word.append(word2[idx_2])
                idx_2 += 1

        return "".join(merge_word)


def main():
    # Example 1: Output: "cbcabaaaaa"
    # word1, word2 = "cabaa", "bcaaa"

    # Example 2: Output: "abdcabcabcaba"
    word1, word2 = "abcabc", "abdcaba"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largestMerge(word1, word2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
