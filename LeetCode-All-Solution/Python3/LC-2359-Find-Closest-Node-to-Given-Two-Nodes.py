#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2359-Find-Closest-Node-to-Given-Two-Nodes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-25
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2359 - (Medium) - Find Closest Node to Given Two Nodes
https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

Description & Requirement:
    You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

    The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge 
    from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

    You are also given two integers node1 and node2.

    Return the index of the node that can be reached from both node1 and node2, 
    such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. 
    If there are multiple answers, return the node with the smallest index, 
    and if no possible answer exists, return -1.

    Note that edges may contain cycles.

Example 1:
    Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
    Output: 2
    Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
        The maximum of those two distances is 1. 
        It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
Example 2:
    Input: edges = [1,2,-1], node1 = 0, node2 = 2
    Output: 2
    Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
        The maximum of those two distances is 2. 
        It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.

Constraints:
    n == edges.length
    2 <= n <= 10^5
    -1 <= edges[i] < n
    edges[i] != i
    0 <= node1, node2 < n
"""


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # exception case
        assert isinstance(edges, list) and len(edges) >= 2
        assert isinstance(node1, int) and node1 >= 0
        assert isinstance(node2, int) and node2 >= 0
        # main method: (scan graph)
        return self._closestMeetingNode(edges, node1, node2)

    def _closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        assert isinstance(edges, list) and len(edges) >= 2
        assert isinstance(node1, int) and node1 >= 0
        assert isinstance(node2, int) and node2 >= 0

        n = len(edges)
        min_dist = len(edges)
        res = -1

        def calc_dis(x: int) -> List[int]:
            dist_list = [n] * n
            cur_dist = 0
            while x >= 0 and dist_list[x] == n:
                dist_list[x] = cur_dist
                cur_dist += 1
                x = edges[x]
            return dist_list

        for idx, dist in enumerate(map(max, zip(calc_dis(node1), calc_dis(node2)))):
            if dist < min_dist:
                min_dist, res = dist, idx

        return res


def main():
    # Example 1: Output: 2
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1

    # Example 2: Output: 2
    # edges = [1, 2, -1]
    # node1 = 0
    # node2 = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.closestMeetingNode(edges, node1, node2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
