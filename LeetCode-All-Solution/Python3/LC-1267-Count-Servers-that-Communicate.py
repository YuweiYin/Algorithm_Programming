#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1267-Count-Servers-that-Communicate.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-24
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 1267 - (Medium) Count Servers that Communicate
https://leetcode.com/problems/count-servers-that-communicate/

Description & Requirement:
    You are given a map of a server center, represented as a m * n integer matrix grid, 
    where 1 means that on that cell there is a server and 0 means that it is no server. 
    Two servers are said to communicate if they are on the same row or on the same column.

    Return the number of servers that communicate with any other server.

Example 1:
    Input: grid = [[1,0],[0,1]]
    Output: 0
    Explanation: No servers can communicate with others.
Example 2:
    Input: grid = [[1,0],[1,1]]
    Output: 3
    Explanation: All three servers can communicate with at least one other server.
Example 3:
    Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    Output: 4
    Explanation: The two servers in the first row can communicate with each other. 
        The two servers in the third column can communicate with each other. 
        The server at right bottom corner can't communicate with any other server.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m <= 250
    1 <= n <= 250
    grid[i][j] == 0 or 1
"""


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # exception case
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1
        # main method: (hash counter)
        return self._countServers(grid)

    def _countServers(self, grid: List[List[int]]) -> int:
        assert isinstance(grid, list) and len(grid) >= 1 and len(grid[0]) >= 1

        m, n = len(grid), len(grid[0])
        rows, cols = collections.Counter(), collections.Counter()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    res += 1

        return res


def main():
    # Example 1: Output: 0
    # grid = [[1, 0], [0, 1]]

    # Example 2: Output: 3
    # grid = [[1, 0], [1, 1]]

    # Example 3: Output: 4
    grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.countServers(grid)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
