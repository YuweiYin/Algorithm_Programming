#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0916-Word-Subsets.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-30
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0916 - (Medium) - Word Subsets
https://leetcode.com/problems/word-subsets/

Description & Requirement:
    You are given two string arrays words1 and words2.

    A string b is a subset of string a if every letter in b occurs in a including multiplicity.

    For example, "wrr" is a subset of "warrior" but is not a subset of "world".
    A string a from words1 is universal if for every string b in words2, b is a subset of a.

    Return an array of all the universal strings in words1. You may return the answer in any order.

Example 1:
    Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
    Output: ["facebook","google","leetcode"]
Example 2:
    Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
    Output: ["apple","google","leetcode"]

Constraints:
    1 <= words1.length, words2.length <= 10^4
    1 <= words1[i].length, words2[i].length <= 10
    words1[i] and words2[i] consist only of lowercase English letters.
    All the strings of words1 are unique.
"""


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # exception case
        assert isinstance(words1, list) and len(words1) >= 1
        assert isinstance(words2, list) and len(words2) >= 1
        for word in words1:
            assert isinstance(word, str) and len(word) >= 1
        for word in words2:
            assert isinstance(word, str) and len(word) >= 1
        # main method: (count chars)
        return self._wordSubsets(words1, words2)

    def _wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        assert isinstance(words1, list) and len(words1) >= 1
        assert isinstance(words2, list) and len(words2) >= 1

        N = 26
        ord_a = ord("a")

        def __count(words) -> List[int]:
            counter = [0 for _ in range(N)]
            for w in words:
                assert isinstance(w, str)
                for c in w:
                    counter[ord(c) - ord_a] += 1
            return counter

        words2_merge = [0] * 26
        for word in words2:
            for idx, ch in enumerate(__count(word)):
                words2_merge[idx] = max(words2_merge[idx], ch)

        res = []
        for word in words1:
            if all(x >= y for x, y in zip(__count(word), words2_merge)):
                res.append(word)

        return res


def main():
    # Example 1: Output: ["facebook","google","leetcode"]
    # words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    # words2 = ["e", "o"]

    # Example 2: Output: ["apple","google","leetcode"]
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["l", "e"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.wordSubsets(words1, words2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
