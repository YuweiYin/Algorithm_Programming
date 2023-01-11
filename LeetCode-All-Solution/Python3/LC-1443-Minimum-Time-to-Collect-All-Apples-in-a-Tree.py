#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1443-Minimum-Time-to-Collect-All-Apples-in-a-Tree.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-11
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1443 - (Medium) - Minimum Time to Collect All Apples in a Tree
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

Description & Requirement:
    Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. 
    You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend 
    to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

    The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that 
    exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, 
    where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

Example 1:
    Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
    Output: 8 
    Explanation: The figure above represents the given tree where red vertices have an apple. 
        One optimal path to collect all apples is shown by the green arrows.  
Example 2:
    Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
    Output: 6
    Explanation: The figure above represents the given tree where red vertices have an apple. 
        One optimal path to collect all apples is shown by the green arrows.  
Example 3:
    Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
    Output: 0

Constraints:
    1 <= n <= 10^5
    edges.length == n - 1
    edges[i].length == 2
    0 <= ai < bi <= n - 1
    from_i < to_i
    hasApple.length == n
"""


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(edges, list) and len(edges) == n - 1
        for edge in edges:
            assert isinstance(edge, list) and len(edge) == 2
        assert isinstance(hasApple, list) and len(hasApple) == n
        # main method: (Union Find Set)
        return self._minTime(n, edges, hasApple)

    def _minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(edges, list) and len(edges) == n - 1
        for edge in edges:
            assert isinstance(edge, list) and len(edge) == 2
        assert isinstance(hasApple, list) and len(hasApple) == n

        ufs_pa = [0 for _ in range(n)]  # parents
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        queue = [0]
        visited = set()
        visited.add(0)
        while len(queue) > 0:
            for _ in range(len(queue)):
                cur_idx = queue.pop(0)
                for next_idx in adj[cur_idx]:
                    if next_idx not in visited:
                        visited.add(next_idx)
                        ufs_pa[next_idx] = cur_idx
                        queue.append(next_idx)

        res = 0
        visited = set()
        for idx in range(n - 1, -1, -1):
            if hasApple[idx]:
                if idx == 0:
                    continue
                pa = idx
                while pa != 0 and pa not in visited:
                    visited.add(pa)
                    pa = ufs_pa[pa]
                    res += 2

        return res


def main():
    # Example 1: Output: 8
    # n = 7
    # edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    # hasApple = [False, False, True, False, True, True, False]

    # Example 2: Output: 6
    # n = 7
    # edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    # hasApple = [False, False, True, False, False, True, False]

    # Example 3: Output: 0
    n = 7
    edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    hasApple = [False, False, False, False, False, False, False]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minTime(n, edges, hasApple)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
