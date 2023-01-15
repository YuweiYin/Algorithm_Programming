#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2421-Number-of-Good-Paths.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-15
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2421 - (Hard) - Number of Good Paths
https://leetcode.com/problems/number-of-good-paths/

Description & Requirement:
    There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes 
    numbered from 0 to n - 1 and exactly n - 1 edges.

    You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. 
    You are also given a 2D integer array edges where 
    edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

    A good path is a simple path that satisfies the following conditions:

    The starting node and the ending node have the same value.
    All nodes between the starting node and the ending node have values less than or equal to the starting node 
    (i.e. the starting node's value should be the maximum value along the path).

    Return the number of distinct good paths.

    Note that a path and its reverse are counted as the same path. 
    For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.

Example 1:
    Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
    Output: 6
    Explanation: There are 5 good paths consisting of a single node.
        There is 1 additional good path: 1 -> 0 -> 2 -> 4.
        (The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
        Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
Example 2:
    Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
    Output: 7
    Explanation: There are 5 good paths consisting of a single node.
        There are 2 additional good paths: 0 -> 1 and 2 -> 3.
Example 3:
    Input: vals = [1], edges = []
    Output: 1
    Explanation: The tree consists of only one node, so there is one good path.

Constraints:
    n == vals.length
    1 <= n <= 3 * 10^4
    0 <= vals[i] <= 10^5
    edges.length == n - 1
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    edges represents a valid tree.
"""


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # exception case
        assert isinstance(vals, list) and len(vals) >= 1
        assert isinstance(edges, list) and len(vals) == len(edges) + 1
        # main method: (Union Find Set)
        return self._numberOfGoodPaths(vals, edges)

    def _numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        """
        Time: beats 92.92%; Space: beats 15.59%
        """
        assert isinstance(vals, list) and len(vals) >= 1
        assert isinstance(edges, list) and len(vals) == len(edges) + 1

        n = len(vals)
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        parent = list(range(n))
        size = [1] * n

        def __find(x: int) -> int:
            if parent[x] != x:
                parent[x] = __find(parent[x])
            return parent[x]

        res = n
        for x_val, x in sorted(zip(vals, range(n))):
            x_parent = __find(x)
            for y in graph[x]:
                assert isinstance(y, int)
                y = __find(y)
                if y == x_parent or vals[y] > x_val:
                    continue
                if vals[y] == x_val:
                    res += size[x_parent] * size[y]
                    size[x_parent] += size[y]
                parent[y] = x_parent

        return res


def main():
    # Example 1: Output: 6
    # vals = [1, 3, 2, 1, 3]
    # edges = [[0, 1], [0, 2], [2, 3], [2, 4]]

    # Example 2: Output: 7
    vals = [1, 1, 2, 2, 3]
    edges = [[0, 1], [1, 2], [2, 3], [2, 4]]

    # Example 3: Output: 1
    # vals = [1]
    # edges = []

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numberOfGoodPaths(vals, edges)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
