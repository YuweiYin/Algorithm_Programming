#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1170-Compare-Strings-by-Frequency-of-the-Smallest-Character.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-10
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1170 - (Medium) - Compare Strings by Frequency of the Smallest Character
https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

Description & Requirement:
    Let the function f(s) be the frequency of the lexicographically smallest character 
    in a non-empty string s. For example, if s = "dcce" then f(s) = 2 because 
    the lexicographically smallest character is 'c', which has a frequency of 2.

    You are given an array of strings words and another array of query strings queries. 
    For each query queries[i], count the number of words in words 
    such that f(queries[i]) < f(W) for each W in words.

    Return an integer array answer, where each answer[i] is the answer to the ith query.

Example 1:
    Input: queries = ["cbd"], words = ["zaaaz"]
    Output: [1]
    Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:
    Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
    Output: [1,2]
    Explanation: On the first query only f("bbb") < f("aaaa"). 
        On the second query both f("aaa") and f("aaaa") are both > f("cc").

Constraints:
    1 <= queries.length <= 2000
    1 <= words.length <= 2000
    1 <= queries[i].length, words[i].length <= 10
    queries[i][j], words[i][j] consist of lowercase English letters.
"""


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # exception case
        assert isinstance(queries, list) and len(queries) >= 1
        assert isinstance(words, list) and len(words) >= 1
        # main method: (suffix sum)
        return self._numSmallerByFrequency(queries, words)

    def _numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        assert isinstance(queries, list) and len(queries) >= 1
        assert isinstance(words, list) and len(words) >= 1

        def __count(s: str) -> int:
            cnt = 0
            ch = "z"
            for cur_ch in s:
                if cur_ch < ch:
                    ch = cur_ch
                    cnt = 1
                elif cur_ch == ch:
                    cnt += 1
            return cnt

        count = [0] * 12
        for word in words:
            count[__count(word)] += 1
        for i in range(9, 0, -1):
            count[i] += count[i + 1]

        res = []
        for query in queries:
            res.append(count[__count(query) + 1])

        return res


def main():
    # Example 1: Output: [1]
    # queries = ["cbd"]
    # words = ["zaaaz"]

    # Example 2: Output: [1,2]
    queries = ["bbb", "cc"]
    words = ["a", "aa", "aaa", "aaaa"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numSmallerByFrequency(queries, words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
