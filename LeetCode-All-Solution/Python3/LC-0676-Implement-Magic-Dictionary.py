#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0676-Implement-Magic-Dictionary.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-11
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0676 - (Medium) - Implement Magic Dictionary
https://leetcode.com/problems/implement-magic-dictionary/

Description & Requirement:
    Design a data structure that is initialized with a list of different words. 
    Provided a string, you should determine if you can change exactly one character in this string 
    to match any word in the data structure.

    Implement the MagicDictionary class:
        MagicDictionary() Initializes the object.
        void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
        bool search(String searchWord) Returns true if you can change exactly one character in searchWord 
            to match any string in the data structure, otherwise returns false.

Example 1:
    Input
        ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
        [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
    Output
        [null, null, false, true, false, false]
    Explanation
        MagicDictionary magicDictionary = new MagicDictionary();
        magicDictionary.buildDict(["hello", "leetcode"]);
        magicDictionary.search("hello"); // return False
        magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
        magicDictionary.search("hell"); // return False
        magicDictionary.search("leetcoded"); // return False

Constraints:
    1 <= dictionary.length <= 100
    1 <= dictionary[i].length <= 100
    dictionary[i] consists of only lower-case English letters.
    All the strings in dictionary are distinct.
    1 <= searchWord.length <= 100
    searchWord consists of only lower-case English letters.
    buildDict will be called only once before search.
    At most 100 calls will be made to search.
"""


class Trie:
    def __init__(self):
        self.child = dict()
        self.is_finished = False


class MagicDictionary:

    def __init__(self):
        self.root = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur_node = self.root
            for ch in word:
                if ch not in cur_node.child:
                    cur_node.child[ch] = Trie()  # build child node
                cur_node = cur_node.child[ch]  # move to the child node
            cur_node.is_finished = True  # word ending tag

    def search(self, searchWord: str) -> bool:
        def __dfs(node: Trie, ch_idx: int, modified: bool) -> bool:
            """
            :param node: the current Trie node
            :param ch_idx: the current char index of the searchWord
            :param modified: True if the searchWord has been modified, False otherwise
            :return: True if the current Trie is matched
            """
            if ch_idx == len(searchWord):
                return modified and node.is_finished

            ch = searchWord[ch_idx]
            if ch in node.child:
                if __dfs(node.child[ch], ch_idx + 1, modified):
                    return True

            if not modified:
                for next_ch in node.child:
                    if ch != next_ch:
                        if __dfs(node.child[next_ch], ch_idx + 1, True):
                            return True

            return False

        return __dfs(self.root, 0, False)


def main():
    # Example 1: Output: [null, null, false, true, false, false]
    command_list = ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
    param_list = [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]

    # init instance
    # solution = Solution()
    obj = MagicDictionary()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    obj.buildDict(param_list[1][0])
    ans.append("null")
    for idx in range(2, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "search" and isinstance(param, list) and len(param) == 1:
            ans.append(obj.search(param[0]))
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
