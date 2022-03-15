#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1249-Minimum-Remove-to-Make-Valid-Parentheses.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-15
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 1249 - (Medium) - Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Description & Requirement:
    Given a string s of '(' , ')' and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( '(' or ')', 
    in any positions ) so that the resulting parentheses string is valid and return any valid string.

    Formally, a parentheses string is valid if and only if:
        It is the empty string, contains only lowercase characters, or
        It can be written as AB (A concatenated with B), where A and B are valid strings, or
        It can be written as (A), where A is a valid string.

Example 1:
    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:
    Input: s = "a)b(c)d"
    Output: "ab(c)d"
Example 3:
    Input: s = "))(("
    Output: ""
    Explanation: An empty string is also valid.

Constraints:
    1 <= s.length <= 105
    s[i] is either'(' , ')', or lowercase English letter.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) > 0
        # main method: (stack, record invalid idx)
        return self._minRemoveToMakeValid(s)

    def _minRemoveToMakeValid(self, s: str) -> str:
        len_s = len(s)
        assert len_s > 0

        stack = []
        invalid_indices = []
        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append(idx)
            elif ch == ")":
                if len(stack) > 0:  # get paired
                    stack.pop()
                else:  # a ")" without paired "("
                    invalid_indices.append(idx)
            else:
                continue

        invalid_indices.extend(stack)
        invalid_indices = set(invalid_indices)
        res = ""
        for idx, ch in enumerate(s):
            if idx not in invalid_indices:
                res += ch

        return res


def main():
    # Example 1: Output: "lee(t(c)o)de"
    s = "lee(t(c)o)de)"

    # Example 2: Output: "ab(c)d"
    # s = "a)b(c)d"

    # Example 3: Output: ""
    # s = "))(("

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minRemoveToMakeValid(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
