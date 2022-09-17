#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0336-Palindrome-Pairs.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-17
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0336 - (Hard) - Palindrome Pairs
https://leetcode.com/problems/palindrome-pairs/

Description & Requirement:
    Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, 
    so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:
    Input: words = ["abcd","dcba","lls","s","sssll"]
    Output: [[0,1],[1,0],[3,2],[2,4]]
    Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:
    Input: words = ["bat","tab","cat"]
    Output: [[0,1],[1,0]]
    Explanation: The palindromes are ["battab","tabbat"]
Example 3:
    Input: words = ["a",""]
    Output: [[0,1],[1,0]]

Constraints:
    1 <= words.length <= 5000
    0 <= words[i].length <= 300
    words[i] consists of lower-case English letters.
"""


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        for word in words:
            assert isinstance(word, str)
        # main method: (Trie/Hash + Manacher)
        return self._palindromePairs(words)

    def _palindromePairs(self, words: List[str]) -> List[List[int]]:
        assert isinstance(words, list) and len(words) >= 1

        indices = {word[::-1]: i for i, word in enumerate(words)}

        def __find_word(s: str, left: int, right: int) -> int:
            return indices.get(s[left:right + 1], -1)

        def __is_palindrome(s: str, left: int, right: int) -> bool:
            return (sub := s[left:right + 1]) == sub[::-1]

        res = []
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if __is_palindrome(word, j, m - 1):
                    left_id = __find_word(word, 0, j - 1)
                    if left_id != -1 and left_id != i:
                        res.append([i, left_id])
                if j and __is_palindrome(word, 0, j - 1):
                    right_id = __find_word(word, j, m - 1)
                    if right_id != -1 and right_id != i:
                        res.append([right_id, i])

        return res


def main():
    # Example 1: Output: [[0,1],[1,0],[3,2],[2,4]]
    words = ["abcd", "dcba", "lls", "s", "sssll"]

    # Example 2: Output: [[0,1],[1,0]]
    # words = ["bat", "tab", "cat"]

    # Example 3: Output: [[0,1],[1,0]]
    # words = ["a", ""]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.palindromePairs(words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
