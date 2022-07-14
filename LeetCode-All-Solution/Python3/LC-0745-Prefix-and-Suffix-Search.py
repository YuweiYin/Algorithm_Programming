#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0745-Prefix-and-Suffix-Search.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-18
=================================================================="""

import sys
import time
from typing import List
import itertools
# import collections
# import functools

"""
LeetCode - 0745 - (Hard) - Prefix and Suffix Search
https://leetcode.com/problems/prefix-and-suffix-search/

Description & Requirement:
    Design a special dictionary with some words that searches the words in it by a prefix and a suffix.

    Implement the WordFilter class:
        WordFilter(string[] words) Initializes the object with the words in the dictionary.
        f(string prefix, string suffix) Returns the index of the word in the dictionary, 
            which has the prefix prefix and the suffix suffix. If there is more than one valid index, 
            return the largest of them. If there is no such word in the dictionary, return -1.

Example 1:
    Input:
        ["WordFilter", "f"]
        [[["apple"]], ["a", "e"]]
    Output:
        [null, 0]
    Explanation:
        WordFilter wordFilter = new WordFilter(["apple"]);
        wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".

Constraints:
    1 <= words.length <= 15000
    1 <= words[i].length <= 10
    1 <= prefix.length, suffix.length <= 10
    words[i], prefix and suffix consist of lower-case English letters only.
    At most 15000 calls will be made to the function f.
"""


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.weightKey = ('#', '#')
        for i, word in enumerate(words):
            cur_node = self.trie
            len_word = len(word)
            for j in range(len_word):
                tmp = cur_node
                for k in range(j, len_word):
                    key = (word[k], '#')
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[self.weightKey] = i
                tmp = cur_node
                for k in range(j, len_word):
                    key = ('#', word[-k - 1])
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[self.weightKey] = i
                key = (word[j], word[-j - 1])
                if key not in cur_node:
                    cur_node[key] = {}
                cur_node = cur_node[key]
                cur_node[self.weightKey] = i

    def f(self, pref: str, suf: str) -> int:
        cur_node = self.trie
        for key in itertools.zip_longest(pref, suf[::-1], fillvalue='#'):
            if key not in cur_node:
                return -1
            cur_node = cur_node[key]
        return cur_node[self.weightKey]


# Trie = lambda: collections.defaultdict(Trie)


# class WordFilter:
#
#     def __init__(self, words: List[str]):
#         self.WEIGHT = False
#         self.trie_prefix = Trie()
#         self.trie_suffix = Trie()
#         self.answer = dict({})  # key: (prefix, suffix); value: answer.
#
#         def __add_word(trie, word_idx):
#             if self.WEIGHT not in trie:
#                 trie[self.WEIGHT] = {word_idx}
#             else:
#                 trie[self.WEIGHT].add(word_idx)
#
#         for idx, word in enumerate(words):
#             cur_trie = self.trie_prefix
#             __add_word(cur_trie, idx)
#             for ch in word:
#                 cur_trie = cur_trie[ch]  # next level
#                 __add_word(cur_trie, idx)
#
#             cur_trie = self.trie_suffix
#             __add_word(cur_trie, idx)
#             for ch in word[::-1]:  # reverse
#                 cur_trie = cur_trie[ch]  # next level
#                 __add_word(cur_trie, idx)
#
#     def f(self, prefix: str, suffix: str) -> int:
#         """
#         Runtime: 863 ms, faster than 96.94% of Python3 online submissions for Prefix and Suffix Search.
#         Memory Usage: 36.5 MB, less than 62.39% of Python3 online submissions for Prefix and Suffix Search.
#         """
#         _input = (prefix, suffix)
#         if _input in self.answer:
#             return self.answer[_input]
#
#         trie_pre = self.trie_prefix
#         for ch in prefix:
#             if ch not in trie_pre:
#                 return -1
#             trie_pre = trie_pre[ch]  # next level
#
#         trie_suf = self.trie_suffix
#         for ch in suffix[::-1]:
#             if ch not in trie_suf:
#                 return -1
#             trie_suf = trie_suf[ch]  # next level
#
#         ans = max(trie_pre[self.WEIGHT] & trie_suf[self.WEIGHT])
#         self.answer[_input] = ans
#         return ans


def main():
    # Example 1: Output: [null, 0]
    command_list = ["WordFilter", "f"]
    param_list = [[["apple"]], ["a", "e"]]

    # init instance
    # solution = Solution()
    words = param_list[0][0]
    obj = WordFilter(words)

    # run & time
    start = time.process_time()
    ans = ["null"]
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "f" and isinstance(param, list) and len(param) == 2:
            ans.append(obj.f(param[0], param[1]))
        else:
            ans.append(["null"])
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
