#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0820-Short-Encoding-of-Words.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-20
=================================================================="""

import sys
import time
from typing import List
import collections
import functools

"""
LeetCode - 0820 - (Medium) - Short Encoding of Words
https://leetcode.com/problems/short-encoding-of-words/

Description & Requirement:
    A valid encoding of an array of words is any reference string s and array of indices indices such that:
        words.length == indices.length
        The reference string s ends with the '#' character.
        For each index indices[i], the substring of s starting from indices[i] and up to (but not including) 
            the next '#' character is equal to words[i].

    Given an array of words, 
    return the length of the shortest reference string s possible of any valid encoding of words.

Example 1:
    Input: words = ["time", "me", "bell"]
    Output: 10
    Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
        words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
        words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
        words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"
Example 2:
    Input: words = ["t"]
    Output: 2
    Explanation: A valid encoding would be s = "t#" and indices = [0].

Constraints:
    1 <= words.length <= 2000
    1 <= words[i].length <= 7
    words[i] consists of only lowercase letters.
"""

Trie = lambda: collections.defaultdict(Trie)


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # exception case
        assert isinstance(words, list) and len(words) >= 1
        for word in words:
            assert isinstance(word, str) and len(word) >= 1
        # main method: (suffix Trie)
        return self._minimumLengthEncoding(words)

    def _minimumLengthEncoding(self, words: List[str]) -> int:
        assert isinstance(words, list) and len(words) >= 1

        # remove duplicates
        words = list(set(words))

        # init Trie
        trie = Trie()

        # construct Trie
        nodes = [functools.reduce(dict.__getitem__, word[::-1], trie) for word in words]

        # append (word + "#") if the node has no neighbors
        return sum(len(word) + 1 for idx, word in enumerate(words) if len(nodes[idx]) == 0)


def main():
    # Example 1: Output: 10
    words = ["time", "me", "bell"]

    # Example 2: Output: 2
    # words = ["t"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumLengthEncoding(words)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
