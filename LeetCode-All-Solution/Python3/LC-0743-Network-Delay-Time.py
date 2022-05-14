#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0743-Network-Delay-Time.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-14
=================================================================="""

import sys
import time
from typing import List
import heapq
# import collections
# import functools

"""
LeetCode - 0743 - (Medium) - Network Delay Time
https://leetcode.com/problems/network-delay-time/

Description & Requirement:
    You are given a network of n nodes, labeled from 1 to n. You are also given times, 
    a list of travel times as directed edges times[i] = (ui, vi, wi), 
    where ui is the source node, vi is the target node, 
    and wi is the time it takes for a signal to travel from source to target.

    We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. 
    If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2
Example 2:
    Input: times = [[1,2,1]], n = 2, k = 1
    Output: 1
Example 3:
    Input: times = [[1,2,1]], n = 2, k = 2
    Output: -1

Constraints:
    1 <= k <= n <= 100
    1 <= times.length <= 6000
    times[i].length == 3
    1 <= ui, vi <= n
    ui != vi
    0 <= wi <= 100
    All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # exception case
        assert isinstance(times, list) and len(times) >= 1
        for edge in times:
            isinstance(edge, list) and len(edge) == 3 and 1 <= edge[0] <= n and 1 <= edge[1] <= n and 0 <= edge[2]
        assert isinstance(k, int) and 1 <= k <= n
        # main method: (Dijkstra + heap)
        return self._networkDelayTime(times, n, k)

    def _networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = dict({})
        for node in range(1, n + 1):
            graph[node] = []
        for edge in times:
            u_i, v_i, w_i = edge
            if u_i in graph:
                graph[u_i].append((v_i, w_i))

        if k < 1 or k > n:
            return -1

        distance = [int(1e9+7) for _ in range(n + 1)]
        distance[k] = 0
        heap_queue = [(0, k)]
        while len(heap_queue) > 0:
            cur_time, cur_node = heapq.heappop(heap_queue)
            if distance[cur_node] < cur_time or cur_node not in graph:
                continue
            for v_i, w_i in graph[cur_node]:
                new_dist = distance[cur_node] + w_i
                if new_dist < distance[v_i]:
                    distance[v_i] = new_dist
                    heapq.heappush(heap_queue, (new_dist, v_i))

        res = max(distance[1:])
        return res if res < int(1e9+7) else -1


def main():
    # Example 1: Output: 2
    # times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    # n = 4
    # k = 2

    # Example 2: Output: 1
    # times = [[1, 2, 1]]
    # n = 2
    # k = 1

    # Example 3: Output: -1
    times = [[1, 2, 1]]
    n = 2
    k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.networkDelayTime(times, n, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
