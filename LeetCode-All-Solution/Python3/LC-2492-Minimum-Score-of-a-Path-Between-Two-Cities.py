#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2492-Minimum-Score-of-a-Path-Between-Two-Cities.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-22
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2492 - (Medium) - Minimum Score of a Path Between Two Cities
https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

Description & Requirement:
    You are given a positive integer n representing n cities numbered from 1 to n. 
    You are also given a 2D array roads where roads[i] = [ai, bi, distance_i] indicates that 
    there is a bidirectional road between cities ai and bi with a distance equal to distance_i. 
    The cities graph is not necessarily connected.

    The score of a path between two cities is defined as the minimum distance of a road in this path.

    Return the minimum possible score of a path between cities 1 and n.

    Note:
        A path is a sequence of roads between two cities.
        It is allowed for a path to contain the same road multiple times, and 
            you can visit cities 1 and n multiple times along the path.
        The test cases are generated such that there is at least one path between 1 and n.

Example 1:
    Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
    Output: 5
    Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. 
        The score of this path is min(9,5) = 5.
        It can be shown that no other path has less score.
Example 2:
    Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
    Output: 2
    Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. 
        The score of this path is min(2,2,4,7) = 2.

Constraints:
    2 <= n <= 10^5
    1 <= roads.length <= 10^5
    roads[i].length == 3
    1 <= ai, bi <= n
    ai != bi
    1 <= distance_i <= 10^4
    There are no repeated edges.
    There is at least one path between 1 and n.
"""


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # exception case
        assert isinstance(n, int) and n >= 2
        assert isinstance(roads, list) and len(roads) >= 1
        # main method: (DFS)
        return self._minScore(n, roads)

    def _minScore(self, n: int, roads: List[List[int]]) -> int:
        assert isinstance(n, int) and n >= 2
        assert isinstance(roads, list) and len(roads) >= 1

        graph = [[] for _ in range(n)]
        for _from, _to, dist in roads:
            graph[_from - 1].append([_to - 1, dist])
            graph[_to - 1].append([_from - 1, dist])

        res = [int(1e9+7)]
        visited = [False] * n

        def __dfs(cur_node: int) -> None:
            visited[cur_node] = True
            for next_node, dist in graph[cur_node]:
                res[0] = min(res[0], dist)
                if not visited[next_node]:
                    __dfs(next_node)

        __dfs(0)
        return res[0]


def main():
    # Example 1: Output: 5
    # n = 4
    # roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]

    # Example 2: Output: 2
    n = 4
    roads = [[1, 2, 2], [1, 3, 4], [3, 4, 7]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minScore(n, roads)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
