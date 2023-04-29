#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2423-Remove-Letter-To-Equalize-Frequency.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-29
=================================================================="""

import sys
import time
# from typing import List
import collections
# import functools

"""
LeetCode - 2423 - (Easy) - Remove Letter To Equalize Frequency
https://leetcode.com/problems/remove-letter-to-equalize-frequency/

Description & Requirement:
    You are given a 0-indexed string word, consisting of lowercase English letters. 
    You need to select one index and remove the letter at that index from word so that 
    the frequency of every letter present in word is equal.

    Return true if it is possible to remove one letter so that 
    the frequency of all letters in word are equal, and false otherwise.

    Note:
        The frequency of a letter x is the number of times it occurs in the string.
        You must remove exactly one letter and cannot chose to do nothing.

Example 1:
    Input: word = "abcc"
    Output: true
    Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
Example 2:
    Input: word = "aazz"
    Output: false
    Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, 
        or vice versa. It is impossible to make all present letters have equal frequency.

Constraints:
    2 <= word.length <= 100
    word consists of lowercase English letters only.
"""


class Solution:
    def equalFrequency(self, word: str) -> bool:
        # exception case
        assert isinstance(word, str) and len(word) >= 2
        # main method: (hash counter)
        return self._equalFrequency(word)

    def _equalFrequency(self, word: str) -> bool:
        assert isinstance(word, str) and len(word) >= 2

        counter = [v for k, v in collections.Counter(word).items()]
        for i in range(len(counter)):
            counter[i] -= 1
            cnt = collections.Counter(counter)
            if len(cnt) == 1 or (len(cnt) == 2 and 0 in cnt):
                return True
            counter[i] += 1

        return False


def main():
    # Example 1: Output: true
    word = "abcc"

    # Example 2: Output: false
    # word = "aazz"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.equalFrequency(word)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
