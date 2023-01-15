#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1061-Lexicographically-Smallest-Equivalent-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-14
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1061 - (Medium) - Lexicographically Smallest Equivalent String
https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

Description & Requirement:
    You are given two strings of the same length s1 and s2 and a string baseStr.

    We say s1[i] and s2[i] are equivalent characters.
        For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.

    Equivalent characters follow the usual rules of any equivalence relation:
        Reflexivity: 'a' == 'a'.
        Symmetry: 'a' == 'b' implies 'b' == 'a'.
        Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.

    For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

    Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

Example 1:
    Input: s1 = "parker", s2 = "morris", baseStr = "parser"
    Output: "makkek"
    Explanation: Based on the equivalency information in s1 and s2, 
        we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
        The characters in each group are equivalent and sorted in lexicographical order.
        So the answer is "makkek".
Example 2:
    Input: s1 = "hello", s2 = "world", baseStr = "hold"
    Output: "hdld"
    Explanation: Based on the equivalency information in s1 and s2, 
        we can group their characters as [h,w], [d,e,o], [l,r].
        So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
Example 3:
    Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
    Output: "aauaaaaada"
    Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], 
        thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".

Constraints:
    1 <= s1.length, s2.length, baseStr <= 1000
    s1.length == s2.length
    s1, s2, and baseStr consist of lowercase English letters.
"""


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]

    def find(self, x):
        if x != self.root[x]:
            root_x = self.find(self.root[x])
            self.root[x] = root_x
            return root_x
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if root_x < root_y:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # exception case
        assert isinstance(s1, str) and len(s1) >= 1
        assert isinstance(s2, str) and len(s2) >= 1
        assert isinstance(baseStr, str) and len(baseStr) >= 1
        # main method: (Union Find Set)
        return self._smallestEquivalentString(s1, s2, baseStr)

    def _smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        assert isinstance(s1, str) and len(s1) >= 1
        assert isinstance(s2, str) and len(s2) >= 1
        assert isinstance(baseStr, str) and len(baseStr) >= 1

        ord_a = ord("a")
        ufs = UnionFind(26)
        for i in range(len(s1)):
            ufs.union(ord(s1[i]) - ord_a, ord(s2[i]) - ord_a)

        res = ""
        for w in baseStr:
            res += chr(ufs.find(ord(w) - ord_a) + ord_a)

        return res


def main():
    # Example 1: Output: "makkek"
    # s1 = "parker"
    # s2 = "morris"
    # baseStr = "parser"

    # Example 2: Output: "hdld"
    # s1 = "hello"
    # s2 = "world"
    # baseStr = "hold"

    # Example 3: Output: "aauaaaaada"
    s1 = "leetcode"
    s2 = "programs"
    baseStr = "sourcecode"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.smallestEquivalentString(s1, s2, baseStr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
