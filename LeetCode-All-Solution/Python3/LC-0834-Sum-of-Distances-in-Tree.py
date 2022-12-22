#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0834-Sum-of-Distances-in-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-22
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0834 - (Hard) - Sum of Distances in Tree
https://leetcode.com/problems/sum-of-distances-in-tree/

Description & Requirement:
    There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

    You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that 
    there is an edge between nodes ai and bi in the tree.

    Return an array answer of length n where answer[i] is the sum of the distances 
    between the i-th node in the tree and all other nodes.

Example 1:
    Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    Output: [8,12,6,10,10,10]
    Explanation: The tree is shown above.
        We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
        equals 1 + 1 + 2 + 2 + 2 = 8.
        Hence, answer[0] = 8, and so on.
Example 2:
    Input: n = 1, edges = []
    Output: [0]
Example 3:
    Input: n = 2, edges = [[1,0]]
    Output: [1,1]

Constraints:
    1 <= n <= 3 * 10^4
    edges.length == n - 1
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    The given input represents a valid tree.
"""


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(edges, list) and len(edges) == n - 1
        # main method: (Tree-based Dynamic Programming)
        return self._sumOfDistancesInTree(n, edges)

    def _sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        assert isinstance(n, int) and n >= 1
        assert isinstance(edges, list) and len(edges) == n - 1

        def __dfs_1(u, f):
            sz[u] = 1
            dp[u] = 0
            for v in graph[u]:
                if v == f:
                    continue
                __dfs_1(v, u)
                dp[u] += (dp[v] + sz[v])
                sz[u] += sz[v]

        def __dfs_2(u, f):
            res[u] = dp[u]
            for v in graph[u]:
                if v == f:
                    continue
                pu = dp[u]
                pv = dp[v]
                su = sz[u]
                sv = sz[v]
                dp[u] -= (dp[v] + sz[v])
                sz[u] -= sz[v]
                dp[v] += (dp[u] + sz[u])
                sz[v] += sz[u]
                __dfs_2(v, u)
                dp[u] = pu
                dp[v] = pv
                sz[u] = su
                sz[v] = sv

        res = [0 for _ in range(n)]
        sz = [0 for _ in range(n)]
        dp = [0 for _ in range(n)]

        graph = [[] for _ in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            graph[u].append(v)
            graph[v].append(u)

        __dfs_1(0, -1)
        __dfs_2(0, -1)

        return res


def main():
    # Example 1: Output: [8,12,6,10,10,10]
    n = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]

    # Example 2: Output: [0]
    # n = 1
    # edges = []

    # Example 3: Output: [1,1]
    # n = 2
    # edges = [[1, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sumOfDistancesInTree(n, edges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
