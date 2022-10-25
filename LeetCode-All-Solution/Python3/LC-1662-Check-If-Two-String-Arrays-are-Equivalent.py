#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1662-Check-If-Two-String-Arrays-are-Equivalent.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-25
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1662 - (Easy) - Check If Two String Arrays are Equivalent
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

Description & Requirement:
    Given two string arrays word1 and word2, 
    return true if the two arrays represent the same string, and false otherwise.

    A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:
    Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
    Output: true
    Explanation:
        word1 represents string "ab" + "c" -> "abc"
        word2 represents string "a" + "bc" -> "abc"
        The strings are the same, so return true.
Example 2:
    Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
    Output: false
Example 3:
    Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
    Output: true

Constraints:
    1 <= word1.length, word2.length <= 10^3
    1 <= word1[i].length, word2[i].length <= 10^3
    1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
    word1[i] and word2[i] consist of lowercase letters.
"""


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # exception case
        assert isinstance(word1, list) and len(word1) >= 1
        assert isinstance(word2, list) and len(word2) >= 1
        # main method: (just check the two concatenated string is the same or not)
        return self._arrayStringsAreEqual(word1, word2)

    def _arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        Runtime: 24 ms, faster than 99.41% of Python3 submissions for Check If Two String Arrays are Equivalent.
        Memory Usage: 13.9 MB, less than 75.82% of Python3 submissions for Check If Two String Arrays are Equivalent.
        """
        assert isinstance(word1, list) and len(word1) >= 1
        assert isinstance(word2, list) and len(word2) >= 1

        return "".join(word1) == "".join(word2)


def main():
    # Example 1: Output: true
    # word1 = ["ab", "c"]
    # word2 = ["a", "bc"]

    # Example 2: Output: false
    # word1 = ["a", "cb"]
    # word2 = ["ab", "c"]

    # Example 3: Output: true
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.arrayStringsAreEqual(word1, word2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
