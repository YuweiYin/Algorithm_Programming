#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1805-Number-of-Different-Integers-in-a-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-06
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1805 - (Easy) - Number of Different Integers in a String
https://leetcode.com/problems/number-of-different-integers-in-a-string/

Description & Requirement:
    You are given a string word that consists of digits and lowercase English letters.

    You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34".
    Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".

    Return the number of different integers after performing the replacement operations on word.

    Two integers are considered different if their decimal representations without any leading zeros are different.

Example 1:
    Input: word = "a123bc34d8ef34"
    Output: 3
    Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.
Example 2:
    Input: word = "leet1234code234"
    Output: 2
Example 3:
    Input: word = "a1b01c001"
    Output: 1
    Explanation: The three integers "1", "01", and "001" all represent the same integer because
        the leading zeros are ignored when comparing their decimal values.

Constraints:
    1 <= word.length <= 1000
    word consists of digits and lowercase English letters.
"""


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # exception case
        assert isinstance(word, str) and len(word) >= 1
        # main method: (hash set and two pointers)
        return self._numDifferentIntegers(word)

    def _numDifferentIntegers(self, word: str) -> int:
        assert isinstance(word, str) and len(word) >= 1

        s = set()
        n = len(word)
        left = 0
        while True:
            while left < n and not word[left].isdigit():
                left += 1
            if left == n:
                break

            right = left
            while right < n and word[right].isdigit():
                right += 1
            while right - left > 1 and word[left] == '0':  # delete leftmost 0s
                left += 1
            s.add(word[left: right])
            left = right

        return len(s)


def main():
    # Example 1: Output: 3
    # word = "a123bc34d8ef34"

    # Example 2: Output: 2
    # word = "leet1234code234"

    # Example 3: Output: 1
    word = "a1b01c001"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numDifferentIntegers(word)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
