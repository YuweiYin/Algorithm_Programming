#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2699-Modify-Graph-Edge-Weights.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-09
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2699 - (Hard) - Modify Graph Edge Weights
https://leetcode.com/problems/modify-graph-edge-weights/

Description & Requirement:
    You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1, 
    and an integer array edges where edges[i] = [ai, bi, wi] indicates that 
    there is an edge between nodes ai and bi with weight wi.

    Some edges have a weight of -1 (wi = -1), while others have a positive weight (wi > 0).

    Your task is to modify all edges with a weight of -1 by assigning them positive integer values 
    in the range [1, 2 * 109] so that the shortest distance between the nodes source and destination becomes 
    equal to an integer target. If there are multiple modifications that make the shortest distance 
    between source and destination equal to target, any of them will be considered correct.

    Return an array containing all edges (even unmodified ones) in any order 
    if it is possible to make the shortest distance from source to destination equal to target, 
    or an empty array if it's impossible.

    Note: You are not allowed to modify the weights of edges with initial positive weights.

Example 1:
    Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
    Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
    Explanation: The graph above shows a possible modification to the edges, 
        making the distance from 0 to 1 equal to 5.
Example 2:
    Input: n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
    Output: []
    Explanation: The graph above contains the initial edges. 
        It is not possible to make the distance from 0 to 2 equal to 6 by modifying the edge with weight -1. 
        So, an empty array is returned.
Example 3:
    Input: n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
    Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
    Explanation: The graph above shows a modified graph having the shortest distance from 0 to 2 as 6.

Constraints:
    1 <= n <= 100
    1 <= edges.length <= n * (n - 1) / 2
    edges[i].length == 3
    0 <= ai, bi < n
    wi = -1 or 1 <= wi <= 10^7
    ai != bi
    0 <= source, destination < n
    source != destination
    1 <= target <= 10^9
    The graph is connected, and there are no self-loops or repeated edges
"""


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]],
                           source: int, destination: int, target: int) -> List[List[int]]:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(edges, list) and 1 <= len(edges) <= int(n * (n - 1) / 2)
        assert isinstance(source, int) and 0 <= source <= n
        assert isinstance(destination, int) and 0 <= destination <= n and source != destination
        assert isinstance(target, int) and target >= 1
        # main method: (Dijkstra)
        return self._modifiedGraphEdges(n, edges, source, destination, target)

    def _modifiedGraphEdges(self, n: int, edges: List[List[int]],
                            source: int, destination: int, target: int) -> List[List[int]]:
        assert isinstance(n, int) and n >= 1
        assert isinstance(edges, list) and 1 <= len(edges) <= int(n * (n - 1) / 2)
        assert isinstance(source, int) and 0 <= source <= n
        assert isinstance(destination, int) and 0 <= destination <= n and source != destination
        assert isinstance(target, int) and target >= 1

        def __dijkstra(edges: List[List[int]]) -> int:
            graph = [[INF] * n for _ in range(n)]
            for s, t, w in edges:
                if w == -1:
                    continue
                graph[s][t] = graph[t][s] = w

            dist = [INF] * n
            dist[source] = 0
            visited = [False] * n
            for _ in range(n):
                k = -1
                for j in range(n):
                    if not visited[j] and (k == -1 or dist[k] > dist[j]):
                        k = j
                visited[k] = True
                for j in range(n):
                    dist[j] = min(dist[j], dist[k] + graph[k][j])

            return dist[destination]

        INF = 2 * int(1e9)
        dij = __dijkstra(edges)

        if dij < target:
            return []

        flag = dij == target
        for edge in edges:
            if edge[2] > 0:
                continue
            if flag:
                edge[2] = INF
                continue
            edge[2] = 1

            dij = __dijkstra(edges)
            if dij <= target:
                flag = True
                edge[2] += target - dij

        return edges if flag else []


def main():
    # Example 1: Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
    n = 5
    edges = [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]]
    source = 0
    destination = 1
    target = 5

    # Example 2: Output: []
    # n = 3
    # edges = [[0, 1, -1], [0, 2, 5]]
    # source = 0
    # destination = 2
    # target = 6

    # Example 3: Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
    # n = 4
    # edges = [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]]
    # source = 0
    # destination = 2
    # target = 6

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.modifiedGraphEdges(n, edges, source, destination, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
