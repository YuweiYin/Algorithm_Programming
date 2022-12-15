#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1697-Checking-Existence-of-Edge-Length-Limited-Paths.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-14
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1697 - (Hard) - Checking Existence of Edge Length Limited Paths
https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

Description & Requirement:
    An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, dis_i] 
    denotes an edge between nodes ui and vi with distance dis_i. 
    Note that there may be multiple edges between two nodes.

    Given an array queries, where queries[j] = [pj, qj, limit_j], your task is to determine for each queries[j] 
    whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limit_j.

    Return a boolean array answer, where answer.length == queries.length and the j-th value of answer is true 
    if there is a path for queries[j] is true, and false otherwise.

Example 1:
    Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
    Output: [false,true]
    Explanation: The above figure shows the given graph. 
        Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
        For the first query, between 0 and 1 there is no path where each distance is less than 2, 
            thus we return false for this query.
        For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, 
            thus we return true for this query.
Example 2:
    Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
    Output: [true,false]
    Explanation: The above figure shows the given graph.

Constraints:
    2 <= n <= 10^5
    1 <= edgeList.length, queries.length <= 10^5
    edgeList[i].length == 3
    queries[j].length == 3
    0 <= ui, vi, pj, qj <= n - 1
    ui != vi
    pj != qj
    1 <= dis_i, limit_j <= 10^9
    There may be multiple edges between two nodes.
"""


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # exception case
        assert isinstance(n, int) and n >= 2
        assert isinstance(edgeList, list) and len(edgeList) >= 1
        assert isinstance(queries, list) and len(queries) >= 1
        # main method: (Union Find Set)
        return self._distanceLimitedPathsExist(n, edgeList, queries)

    def _distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        Time: beats 97.71%; Space: beats 53.59%
        """
        assert isinstance(n, int) and n >= 2
        assert isinstance(edgeList, list) and len(edgeList) >= 1
        assert isinstance(queries, list) and len(queries) >= 1

        edgeList.sort(key=lambda e: e[2])

        ufs = list(range(n))

        def _find(_item: int) -> int:
            if ufs[_item] != _item:
                ufs[_item] = _find(ufs[_item])
            return ufs[_item]

        def _merge(_from: int, _to: int) -> None:
            ufs[_find(_from)] = _find(_to)

        res, k = [False] * len(queries), 0

        for idx, (p, q, limit) in sorted(enumerate(queries), key=lambda x: x[1][2]):
            while k < len(edgeList) and edgeList[k][2] < limit:
                _merge(edgeList[k][0], edgeList[k][1])
                k += 1
            res[idx] = _find(p) == _find(q)

        return res


def main():
    # Example 1: Output: [false,true]
    # n = 3
    # edgeList = [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]]
    # queries = [[0, 1, 2], [0, 2, 5]]

    # Example 2: Output: [true,false]
    n = 5
    edgeList = [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]]
    queries = [[0, 4, 14], [1, 4, 13]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.distanceLimitedPathsExist(n, edgeList, queries)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
