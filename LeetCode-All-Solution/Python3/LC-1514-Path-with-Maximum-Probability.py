#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1514-Path-with-Maximum-Probability.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-28
=================================================================="""

import sys
import time
from typing import List
import collections
import heapq
# import functools
# import itertools

"""
LeetCode - 1514 - (Medium) - Path with Maximum Probability
https://leetcode.com/problems/path-with-maximum-probability/

Description & Requirement:
    You are given an undirected weighted graph of n nodes (0-indexed), represented by 
    an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a 
    and b with a probability of success of traversing that edge succProb[i].

    Given two nodes start and end, find the path with the maximum probability of success 
    to go from start to end and return its success probability.

    If there is no path from start to end, return 0. Your answer will be accepted if 
    it differs from the correct answer by at most 1e-5.

Example 1:
    Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
    Output: 0.25000
    Explanation: There are two paths from start to end, one having a probability of success = 0.2 
        and the other has 0.5 * 0.5 = 0.25.
Example 2:
    Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
    Output: 0.30000
Example 3:
    Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
    Output: 0.00000
    Explanation: There is no path between 0 and 2.

Constraints:
    2 <= n <= 10^4
    0 <= start, end < n
    start != end
    0 <= a, b < n
    a != b
    0 <= succProb.length == edges.length <= 2*10^4
    0 <= succProb[i] <= 1
    There is at most one edge between every two nodes.
"""


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # exception case
        assert isinstance(n, int) and n >= 2
        assert isinstance(edges, list) and len(edges) >= 1
        assert isinstance(succProb, list) and len(succProb) >= 1
        assert isinstance(start, int) and 0 <= start < n
        assert isinstance(end, int) and 0 <= end < n and start != end
        # main method: (Dijkstra)
        return self._maxProbability(n, edges, succProb, start, end)

    def _maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        assert isinstance(n, int) and n >= 2
        assert isinstance(edges, list) and len(edges) >= 1
        assert isinstance(succProb, list) and len(succProb) >= 1
        assert isinstance(start, int) and 0 <= start < n
        assert isinstance(end, int) and 0 <= end < n and start != end

        graph = collections.defaultdict(list)
        for i, (x, y) in enumerate(edges):
            graph[x].append((succProb[i], y))
            graph[y].append((succProb[i], x))

        queue = [(-1.0, start)]
        prob = [0.0] * n
        prob[start] = 1.0

        while queue:
            p, node = heapq.heappop(queue)
            p = -p
            if p < prob[node]:
                continue
            for p_next, node_next in graph[node]:
                if prob[node_next] < prob[node] * p_next:
                    prob[node_next] = prob[node] * p_next
                    heapq.heappush(queue, (-prob[node_next], node_next))

        return float(prob[end])


def main():
    # Example 1: Output: 0.25000
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start = 0
    end = 2

    # Example 2: Output: 0.30000
    # n = 3
    # edges = [[0, 1], [1, 2], [0, 2]]
    # succProb = [0.5, 0.5, 0.3]
    # start = 0
    # end = 2

    # Example 3: Output: 0.00000
    # n = 3
    # edges = [[0, 1]]
    # succProb = [0.5]
    # start = 0
    # end = 2

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.maxProbability(n, edges, succProb, start, end)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
