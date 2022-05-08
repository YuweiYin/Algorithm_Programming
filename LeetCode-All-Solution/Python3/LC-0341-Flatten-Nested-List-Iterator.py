#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0341-Flatten-Nested-List-Iterator.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-08
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0341 - (Medium) - Flatten Nested List Iterator
https://leetcode.com/problems/flatten-nested-list-iterator/

Description & Requirement:
    You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements 
    may also be integers or other lists. Implement an iterator to flatten it.

    Implement the NestedIterator class:
        NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
        int next() Returns the next integer in the nested list.
        boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

    Your code will be tested with the following pseudocode:
        initialize iterator with nestedList
        res = []
        while iterator.hasNext()
            append iterator.next() to the end of res
        return res

    If res matches the expected flattened list, then your code will be judged as correct.

Example 1:
    Input: nestedList = [[1,1],2,[1,1]]
    Output: [1,1,2,1,1]
    Explanation: By calling next repeatedly until hasNext returns false, 
        the order of elements returned by next should be: [1,1,2,1,1].
Example 2:
    Input: nestedList = [1,[4,[6]]]
    Output: [1,4,6]
    Explanation: By calling next repeatedly until hasNext returns false, 
        the order of elements returned by next should be: [1,4,6].

Constraints:
    1 <= nestedList.length <= 500
    The values of the integers in the nested list is in the range [-10^6, 10^6].
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, item):
        self.item = item

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return isinstance(self.item, int)

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.item

    # def getList(self) -> [NestedInteger]:
    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.item


class NestedIterator:

    def __init__(self, nestedList: List[NestedInteger]):
        self.val_list = []
        self.cursor = 0
        self._dfs(nestedList)

    def next(self) -> int:
        if self.hasNext():
            self.cursor += 1
            return self.val_list[self.cursor - 1]
        else:
            return int(1e9+7)  # val \in [-10^6, 10^6]

    def hasNext(self) -> bool:
        return self.cursor != len(self.val_list)

    def _dfs(self, nestedList: List[NestedInteger]):
        for ni in nestedList:
            if ni.isInteger():
                self.val_list.append(ni.getInteger())
            else:
                self._dfs(ni.getList())


def main():
    # Example 1: Output: [1,1,2,1,1]
    # nestedList = [[1, 1], 2, [1, 1]]

    # Example 2: Output: [1,4,6]
    # nestedList = [1, [4, [6]]]

    # init instance
    # solution = Solution()
    nl1 = NestedInteger([NestedInteger(1), NestedInteger(1)])
    nl2 = NestedInteger(2)
    nl3 = NestedInteger([NestedInteger(1), NestedInteger(1)])
    nestedList = [nl1, nl2, nl3]
    ni, ans = NestedIterator(nestedList), []

    # run & time
    start = time.process_time()
    # ans = solution.find132pattern(nestedList)
    while ni.hasNext():
        ans.append(ni.next())
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
