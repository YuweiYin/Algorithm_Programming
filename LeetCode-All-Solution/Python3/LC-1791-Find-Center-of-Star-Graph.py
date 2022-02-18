#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1791-Find-Center-of-Star-Graph.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-18
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1791 - (Easy) - Find Center of Star Graph
https://leetcode.com/problems/find-center-of-star-graph/

Description & Requirement:
    There is an undirected star graph consisting of n nodes labeled from 1 to n. 
    A star graph is a graph where there is one center node and exactly n - 1 edges 
    that connect the center node with every other node.

    You are given a 2D integer array edges where each edges[i] = [u_i, v_i] indicates that 
    there is an edge between the nodes u_i and v_i. 
    Return the center of the given star graph.

Example 1:
    Input: edges = [[1,2],[2,3],[4,2]]
    Output: 2
    Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
Example 2:
    Input: edges = [[1,2],[5,1],[1,3],[1,4]]
    Output: 1

Constraints:
    3 <= n <= 10^5
    edges.length == n - 1
    edges[i].length == 2
    1 <= u_i, v_i <= n
    u_i != v_i
    The given edges represent a valid star graph.
"""


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # exception case
        assert isinstance(edges, list) and len(edges) >= 2
        for edge in edges:
            assert isinstance(edge, list) and len(edge) == 2
        # main method: (dict counter, the degree of star center is equal to the number of edges)
        #     optimize: just randomly pick two edges, find the node that appears twice, that is star center
        # return self._findCenter(edges)  # Time: O(n); Space: O(n).
        return self._findCenterOptimize(edges)  # Time: O(1); Space: O(1).

    def _findCenter(self, edges: List[List[int]]) -> int:
        len_edges = len(edges)

        counter = dict({})
        for edge in edges:
            for node in edge:
                if node not in counter:
                    counter[node] = 1
                else:
                    counter[node] += 1

        res = 1
        for node, count in counter.items():
            if count == len_edges:
                res = node
                break

        return res

    def _findCenterOptimize(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]  # edges[0][0] appears twice
        else:
            return edges[0][1]  # else, edges[0][1] must appear twice


def main():
    # Example 1: Output: 2
    # edges = [[1, 2], [2, 3], [4, 2]]

    # Example 2: Output: 1
    edges = [[1, 2], [5, 1], [1, 3], [1, 4]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findCenter(edges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
