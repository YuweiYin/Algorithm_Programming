#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0947-Most-Stones-Removed-with-Same-Row-or-Column.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-14
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0947 - (Hard) - Most Stones Removed with Same Row or Column
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

Description & Requirement:
    On a 2D plane, we place n stones at some integer coordinate points. 
    Each coordinate point may have at most one stone.

    A stone can be removed if it shares either the same row 
    or the same column as another stone that has not been removed.

    Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, 
    return the largest possible number of stones that can be removed.

Example 1:
    Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    Output: 5
    Explanation: One way to remove 5 stones is as follows:
        1. Remove stone [2,2] because it shares the same row as [2,1].
        2. Remove stone [2,1] because it shares the same column as [0,1].
        3. Remove stone [1,2] because it shares the same row as [1,0].
        4. Remove stone [1,0] because it shares the same column as [0,0].
        5. Remove stone [0,1] because it shares the same row as [0,0].
        Stone [0,0] cannot be removed since it does not share a row/column 
            with another stone still on the plane.
Example 2:
    Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    Output: 3
    Explanation: One way to make 3 moves is as follows:
        1. Remove stone [2,2] because it shares the same row as [2,0].
        2. Remove stone [2,0] because it shares the same column as [0,0].
        3. Remove stone [0,2] because it shares the same row as [0,0].
        Stones [0,0] and [1,1] cannot be removed since they do not share a row/column 
            with another stone still on the plane.
Example 3:
    Input: stones = [[0,0]]
    Output: 0
    Explanation: [0,0] is the only stone on the plane, so you cannot remove it.

Constraints:
    1 <= stones.length <= 1000
    0 <= xi, yi <= 10^4
    No two stones are at the same coordinate point.
"""


class UnionFindSet:
    def __init__(self):
        self.sets = dict()
        self.rank = dict()

    def find(self, x: int) -> int:
        if x not in self.sets:
            self.sets[x] = x
            self.rank[x] = 1
            return x
        if self.sets[x] == x:
            return x
        self.sets[x] = self.find(self.sets[x])
        return self.sets[x]

    def union(self, x: int, y: int):
        x_set, y_set = self.find(x), self.find(y)
        if x_set == y_set:
            return
        if self.rank[x_set] < self.rank[y_set]:
            x_set, y_set = y_set, x_set
        self.rank[x_set] += self.rank[y_set]
        self.sets[y_set] = x_set

    def number_of_connected_component(self) -> int:
        return sum(1 for x, x_set in self.sets.items() if x == x_set)


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # exception case
        assert isinstance(stones, list) and len(stones) >= 1
        # main method: (Union Find Set)
        return self._removeStones(stones)

    def _removeStones(self, stones: List[List[int]]) -> int:
        """
        Runtime: 375 ms, faster than 58.42% of Python3 submissions for Most Stones Removed with Same Row or Column.
        Memory Usage: 14.7 MB, less than 72.25% of Python3 submissions for Most Stones Removed with Same Row or Column.
        """
        assert isinstance(stones, list) and len(stones) >= 1

        INF = int(1e9+7)
        ufs = UnionFindSet()
        for x, y in stones:
            ufs.union(x, y + INF)

        return len(stones) - ufs.number_of_connected_component()


def main():
    # Example 1: Output: 5
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]

    # Example 2: Output: 3
    # stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]

    # Example 3: Output: 0
    # stones = [[0, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.removeStones(stones)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
