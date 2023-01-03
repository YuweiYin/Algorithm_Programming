#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2042-Check-if-Numbers-Are-Ascending-in-a-Sentence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-03
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2042 - (Easy) - Check if Numbers Are Ascending in a Sentence
https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

Description & Requirement:
    A sentence is a list of tokens separated by a single space with no leading or trailing spaces. 
    Every token is either a positive number consisting of digits 0-9 with no leading zeros, 
    or a word consisting of lowercase English letters.

        For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: 
        "2" and "4" are numbers and the other tokens such as "puppy" are words.

    Given a string s representing a sentence, 
    you need to check if all the numbers in s are strictly increasing from left to right 
    (i.e., other than the last number, each number is strictly smaller than the number on its right in s).

    Return true if so, or false otherwise.

Example 1:
    Input: s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
    Output: true
    Explanation: The numbers in s are: 1, 3, 4, 6, 12.
        They are strictly increasing from left to right: 1 < 3 < 4 < 6 < 12.
Example 2:
    Input: s = "hello world 5 x 5"
    Output: false
    Explanation: The numbers in s are: 5, 5. They are not strictly increasing.
Example 3:
    Input: s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
    Output: false
    Explanation: The numbers in s are: 7, 51, 50, 60. They are not strictly increasing.

Constraints:
    3 <= s.length <= 200
    s consists of lowercase English letters, spaces, and digits from 0 to 9, inclusive.
    The number of tokens in s is between 2 and 100, inclusive.
    The tokens in s are separated by a single space.
    There are at least two numbers in s.
    Each number in s is a positive number less than 100, with no leading zeros.
    s contains no leading or trailing spaces.
"""


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # exception case
        assert isinstance(s, str) and len(s) >= 3
        # main method: (scan and compare numbers)
        return self._areNumbersAscending(s)

    def _areNumbersAscending(self, s: str) -> bool:
        assert isinstance(s, str) and len(s) >= 3

        words = s.split()
        num = - int(1e9+7)
        for word in words:
            if word.isdigit():
                word_int = int(word)
                if word_int > num:
                    num = word_int
                else:
                    return False

        return True


def main():
    # Example 1: Output: true
    s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"

    # Example 2: Output: false
    # s = "hello world 5 x 5"

    # Example 3: Output: false
    # s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.areNumbersAscending(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
