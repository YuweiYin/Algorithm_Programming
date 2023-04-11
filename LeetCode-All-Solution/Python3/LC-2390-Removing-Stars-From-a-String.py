#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2390-Removing-Stars-From-a-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-11
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2390 - (Medium) - Removing Stars From a String
https://leetcode.com/problems/removing-stars-from-a-string/

Description & Requirement:
    You are given a string s, which contains stars *.

    In one operation, you can:
        Choose a star in s.
        Remove the closest non-star character to its left, as well as remove the star itself.

    Return the string after all stars have been removed.

    Note:
        The input will be generated such that the operation is always possible.
        It can be shown that the resulting string will always be unique.

Example 1:
    Input: s = "leet**cod*e"
    Output: "lecoe"
    Explanation: Performing the removals from left to right:
        - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
        - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
        - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
        There are no more stars, so we return "lecoe".
Example 2:
    Input: s = "erase*****"
    Output: ""
    Explanation: The entire string is removed, so we return an empty string.

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters and stars *.
    The operation above can be performed on s.
"""


class Solution:
    def removeStars(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (stack)
        return self._removeStars(s)

    def _removeStars(self, s: str) -> str:
        assert isinstance(s, str) and len(s) >= 1

        stack = []
        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


def main():
    # Example 1: Output: "lecoe"
    s = "leet**cod*e"

    # Example 2: Output: ""
    # s = "erase*****"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.removeStars(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
