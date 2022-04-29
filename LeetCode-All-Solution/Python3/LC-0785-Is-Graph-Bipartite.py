#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0785-Is-Graph-Bipartite.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-29
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0785 - (Medium) - Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/

Description & Requirement:
    There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. 
    You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. 
    More formally, for each v in graph[u], there is an undirected edge between node u and node v. 

    The graph has the following properties:
        There are no self-edges (graph[u] does not contain u).
        There are no parallel edges (graph[u] does not contain duplicate values).
        If v is in graph[u], then u is in graph[v] (the graph is undirected).
        The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

    A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that 
    every edge in the graph connects a node in set A and a node in set B.

    Return true if and only if it is bipartite.

Example 1:
    Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    Output: false
    Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:
    Input: graph = [[1,3],[0,2],[1,3],[0,2]]
    Output: true
    Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

Constraints:
    graph.length == n
    1 <= n <= 100
    0 <= graph[u].length < n
    0 <= graph[u][i] <= n - 1
    graph[u] does not contain u.
    All the values of graph[u] are unique.
    If graph[u] contains v, then graph[v] contains u.
"""


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # exception case
        assert isinstance(graph, list)
        # main method: (BFS. If two nodes are directly connected, they must have different COLOR)
        #     If a colored node has to be drawn on another color, then return False.
        return self._isBipartite(graph)

    def _isBipartite(self, graph: List[List[int]]) -> bool:
        assert isinstance(graph, list)
        node_num = len(graph)  # the number of nodes
        if node_num == 0:
            return False
        if node_num == 1:
            return True

        color = [0 for _ in range(node_num)]  # 0: no color; 1: color 1; 2: color 2

        for source_node in range(node_num):
            if color[source_node] == 0:
                bfs_queue = collections.deque()
                bfs_queue.append(source_node)
                color[source_node] = 1

                while len(bfs_queue) > 0:
                    cur_node = bfs_queue.popleft()
                    cur_color = color[cur_node]
                    # assert cur_color != 0
                    # assert 0 <= cur_node < node_num
                    for neighbor in graph[cur_node]:
                        # assert 0 <= neighbor < node_num
                        if color[neighbor] == 0:
                            color[neighbor] = 1 if cur_color != 1 else 2
                            bfs_queue.append(neighbor)
                        else:
                            if color[neighbor] == cur_color:  # color conflict
                                return False

        return True


def main():
    # Example 1: Output: false
    # graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]

    # Example 2: Output: true
    # graph = [[1, 3], [0, 2], [1, 3], [0, 2]]

    # Example 3: Output: false
    graph = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
             [2, 4, 5, 6, 7, 8]]

    # Example 4: Output: true
    # graph = [[4], [], [4], [4], [0, 2, 3]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isBipartite(graph)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
