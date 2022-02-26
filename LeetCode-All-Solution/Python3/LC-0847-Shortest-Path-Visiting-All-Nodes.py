#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0847-Shortest-Path-Visiting-All-Nodes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-25
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0847 - (Hard) - Shortest Path Visiting All Nodes
https://leetcode.com/problems/shortest-path-visiting-all-nodes/

Description & Requirement:
    You have an undirected, connected graph of n nodes labeled from 0 to n - 1. 
    You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

    Return the length of the shortest path that visits every node. 
    You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Example 1:
    Input: graph = [[1,2,3],[0],[0],[0]]
    Output: 4
    Explanation: One possible path is [1,0,2,0,3]
Example 2:
    Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    Output: 4
    Explanation: One possible path is [0,1,4,2,3]

Constraints:
    n == graph.length
    1 <= n <= 12
    0 <= graph[i].length < n
    graph[i] does not contain i.
    If graph[a] contains b, then graph[b] contains a.
    The input graph is always connected.
"""


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # exception case
        assert isinstance(graph, list) and len(graph) > 0
        # main method: (multi-source BFS from every node, get the shortest path)
        #     space optimize: set can be replaced by a number, the i-th bit indicates if the i-th node is visited
        return self._shortestPathLengthBfs(graph)

    def _shortestPathLengthBfs(self, graph: List[List[int]]) -> int:
        num_nodes = len(graph)
        res = [(num_nodes << 1) + 1]  # at most (num_nodes << 1) steps, so (num_nodes << 1 + 1) is INF upper bound
        target_visited_nodes_set = (1 << num_nodes) - 1

        dealt_state = set()  # store the dealt state to avoid repeatedly searching from the same state
        bfs_queue = collections.deque()
        for node in range(num_nodes):
            bfs_queue.append((node, 0, (1 << node)))  # element: (cur_node, cur_path_len, visited_nodes_set)
            # dealt_state.add((node, {node}))  # element: (cur_node, visited_nodes_set)

        while len(bfs_queue) > 0:
            cur_node, cur_path_len, visited_nodes_set = bfs_queue.popleft()
            if (cur_node, visited_nodes_set) in dealt_state:  # avoid repeatedly searching from the same state
                continue
            else:
                dealt_state.add((cur_node, visited_nodes_set))
            if cur_path_len >= res[0]:  # prune
                continue
            # if len(visited_nodes_set) == len(graph):  # the first reach len(graph) is the answer
            if visited_nodes_set == target_visited_nodes_set:  # bit indicator matching
                res[0] = cur_path_len
                break
            # assert isinstance(visited_nodes_set, set)
            for neighbor in graph[cur_node]:
                # new_visited_nodes_set = visited_nodes_set.copy()
                # if neighbor not in new_visited_nodes_set:  # can repeatedly visit the same node
                #     new_visited_nodes_set.add(neighbor)
                new_visited_nodes_set = (1 << neighbor) | visited_nodes_set
                bfs_queue.append((neighbor, cur_path_len + 1, new_visited_nodes_set))

        return res[0]


def main():
    # Example 1: Output: 4
    # graph = [[1, 2, 3], [0], [0], [0]]

    # Example 2: Output: 4
    # graph = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]

    # Example 3: Output:
    graph = [[2, 5, 7], [2, 4], [0, 1], [5], [5, 6, 1], [4, 10, 8, 0, 3], [4, 9], [0], [5], [6], [5]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.shortestPathLength(graph)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
