#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1617-Count-Subtrees-With-Max-Distance-Between-Cities.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-12
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1617 - (Hard) - Count Subtrees With Max Distance Between Cities
https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

Description & Requirement:
    There are n cities numbered from 1 to n. You are given an array edges of size n-1, 
    where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. 
    There exists a unique path between each pair of cities. In other words, the cities form a tree.

    A subtree is a subset of cities where every city is reachable from every other city in the subset, 
    where the path between each pair passes through only the cities from the subset. 
    Two subtrees are different if there is a city in one subtree that is not present in the other.

    For each d from 1 to n-1, find the number of subtrees in which the maximum distance 
    between any two cities in the subtree is equal to d.

    Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees 
    in which the maximum distance between any two cities is equal to d.

    Notice that the distance between the two cities is the number of edges in the path between them.

Example 1:
    Input: n = 4, edges = [[1,2],[2,3],[2,4]]
    Output: [3,4,0]
    Explanation:
        The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
        The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
        No subtree has two nodes where the max distance between them is 3.
Example 2:
    Input: n = 2, edges = [[1,2]]
    Output: [1]
Example 3:
    Input: n = 3, edges = [[1,2],[2,3]]
    Output: [2,1]

Constraints:
    2 <= n <= 15
    edges.length == n-1
    edges[i].length == 2
    1 <= ui, vi <= n
    All pairs (ui, vi) are distinct.
"""


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(n, int) and n >= 2
        assert isinstance(edges, list) and len(edges) == (n - 1)
        # main method: (DFS + binary mask)
        return self._countSubgraphsForEachDiameter(n, edges)

    def _countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        assert isinstance(n, int) and n >= 2
        assert isinstance(edges, list) and len(edges) == (n - 1)

        graph = collections.defaultdict(list)
        for _from, _to in edges:
            _from, _to = _from - 1, _to - 1
            graph[_from].append(_to)
            graph[_to].append(_from)

        def __dfs(node: int, dis: int = 0):
            nonlocal mx, nxt, msk
            if mx < dis:
                mx, nxt = dis, node
            msk ^= 1 << node
            for nei in graph[node]:
                if msk >> nei & 0x01:
                    __dfs(nei, dis + 1)

        res = [0] * (n - 1)
        nxt = mx = 0
        for mask in range(1, 1 << n):
            if mask & (mask - 1) == 0:
                continue
            msk, mx = mask, 0
            cur = msk.bit_length() - 1
            __dfs(cur)
            if msk == 0:
                msk, mx = mask, 0
                __dfs(nxt)
                res[mx - 1] += 1

        return res


def main():
    # Example 1: Output: [3,4,0]
    # n = 4
    # edges = [[1, 2], [2, 3], [2, 4]]

    # Example 2: Output: [1]
    # n = 2
    # edges = [[1, 2]]

    # Example 3: Output: [2,1]
    n = 3
    edges = [[1, 2], [2, 3]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.countSubgraphsForEachDiameter(n, edges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
