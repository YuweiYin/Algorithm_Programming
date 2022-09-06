#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0828-Count-Unique-Characters-of-All-Substrings-of-a-Given-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-06
=================================================================="""

import sys
import time
import collections
# from typing import List
# import functools

"""
LeetCode - 0828 - (Hard) - Count Unique Characters of All Substrings of a Given String
https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

Description & Requirement:
    Let's define a function countUniqueChars(s) that returns the number of unique characters on s.
        For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are 
        the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.

    Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. 
    The test cases are generated such that the answer fits in a 32-bit integer.

    Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

Example 1:
    Input: s = "ABC"
    Output: 10
    Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
        Every substring is composed with only unique letters.
        Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
Example 2:
    Input: s = "ABA"
    Output: 8
    Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
Example 3:
    Input: s = "LEETCODE"
    Output: 92

Constraints:
    1 <= s.length <= 10^5
    s consists of uppercase English letters only.
"""


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (calculate the contribution of each char)
        return self._uniqueLetterString(s)

    def _uniqueLetterString(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1

        ch_to_idx = collections.defaultdict(list)
        for idx, ch in enumerate(s):
            ch_to_idx[ch].append(idx)

        res = 0
        for arr in ch_to_idx.values():
            arr = [-1] + arr + [len(s)]
            for idx in range(1, len(arr) - 1):
                res += (arr[idx] - arr[idx - 1]) * (arr[idx + 1] - arr[idx])

        return res


def main():
    # Example 1: Output: 10
    # s = "ABC"

    # Example 2: Output: 8
    # s = "ABA"

    # Example 3: Output: 92
    s = "LEETCODE"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.uniqueLetterString(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
