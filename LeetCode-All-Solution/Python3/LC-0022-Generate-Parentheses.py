#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0022-Generate-Parentheses.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-24
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0022 - (Medium) - Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

Description & Requirement:
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
    Input: n = 1
    Output: ["()"]

Constraints:
    1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # exception case
        if not isinstance(n, int) or n <= 0:
            return []  # Error input type
        if n == 1:
            return ["()"]
        # main method: (stack & dfs & backtrace.)
        return self._generateParenthesis(n)

    def _generateParenthesis(self, n: int) -> List[str]:
        assert n > 1

        res_list = []
        # paren_stack = []  # stack of parenthesis, when the stack is empty, can't put in ")"

        def __dfs(cur_combo: List[str], cur_left_paren: int, cur_right_paren: int):
            if cur_right_paren == n:  # use up all ")", done
                res_list.append("".join(cur_combo[:]))
                return
            if cur_left_paren == n:  # use up all "(", so append all rest ")" to the end
                cur_combo_str = "".join(cur_combo[:])
                for _ in range(cur_left_paren - cur_right_paren):
                    cur_combo_str += ")"
                res_list.append(cur_combo_str)
                return
            for next_paren in ["(", ")"]:  # for the current step, choose either "(" or ")"
                # if len(paren_stack) == 0 and next_paren == ")":
                #     continue
                if cur_left_paren == cur_right_paren and next_paren == ")":  # can't put in ")" now
                    continue
                # paren_stack.append(next_paren)
                cur_combo.append(next_paren)
                if next_paren == "(":
                    __dfs(cur_combo, cur_left_paren + 1, cur_right_paren)  # add "(", go deeper
                else:
                    __dfs(cur_combo, cur_left_paren, cur_right_paren + 1)  # add ")", go deeper
                cur_combo.pop()  # backtrace

        # paren_stack.append("(")
        __dfs(["("], 1, 0)
        return res_list


def main():
    # Example 1: Output: ["((()))","(()())","(())()","()(())","()()()"]
    # n = 3

    # Example 2: Output: ["()"]
    # n = 1

    # Example 3: Output:
    n = 8

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.generateParenthesis(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
