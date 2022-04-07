#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0796-Rotate-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-07
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0796 - (Easy) - Rotate String
https://leetcode.com/problems/rotate-string/

Description & Requirement:
    Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

    A shift on s consists of moving the leftmost character of s to the rightmost position.

    For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1:
    Input: s = "abcde", goal = "cdeab"
    Output: true
Example 2:
    Input: s = "abcde", goal = "abced"
    Output: false

Constraints:
    1 <= s.length, goal.length <= 100
    s and goal consist of lowercase English letters.
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        assert isinstance(goal, str) and len(goal) >= 1
        # main method: (rotation stimulate, rotate at most len(s)-1)
        return self._rotateString(s, goal)

    def _rotateString(self, s: str, goal: str) -> bool:
        len_s = len(s)
        len_g = len(goal)
        assert len_s >= 1 and len_g >= 1

        if len_s != len_g:
            return False

        # if s == goal:
        #     return True

        # try rotating
        for idx in range(len_s):
            rotation_s = s[idx:] + s[0: idx]
            if rotation_s == goal:
                return True

        return False


def main():
    # Example 1: Output: true
    s = "abcde"
    goal = "cdeab"

    # Example 2: Output: false
    # s = "abcde"
    # goal = "abced"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.rotateString(s, goal)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
