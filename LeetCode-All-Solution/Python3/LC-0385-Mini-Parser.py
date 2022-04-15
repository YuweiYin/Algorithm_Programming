#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0385-Mini-Parser.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-15
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0385 - (Medium) - Mini Parser
https://leetcode.com/problems/mini-parser/

Description & Requirement:
    Given a string s represents the serialization of a nested list, 
    implement a parser to deserialize it and return the deserialized NestedInteger.

    Each element is either an integer or a list whose elements may also be integers or other lists.

Example 1:
    Input: s = "324"
    Output: 324
    Explanation: You should return a NestedInteger object which contains a single integer 324.
Example 2:
    Input: s = "[123,[456,[789]]]"
    Output: [123,[456,[789]]]
    Explanation: Return a NestedInteger object containing a nested list with 2 elements:
        1. An integer containing value 123.
        2. A nested list containing two elements:
            i.  An integer containing value 456.
            ii. A nested list with one element:
                a. An integer containing value 789

Constraints:
    1 <= s.length <= 5 * 10^4
    s consists of digits, square brackets "[]", negative sign '-', and commas ','.
    s is the serialization of valid NestedInteger.
    All the values in the input are in the range [-10^6, 10^6].
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise, initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # exception case
        assert isinstance(s, str) and len(s) >= 1
        # main method: (deal with each char in the string)
        return self._deserialize(s)

    def _deserialize(self, s: str) -> NestedInteger:
        """
        Runtime: 72 ms, faster than 88.33% of Python3 online submissions for Mini Parser.
        Memory Usage: 17.4 MB, less than 73.60% of Python3 online submissions for Mini Parser.
        """
        s_idx = [0]

        def __dfs() -> NestedInteger:
            if s[s_idx[0]] == "[":  # add a nested list
                s_idx[0] += 1
                ni = NestedInteger()
                while s[s_idx[0]] != "]":
                    ni.add(__dfs())  # recursion
                    if s[s_idx[0]] == ",":
                        s_idx[0] += 1
                s_idx[0] += 1
                return ni
            else:  # add a number
                if s[s_idx[0]] == "-":
                    neg = True  # record the sign
                    s_idx[0] += 1
                else:
                    neg = False
                # add a digit
                number = 0
                while s_idx[0] < len(s) and s[s_idx[0]].isdigit():
                    number *= 10
                    number += int(s[s_idx[0]])
                    s_idx[0] += 1
                if neg:
                    number = - number
                return NestedInteger(number)

        return __dfs()


def main():
    # Example 1: Output: 324
    # s = "324"

    # Example 2: Output: [123,[456,[789]]]
    s = "[123,[456,[789]]]"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.deserialize(s)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
