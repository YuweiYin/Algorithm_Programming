#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2490-Circular-Sentence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-30
=================================================================="""

import sys
import time
from typing import List
import collections
import heapq
# import functools
# import itertools

"""
LeetCode - 2490 - (Easy) - Circular Sentence
https://leetcode.com/problems/circular-sentence/

Description & Requirement:
    A sentence is a list of words that are separated by 
    a single space with no leading or trailing spaces.
        For example, "Hello World", "HELLO", "hello world hello world" are all sentences.

    Words consist of only uppercase and lowercase English letters. 
    Uppercase and lowercase English letters are considered different.

    A sentence is circular if:
        The last character of a word is equal to the first character of the next word.
        The last character of the last word is equal to the first character of the first word.

    For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" 
    are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" 
    and "I like Leetcode" are not circular sentences.

    Given a string sentence, return true if it is circular. Otherwise, return false.

Example 1:
    Input: sentence = "leetcode exercises sound delightful"
    Output: true
    Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
        - leetcode's last character is equal to exercises's first character.
        - exercises's last character is equal to sound's first character.
        - sound's last character is equal to delightful's first character.
        - delightful's last character is equal to leetcode's first character.
        The sentence is circular.
Example 2:
    Input: sentence = "eetcode"
    Output: true
    Explanation: The words in sentence are ["eetcode"].
        - eetcode's last character is equal to eetcode's first character.
        The sentence is circular.
Example 3:
    Input: sentence = "Leetcode is cool"
    Output: false
    Explanation: The words in sentence are ["Leetcode", "is", "cool"].
        - Leetcode's last character is not equal to is's first character.
        The sentence is not circular.

Constraints:
    1 <= sentence.length <= 500
    sentence consist of only lowercase and uppercase English letters and spaces.
    The words in sentence are separated by a single space.
    There are no leading or trailing spaces.
"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # exception case
        assert isinstance(sentence, str) and len(sentence) >= 1
        # main method: (scan the array)
        return self._isCircularSentence(sentence)

    def _isCircularSentence(self, sentence: str) -> bool:
        assert isinstance(sentence, str) and len(sentence) >= 1

        n = len(sentence)
        if sentence[n - 1] != sentence[0]:
            return False

        for idx in range(n):
            if sentence[idx] == " " and (sentence[min(n - 1, idx + 1)] != sentence[max(0, idx - 1)]):
                return False

        return True


def main():
    # Example 1: Output: true
    sentence = "leetcode exercises sound delightful"

    # Example 2: Output: true
    # sentence = "eetcode"

    # Example 3: Output: false
    # sentence = "Leetcode is cool"

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.isCircularSentence(sentence)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
