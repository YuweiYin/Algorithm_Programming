#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0856-Score-of-Parentheses.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-17
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0856 - (Medium) - Score of Parentheses
https://leetcode.com/problems/score-of-parentheses/

Description & Requirement:
    Given a balanced parentheses string s, return the score of the string.

    The score of a balanced parentheses string is based on the following rule:
        "()" has score 1.
        AB has score A + B, where A and B are balanced parentheses strings.
        (A) has score 2 * A, where A is a balanced parentheses string.

Example 1:
    Input: s = "()"
    Output: 1
Example 2:
    Input: s = "(())"
    Output: 2
Example 3:
    Input: s = "()()"
    Output: 2

Constraints:
    2 <= s.length <= 50
    s consists of only '(' and ')'.
    s is a balanced parentheses string.
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # exception case
        assert isinstance(s, str) and len(s) >= 2
        # main method: (stack or dfs)
        return self._scoreOfParentheses(s)

    def _scoreOfParentheses(self, s: str) -> int:
        len_s = len(s)
        assert len_s >= 2

        stack = [0]  # the base layer

        for ch in s:
            if ch == "(":
                stack.append(0)
            elif ch == ")":
                inner_score = stack.pop()
                stack[-1] += max(1, inner_score << 1)  # inner parentheses worth at least 1 score
            else:  # error input
                pass

        return stack.pop()


def main():
    # Example 1: Output: 1
    # s = "()"

    # Example 2: Output: 2
    s = "(())"

    # Example 3: Output: 2
    # s = "()()"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.scoreOfParentheses(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
