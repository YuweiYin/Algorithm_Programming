#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0211-Design-Add-and-Search-Words-Data-Structure.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-28
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0211 - (Medium) - Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Description & Requirement:
    Design a data structure that supports adding new words and 
    finding if a string matches any previously added string.

    Implement the WordDictionary class:
        WordDictionary() Initializes the object.
        void addWord(word) Adds word to the data structure, it can be matched later.
        bool search(word) Returns true if there is any string in the data structure that 
            matches word or false otherwise. 
            word may contain dots '.' where dots can be matched with any letter.

Example:
    Input
        ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    Output
        [null,null,null,null,false,true,true,true]
    Explanation
        WordDictionary wordDictionary = new WordDictionary();
        wordDictionary.addWord("bad");
        wordDictionary.addWord("dad");
        wordDictionary.addWord("mad");
        wordDictionary.search("pad"); // return False
        wordDictionary.search("bad"); // return True
        wordDictionary.search(".ad"); // return True
        wordDictionary.search("b.."); // return True

Constraints:
    1 <= word.length <= 500
    word in addWord consists lower-case English letters.
    word in search consist of  '.' or lower-case English letters.
    At most 50000 calls will be made to addWord and search.
"""


class WordDictionary:

    def __init__(self):
        # idea: Trie. node[0] is next layer dict; node[1] indicates word end
        self.root = [dict({}), False]  # multi layer dict

    def addWord(self, word: str) -> None:
        if isinstance(word, str):
            len_word = len(word)
            if len_word == 0:
                self.root[1] = True
                return
            cur_dict_layer = self.root[0]
            for idx, char in enumerate(word):  # each char is one layer
                if char not in cur_dict_layer:
                    # node[0] is next layer dict; node[1] indicates word end
                    if idx < len_word - 1:
                        cur_dict_layer[char] = [dict({}), False]
                    else:
                        cur_dict_layer[char] = [dict({}), True]
                        return
                cur_dict_layer = cur_dict_layer[char][0]  # next dict layer

    def search(self, word: str) -> bool:
        """
        Runtime: 292 ms, faster than 86.96% of Python3 online submissions for Design Add and Search Words DS.
        Memory Usage: 26.7 MB, less than 61.39% of Python3 online submissions for Design Add and Search Words DS.
        """
        LEN_WORD = len(word)

        def __dfs(cur_dict_layer: list, cur_char_index: int):
            if cur_char_index == LEN_WORD:  # match all
                return cur_dict_layer[1]

            cur_char = word[cur_char_index]
            if cur_char != ".":  # not ".", must exact match
                if cur_char not in cur_dict_layer[0]:  # not match
                    return False
                else:  # dfs match the next char
                    return __dfs(cur_dict_layer[0][cur_char], cur_char_index + 1)
            else:  # is ".", many possible branches
                for k, v in cur_dict_layer[0].items():  # go to each possible branch
                    if __dfs(cur_dict_layer[0][k], cur_char_index + 1):
                        return True
                return False

        if isinstance(word, str):
            if len(word) == 0:  # word is ""
                return self.root[1]
            return __dfs(self.root, 0)
        else:  # not even a string
            return False


def main():
    # Example 1: Output: [null,null,null,null,false,true,true,true]
    #     Explanation
    #         WordDictionary wordDictionary = new WordDictionary();
    #         wordDictionary.addWord("bad");
    #         wordDictionary.addWord("dad");
    #         wordDictionary.addWord("mad");
    #         wordDictionary.search("pad"); // return False
    #         wordDictionary.search("bad"); // return True
    #         wordDictionary.search(".ad"); // return True
    #         wordDictionary.search("b.."); // return True
    command_list = ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
    param_list = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]

    # Example 2: Output: [null,null,null,true,true,true,false,true,false,true,true]
    # command_list = ["WordDictionary", "addWord", "addWord", "search", "search", "search", "search", "search",
    #                 "search", "search", "search"]
    # param_list = [[], ["a"], ["ab"], ["a"], ["a."], ["ab"], [".a"], [".b"], ["ab."], ["."], [".."]]

    # init instance
    # solution = Solution()

    # run & time
    start = time.process_time()
    obj = WordDictionary()
    assert len(command_list) == len(param_list)
    for index in range(1, len(command_list)):
        if command_list[index] == "addWord":
            obj.addWord(param_list[index][0])
        elif command_list[index] == "search":
            print(obj.search(param_list[index][0]))
    end = time.process_time()

    # show answer
    # print('\nAnswer:')
    # print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
