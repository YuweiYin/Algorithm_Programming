#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2363-Merge-Similar-Items.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-28
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 2363 - (Easy) - Merge Similar Items
https://leetcode.com/problems/merge-similar-items/

Description & Requirement:
    You are given two 2D integer arrays, items1 and items2, representing two sets of items. 
    Each array items has the following properties:
        items[i] = [value_i, weight_i] where value_i represents the value and weight_i 
            represents the weight of the ith item.
        The value of each item in items is unique.

    Return a 2D integer array ret where ret[i] = [value_i, weight_i], 
    with weight_i being the sum of weights of all items with value value_i.

    Note: ret should be returned in ascending order by value.

Example 1:
    Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
    Output: [[1,6],[3,9],[4,5]]
    Explanation: 
        The item with value = 1 occurs in items1 with weight = 1 and 
            in items2 with weight = 5, total weight = 1 + 5 = 6.
        The item with value = 3 occurs in items1 with weight = 8 and 
            in items2 with weight = 1, total weight = 8 + 1 = 9.
        The item with value = 4 occurs in items1 with weight = 5, total weight = 5.  
        Therefore, we return [[1,6],[3,9],[4,5]].
Example 2:
    Input: items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]
    Output: [[1,4],[2,4],[3,4]]
    Explanation: 
        The item with value = 1 occurs in items1 with weight = 1 and 
            in items2 with weight = 3, total weight = 1 + 3 = 4.
        The item with value = 2 occurs in items1 with weight = 3 and 
            in items2 with weight = 1, total weight = 3 + 1 = 4.
        The item with value = 3 occurs in items1 with weight = 2 and 
            in items2 with weight = 2, total weight = 2 + 2 = 4.
        Therefore, we return [[1,4],[2,4],[3,4]].
Example 3:
    Input: items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]
    Output: [[1,7],[2,4],[7,1]]
    Explanation:
        The item with value = 1 occurs in items1 with weight = 3 and 
            in items2 with weight = 4, total weight = 3 + 4 = 7. 
        The item with value = 2 occurs in items1 with weight = 2 and 
            in items2 with weight = 2, total weight = 2 + 2 = 4. 
        The item with value = 7 occurs in items2 with weight = 1, total weight = 1.
        Therefore, we return [[1,7],[2,4],[7,1]].

Constraints:
    1 <= items1.length, items2.length <= 1000
    items1[i].length == items2[i].length == 2
    1 <= value_i, weight_i <= 1000
    Each value_i in items1 is unique.
    Each value_i in items2 is unique.
"""


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(items1, list) and len(items1) >= 1
        assert isinstance(items2, list) and len(items2) >= 1
        # main method: (hash counter)
        return self._mergeSimilarItems(items1, items2)

    def _mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        assert isinstance(items1, list) and len(items1) >= 1
        assert isinstance(items2, list) and len(items2) >= 1

        cnt = collections.Counter()

        for v, w in items1:
            cnt[v] += w

        for v, w in items2:
            cnt[v] += w

        return sorted([a, b] for a, b in cnt.items())


def main():
    # Example 1: Output: [[1,6],[3,9],[4,5]]
    items1 = [[1, 1], [4, 5], [3, 8]]
    items2 = [[3, 1], [1, 5]]

    # Example 2: Output: [[1,4],[2,4],[3,4]]
    # items1 = [[1, 1], [3, 2], [2, 3]]
    # items2 = [[2, 1], [3, 2], [1, 3]]

    # Example 3: Output: [[1,7],[2,4],[7,1]]
    # items1 = [[1, 3], [2, 2]]
    # items2 = [[7, 1], [2, 2], [1, 4]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.mergeSimilarItems(items1, items2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
