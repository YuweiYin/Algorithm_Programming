#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0990-Satisfiability-of-Equality-Equations.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-03
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0990 - (Medium) - Satisfiability of Equality Equations
https://leetcode.com/problems/satisfiability-of-equality-equations/

Description & Requirement:
    You are given an array of strings equations that represent relationships between variables 
    where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".
    Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

    Return true if it is possible to assign integers to variable names 
    so as to satisfy all the given equations, or false otherwise.

Example 1:
    Input: equations = ["a==b","b!=a"]
    Output: false
    Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
    There is no way to assign the variables to satisfy both equations.
Example 2:
    Input: equations = ["b==a","a==b"]
    Output: true
    Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Constraints:
    1 <= equations.length <= 500
    equations[i].length == 4
    equations[i][0] is a lowercase letter.
    equations[i][1] is either '=' or '!'.
    equations[i][2] is '='.
    equations[i][3] is a lowercase letter.
"""


class UnionFind:
    def __init__(self):
        self.parent = list(range(26))

    def find(self, item):
        if item == self.parent[item]:
            return item
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, item_1, item_2):
        self.parent[self.find(item_1)] = self.find(item_2)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # exception case
        assert isinstance(equations, list) and len(equations) >= 1
        for equ in equations:
            assert isinstance(equ, str) and len(equ) == 4
        # main method: (union find set)
        return self._equationsPossible(equations)

    def _equationsPossible(self, equations: List[str]) -> bool:
        assert isinstance(equations, list) and len(equations) >= 1

        uf = UnionFind()
        for equ in equations:
            if equ[1] == "=":
                idx_1 = ord(equ[0]) - ord("a")
                idx_2 = ord(equ[3]) - ord("a")
                uf.union(idx_1, idx_2)

        for equ in equations:
            if equ[1] == "!":
                idx_1 = ord(equ[0]) - ord("a")
                idx_2 = ord(equ[3]) - ord("a")
                if uf.find(idx_1) == uf.find(idx_2):
                    return False

        return True


def main():
    # Example 1: Output: false
    equations = ["a==b", "b!=a"]

    # Example 2: Output: true
    # equations = ["b==a", "a==b"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.equationsPossible(equations)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
