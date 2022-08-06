#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1408-String-Matching-in-an-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-06
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1408 - (Easy) - String Matching in an Array
https://leetcode.com/problems/string-matching-in-an-array/

Description & Requirement:
    Given an array of string words. Return all strings in words which is substring of another word in any order. 

    String words[i] is substring of words[j], 
    if can be obtained removing some characters to left and/or right side of words[j].

Example 1:
    Input: words = ["mass","as","hero","superhero"]
    Output: ["as","hero"]
    Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
        ["hero","as"] is also a valid answer.
Example 2:
    Input: words = ["leetcode","et","code"]
    Output: ["et","code"]
    Explanation: "et", "code" are substring of "leetcode".
Example 3:
    Input: words = ["blue","green","bu"]
    Output: []

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 30
    words[i] contains only lowercase English letters.
    It's guaranteed that words[i] will be unique.
"""


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        for word in words:
            assert isinstance(word, str) and len(word) >= 1
        # main method: (just match substring)
        return self._stringMatching(words)

    def _stringMatching(self, words: List[str]) -> List[str]:
        assert isinstance(words, list) and len(words) >= 1

        res = set()
        words = list(set(words))

        for i, word_1 in enumerate(words):
            for j, word_2 in enumerate(words):
                if j != i and word_1 in word_2:
                    res.add(word_1)
                    break

        return list(res)


def main():
    # Example 1: Output: ["as","hero"]
    words = ["mass", "as", "hero", "superhero"]

    # Example 2: Output: ["et","code"]
    # words = ["leetcode", "et", "code"]

    # Example 3: Output: []
    # words = ["blue", "green", "bu"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.stringMatching(words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
