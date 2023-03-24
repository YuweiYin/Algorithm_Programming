#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1466-Reorder-Routes-to-Make-All-Paths-Lead-to-the-City-Zero.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-24
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1466 - (Medium) - Reorder Routes to Make All Paths Lead to the City Zero
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

Description & Requirement:
    There are n cities numbered from 0 to n - 1 and n - 1 roads such that 
    there is only one way to travel between two different cities (this network form a tree). 
    Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

    Roads are represented by connections where connections[i] = [ai, bi] 
    represents a road from city ai to city bi.

    This year, there will be a big event in the capital (city 0), 
    and many people want to travel to this city.

    Your task consists of reorienting some roads such that each city can visit the city 0. 
    Return the minimum number of edges changed.

    It's guaranteed that each city can reach city 0 after reorder.

Example 1:
    Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    Output: 3
    Explanation: Change the direction of edges show in red such that 
        each node can reach the node 0 (capital).
Example 2:
    Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
    Output: 2
    Explanation: Change the direction of edges show in red such that 
        each node can reach the node 0 (capital).
Example 3:
    Input: n = 3, connections = [[1,0],[2,0]]
    Output: 0

Constraints:
    2 <= n <= 5 * 10^4
    connections.length == n - 1
    connections[i].length == 2
    0 <= ai, bi <= n - 1
    ai != bi
"""


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # exception case
        assert isinstance(n, int) and n >= 2
        assert isinstance(connections, list) and len(connections) == n - 1
        # main method: (BFS)
        return self._minReorder(n, connections)

    def _minReorder(self, n: int, connections: List[List[int]]) -> int:
        assert isinstance(n, int) and n >= 2
        assert isinstance(connections, list) and len(connections) == n - 1

        edge_1, edge_2 = [[] for _ in range(n)], [[] for _ in range(n)]
        start = [False] * n

        for conn in connections:
            edge_1[conn[0]].append(conn[1])
            edge_2[conn[1]].append(conn[0])

        res = 0
        queue = [0]
        start[0] = True

        while len(queue) > 0:
            front = queue[0]

            for e in edge_1[front]:
                assert isinstance(e, int)
                if not start[e]:
                    start[e] = True
                    queue.append(e)
                    res += 1

            for e in edge_2[front]:
                assert isinstance(e, int)
                if not start[e]:
                    start[e] = True
                    queue.append(e)

            queue = queue[1:]

        return res


def main():
    # Example 1: Output: 3
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

    # Example 2: Output: 2
    # n = 5
    # connections = [[1, 0], [1, 2], [3, 2], [3, 4]]

    # Example 3: Output: 0
    # n = 3
    # connections = [[1, 0], [2, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minReorder(n, connections)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
