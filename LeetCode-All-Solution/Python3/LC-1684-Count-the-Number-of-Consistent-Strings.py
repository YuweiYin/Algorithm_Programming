#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1684-Count-the-Number-of-Consistent-Strings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-08
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1684 - (Easy) - Count the Number of Consistent Strings
https://leetcode.com/problems/count-the-number-of-consistent-strings/

Description & Requirement:
    You are given a string allowed consisting of distinct characters and an array of strings words. 
    A string is consistent if all characters in the string appear in the string allowed.

    Return the number of consistent strings in the array words.

Example 1:
    Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
    Output: 2
    Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:
    Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
    Output: 7
    Explanation: All strings are consistent.
Example 3:
    Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
    Output: 4
    Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

Constraints:
    1 <= words.length <= 10^4
    1 <= allowed.length <= 26
    1 <= words[i].length <= 10
    The characters in allowed are distinct.
    words[i] and allowed contain only lowercase English letters.
"""


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # exception case
        assert isinstance(allowed, str) and len(allowed) >= 1
        assert isinstance(words, list) and len(words) >= 1
        for word in words:
            assert isinstance(word, str) and len(word) >= 1
        # main method: (hash set)
        return self._countConsistentStrings(allowed, words)

    def _countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        assert isinstance(allowed, str) and len(allowed) >= 1
        assert isinstance(words, list) and len(words) >= 1

        res = 0
        allowed_set = set([ch for ch in allowed])
        for word in words:
            is_allowed = True
            for ch in word:
                if ch not in allowed_set:
                    is_allowed = False
                    break
            if is_allowed:
                res += 1

        return res


def main():
    # Example 1: Output: 2
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]

    # Example 2: Output: 7
    # allowed = "abc"
    # words = ["a", "b", "c", "ab", "ac", "bc", "abc"]

    # Example 3: Output: 4
    # allowed = "cad"
    # words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countConsistentStrings(allowed, words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
