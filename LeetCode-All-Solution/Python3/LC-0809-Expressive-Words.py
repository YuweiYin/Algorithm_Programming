#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0809-Expressive-Words.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-25
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0809 - (Medium) - Expressive Words
https://leetcode.com/problems/expressive-words/

Description & Requirement:
    Sometimes people repeat letters to represent extra feeling. For example:
        "hello" -> "heeellooo"
        "hi" -> "hiiii"

    In these strings like "heeellooo", we have groups of adjacent letters that are all the same: 
        "h", "eee", "ll", "ooo".

    You are given a string s and an array of query strings words. A query word is stretchy if 
    it can be made to be equal to s by any number of applications of the following extension operation: 
    choose a group consisting of characters c, and add some number of characters c to the group 
    so that the size of the group is three or more.

    For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", 
    but we cannot get "helloo" since the group "oo" has a size less than three. 
    Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". 
    If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: 
    query = "hello" -> "hellooo" -> "helllllooo" = s.

    Return the number of query strings that are stretchy.

Example 1:
    Input: s = "heeellooo", words = ["hello", "hi", "helo"]
    Output: 1
    Explanation: 
        We can extend "e" and "o" in the word "hello" to get "heeellooo".
        We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
Example 2:
    Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
    Output: 3

Constraints:
    1 <= s.length, words.length <= 100
    1 <= words[i].length <= 100
    s and words[i] consist of lowercase letters.
"""


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(words, list) and len(words) >= 1
        for word in words:
            assert isinstance(word, str) and len(word) >= 1
        # main method: (two pointers)
        return self._expressiveWords(s, words)

    def _expressiveWords(self, s: str, words: List[str]) -> int:
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(words, list) and len(words) >= 1

        def __expand(t: str) -> bool:
            i = j = 0
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    return False
                ch = s[i]
                cnt_i = 0
                while i < len(s) and s[i] == ch:
                    cnt_i += 1
                    i += 1
                cnt_j = 0
                while j < len(t) and t[j] == ch:
                    cnt_j += 1
                    j += 1

                if cnt_i < cnt_j:
                    return False
                if cnt_i != cnt_j and cnt_i < 3:
                    return False

            return i == len(s) and j == len(t)

        return sum(int(__expand(word)) for word in words)


def main():
    # Example 1: Output: 1
    # s = "heeellooo"
    # words = ["hello", "hi", "helo"]

    # Example 2: Output: 3
    s = "zzzzzyyyyy"
    words = ["zzyy", "zy", "zyy"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.expressiveWords(s, words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
