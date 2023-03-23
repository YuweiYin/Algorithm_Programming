#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1319-Number-of-Operations-to-Make-Network-Connected.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-23
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1319 - (Medium) - Number of Operations to Make Network Connected
https://leetcode.com/problems/number-of-operations-to-make-network-connected/

Description & Requirement:
    There are n computers numbered from 0 to n - 1 connected by ethernet cables connections 
    forming a network where connections[i] = [ai, bi] represents a connection between computers 
    ai and bi. Any computer can reach any other computer directly or indirectly through the network.

    You are given an initial computer network connections. You can extract certain cables between 
    two directly connected computers, and place them between any pair of disconnected computers 
    to make them directly connected.

    Return the minimum number of times you need to do this in order to make all the computers connected. 
    If it is not possible, return -1.

Example 1:
    Input: n = 4, connections = [[0,1],[0,2],[1,2]]
    Output: 1
    Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:
    Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
    Output: 2
Example 3:
    Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
    Output: -1
    Explanation: There are not enough cables.

Constraints:
    1 <= n <= 10^5
    1 <= connections.length <= min(n * (n - 1) / 2, 10^5)
    connections[i].length == 2
    0 <= ai, bi < n
    ai != bi
    There are no repeated connections.
    No two computers are connected by more than one cable.
"""


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(connections, list) and len(connections) >= 1
        # main method: (DFS)
        return self._makeConnected(n, connections)

    def _makeConnected(self, n: int, connections: List[List[int]]) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(connections, list) and len(connections) >= 1

        if len(connections) < n - 1:
            return -1

        graph = collections.defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()

        def __dfs(u: int):
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    __dfs(v)

        ans = 0
        for i in range(n):
            if i not in visited:
                __dfs(i)
                ans += 1

        return ans - 1


def main():
    # Example 1: Output: 1
    # n = 4
    # connections = [[0, 1], [0, 2], [1, 2]]

    # Example 2: Output: 2
    # n = 6
    # connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]

    # Example 3: Output: -1
    n = 6
    connections = [[0, 1], [0, 2], [0, 3], [1, 2]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.makeConnected(n, connections)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
