#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1489-Find-Critical-and-Pseudo-Critical-Edges-in-Minimum-Spanning-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-19
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 1489 - (Hard) Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

Description & Requirement:
    Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, 
    and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and 
    weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges 
    that connects all vertices without cycles and with the minimum possible total edge weight.

    Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). 
    An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. 
    On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

    Note that you can return the indices of the edges in any order.

Example 1:
    Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    Output: [[0,1],[2,3,4,5]]
    Explanation: The figure above describes the graph.
        The following figure shows all the possible MSTs:
        Notice that the two edges 0 and 1 appear in all MSTs, 
        therefore they are critical edges, 
        so we return them in the first list of the output.
        The edges 2, 3, 4, and 5 are only part of some MSTs, 
        therefore they are considered pseudo-critical edges. 
        We add them to the second list of the output.
Example 2:
    Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
    Output: [[],[0,1,2,3]]
    Explanation: We can observe that since all 4 edges have equal weight, 
        choosing any 3 edges from the given 4 will yield an MST. 
        Therefore all 4 edges are pseudo-critical.

Constraints:
    2 <= n <= 100
    1 <= edges.length <= min(200, n * (n - 1) / 2)
    edges[i].length == 3
    0 <= ai < bi < n
    1 <= weighti <= 1000
    All pairs (ai, bi) are distinct.
"""


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        self.setCount = n
    
    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]
    
    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y


class TarjanSCC:
    def __init__(self, n: int, edges: List[List[int]], edgesId: List[List[int]]):
        self.n = n
        self.edges = edges
        self.edgesId = edgesId
        self.low = [-1] * n
        self.dfn = [-1] * n
        self.ans = list()
        self.ts = -1
    
    def getCuttingEdge(self) -> List[int]:
        for i in range(self.n):
            if self.dfn[i] == -1:
                self.pGetCuttingEdge(i, -1)
        return self.ans
    
    def pGetCuttingEdge(self, u: int, parentEdgeId: int):
        self.ts += 1
        self.low[u] = self.dfn[u] = self.ts
        for v, iden in zip(self.edges[u], self.edgesId[u]):
            if self.dfn[v] == -1:
                self.pGetCuttingEdge(v, iden)
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[v] > self.dfn[u]:
                    self.ans.append(iden)
            elif iden != parentEdgeId:
                self.low[u] = min(self.low[u], self.dfn[v])


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(n, int) and n >= 2
        assert isinstance(edges, list) and len(edges) >= 1
        # main method: (Union Find Set & Tarjan Algorithm)
        return self._findCriticalAndPseudoCriticalEdges(n, edges)

    def _findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        assert isinstance(n, int) and n >= 2
        assert isinstance(edges, list) and len(edges) >= 1

        m = len(edges)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])

        uf = UnionFind(n)
        res0 = []
        label = [0] * m

        i = 0
        while i < m:
            w = edges[i][2]
            j = i
            while j < m and edges[j][2] == edges[i][2]:
                j += 1

            compToId = dict({})
            gn = 0

            for k in range(i, j):
                x = uf.findset(edges[k][0])
                y = uf.findset(edges[k][1])
                if x != y:
                    if x not in compToId:
                        compToId[x] = gn
                        gn += 1
                    if y not in compToId:
                        compToId[y] = gn
                        gn += 1
                else:
                    label[edges[k][3]] = -1

            gm = collections.defaultdict(list)
            gmid = collections.defaultdict(list)

            for k in range(i, j):
                x = uf.findset(edges[k][0])
                y = uf.findset(edges[k][1])
                if x != y:
                    idx, idy = compToId[x], compToId[y]
                    gm[idx].append(idy)
                    gmid[idx].append(edges[k][3])
                    gm[idy].append(idx)
                    gmid[idy].append(edges[k][3])

            bridges = TarjanSCC(gn, gm, gmid).getCuttingEdge()
            res0.extend(bridges)
            for iden in bridges:
                label[iden] = 1

            for k in range(i, j):
                uf.unite(edges[k][0], edges[k][1])

            i = j

        res1 = [i for i in range(m) if label[i] == 0]

        return [res0, res1]


def main():
    # Example 1: Output: [[0,1],[2,3,4,5]]
    # n = 5
    # edges = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]

    # Example 2: Output: [[],[0,1,2,3]]
    n = 4
    edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.findCriticalAndPseudoCriticalEdges(n, edges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
