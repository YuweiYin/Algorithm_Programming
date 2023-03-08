#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1096-Brace-Expansion-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-07
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1096 - (Hard) - Brace Expansion II
https://leetcode.com/problems/brace-expansion-ii/

Description & Requirement:
    Under the grammar given below, strings can represent a set of lowercase words. 
    Let R(expr) denote the set of words the expression represents.

    The grammar can best be understood through simple examples:

    Single letters represent a singleton set containing that word.
        R("a") = {"a"}
        R("w") = {"w"}

    When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
        R("{a,b,c}") = {"a","b","c"}
        R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)

    When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
        R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
        R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}

    Formally, the three rules for our grammar:
        For every lowercase letter x, we have R(x) = {x}.
        For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
        For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.

    Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

Example 1:
    Input: expression = "{a,b}{c,{d,e}}"
    Output: ["ac","ad","ae","bc","bd","be"]
Example 2:
    Input: expression = "{{a,z},a{b,c},{ab,z}}"
    Output: ["a","ab","ac","z"]
    Explanation: Each distinct word is written only once in the final answer.

Constraints:
    1 <= expression.length <= 60
    expression[i] consists of '{', '}', ','or lowercase English letters.
    The given expression represents a set of words based on the grammar given in the description.
"""


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        # exception case
        assert isinstance(expression, str) and len(expression) >= 1
        # main method: (DFS recursion)
        return self._braceExpansionII(expression)

    def _braceExpansionII(self, expression: str) -> List[str]:
        assert isinstance(expression, str) and len(expression) >= 1

        res = set()

        def __dfs(exp):
            j = exp.find("}")
            if j == -1:
                res.add(exp)
                return
            i = exp.rfind("{", 0, j - 1)
            a, c = exp[:i], exp[j + 1:]
            for b in exp[i + 1: j].split(","):
                __dfs(a + b + c)

        __dfs(expression)

        return sorted(list(res))


def main():
    # Example 1: Output: ["ac","ad","ae","bc","bd","be"]
    expression = "{a,b}{c,{d,e}}"

    # Example 2: Output: ["a","ab","ac","z"]
    # expression = "{{a,z},a{b,c},{ab,z}}"

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.braceExpansionII(expression)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
