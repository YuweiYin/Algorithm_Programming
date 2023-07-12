#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0802-Find-Eventual-Safe-States.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-12
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 0802 - (Medium) - Find Eventual Safe States
https://leetcode.com/problems/find-eventual-safe-states/

Description & Requirement:
    There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
    The graph is represented by a 0-indexed 2D integer array graph where graph[i] 
    is an integer array of nodes adjacent to node i, meaning 
    there is an edge from node i to each node in graph[i].

    A node is a terminal node if there are no outgoing edges. 
    A node is a safe node if every possible path starting from that 
    node leads to a terminal node (or another safe node).

    Return an array containing all the safe nodes of the graph. 
    The answer should be sorted in ascending order.

Example 1:
    Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    Output: [2,4,5,6]
    Explanation: The given graph is shown above.
        Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
        Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
Example 2:
    Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    Output: [4]
    Explanation:
        Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.

Constraints:
    n == graph.length
    1 <= n <= 10^4
    0 <= graph[i].length <= n
    0 <= graph[i][j] <= n - 1
    graph[i] is sorted in a strictly increasing order.
    The graph may contain self-loops.
    The number of edges in the graph will be in the range [1, 4 * 10^4].
"""


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(graph, list) and len(graph) >= 1
        # main method: (DFS)
        return self._eventualSafeNodes(graph)

    def _eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        assert isinstance(graph, list) and len(graph) >= 1

        n = len(graph)
        color = [0] * n

        def __dfs(x: int) -> bool:
            if color[x] > 0:
                return color[x] == 2

            color[x] = 1
            for y in graph[x]:
                if not __dfs(y):
                    return False

            color[x] = 2
            return True

        return [i for i in range(n) if __dfs(i)]


def main():
    # Example 1: Output: [2,4,5,6]
    # graph = [[1, 2], [2, 3], [5], [0], [5], [], []]

    # Example 2: Output: [4]
    graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.eventualSafeNodes(graph)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
