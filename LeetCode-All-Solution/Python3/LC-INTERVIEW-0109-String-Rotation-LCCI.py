#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-INTERVIEW-0109-String-Rotation-LCCI.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-29
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - INTERVIEW-1709 - (Easy) - String Rotation
https://leetcode.cn/problems/string-rotation-lcci/

Description & Requirement:
    Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 
    (e.g.,"waterbottle" is a rotation of"erbottlewat").
    Can you use only one call to the method that checks if one word is a substring of another?

Example 1:
    Input: s1 = "waterbottle", s2 = "erbottlewat"
    Output: True
Example 2:
    Input: s1 = "aa", s2 = "aba"
    Output: False

Note:
    0 <= s1.length, s2.length <= 100000
"""


class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        # exception case
        assert isinstance(s1, str) and isinstance(s2, str)
        # main method: (try rotating len(s) times, O(n^2), n is len(s); match s2 with s1+s2, O(n), n is len(s))
        return self._isFlipedString(s1, s2)

    def _isFlipedString(self, s1: str, s2: str) -> bool:
        assert isinstance(s1, str) and isinstance(s2, str)

        if len(s1) != len(s2):
            return False

        # for idx in range(len(s1)):
        #     if s1 == s2[idx:] + s2[:idx]:
        #         return True

        return s2 in s1 + s1


def main():
    # Example 1: Output: True
    s1, s2 = "waterbottle", "erbottlewat"

    # Example 2: Output: False
    # s1, s2 = "aa", "aba"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isFlipedString(s1, s2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
