#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1857-Largest-Color-Value-in-a-Directed-Graph.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-09
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1857 - (Hard) - Largest Color Value in a Directed Graph
https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

Description & Requirement:
    There is a directed graph of n colored nodes and m edges. 
    The nodes are numbered from 0 to n - 1.

    You are given a string colors where colors[i] is a lowercase English letter representing 
    the color of the ith node in this graph (0-indexed). 
    You are also given a 2D array edges where edges[j] = [aj, bj] indicates that 
    there is a directed edge from node aj to node bj.

    A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that 
    there is a directed edge from xi to xi+1 for every 1 <= i < k. 
    The color value of the path is the number of nodes that 
    are colored the most frequently occurring color along that path.

    Return the largest color value of any valid path in the given graph, 
    or -1 if the graph contains a cycle.

Example 1:
    Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
    Output: 3
    Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
Example 2:
    Input: colors = "a", edges = [[0,0]]
    Output: -1
    Explanation: There is a cycle from 0 to 0.

Constraints:
    n == colors.length
    m == edges.length
    1 <= n <= 10^5
    0 <= m <= 10^5
    colors consists of lowercase English letters.
    0 <= aj, bj < n
"""


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # exception case
        assert isinstance(colors, str) and len(colors) >= 1
        assert isinstance(edges, list)
        # main method: (topology sorting and dynamic programming)
        return self._largestPathValue(colors, edges)

    def _largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        assert isinstance(colors, str) and len(colors) >= 1
        assert isinstance(edges, list)

        n = len(colors)
        graph = collections.defaultdict(list)
        in_degree = [0] * n

        for x, y in edges:
            in_degree[y] += 1
            graph[x].append(y)

        flog = 0
        dp = [[0] * 26 for _ in range(n)]
        queue = collections.deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        while len(queue) > 0:
            flog += 1
            u = queue.popleft()
            dp[u][ord(colors[u]) - ord("a")] += 1

            for v in graph[u]:
                in_degree[v] -= 1
                for ch in range(26):
                    dp[v][ch] = max(dp[v][ch], dp[u][ch])
                if in_degree[v] == 0:
                    queue.append(v)

        if flog != n:
            return -1

        res = 0
        for i in range(n):
            res = max(res, max(dp[i]))

        return res


def main():
    # Example 1: Output: 3
    colors = "abaca"
    edges = [[0, 1], [0, 2], [2, 3], [3, 4]]

    # Example 2: Output: -1
    # colors = "a"
    # edges = [[0, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.largestPathValue(colors, edges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
