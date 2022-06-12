#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0890-Find-and-Replace-Pattern.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-12
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0890 - (Medium) - Find and Replace Pattern
https://leetcode.com/problems/find-and-replace-pattern/

Description & Requirement:
    Given a list of strings words and a string pattern, return a list of words[i] that match pattern. 
    You may return the answer in any order.

    A word matches the pattern if there exists a permutation of letters p so that 
    after replacing every letter x in the pattern with p(x), we get the desired word.

    Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, 
    and no two letters map to the same letter.

Example 1:
    Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
    Output: ["mee","aqq"]
    Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
    "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
Example 2:
    Input: words = ["a","b","c"], pattern = "a"
    Output: ["a","b","c"]

Constraints:
    1 <= pattern.length <= 20
    1 <= words.length <= 50
    words[i].length == pattern.length
    pattern and words[i] are lowercase English letters.
"""


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(pattern, str) and len(pattern) >= 1
        len_p = len(pattern)
        for word in words:
            assert isinstance(word, str) and len(word) == len_p
        # main method: (convert the pattern string and every word string to integer tuple, and then perform matching.)
        return self._findAndReplacePattern(words, pattern)

    def _findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        assert isinstance(words, list) and len(words) >= 1
        assert isinstance(pattern, str) and len(pattern) >= 1

        def __convert_to_integer_list(s: str) -> tuple:
            ch_dict = dict({})
            cur_int = 0
            s_list = []
            for ch in s:
                if ch in ch_dict:
                    s_list.append(ch_dict[ch])
                else:
                    ch_dict[ch] = cur_int
                    s_list.append(cur_int)
                    cur_int += 1
            return tuple(s_list)

        res = []
        p_tuple = __convert_to_integer_list(pattern)
        for word in words:
            word_tuple = __convert_to_integer_list(word)
            if word_tuple == p_tuple:
                res.append(word)

        return res


def main():
    # Example 1: Output: ["mee","aqq"]
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"

    # Example 2: Output: ["a","b","c"]
    # words = ["a", "b", "c"]
    # pattern = "a"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findAndReplacePattern(words, pattern)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
