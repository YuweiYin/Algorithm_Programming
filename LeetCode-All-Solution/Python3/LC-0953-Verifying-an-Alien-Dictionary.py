#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0953-Verifying-an-Alien-Dictionary.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-17
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0953 - (Easy) - Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/

Description & Requirement:
    In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. 
    The order of the alphabet is some permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of the alphabet, 
    return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:
    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:
    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:
    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # exception case
        assert isinstance(order, str) and order.islower() and len(order) == 26
        assert isinstance(words, list) and len(words) >= 1 and isinstance(words[0], str)
        assert all([isinstance(word, str) and word.islower() and len(word) > 0 for word in words])
        # main method: (convert every char in each word into an integer, and then check words[i] <= words[i+1])
        return self._isAlienSorted(words, order)

    def _isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True

        map_dict = dict({})
        for idx, ch in enumerate(order):
            map_dict[ch] = idx

        last_word = [[map_dict[ch] for ch in words[0]]]
        for word in words[1:]:
            cur_word = [[map_dict[ch] for ch in word]]
            if last_word <= cur_word:
                last_word = cur_word
            else:
                return False

        return True


def main():
    # Example 1: Output: true
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"

    # Example 2: Output: false
    # words = ["word", "world", "row"]
    # order = "worldabcefghijkmnpqstuvxyz"

    # Example 3: Output: false
    # words = ["apple", "app"]
    # order = "abcdefghijklmnopqrstuvwxyz"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isAlienSorted(words, order)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
