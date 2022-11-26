#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0882-Reachable-Nodes-In-Subdivided-Graph.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-26
=================================================================="""

import sys
import time
from typing import List
import heapq
import collections
# import functools

"""
LeetCode - 0882 - (Hard) - Reachable Nodes In Subdivided Graph
https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

Description & Requirement:
    You are given an undirected graph (the "original graph") with n nodes labeled from 0 to n - 1. 
    You decide to subdivide each edge in the graph into a chain of nodes, 
    with the number of new nodes varying between each edge.

    The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnt_i] indicates that 
    there is an edge between nodes ui and vi in the original graph, and cnt_i is the total number of new nodes 
    that you will subdivide the edge into. Note that cnt_i == 0 means you will not subdivide the edge.

    To subdivide the edge [ui, vi], replace it with (cnt_i + 1) new edges and cnt_i new nodes. 
    The new nodes are x1, x2, ..., x_cnt_i, 
    and the new edges are [ui, x1], [x1, x2], [x2, x3], ..., [x_cnt_i-1, x_cnt_i], [x_cnt_i, vi].

    In this new graph, you want to know how many nodes are reachable from the node 0, 
    where a node is reachable if the distance is maxMoves or less.

    Given the original graph and maxMoves, return the number of nodes that are reachable from node 0 in the new graph.

Example 1:
    Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
    Output: 13
    Explanation: The edge subdivisions are shown in the image above.
        The nodes that are reachable are highlighted in yellow.
Example 2:
    Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
    Output: 23
Example 3:
    Input: edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
    Output: 1
    Explanation: Node 0 is disconnected from the rest of the graph, so only node 0 is reachable.

Constraints:
    0 <= edges.length <= min(n * (n - 1) / 2, 10^4)
    edges[i].length == 3
    0 <= ui < vi < n
    There are no multiple edges in the graph.
    0 <= cnt_i <= 10^4
    0 <= maxMoves <= 10^9
    1 <= n <= 3000
"""


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(maxMoves, int) and maxMoves >= 0
        assert isinstance(edges, list)
        # main method: (Dijkstra)
        return self._reachableNodes(edges, maxMoves, n)

    def _reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        """
        Runtime: 679 ms, faster than 82.20% of Python3 online submissions for Reachable Nodes In Subdivided Graph.
        Memory Usage: 21.9 MB, less than 42.37% of Python3 online submissions for Reachable Nodes In Subdivided Graph.
        """
        assert isinstance(n, int) and n >= 1
        assert isinstance(maxMoves, int) and maxMoves >= 0
        assert isinstance(edges, list)

        adj = collections.defaultdict(list)
        for u, v, nodes in edges:
            adj[u].append([v, nodes])
            adj[v].append([u, nodes])

        used = {}
        visited = set()
        res = 0
        pq = [[0, 0]]

        while pq and pq[0][0] <= maxMoves:
            step, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            res += 1
            for v, nodes in adj[u]:
                if nodes + step + 1 <= maxMoves and v not in visited:
                    heapq.heappush(pq, [nodes + step + 1, v])
                used[(u, v)] = min(nodes, maxMoves - step)

        for u, v, nodes in edges:
            res += min(nodes, used.get((u, v), 0) + used.get((v, u), 0))

        return res


def main():
    # Example 1: Output: 13
    # edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2]]
    # maxMoves = 6
    # n = 3

    # Example 2: Output: 23
    # edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]]
    # maxMoves = 10
    # n = 4

    # Example 3: Output: 1
    edges = [[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]]
    maxMoves = 17
    n = 5

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.reachableNodes(edges, maxMoves, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
