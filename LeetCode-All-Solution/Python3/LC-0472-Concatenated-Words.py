#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0472-Concatenated-Words.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-27
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0472 - (Hard) - Concatenated Words
https://leetcode.com/problems/concatenated-words/

Description & Requirement:
    Given an array of strings words (without duplicates), 
    return all the concatenated words in the given list of words.

    A concatenated word is defined as a string that is comprised entirely of 
    at least two shorter words in the given array.

Example 1:
    Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
    Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
        "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
        "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:
    Input: words = ["cat","dog","catdog"]
    Output: ["catdog"]

Constraints:
    1 <= words.length <= 10^4
    1 <= words[i].length <= 30
    words[i] consists of only lowercase English letters.
    All the strings of words are unique.
    1 <= sum(words[i].length) <= 10^5
"""


class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

    def insert(self, word: str):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def dfs(self, word: str, start: int, visited: List[bool]) -> bool:
        if start == len(word):
            return True
        if visited[start]:
            return False

        visited[start] = True
        node = self

        for i in range(start, len(word)):
            node = node.children[ord(word[i]) - ord('a')]
            if node is None:
                return False
            if node.isEnd and self.dfs(word, i + 1, visited):
                return True

        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        # main method: (Trie)
        return self._findAllConcatenatedWordsInADict(words)

    def _findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        assert isinstance(words, list) and len(words) >= 1

        res = []
        root = Trie()

        words.sort(key=len)
        for word in words:
            if word == "":
                continue
            if root.dfs(word, 0, [False] * len(word)):
                res.append(word)
            else:
                root.insert(word)

        return res


def main():
    # Example 1: Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]

    # Example 2: Output: ["catdog"]
    # words = ["cat", "dog", "catdog"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findAllConcatenatedWordsInADict(words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
