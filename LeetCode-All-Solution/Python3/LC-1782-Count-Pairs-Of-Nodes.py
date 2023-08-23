#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1782-Count-Pairs-Of-Nodes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-23
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 1782 - (Hard) Count Pairs Of Nodes
https://leetcode.com/problems/count-pairs-of-nodes/

Description & Requirement:
    You are given an undirected graph defined by an integer n, the number of nodes, and 
    a 2D integer array edges, the edges in the graph, where edges[i] = [ui, vi] indicates that 
    there is an undirected edge between ui and vi. You are also given an integer array queries.

    Let incident(a, b) be defined as the number of edges that are connected to either node a or b.

    The answer to the j-th query is the number of pairs of nodes (a, b) that 
    satisfy both of the following conditions:
        a < b
        incident(a, b) > queries[j]

    Return an array answers such that answers.length == queries.length and 
    answers[j] is the answer of the j-th query.

    Note that there can be multiple edges between the same two nodes.

Example 1:
    Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
    Output: [6,5]
    Explanation: The calculations for incident(a, b) are shown in the table above.
    The answers for each of the queries are as follows:
    - answers[0] = 6. All the pairs have an incident(a, b) value greater than 2.
    - answers[1] = 5. All the pairs except (3, 4) have an incident(a, b) value greater than 3.
Example 2:
    Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
    Output: [10,10,9,8,6]

Constraints:
    2 <= n <= 2 * 10^4
    1 <= edges.length <= 10^5
    1 <= ui, vi <= n
    ui != vi
    1 <= queries.length <= 20
    0 <= queries[j] < edges.length
"""


class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        # exception case
        assert isinstance(n, int) and n >= 2
        assert isinstance(edges, list) and len(edges) >= 1
        assert isinstance(queries, list) and len(queries) >= 1
        # main method: (two pointers)
        return self._countPairs(n, edges, queries)

    def _countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        assert isinstance(n, int) and n >= 2
        assert isinstance(edges, list) and len(edges) >= 1
        assert isinstance(queries, list) and len(queries) >= 1

        degree = [0 for _ in range(n)]
        cnt = collections.defaultdict(int)
        for edge in edges:
            x, y = edge[0] - 1, edge[1] - 1
            if x > y:
                x, y = y, x
            degree[x] += 1
            degree[y] += 1
            cnt[x * n + y] += 1

        arr = sorted(degree)
        res = []
        for bound in queries:
            total = 0
            j = n - 1
            for i in range(n):
                while j > i and arr[i] + arr[j] > bound:
                    j -= 1
                total += n - 1 - max(i, j)
            for val, freq in cnt.items():
                x, y = val // n, val % n
                if degree[x] + degree[y] > bound >= degree[x] + degree[y] - freq:
                    total -= 1
            res.append(total)

        return res


def main():
    # Example 1: Output: [6,5]
    # n = 4
    # edges = [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]]
    # queries = [2, 3]

    # Example 2: Output: [10,10,9,8,6]
    n = 5
    edges = [[1, 5], [1, 5], [3, 4], [2, 5], [1, 3], [5, 1], [2, 3], [2, 5]]
    queries = [1, 2, 3, 4, 5]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.countPairs(n, edges, queries)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
