#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1768-Merge-Strings-Alternately.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-23
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1768 - (Easy) - Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/

Description & Requirement:
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
    starting with word1. If a string is longer than the other, 
    append the additional letters onto the end of the merged string.

    Return the merged string.

Example 1:
    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: The merged string will be merged as so:
        word1:  a   b   c
        word2:    p   q   r
        merged: a p b q c r
Example 2:
    Input: word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"
    Explanation: Notice that as word2 is longer, "rs" is appended to the end.
        word1:  a   b 
        word2:    p   q   r   s
        merged: a p b q   r   s
Example 3:
    Input: word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    Explanation: Notice that as word1 is longer, "cd" is appended to the end.
        word1:  a   b   c   d
        word2:    p   q 
        merged: a p b q c   d

Constraints:
    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # exception case
        assert isinstance(word1, str) and len(word1) >= 1
        assert isinstance(word2, str) and len(word2) >= 1
        # main method: (deal with the alternating part first, and then append the rest part of the longer string)
        return self._mergeAlternately(word1, word2)

    def _mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Runtime: 67 ms, faster than 14.21% of Python3 online submissions for Merge Strings Alternately.
        Memory Usage: 13.8 MB, less than 99.05% of Python3 online submissions for Merge Strings Alternately.
        """
        assert isinstance(word1, str) and len(word1) >= 1
        assert isinstance(word2, str) and len(word2) >= 1

        res = ""
        idx = 0
        bound = min(len(word1), len(word2))
        while idx < bound:
            res += word1[idx] + word2[idx]
            idx += 1

        if len(word1) > len(word2):
            res += word1[idx:]
        if len(word2) > len(word1):
            res += word2[idx:]

        return res


def main():
    # Example 1: Output: "apbqcr"
    # word1 = "abc"
    # word2 = "pqr"

    # Example 2: Output: "apbqrs"
    # word1 = "ab"
    # word2 = "pqrs"

    # Example 3: Output: "apbqcd"
    word1 = "abcd"
    word2 = "pq"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.mergeAlternately(word1, word2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
