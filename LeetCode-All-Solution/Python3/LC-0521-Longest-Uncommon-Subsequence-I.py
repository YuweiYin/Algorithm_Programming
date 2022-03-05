#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0521-Longest-Uncommon-Subsequence-I.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-05
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0521 - (Easy) - Longest Uncommon Subsequence I
https://leetcode.com/problems/longest-uncommon-subsequence-i/

Description & Requirement:
    Given two strings a and b, return the length of the longest uncommon subsequence between a and b. 
    If the longest uncommon subsequence does not exist, return -1.

    An uncommon subsequence between two strings is a string that is a subsequence of one but not the other.

    A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

    For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters 
    in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

Example 1:
    Input: a = "aba", b = "cdc"
    Output: 3
    Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
    Note that "cdc" is also a longest uncommon subsequence.
Example 2:
    Input: a = "aaa", b = "bbb"
    Output: 3
    Explanation: The longest uncommon subsequences are "aaa" and "bbb".
Example 3:
    Input: a = "aaa", b = "aaa"
    Output: -1
    Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, 
        every subsequence of string b is also a subsequence of string a.

Constraints:
    1 <= a.length, b.length <= 100
    a and b consist of lower-case English letters.
"""


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # exception case
        assert isinstance(a, str) and len(a) > 0
        assert isinstance(b, str) and len(b) > 0
        # main method: (rules and tricks)
        # return self._findLUSlength(a, b)
        return self._findLUSlengthShort(a, b)

    def _findLUSlength(self, a: str, b: str) -> int:
        len_a = len(a)
        len_b = len(b)
        assert len_a > 0 and len_b > 0

        if len_a != len_b:  # if len(a) > len(b), then subseq `a` itself must not be a subseq of `b`
            return max(len_a, len_b)
        if a == b:
            return -1

        # now len(a) == len(b) and a != b, so either `a` or `b` is the longest subseq
        return len_a

    def _findLUSlengthShort(self, a: str, b: str) -> int:
        """
        Runtime: 28 ms, faster than 94.27% of Python3 online submissions for Longest Uncommon Subsequence I.
        Memory Usage: 13.9 MB, less than 46.15% of Python3 online submissions for Longest Uncommon Subsequence I.
        """
        return max(len(a), len(b)) if a != b else -1


def main():
    # Example 1: Output: 3
    # a = "aba"
    # b = "cdc"

    # Example 2: Output: 3
    a = "aaa"
    b = "bbb"

    # Example 3: Output: -1
    # a = "aaa"
    # b = "aaa"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findLUSlength(a, b)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
