#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1557-Minimum-Number-of-Vertices-to-Reach-All-Nodes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-29
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1557 - (Medium) - Minimum Number of Vertices to Reach All Nodes
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

Description & Requirement:
    Given a directed acyclic graph, with n vertices numbered from 0 to n-1, 
    and an array edges where edges[i] = [from_i, to_i] represents a directed edge from node from_i to node to_i.

    Find the smallest set of vertices from which all nodes in the graph are reachable. 
    It's guaranteed that a unique solution exists.

    Notice that you can return the vertices in any order.

Example 1:
    Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
    Output: [0,3]
    Explanation: It's not possible to reach all the nodes from a single vertex. 
        From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
Example 2:
    Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
    Output: [0,2,3]
    Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, 
        so we must include them. Also any of these vertices can reach nodes 1 and 4.

Constraints:
    2 <= n <= 10^5
    1 <= edges.length <= min(10^5, n * (n - 1) / 2)
    edges[i].length == 2
    0 <= from_i, to_i < n
    All pairs (from_i, to_i) are distinct.
"""


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(n, int) and n >= 2
        assert isinstance(edges, list) and len(edges) >= 1
        # main method: (reverse the link, find all source nodes: degree == 0)
        return self._findSmallestSetOfVertices(n, edges)

    def _findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph_reverse = dict({})
        for node_id in range(n):
            graph_reverse[node_id] = []
        for node_id, edge in enumerate(edges):
            graph_reverse[edge[1]].append(edge[0])

        res = []
        for from_i, to_i in graph_reverse.items():
            if len(to_i) > 0:
                continue
            else:
                res.append(from_i)

        return res


def main():
    # Example 1: Output: [0,3]
    n = 6
    edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]

    # Example 2: Output: [0,2,3]
    # n = 5
    # edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findSmallestSetOfVertices(n, edges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
