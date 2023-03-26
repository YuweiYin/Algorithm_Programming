#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2360-Longest-Cycle-in-a-Graph.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-26
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2360 - (Hard) - Longest Cycle in a Graph
https://leetcode.com/problems/longest-cycle-in-a-graph/

Description & Requirement:
    You are given a directed graph of n nodes numbered from 0 to n - 1, 
    where each node has at most one outgoing edge.

    The graph is represented with a given 0-indexed array edges of size n, indicating that 
    there is a directed edge from node i to node edges[i]. 
    If there is no outgoing edge from node i, then edges[i] == -1.

    Return the length of the longest cycle in the graph. If no cycle exists, return -1.

    A cycle is a path that starts and ends at the same node.

Example 1:
    Input: edges = [3,3,4,2,3]
    Output: 3
    Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
        The length of this cycle is 3, so 3 is returned.
Example 2:
    Input: edges = [2,-1,3,1]
    Output: -1
    Explanation: There are no cycles in this graph.

Constraints:
    n == edges.length
    2 <= n <= 10^5
    -1 <= edges[i] < n
    edges[i] != i
"""


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # exception case
        assert isinstance(edges, list) and len(edges) >= 2
        # main method: (topology sorting & BFS)
        return self._longestCycle(edges)

    def _longestCycle(self, edges: List[int]) -> int:
        assert isinstance(edges, list) and len(edges) >= 2

        n = len(edges)

        in_degree = [0] * n
        for u in edges:
            if u == -1:
                continue
            in_degree[u] += 1

        queue = [u for u in range(n) if in_degree[u] == 0]
        while len(queue) >= 1:
            u = queue.pop()
            v = edges[u]
            if v == -1:
                continue
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

        if max(in_degree) == 0:
            return -1

        def __bfs(u):
            step = 0
            while True:
                if u in visited:
                    return step
                visited.add(u)
                u = edges[u]
                step += 1

        res = 0
        visited = set()
        for u in range(n):
            if in_degree[u] == 0 or u in visited:
                continue
            circle_len = __bfs(u)
            res = max(res, circle_len)

        return res


def main():
    # Example 1: Output: 3
    edges = [3, 3, 4, 2, 3]

    # Example 2: Output: -1
    # edges = [2, -1, 3, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestCycle(edges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
