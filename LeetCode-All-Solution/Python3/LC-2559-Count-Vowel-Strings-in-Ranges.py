#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2559-Count-Vowel-Strings-in-Ranges.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-02
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2559 - (Medium) - Count Vowel Strings in Ranges
https://leetcode.com/problems/count-vowel-strings-in-ranges/

Description & Requirement:
    You are given a 0-indexed array of strings words and a 2D array of integers queries.

    Each query queries[i] = [li, ri] asks us to find the number of strings present 
    in the range li to ri (both inclusive) of words that start and end with a vowel.

    Return an array ans of size queries.length, where ans[i] is the answer to the i-th query.

    Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
    Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
    Output: [2,3,0]
    Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
        The answer to the query [0,2] is 2 (strings "aba" and "ece").
        to query [1,4] is 3 (strings "ece", "aa", "e").
        to query [1,1] is 0.
        We return [2,3,0].
Example 2:
    Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
    Output: [3,2,1]
    Explanation: Every string satisfies the conditions, so we return [3,2,1].

Constraints:
    1 <= words.length <= 10^5
    1 <= words[i].length <= 40
    words[i] consists only of lowercase English letters.
    sum(words[i].length) <= 3 * 10^5
    1 <= queries.length <= 10^5
    0 <= li <= ri < words.length
"""


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(queries, list) and len(queries) >= 1
        # main method: (prefix sum)
        return self._vowelStrings(words, queries)

    def _vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(queries, list) and len(queries) >= 1

        def __is_vowel_letter(c):
            return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"

        def __is_vowel_string(word):
            return __is_vowel_letter(word[0]) and __is_vowel_letter(word[-1])

        n = len(words)
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            value = 1 if __is_vowel_string(words[i]) else 0
            prefix_sums[i + 1] = prefix_sums[i] + value

        res = []
        for i in range(len(queries)):
            start, end = queries[i]
            res.append(prefix_sums[end + 1] - prefix_sums[start])

        return res


def main():
    # Example 1: Output: [2,3,0]
    words = ["aba", "bcb", "ece", "aa", "e"]
    queries = [[0, 2], [1, 4], [1, 1]]

    # Example 2: Output: [3,2,1]
    # words = ["a", "e", "i"]
    # queries = [[0, 2], [0, 1], [2, 2]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.vowelStrings(words, queries)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
