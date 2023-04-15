#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1042-Flower-Planting-With-No-Adjacent.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-15
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1042 - (Medium) - Flower Planting With No Adjacent
https://leetcode.com/problems/flower-planting-with-no-adjacent/

Description & Requirement:
    You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] 
    describes a bidirectional path between garden xi to garden yi. 
    In each garden, you want to plant one of 4 types of flowers.

    All gardens have at most 3 paths coming into or leaving it.

    Your task is to choose a flower type for each garden such that, 
    for any two gardens connected by a path, they have different types of flowers.

    Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden.
    The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

Example 1:
    Input: n = 3, paths = [[1,2],[2,3],[3,1]]
    Output: [1,2,3]
    Explanation:
        Gardens 1 and 2 have different types.
        Gardens 2 and 3 have different types.
        Gardens 3 and 1 have different types.
        Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].
Example 2:
    Input: n = 4, paths = [[1,2],[3,4]]
    Output: [1,2,1,2]
Example 3:
    Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
    Output: [1,2,3,4]

Constraints:
    1 <= n <= 10^4
    0 <= paths.length <= 2 * 10^4
    paths[i].length == 2
    1 <= xi, yi <= n
    xi != yi
    Every garden has at most 3 paths coming into or leaving it.
"""


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(paths, list)
        # main method: (hashing)
        return self._gardenNoAdj(n, paths)

    def _gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        assert isinstance(n, int) and n >= 1
        assert isinstance(paths, list)

        graph = [[] for _ in range(n)]
        for u, v in paths:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        color = [0] * n
        for idx, nodes in enumerate(graph):
            color[idx] = (set(range(1, 5)) - {color[node] for node in nodes}).pop()

        return color


def main():
    # Example 1: Output: [1,2,3]
    # n = 3
    # paths = [[1, 2], [2, 3], [3, 1]]

    # Example 2: Output: [1,2,1,2]
    # n = 4
    # paths = [[1, 2], [3, 4]]

    # Example 3: Output: [1,2,3,4]
    n = 4
    paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.gardenNoAdj(n, paths)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
