#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2451-Odd-String-Difference.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-25
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2451 - (Medium) - Odd String Difference
https://leetcode.com/problems/odd-string-difference/

Description & Requirement:
    You are given an array of equal-length strings words. Assume that the length of each string is n.

    Each string words[i] can be converted into a difference integer array difference[i] of length n - 1 
    where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the difference 
    between two letters is the difference between their positions in the alphabet i.e. 
    the position of 'a' is 0, 'b' is 1, and 'z' is 25.

        For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].

    All the strings in words have the same difference integer array, except one. You should find that string.

    Return the string in words that has different difference integer array.

Example 1:
    Input: words = ["adc","wzy","abc"]
    Output: "abc"
    Explanation: 
        - The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
        - The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
        - The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1]. 
        The odd array out is [1, 1], so we return the corresponding string, "abc".
Example 2:
    Input: words = ["aaa","bob","ccc","ddd"]
    Output: "bob"
    Explanation: All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].

Constraints:
    3 <= words.length <= 100
    n == words[i].length
    2 <= n <= 20
    words[i] consists of lowercase English letters.
"""


class Solution:
    def oddString(self, words: List[str]) -> str:
        # exception case
        assert isinstance(words, list) and len(words) >= 3
        # main method: (scan)
        return self._oddString(words)

    def _oddString(self, words: List[str]) -> str:
        assert isinstance(words, list) and len(words) >= 3

        def __get_diff(word):
            diff = [0] * (len(word) - 1)
            for i in range(len(word) - 1):
                diff[i] = ord(word[i + 1]) - ord(word[i])
            return diff

        diff0 = __get_diff(words[0])
        diff1 = __get_diff(words[1])
        if diff0 == diff1:
            for i in range(2, len(words)):
                if diff0 != __get_diff(words[i]):
                    return words[i]

        return words[1] if diff0 == __get_diff(words[2]) else words[0]


def main():
    # Example 1: Output: "abc"
    words = ["adc", "wzy", "abc"]

    # Example 2: Output: "bob"
    # words = ["aaa", "bob", "ccc", "ddd"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.oddString(words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
