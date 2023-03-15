#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1615-Maximal-Network-Rank.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-15
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1615 - (Medium) - Maximal Network Rank
https://leetcode.com/problems/maximal-network-rank/

Description & Requirement:
    There is an infrastructure of n cities with some number of roads connecting these cities. 
    Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

    The network rank of two different cities is defined as the total number of directly connected 
    roads to either city. If a road is directly connected to both cities, it is only counted once.

    The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

    Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Example 1:
    Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
    Output: 4
    Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that 
        are connected to either 0 or 1. The road between 0 and 1 is only counted once.
Example 2:
    Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
    Output: 5
    Explanation: There are 5 roads that are connected to cities 1 or 2.
Example 3:
    Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
    Output: 5
    Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.

Constraints:
    2 <= n <= 100
    0 <= roads.length <= n * (n - 1) / 2
    roads[i].length == 2
    0 <= ai, bi <= n-1
    ai != bi
    Each pair of cities has at most one road connecting them.
"""


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # exception case
        assert isinstance(n, int) and n >= 2
        assert isinstance(roads, list)
        # main method: (enumeration)
        return self._maximalNetworkRank(n, roads)

    def _maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        assert isinstance(n, int) and n >= 2
        assert isinstance(roads, list)

        connect = [[False] * n for _ in range(n)]
        degree = [0] * n
        for a, b in roads:
            connect[a][b] = True
            connect[b][a] = True
            degree[a] += 1
            degree[b] += 1

        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j] - connect[i][j]
                max_rank = max(max_rank, rank)

        return max_rank


def main():
    # Example 1: Output: 4
    # n = 4
    # roads = [[0, 1], [0, 3], [1, 2], [1, 3]]

    # Example 2: Output: 5
    # n = 5
    # roads = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]

    # Example 3: Output: 5
    n = 8
    roads = [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.maximalNetworkRank(n, roads)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
