#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0547-Number-of-Provinces.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-19
=================================================================="""

import sys
import time
from typing import List
import collections

"""
LeetCode - 0547 - (Medium) - Number of Provinces
https://leetcode.com/problems/number-of-provinces/

Description & Requirement:
    There are n cities. Some of them are connected, while some are not. 
    If city a is connected directly with city b, and city b is connected directly with city c, 
    then city a is connected indirectly with city c.

    A province is a group of directly or indirectly connected cities 
    and no other cities outside of the group.

    You are given an n x n matrix isConnected where isConnected[i][j] = 1 
    if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

    Return the total number of provinces.

Example 1:
    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2
Example 2:
    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3

Constraints:
    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]
"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # exception case
        if not isinstance(isConnected, list) or len(isConnected) <= 0:
            return 0  # Error input type
        if not isinstance(isConnected[0], list) or len(isConnected[0]) <= 0:
            return 0  # Error input type
        n = len(isConnected)
        for row in isConnected:
            if len(row) != n:
                return 0  # Error input type (must be n * n matrix)
        # main method: (dfs on directed graph)
        return self._findCircleNum(isConnected)

    def _findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        assert n > 0
        city_done_dfs = [False for _ in range(n)]  # False: uncharted city; True: charted city.

        def __dfs(start_city: int) -> int:
            if not (0 <= start_city < n):
                return 0
            for to_city in range(n):  # go to each directly connected city, except the start_city itself
                if to_city != start_city and not city_done_dfs[to_city] and isConnected[start_city][to_city] == 1:
                    city_done_dfs[to_city] = True
                    __dfs(to_city)
            return 1  # have traversed one whole province

        province_counter = 0
        for city in range(n):
            if not city_done_dfs[city]:
                city_done_dfs[city] = True  # mark the start city
                province_counter += __dfs(city)  # dfs for each uncharted city

        return province_counter


def main():
    # Example 1: Output: 2
    # isConnected = [
    #     [1, 1, 0],
    #     [1, 1, 0],
    #     [0, 0, 1]
    # ]

    # Example 2: Output: 3
    # isConnected = [
    #     [1, 0, 0],
    #     [0, 1, 0],
    #     [0, 0, 1]
    # ]

    # Example 2: Output: 1
    isConnected = [
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 1]
    ]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findCircleNum(isConnected)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
