#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0797-All-Paths-From-Source-to-Target.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-21
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0797 - (Medium) - All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target/

Description & Requirement:
    Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
    find all possible paths from node 0 to node n - 1 and return them in any order.

    The graph is given as follows: graph[i] is a list of all nodes you can visit from node i 
    (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:
    Input: graph = [[1,2],[3],[3],[]]
    Output: [[0,1,3],[0,2,3]]
    Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:
    Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
    Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Constraints:
    n == graph.length
    2 <= n <= 15
    0 <= graph[i][j] < n
    graph[i][j] != i (i.e., there will be no self-loops).
    All the elements of graph[i] are unique.
    The input graph is guaranteed to be a DAG.
"""


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # exception case
        if not isinstance(graph, list) or len(graph) <= 0 or not isinstance(graph[0], list) or len(graph[0]) <= 0:
            return []  # Error input type
        # main method: (dfs & backtrace, find all paths)
        return self._allPathsSourceTarget(graph)

    def _allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)  # number of nodes
        assert n > 0

        res_path = []

        def __dfs(start_node: int, cur_path: list):
            assert 0 <= start_node < n
            cur_path.append(start_node)
            if start_node == n - 1:
                res_path.append(cur_path[:])  # find a valid path
                return

            for next_node in graph[start_node]:
                __dfs(next_node, cur_path)  # go deeper to each possible next node
                cur_path.pop()  # backtrace

        __dfs(0, [])
        return res_path


def main():
    # Example 1: Output: [[0,1,3],[0,2,3]]
    graph = [[1, 2], [3], [3], []]

    # Example 2: Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    # graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.allPathsSourceTarget(graph)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
