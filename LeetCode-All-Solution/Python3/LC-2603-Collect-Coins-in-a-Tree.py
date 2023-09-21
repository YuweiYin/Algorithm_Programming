#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2603-Collect-Coins-in-a-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-21
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2603 - (Hard) Collect Coins in a Tree
https://leetcode.com/problems/collect-coins-in-a-tree/

Description & Requirement:
    There exists an undirected and unrooted tree with n nodes indexed from 0 to n - 1. 
    You are given an integer n and a 2D integer array edges of length n - 1, 
    where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. 
    You are also given an array coins of size n where coins[i] can be either 0 or 1, 
    where 1 indicates the presence of a coin in the vertex i.

    Initially, you choose to start at any vertex in the tree. 
    Then, you can perform the following operations any number of times: 
        - Collect all the coins that are at a distance of at most 2 from the current vertex, or
        - Move to any adjacent vertex in the tree.

    Find the minimum number of edges you need to go through to collect all the coins and go back to the initial vertex.

    Note that if you pass an edge several times, you need to count it into the answer several times.

Example 1:
    Input: coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]
    Output: 2
    Explanation: Start at vertex 2, collect the coin at vertex 0, move to vertex 3, 
        collect the coin at vertex 5 then move back to vertex 2.
Example 2:
    Input: coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]
    Output: 2
    Explanation: Start at vertex 0, collect the coins at vertices 4 and 3, move to vertex 2, 
        collect the coin at vertex 7, then move back to vertex 0.

Constraints:
    n == coins.length
    1 <= n <= 3 * 10^4
    0 <= coins[i] <= 1
    edges.length == n - 1
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    edges represents a valid tree.
"""


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        # exception case
        assert isinstance(coins, list) and len(coins) >= 1
        assert isinstance(edges, list) and len(edges) == len(coins) - 1
        # main method: (Topological Sorting)
        return self._collectTheCoins(coins, edges)

    def _collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        assert isinstance(coins, list) and len(coins) >= 1
        assert isinstance(edges, list) and len(edges) == len(coins) - 1

        n = len(coins)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        deg = list(map(len, g))

        left_edges = n - 1
        q = []
        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c == 0:
                q.append(i)

        while q:
            left_edges -= 1
            for y in g[q.pop()]:
                deg[y] -= 1
                if deg[y] == 1 and coins[y] == 0:
                    q.append(y)

        for i, (d, c) in enumerate(zip(deg, coins)):
            if d == 1 and c:
                q.append(i)

        left_edges -= len(q)
        for x in q:
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 1:
                    left_edges -= 1

        return max(left_edges * 2, 0)


def main():
    # Example 1: Output: 2
    # coins = [1, 0, 0, 0, 0, 1]
    # edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]

    # Example 2: Output: 2
    coins = [0, 0, 0, 1, 1, 0, 0, 1]
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [5, 6], [5, 7]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.collectTheCoins(coins, edges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
