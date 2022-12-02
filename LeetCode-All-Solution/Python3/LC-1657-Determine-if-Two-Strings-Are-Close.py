#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1657-Determine-if-Two-Strings-Are-Close.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-02
=================================================================="""

import sys
import time
from collections import Counter
# from typing import List
# import itertools

"""
LeetCode - 1657 - (Medium) - Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close/

Description & Requirement:
    Two strings are considered close if you can attain one from the other using the following operations:
        Operation 1: Swap any two existing characters.
            For example, abcde -> aecdb
        Operation 2: Transform every occurrence of one existing character into another existing character, 
        and do the same with the other character.
            For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

    You can use the operations on either string as many times as necessary.

    Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:
    Input: word1 = "abc", word2 = "bca"
    Output: true
    Explanation: You can attain word2 from word1 in 2 operations.
        Apply Operation 1: "abc" -> "acb"
        Apply Operation 1: "acb" -> "bca"
Example 2:
    Input: word1 = "a", word2 = "aa"
    Output: false
    Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:
    Input: word1 = "cabbba", word2 = "abbccc"
    Output: true
    Explanation: You can attain word2 from word1 in 3 operations.
        Apply Operation 1: "cabbba" -> "caabbb"
        Apply Operation 2: "caabbb" -> "baaccc"
        Apply Operation 2: "baaccc" -> "abbccc"

Constraints:
    1 <= word1.length, word2.length <= 10^5
    word1 and word2 contain only lowercase English letters.
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # exception case
        assert isinstance(word1, str) and len(word1) >= 1 and word1.isalpha() and word1.lower()
        assert isinstance(word2, str) and len(word2) >= 1 and word2.isalpha() and word2.lower()
        # main method: (counter)
        return self._closeStrings(word1, word2)

    def _closeStrings(self, word1: str, word2: str) -> bool:
        """
        Runtime: 186 ms, faster than 84.80% of Python3 online submissions for Determine if Two Strings Are Close.
        Memory Usage: 15 MB, less than 97.60% of Python3 online submissions for Determine if Two Strings Are Close.
        """
        assert isinstance(word1, str) and len(word1) >= 1 and word1.isalpha() and word1.lower()
        assert isinstance(word2, str) and len(word2) >= 1 and word2.isalpha() and word2.lower()

        return sorted(Counter(word1).values()) == sorted(Counter(word2).values()) and set(word1) == set(word2)


def main():
    # Example 1: Output: true
    # word1 = "abc"
    # word2 = "bca"

    # Example 2: Output: false
    # word1 = "a"
    # word2 = "aa"

    # Example 3: Output: true
    word1 = "cabbba"
    word2 = "abbccc"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.closeStrings(word1, word2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
