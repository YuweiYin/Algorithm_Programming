#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1971-Find-if-Path-Exists-in-Graph.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-19
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1971 - (Easy) - Find if Path Exists in Graph
https://leetcode.com/problems/find-if-path-exists-in-graph/

Description & Requirement:
    There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 
    The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] 
    denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, 
    and no vertex has an edge to itself.

    You want to determine if there is a valid path that exists from vertex source to vertex destination.

    Given edges and the integers n, source, and destination, 
    return true if there is a valid path from source to destination, or false otherwise.

Example 1:
    Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    Output: true
    Explanation: There are two paths from vertex 0 to vertex 2:
        - 0 → 1 → 2
        - 0 → 2
Example 2:
    Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
    Output: false
    Explanation: There is no path from vertex 0 to vertex 5.

Constraints:
    1 <= n <= 2 * 10^5
    0 <= edges.length <= 2 * 10^5
    edges[i].length == 2
    0 <= u_i, v_i <= n - 1
    u_i != v_i
    0 <= source, destination <= n - 1
    There are no duplicate edges.
    There are no self edges.
"""


class UnionFindSet:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0 for _ in range(n)]

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]

        while x != root:
            x, self.parent[x] = self.parent[x], root

        return root

    def union(self, x: int, y: int) -> None:
        x_root, y_root = self.find(x), self.find(y)

        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                x_root, y_root = y_root, x_root

            self.parent[y_root] = x_root

            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(source, int) and 0 <= source <= n - 1
        assert isinstance(destination, int) and 0 <= destination <= n - 1
        assert isinstance(edges, list)
        # main method: (union find set)
        return self._validPath(n, edges, source, destination)

    def _validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        assert isinstance(n, int) and n >= 1
        assert isinstance(source, int) and 0 <= source <= n - 1
        assert isinstance(destination, int) and 0 <= destination <= n - 1
        assert isinstance(edges, list)

        ufs = UnionFindSet(n)

        for u, v in edges:
            ufs.union(u, v)

        return ufs.is_connected(source, destination)


def main():
    # Example 1: Output: true
    # n = 3
    # edges = [[0, 1], [1, 2], [2, 0]]
    # source = 0
    # destination = 2

    # Example 2: Output: false
    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 5

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.validPath(n, edges, source, destination)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
