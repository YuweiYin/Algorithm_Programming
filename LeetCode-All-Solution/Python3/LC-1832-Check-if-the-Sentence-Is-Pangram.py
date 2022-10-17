#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1832-Check-if-the-Sentence-Is-Pangram.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-17
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1832 - (Easy) - Check if the Sentence Is Pangram
https://leetcode.com/problems/check-if-the-sentence-is-pangram/

Description & Requirement:
    A pangram is a sentence where every letter of the English alphabet appears at least once.

    Given a string sentence containing only lowercase English letters, 
    return true if sentence is a pangram, or false otherwise.

Example 1:
    Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
    Output: true
    Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:
    Input: sentence = "leetcode"
    Output: false

Constraints:
    1 <= sentence.length <= 1000
    sentence consists of lowercase English letters.
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # exception case
        assert isinstance(sentence, str) and len(sentence) >= 1 and sentence.islower()
        # main method: (hash set)
        return self._checkIfPangram(sentence)

    def _checkIfPangram(self, sentence: str) -> bool:
        assert isinstance(sentence, str) and len(sentence) >= 1 and sentence.islower()
        # s_set = set([ch for ch in sentence])
        s_set = set(sentence)

        return len(s_set) == 26


def main():
    # Example 1: Output: true
    sentence = "thequickbrownfoxjumpsoverthelazydog"

    # Example 2: Output: false
    # sentence = "leetcode"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.checkIfPangram(sentence)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
