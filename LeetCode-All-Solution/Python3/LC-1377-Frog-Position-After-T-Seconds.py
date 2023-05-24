#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1377-Frog-Position-After-T-Seconds.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-24
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1377 - (-Hard-) - Frog Position After T Seconds
https://leetcode.com/problems/frog-position-after-t-seconds/

Description & Requirement:
    Given an undirected tree consisting of n vertices numbered from 1 to n. 
    A frog starts jumping from vertex 1. In one second, the frog jumps from its current vertex 
    to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. 
    In case the frog can jump to several vertices, it jumps randomly to one of them with the same probability. 
    Otherwise, when the frog can not jump to any unvisited vertex, it jumps forever on the same vertex.

    The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] 
    means that exists an edge connecting the vertices ai and bi.

    Return the probability that after t seconds the frog is on the vertex target. 
    Answers within 10-5 of the actual answer will be accepted.

Example 1:
    Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
    Output: 0.16666666666666666 
    Explanation: The figure above shows the given graph. The frog starts at vertex 1, 
        jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability 
        to vertex 4 after second 2. Thus the probability for the frog is on the vertex 4 after 2 seconds 
        is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 
Example 2:
    Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
    Output: 0.3333333333333333
    Explanation: The figure above shows the given graph. The frog starts at vertex 1, 
        jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. 

Constraints:
    1 <= n <= 100
    edges.length == n - 1
    edges[i].length == 2
    1 <= ai, bi <= n
    1 <= t <= 50
    1 <= target <= n
"""


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(edges, list) and len(edges) == n - 1
        assert isinstance(t, int) and t >= 1
        assert isinstance(target, int) and target >= 1
        # main method: (BFS)
        return self._frogPosition(n, edges, t, target)

    def _frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        assert isinstance(n, int) and n >= 1
        assert isinstance(edges, list) and len(edges) == n - 1
        assert isinstance(t, int) and t >= 1
        assert isinstance(target, int) and target >= 1

        graph = [[] for i in range(n + 1)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = [0] * (n + 1)

        def __dfs(i, t):
            cur_len = len(graph[i])
            if i > 1:
                cur_len -= 1
            if cur_len == 0 or t == 0:
                return 1.0 if i == target else 0.0

            visited[i] = 1
            for j in graph[i]:
                if not visited[j]:
                    p = __dfs(j, t - 1)
                    if p > 0:
                        return p / cur_len
            return 0.0

        return float(__dfs(1, t))


def main():
    # Example 1: Output: 0.16666666666666666
    n = 7
    edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]]
    t = 2
    target = 4

    # Example 2: Output: 0.3333333333333333
    # n = 7
    # edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]]
    # t = 1
    # target = 7

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.frogPosition(n, edges, t, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
