#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1047-Remove-All-Adjacent-Duplicates-In-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-10
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1047 - (Easy) - Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Description & Requirement:
    You are given a string s consisting of lowercase English letters. 
    A duplicate removal consists of choosing two adjacent and equal letters and removing them.

    We repeatedly make duplicate removals on s until we no longer can.

    Return the final string after all such duplicate removals have been made. 
    It can be proven that the answer is unique.

Example 1:
    Input: s = "abbaca"
    Output: "ca"
    Explanation: 
    For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
        and this is the only possible move.  The result of this move is that the string is "aaca", 
        of which only "aa" is possible, so the final string is "ca".
Example 2:
    Input: s = "azxxzy"
    Output: "ay"

Constraints:
    1 <= s.length <= 10^5
    s consists of lowercase English letters.
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (stack)
        return self._removeDuplicates(s)

    def _removeDuplicates(self, s: str) -> str:
        assert isinstance(s, str) and len(s) >= 1

        stack = []
        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
            else:
                if stack[-1] == ch:
                    stack.pop()
                else:
                    stack.append(ch)

        return "".join(stack)


def main():
    # Example 1: Output: "ca"
    # s = "abbaca"

    # Example 2: Output: "ay"
    s = "azxxzy"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.removeDuplicates(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
