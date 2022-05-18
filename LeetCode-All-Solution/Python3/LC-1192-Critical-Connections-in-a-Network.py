#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1192-Critical-Connections-in-a-Network.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-18
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1192 - (Hard) - Critical Connections in a Network
https://leetcode.com/problems/critical-connections-in-a-network/

Description & Requirement:
    There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network
    where connections[i] = [ai, bi] represents a connection between servers ai and bi. 
    Any server can reach other servers directly or indirectly through the network.

    A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

    Return all critical connections in the network in any order.

Example 1:
    Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
    Output: [[1,3]]
    Explanation: [[3,1]] is also accepted.
Example 2:
    Input: n = 2, connections = [[0,1]]
    Output: [[0,1]]

Constraints:
    2 <= n <= 10^5
    n - 1 <= connections.length <= 10^5
    0 <= ai, bi <= n - 1
    ai != bi
    There are no repeated connections.
"""


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # exception case
        assert isinstance(n, int) and n >= 2
        assert isinstance(connections, list) and len(connections) >= n - 1
        # main method: (Tarjan's bridge-finding algorithm)
        return self._criticalConnections(n , connections)

    def _criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        assert isinstance(n, int) and n >= 2
        assert isinstance(connections, list) and len(connections) >= n - 1

        connections_set = set()
        for connection in connections:
            _from, _to = connection
            cur_edge = (_from, _to) if _from <= _to else (_to, _from)
            connections_set.add(cur_edge)

        graph = dict({})
        for node in range(n):
            graph[node] = set()
        for connection in connections_set:
            _from, _to = connection
            if _from == _to:
                continue
            if _from in graph:
                graph[_from].add(_to)
            if _to in graph:
                graph[_to].add(_from)

        depth = [-1 for _ in range(n)]  # DFS depth

        def __dfs(cur_node: int, parent_node: int, cur_depth: int):
            if depth[cur_node] >= 0:
                return depth[cur_node]
            depth[cur_node] = cur_depth

            min_depth = n  # to find the minimal depth, n is INF
            # assert cur_node in graph
            for neighbor in graph[cur_node]:
                if neighbor == parent_node:
                    continue
                backtrace_depth = __dfs(neighbor, cur_node, cur_depth + 1)
                if backtrace_depth <= cur_depth:  # this indicates a loop, which needs to be cut
                    _edge = (cur_node, neighbor) if cur_node <= neighbor else (neighbor, cur_node)
                    connections_set.discard(_edge)
                min_depth = min(min_depth, backtrace_depth)
            return min_depth

        __dfs(0, -1, 0)  # start from node 0
        res = []
        for connection in connections_set:
            _from, _to = connection
            res.append([_from, _to])

        return res


def main():
    # Example 1: Output: [[1,3]]
    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]

    # Example 2: Output: [[0,1]]
    # n = 2
    # connections = [[0, 1]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.criticalConnections(n, connections)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
