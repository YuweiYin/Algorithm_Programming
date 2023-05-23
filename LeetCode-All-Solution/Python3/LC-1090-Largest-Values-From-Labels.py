#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1090-Largest-Values-From-Labels.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-23
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1090 - (Medium) - Largest Values From Labels
https://leetcode.com/problems/largest-values-from-labels/

Description & Requirement:
    There is a set of n items. You are given two integer arrays values and labels 
    where the value and the label of the ith element are values[i] and labels[i] respectively. 
    You are also given two integers numWanted and useLimit.

    Choose a subset s of the n elements such that:
        The size of the subset s is less than or equal to numWanted.
        There are at most useLimit items with the same label in s.

    The score of a subset is the sum of the values in the subset.

    Return the maximum score of a subset s.

Example 1:
    Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
    Output: 9
    Explanation: The subset chosen is the first, third, and fifth items.
Example 2:
    Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
    Output: 12
    Explanation: The subset chosen is the first, second, and third items.
Example 3:
    Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
    Output: 16
    Explanation: The subset chosen is the first and fourth items.

Constraints:
    n == values.length == labels.length
    1 <= n <= 2 * 10^4
    0 <= values[i], labels[i] <= 2 * 10^4
    1 <= numWanted, useLimit <= n
"""


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # exception case
        assert isinstance(values, list) and len(values) >= 1
        assert isinstance(labels, list) and len(labels) == len(values)
        assert isinstance(numWanted, int) and numWanted >= 1
        assert isinstance(useLimit, int) and useLimit >= 1
        # main method: (sorting and hash counter)
        return self._largestValsFromLabels(values, labels, numWanted, useLimit)

    def _largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        assert isinstance(values, list) and len(values) >= 1
        assert isinstance(labels, list) and len(labels) == len(values)
        assert isinstance(numWanted, int) and numWanted >= 1
        assert isinstance(useLimit, int) and useLimit >= 1

        len_val = len(values)

        idx2val = list(range(len_val))
        idx2val.sort(key=lambda index: -values[index])

        res = choose = 0
        cnt = collections.Counter()
        for i in range(len_val):
            label = labels[idx2val[i]]
            if cnt[label] == useLimit:
                continue
            choose += 1
            res += values[idx2val[i]]
            cnt[label] += 1
            if choose == numWanted:
                break

        return res


def main():
    # Example 1: Output: 9
    # values = [5, 4, 3, 2, 1]
    # labels = [1, 1, 2, 2, 3]
    # numWanted = 3
    # useLimit = 1

    # Example 2: Output: 12
    # values = [5, 4, 3, 2, 1]
    # labels = [1, 3, 3, 3, 2]
    # numWanted = 3
    # useLimit = 2

    # Example 3: Output: 16
    values = [9, 8, 8, 7, 6]
    labels = [0, 0, 0, 1, 1]
    numWanted = 3
    useLimit = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largestValsFromLabels(values, labels, numWanted, useLimit)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
