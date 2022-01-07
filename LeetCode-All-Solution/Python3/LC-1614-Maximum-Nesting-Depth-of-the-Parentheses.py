#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1614-Maximum-Nesting-Depth-of-the-Parentheses.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-07
=================================================================="""
# import functools
import sys
import time
# from typing import List

"""
LeetCode - 1614 - (Easy) - Maximum Nesting Depth of the Parentheses
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

Description:
    A string is a valid parentheses string (denoted VPS) if it meets one of the following:
        It is an empty string "", or a single character not equal to "(" or ")",
        It can be written as AB (A concatenated with B), where A and B are VPS's, or
        It can be written as (A), where A is a VPS.
    
    We can similarly define the nesting depth depth(S) of any VPS S as follows:
        depth("") = 0
        depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
        depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
        depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
    For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), 
        and ")(" and "(()" are not VPS's.

Requirement:
    Given a VPS represented as string s, return the nesting depth of s.

Example 1:
    Input: s = "(1+(2*3)+((8)/4))+1"
    Output: 3
    Explanation: Digit 8 is inside of 3 nested parentheses in the string.
Example 2:
    Input: s = "(1)+((2))+(((3)))"
    Output: 3

Constraints:
    1 <= s.length <= 100
    s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
    It is guaranteed that parentheses expression s is a VPS.
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        # exception case
        if not isinstance(s, str) or len(s) <= 0:
            return 0
        # border case
        if len(s) == 1:
            # assert s != "(" and s != ")"
            return 0
        if len(s) == 2:
            # assert (s[0] != "(" and s[1] != ")") or s == "()"
            return 1 if s == "()" else 0
        # main method: dfs & Stack
        return self._maxDepth(s)

    def _maxDepth(self, s: str) -> int:
        # now, 3 <= len(s)
        len_s = len(s)
        # op_set = {"+", "-", "*", "/"}  # operator set  (Do NOT care about numbers and operators!)
        paren_stack = []  # store the index of every "("
        max_stack_depth = 0  # this is just the answer: the max depth of stack == the max depth of paired parentheses

        cur_index = 0
        cur_stack_depth = 0
        while cur_index < len_s:  # scan every char from leftmost to rightmost
            cur_char = s[cur_index]
            if cur_char == "(":
                paren_stack.append(cur_index)  # put "(" into stack
                cur_stack_depth += 1  # stack depth plus 1
                max_stack_depth = max(max_stack_depth, cur_stack_depth)  # update max stack depth
            elif cur_char == ")":
                paren_stack.pop()  # pop "(" out of stack
                cur_stack_depth -= 1  # stack depth minus 1
            else:
                pass  # do nothing
            cur_index += 1

        return max_stack_depth


def main():
    # Example 1: Output: 3
    s = "(1+(2*3)+((8)/4))+1"

    # Example 2: Output: 3
    # s = "(1)+((2))+(((3)))"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxDepth(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
