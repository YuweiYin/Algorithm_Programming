#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1579-Remove-Max-Number-of-Edges-to-Keep-Graph-Fully-Traversable.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-30
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1579 - (Hard) - Remove Max Number of Edges to Keep Graph Fully Traversable
https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

Description & Requirement:
    Alice and Bob have an undirected graph of n nodes and three types of edges:
        Type 1: Can be traversed by Alice only.
        Type 2: Can be traversed by Bob only.
        Type 3: Can be traversed by both Alice and Bob.

    Given an array edges where edges[i] = [type_i, ui, vi] represents a bidirectional edge of type type_i 
    between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, 
    the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob 
    if starting from any node, they can reach all other nodes.

    Return the maximum number of edges you can remove, 
    or return -1 if Alice and Bob cannot fully traverse the graph.

Example 1:
    Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
    Output: 2
    Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. 
        The graph will still be fully traversable by Alice and Bob. Removing any additional edge 
        will not make it so. So the maximum number of edges we can remove is 2.
Example 2:
    Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
    Output: 0
    Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:
    Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
    Output: -1
    Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. 
        Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.

Constraints:
    1 <= n <= 10^5
    1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
    edges[i].length == 3
    1 <= type_i <= 3
    1 <= ui < vi <= n
    All tuples (type_i, ui, vi) are distinct.
"""


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        self.set_count = n

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.set_count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        return x == y


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(edges, list) and len(edges) >= 1
        # main method: (Union-Find Set)
        return self._maxNumEdgesToRemove(n, edges)

    def _maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(edges, list) and len(edges) >= 1

        ufa, ufb = UnionFind(n), UnionFind(n)
        res = 0

        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1

        for t, u, v in edges:
            if t == 3:
                if not ufa.union(u, v):
                    res += 1
                else:
                    ufb.union(u, v)

        for t, u, v in edges:
            if t == 1:
                # Alice
                if not ufa.union(u, v):
                    res += 1
            elif t == 2:
                # Bob
                if not ufb.union(u, v):
                    res += 1

        if ufa.set_count != 1 or ufb.set_count != 1:
            return -1

        return res


def main():
    # Example 1: Output: 2
    n = 4
    edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]

    # Example 2: Output: 0
    # n = 4
    # edges = [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]

    # Example 3: Output: -1
    # n = 4
    # edges = [[3, 2, 3], [1, 1, 2], [2, 3, 4]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxNumEdgesToRemove(n, edges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
