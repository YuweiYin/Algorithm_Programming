#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1021-Remove-Outermost-Parentheses.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-28
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 1021 - (Easy) - Remove Outermost Parentheses
https://leetcode.com/problems/remove-outermost-parentheses/

Description & Requirement:
    A valid parentheses string is either empty "", "(" + A + ")", or A + B, 
    where A and B are valid parentheses strings, and + represents string concatenation.

    For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
    A valid parentheses string s is primitive if it is nonempty, 
    and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

    Given a valid parentheses string s, consider its primitive decomposition: 
    s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

    Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example 1:
    Input: s = "(()())(())"
    Output: "()()()"
    Explanation: 
        The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
        After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:
    Input: s = "(()())(())(()(()))"
    Output: "()()()()(())"
    Explanation: 
        The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
        After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:
    Input: s = "()()"
    Output: ""
    Explanation: 
        The input string is "()()", with primitive decomposition "()" + "()".
        After removing outer parentheses of each part, this is "" + "" = "".

Constraints:
    1 <= s.length <= 10^5
    s[i] is either '(' or ')'.
    s is a valid parentheses string.
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (stack)
        return self._removeOuterParentheses(s)

    def _removeOuterParentheses(self, s: str) -> str:
        """
        Runtime: 42 ms, faster than 80.67% of Python3 online submissions for Remove Outermost Parentheses.
        Memory Usage: 13.8 MB, less than 91.87% of Python3 online submissions for Remove Outermost Parentheses.
        """
        assert isinstance(s, str) and len(s) >= 1

        res = ""
        stack = []
        for idx, cur_ch in enumerate(s):
            if cur_ch == "(":
                stack.append(idx)
            elif cur_ch == ")":
                assert len(stack) > 0
                left_idx = stack.pop()
                if len(stack) == 0:
                    res += s[left_idx + 1: idx]  # get rid of the outermost "(" and ")"
            else:
                pass

        return res


def main():
    # Example 1: Output: "()()()"
    s = "(()())(())"

    # Example 2: Output: "()()()()(())"
    # s = "(()())(())(()(()))"

    # Example 3: Output: ""
    # s = "()()"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.removeOuterParentheses(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
