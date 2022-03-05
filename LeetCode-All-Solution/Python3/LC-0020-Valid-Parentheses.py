#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0020-Valid-Parentheses.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-05
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0020 - (Easy) - Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Description & Requirement:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example 1:
    Input: s = "()"
    Output: true
Example 2:
    Input: s = "()[]{}"
    Output: true
Example 3:
    Input: s = "(]"
    Output: false

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # exception case
        assert isinstance(s, str) and len(s) > 0
        if len(s) & 0x01 == 1:  # len(s) is odd, can't be valid
            return False
        # main method: (stack stimulate)
        return self._isValid(s)

    def _isValid(self, s: str) -> bool:
        """
        Runtime: 32 ms, faster than 87.75% of Python3 online submissions for Valid Parentheses.
        Memory Usage: 13.9 MB, less than 85.48% of Python3 online submissions for Valid Parentheses.
        """
        stack = []
        left_paren = {"(", "[", "{"}
        paren_pair = dict({
            ")": "(",
            "]": "[",
            "}": "{"
        })

        for char in s:
            if char in left_paren:  # put in left paren
                stack.append(char)
            else:
                if len(stack) > 0 and stack[-1] == paren_pair[char]:  # match the stack top
                    stack.pop()
                else:  # not match the stack top
                    return False

        return True if len(stack) == 0 else False


def main():
    # Example 1: Output: true
    # s = "()"

    # Example 2: Output: true
    # s = "()[]{}"

    # Example 3: Output: false
    s = "(]"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isValid(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
