#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0844-Backspace-String-Compare.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-17
=================================================================="""

import sys
import time
# from typing import List

"""
LeetCode - 0844 - (Easy) - Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/

Description & Requirement:
    Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
    '#' means a backspace character.

    Note that after backspacing an empty text, the text will continue empty.

Example 1:
    Input: s = "ab#c", t = "ad#c"
    Output: true
    Explanation: Both s and t become "ac".
Example 2:
    Input: s = "ab##", t = "c#d#"
    Output: true
    Explanation: Both s and t become "".
Example 3:
    Input: s = "a#c", t = "b"
    Output: false
    Explanation: s becomes "c" while t becomes "b".

Constraints:
    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # exception case
        if not isinstance(s, str) or not isinstance(t, str):
            return False  # Error input type
        # main method: (char matching, stack operation)
        #     another method: reverse scan, count the number of '#'s, use it to skip char (after each skip, counter --)
        return self._backspaceCompare(s, t)

    def _backspaceCompare(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        # simulate stack
        stack_s = []
        s_index = 0
        while s_index < len_s:
            if s[s_index] == '#':  # delete char
                if len(stack_s) > 0:  # ignore all leftmost '#'
                    stack_s.pop()
            else:  # append char
                stack_s.append(s[s_index])
            s_index += 1

        stack_t = []
        t_index = 0
        while t_index < len_t:
            if t[t_index] == '#':  # delete char
                if len(stack_t) > 0:  # ignore all leftmost '#'
                    stack_t.pop()
            else:  # append char
                stack_t.append(t[t_index])
            t_index += 1

        if len(stack_s) != len(stack_t):  # faster than list matching
            return False
        if stack_s != stack_t:
            return False

        return True


def main():
    # Example 1: Output: true
    # s = "ab#c"
    # t = "ad#c"

    # Example 2: Output: true
    # s = "ab##"
    # t = "c#d#"

    # Example 3: Output: false
    s = "a#c"
    t = "b"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.backspaceCompare(s, t)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
