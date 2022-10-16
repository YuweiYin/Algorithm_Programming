#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0886-Possible-Bipartition.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-16
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0886 - (Medium) - Possible Bipartition
https://leetcode.com/problems/possible-bipartition/

Description & Requirement:
    We want to split a group of n people (labeled from 1 to n) into two groups of any size. 
    Each person may dislike some other people, and they should not go into the same group.

    Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that 
    the person labeled ai does not like the person labeled bi, 
    return true if it is possible to split everyone into two groups in this way.

Example 1:
    Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
    Output: true
    Explanation: group1 [1,4] and group2 [2,3].
Example 2:
    Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
    Output: false
Example 3:
    Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    Output: false

Constraints:
    1 <= n <= 2000
    0 <= dislikes.length <= 10^4
    dislikes[i].length == 2
    1 <= dislikes[i][j] <= n
    ai < bi
    All the pairs of dislikes are unique.
"""


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # exception case
        assert isinstance(dislikes, list) and isinstance(n, int) and n >= 1
        for dis in dislikes:
            assert isinstance(dis, list) and len(dis) == 2 and 1 <= dis[0] < dis[1] <= n
        # main method: (DFS / BFS / Union Find Set)
        return self._possibleBipartition(n, dislikes)

    def _possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        assert isinstance(dislikes, list) and isinstance(n, int) and n >= 1

        graph = [[] for _ in range(n)]
        for x, y in dislikes:  # bi-directional
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        visit = [0 for _ in range(n)]  # visit[x] == 0 means that node x has not been visited

        def __dfs(_idx: int, _v: int) -> bool:
            visit[_idx] = _v
            return all(visit[_y] != _v and (visit[_y] or __dfs(_y, -_v)) for _y in graph[_idx])

        return all(v or __dfs(idx, 1) for idx, v in enumerate(visit))


def main():
    # Example 1: Output: true
    # n = 4
    # dislikes = [[1, 2], [1, 3], [2, 4]]

    # Example 2: Output: false
    # n = 3
    # dislikes = [[1, 2], [1, 3], [2, 3]]

    # Example 3: Output: false
    n = 5
    dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.possibleBipartition(n, dislikes)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
