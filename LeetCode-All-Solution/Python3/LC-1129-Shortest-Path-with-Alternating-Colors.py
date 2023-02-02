#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1129-Shortest-Path-with-Alternating-Colors.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-02
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1129 - (Medium) - Shortest Path with Alternating Colors
https://leetcode.com/problems/shortest-path-with-alternating-colors/

Description & Requirement:
    You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. 
    Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

    You are given two arrays redEdges and blueEdges where:
        redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
        blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.

    Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x 
    such that the edge colors alternate along the path, or -1 if such a path does not exist.

Example 1:
    Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
    Output: [0,1,-1]
Example 2:
    Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
    Output: [0,1,-1]

Constraints:
    1 <= n <= 100
    0 <= redEdges.length, blueEdges.length <= 400
    redEdges[i].length == blueEdges[j].length == 2
    0 <= ai, bi, uj, vj < n
"""


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(redEdges, list) and isinstance(blueEdges, list)
        # main method: (BFS)
        return self._shortestAlternatingPaths(n, redEdges, blueEdges)

    def _shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        assert isinstance(n, int) and n >= 1
        assert isinstance(redEdges, list) and isinstance(blueEdges, list)

        graph = [[] for _ in range(n)]
        for x, y in redEdges:
            graph[x].append((y, 0))
        for x, y in blueEdges:
            graph[x].append((y, 1))

        dist = [-1] * n
        visited = {(0, 0), (0, 1)}
        queue = [(0, 0), (0, 1)]
        level = 0
        while len(queue) > 0:
            new_queue = []
            for x, color in queue:
                if dist[x] == -1:
                    dist[x] = level
                for p in graph[x]:
                    if p[1] != color and p not in visited:
                        visited.add(p)
                        new_queue.append(p)
            queue = new_queue
            level += 1

        return dist


def main():
    # Example 1: Output: [0,1,-1]
    n = 3
    redEdges = [[0, 1], [1, 2]]
    blueEdges = []

    # Example 2: Output: [0,1,-1]
    # n = 3
    # redEdges = [[0, 1]]
    # blueEdges = [[2, 1]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.shortestAlternatingPaths(n, redEdges, blueEdges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
