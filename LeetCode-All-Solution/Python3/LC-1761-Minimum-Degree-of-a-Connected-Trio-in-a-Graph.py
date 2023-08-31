#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1761-Minimum-Degree-of-a-Connected-Trio-in-a-Graph.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-31
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 1761 - (Hard) Minimum Degree of a Connected Trio in a Graph
https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

Description & Requirement:
    You are given an undirected graph. You are given an integer n 
    which is the number of nodes in the graph and an array edges, 
    where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi.

    A connected trio is a set of three nodes where there is an edge between every pair of them.

    The degree of a connected trio is the number of edges where 
    one endpoint is in the trio, and the other is not.

    Return the minimum degree of a connected trio in the graph, 
    or -1 if the graph has no connected trios.

Example 1:
    Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
    Output: 3
    Explanation: There is exactly one trio, which is [1,2,3]. 
        The edges that form its degree are bolded in the figure above.
Example 2:
    Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
    Output: 0
    Explanation: There are exactly three trios:
        1) [1,4,3] with degree 0.
        2) [2,5,6] with degree 2.
        3) [5,6,7] with degree 2.

Constraints:
    2 <= n <= 400
    edges[i].length == 2
    1 <= edges.length <= n * (n-1) / 2
    1 <= ui, vi <= n
    ui != vi
    There are no repeated edges.
"""


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # exception case
        assert isinstance(edges, list) and len(edges) >= 1
        assert isinstance(n, int) and n >= 2
        # main method: (enumeration)
        return self._minTrioDegree(n, edges)

    def _minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        assert isinstance(edges, list) and len(edges) >= 1
        assert isinstance(n, int) and n >= 2

        graph = collections.defaultdict(set)
        digraph = collections.defaultdict(list)
        degree = [0] * n

        for x, y in edges:
            x, y = x - 1, y - 1
            graph[x].add(y)
            graph[y].add(x)
            degree[x] += 1
            degree[y] += 1

        for x, y in edges:
            x, y = x - 1, y - 1
            if degree[x] < degree[y] or (degree[x] == degree[y] and x < y):
                digraph[x].append(y)
            else:
                digraph[y].append(x)

        res = int(1e9+7)
        for i in range(n):
            for j in digraph[i]:
                for k in digraph[j]:
                    if k in graph[i]:
                        res = min(res, degree[i] + degree[j] + degree[k] - 6)

        return -1 if res == int(1e9+7) else res


def main():
    # Example 1: Output: 3
    # n = 6
    # edges = [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]

    # Example 2: Output: 0
    n = 7
    edges = [[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minTrioDegree(n, edges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
