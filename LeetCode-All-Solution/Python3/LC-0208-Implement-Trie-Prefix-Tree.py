#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0208-Implement-Trie-Prefix-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-17
=================================================================="""

import sys
import time
from typing import Optional
# import collections
# import functools

"""
LeetCode - 0208 - (Medium) - Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

Description & Requirement:
    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and 
    retrieve keys in a dataset of strings. There are various applications of this data structure, 
    such as autocomplete and spellchecker.

    Implement the Trie class:
        Trie() Initializes the trie object.
        void insert(String word) Inserts the string word into the trie.
        boolean search(String word) Returns true if the string word is in the trie 
            (i.e., was inserted before), and false otherwise.
        boolean startsWith(String prefix) Returns true if there is a previously inserted string word that 
            has the prefix prefix, and false otherwise.

Example 1:
    Input
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output
        [null, null, true, false, true, null, true]
    Explanation
        Trie trie = new Trie();
        trie.insert("apple");
        trie.search("apple");   // return True
        trie.search("app");     // return False
        trie.startsWith("app"); // return True
        trie.insert("app");
        trie.search("app");     // return True

Constraints:
    1 <= word.length, prefix.length <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
"""


class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def search_prefix(self, prefix: str) -> Optional["Trie"]:
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not isinstance(node.children[ch], Trie):
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not isinstance(node.children[ch], Trie):
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.search_prefix(prefix) is not None


def main():
    # Example 1: Output: [null, null, true, false, true, null, true]
    command_list = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    param_list = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

    # init instance
    obj = Trie()
    ans = ["null"]

    # run & time
    _start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "insert" and isinstance(param, list) and len(param) == 1:
            obj.insert(param[0])
            ans.append("null")
        elif command == "search" and isinstance(param, list) and len(param) == 1:
            ans.append(obj.search(param[0]))
        elif command == "startsWith" and isinstance(param, list) and len(param) == 1:
            ans.append(obj.startsWith(param[0]))
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
