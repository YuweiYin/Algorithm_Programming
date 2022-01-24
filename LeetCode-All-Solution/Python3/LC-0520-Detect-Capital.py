#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0520-Detect-Capital.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-24
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0520 - (Easy) - Detect Capital
https://leetcode.com/problems/detect-capital/

Description & Requirement:
    We define the usage of capitals in a word to be right when one of the following cases holds:
        All letters in this word are capitals, like "USA".
        All letters in this word are not capitals, like "leetcode".
        Only the first letter in this word is capital, like "Google".
    Given a string word, return true if the usage of capitals in it is right.

Example 1:
    Input: word = "USA"
    Output: true
Example 2:
    Input: word = "FlaG"
    Output: false

Constraints:
    1 <= word.length <= 100
    word consists of lowercase and uppercase English letters.
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # exception case
        if not isinstance(word, str) or len(word) <= 0:
            return False  # Error input type
        if len(word) == 1:
            return True  # whether it is Capital or not, just fine
        # main method: (easy rules)
        return self._detectCapitalUse(word)

    def _detectCapitalUse(self, word: str) -> bool:
        len_word = len(word)
        assert len_word > 1

        if word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()):
            return True
        else:
            return False


def main():
    # Example 1: Output: true
    word = "USA"

    # Example 2: Output: false
    # word = "FlaG"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.detectCapitalUse(word)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
