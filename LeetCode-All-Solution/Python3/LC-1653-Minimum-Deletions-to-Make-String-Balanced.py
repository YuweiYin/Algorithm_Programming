#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1653-Minimum-Deletions-to-Make-String-Balanced.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-06
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1653 - (Medium) - Minimum Deletions to Make String Balanced
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

Description & Requirement:
    You are given a string s consisting only of characters 'a' and 'b'.

    You can delete any number of characters in s to make s balanced. 
    s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

    Return the minimum number of deletions needed to make s balanced.

Example 1:
    Input: s = "aababbab"
    Output: 2
    Explanation: You can either:
        Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
        Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:
    Input: s = "bbaaaaabb"
    Output: 2
    Explanation: The only solution is to delete the first two characters.

Constraints:
    1 <= s.length <= 10^5
    s[i] is 'a' or 'b'.
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (scan the array)
        return self._minimumDeletions(s)

    def _minimumDeletions(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1

        left_b, right_a = 0, s.count("a")
        res = right_a

        for ch in s:
            if ch == "a":
                right_a -= 1
            else:
                left_b += 1
            res = min(res, left_b + right_a)

        return res


def main():
    # Example 1: Output: 2
    s = "aababbab"

    # Example 2: Output: 2
    # s = "bbaaaaabb"

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minimumDeletions(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
