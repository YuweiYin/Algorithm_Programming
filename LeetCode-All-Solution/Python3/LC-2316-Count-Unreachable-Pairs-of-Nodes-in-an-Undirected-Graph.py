#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2316-Count-Unreachable-Pairs-of-Nodes-in-an-Undirected-Graph.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-25
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2316 - (Medium) - Count Unreachable Pairs of Nodes in an Undirected Graph
https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

Description & Requirement:
    You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. 
    You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that 
    there exists an undirected edge connecting nodes ai and bi.

    Return the number of pairs of different nodes that are unreachable from each other.

Example 1:
    Input: n = 3, edges = [[0,1],[0,2],[1,2]]
    Output: 0
    Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
Example 2:
    Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
    Output: 14
    Explanation: There are 14 pairs of nodes that are unreachable from each other:
        [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
        Therefore, we return 14.

Constraints:
    1 <= n <= 10^5
    0 <= edges.length <= 2 * 10^5
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    There are no repeated edges.
"""


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(edges, list)
        # main method: (DFS)
        return self._countPairs(n, edges)

    def _countPairs(self, n: int, edges: List[List[int]]) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(edges, list)

        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited, res, total, size = [False] * n, 0, 0, 0

        def __dfs(x: int) -> None:
            nonlocal size
            visited[x] = True
            size += 1
            for y in graph[x]:
                if not visited[y]:
                    __dfs(y)

        for i in range(n):
            if not visited[i]:
                size = 0
                __dfs(i)
                res += size * total
                total += size

        return res


def main():
    # Example 1: Output: 0
    # n = 3
    # edges = [[0, 1], [0, 2], [1, 2]]

    # Example 2: Output: 14
    n = 7
    edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countPairs(n, edges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
