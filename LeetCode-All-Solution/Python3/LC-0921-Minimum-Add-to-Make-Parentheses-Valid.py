#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0921-Minimum-Add-to-Make-Parentheses-Valid.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-04
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0921 - (Medium) - Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

Description & Requirement:
    A parentheses string is valid if and only if:
        It is the empty string,
        It can be written as AB (A concatenated with B), where A and B are valid strings, or
        It can be written as (A), where A is a valid string.

    You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

    For example, if s = "()))", you can insert an opening parenthesis to be "(()))" 
    or a closing parenthesis to be "())))".

    Return the minimum number of moves required to make s valid.

Example 1:
    Input: s = "())"
    Output: 1
Example 2:
    Input: s = "((("
    Output: 3

Constraints:
    1 <= s.length <= 1000
    s[i] is either '(' or ')'.
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (stack simulation)
        return self._minAddToMakeValid(s)

    def _minAddToMakeValid(self, s: str) -> int:
        assert isinstance(s, str) and len(s) >= 1

        stack = []
        for paren in s:
            if paren == "(":
                stack.append(paren)
            elif paren == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(paren)

        return len(stack)


def main():
    # Example 1: Output: 1
    # s = "())"

    # Example 2: Output: 3
    s = "((("

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minAddToMakeValid(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
