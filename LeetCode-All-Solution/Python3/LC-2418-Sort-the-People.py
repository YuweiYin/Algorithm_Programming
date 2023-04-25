#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2418-Sort-the-People.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-25
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2418 - (Easy) - Sort the People
https://leetcode.com/problems/sort-the-people/

Description & Requirement:
    You are given an array of strings names, and an array heights that 
    consists of distinct positive integers. Both arrays are of length n.

    For each index i, names[i] and heights[i] denote the name and height of the i-th person.

    Return names sorted in descending order by the people's heights.

Example 1:
    Input: names = ["Mary","John","Emma"], heights = [180,165,170]
    Output: ["Mary","Emma","John"]
    Explanation: Mary is the tallest, followed by Emma and John.
Example 2:
    Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
    Output: ["Bob","Alice","Bob"]
    Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

Constraints:
    n == names.length == heights.length
    1 <= n <= 10^3
    1 <= names[i].length <= 20
    1 <= heights[i] <= 10^5
    names[i] consists of lower and upper case English letters.
    All the values of heights are distinct.
"""


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # exception case
        assert isinstance(names, list) and len(names) >= 1
        assert isinstance(heights, list) and len(names) == len(heights)
        # main method: (sorting)
        return self._sortPeople(names, heights)

    def _sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        assert isinstance(names, list) and len(names) >= 1
        assert isinstance(heights, list) and len(names) == len(heights)

        indices = list(range(len(names)))
        indices.sort(key=lambda x: heights[x], reverse=True)

        return [names[i] for i in indices]


def main():
    # Example 1: Output: ["Mary","Emma","John"]
    # names = ["Mary", "John", "Emma"]
    # heights = [180, 165, 170]

    # Example 2: Output: ["Bob","Alice","Bob"]
    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sortPeople(names, heights)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
