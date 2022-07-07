#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0648-Replace-Words.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-07
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0648 - (Medium) - Replace Words
https://leetcode.com/problems/replace-words/

Description & Requirement:
    In English, we have a concept called root, which can be followed by some other word 
    to form another longer word - let's call this word successor. 
    For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

    Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, 
    replace all the successors in the sentence with the root forming it. 
    If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

    Return the sentence after the replacement.

Example 1:
    Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
    Output: "the cat was rat by the bat"
Example 2:
    Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
    Output: "a a b c"

Constraints:
    1 <= dictionary.length <= 1000
    1 <= dictionary[i].length <= 100
    dictionary[i] consists of only lower-case letters.
    1 <= sentence.length <= 10^6
    sentence consists of only lower-case letters and spaces.
    The number of words in sentence is in the range [1, 1000]
    The length of each word in sentence is in the range [1, 1000]
    Every two consecutive words in sentence will be separated by exactly one space.
    sentence does not have leading or trailing spaces.
"""


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # exception case
        assert isinstance(sentence, str) and len(sentence) >= 1
        assert isinstance(dictionary, list) and len(dictionary) >= 1
        for root in dictionary:
            assert isinstance(root, str) and len(root) >= 1
        # main method: (prefix tree / trie)
        return self._replaceWords(dictionary, sentence)

    def _replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        Runtime: 119 ms, faster than 85.43% of Python3 online submissions for Replace Words.
        Memory Usage: 28.3 MB, less than 56.14% of Python3 online submissions for Replace Words.
        """
        assert isinstance(sentence, str) and len(sentence) >= 1
        assert isinstance(dictionary, list) and len(dictionary) >= 1

        trie = dict({})

        for root in dictionary:
            cur_node = trie
            for ch in root:
                if ch not in cur_node:
                    cur_node[ch] = dict({})  # new node
                cur_node = cur_node[ch]  # go to the next level
            cur_node["#"] = dict({})  # root flag

        word_list = sentence.strip().split()
        for i, word in enumerate(word_list):
            cur_node = trie
            for j, ch in enumerate(word):
                if "#" in cur_node:  # now, this is a root
                    word_list[i] = word[:j]  # match the shortest root
                    break
                if ch not in cur_node:  # not match any root
                    break
                cur_node = cur_node[ch]  # go to the next level

        return " ".join(word_list)


def main():
    # Example 1: Output: "the cat was rat by the bat"
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"

    # Example 2: Output: "a a b c"
    # dictionary = ["a", "b", "c"]
    # sentence = "aadsfasf absbs bbab cadsfafs"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.replaceWords(dictionary, sentence)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
