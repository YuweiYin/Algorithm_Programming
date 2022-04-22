#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0032-Longest-Valid-Parentheses.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-22
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0032 - (Hard) - Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/

Description & Requirement:
    Given a string containing just the characters '(' and ')', 
    find the length of the longest valid (well-formed) parentheses substring.

Example 1:
    Input: s = "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()".
Example 2:
    Input: s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".
Example 3:
    Input: s = ""
    Output: 0

Constraints:
    0 <= s.length <= 3 * 10^4
    s[i] is '(', or ')'.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # exception case
        assert isinstance(s, str)
        # main method: (stack)
        return self._longestValidParentheses(s)

    def _longestValidParentheses(self, s: str) -> int:
        assert isinstance(s, str)
        len_s = len(s)
        if len_s == 0:
            return 0

        stack = []
        valid_flag = [False for _ in range(len_s)]
        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append(idx)
            elif ch == ")":
                if len(stack) > 0:
                    match_idx = stack.pop()  # match "(" and ")"
                    valid_flag[idx] = True
                    valid_flag[match_idx] = True
                else:
                    pass
            else:
                pass

        res = 0
        idx = 0
        while idx < len_s:
            if valid_flag[idx]:
                cur_res = 0
                while idx < len_s and valid_flag[idx]:  # consecutive valid parentheses
                    cur_res += 1
                    idx += 1
                res = max(res, cur_res)
            else:
                idx += 1

        return res


def main():
    # Example 1: Output: 2
    # s = "(()"

    # Example 2: Output: 4
    s = ")()())"

    # Example 3: Output: 0
    # s = ""

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestValidParentheses(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
