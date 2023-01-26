#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0787-Cheapest-Flights-Within-K-Stops.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-26
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0787 - (Medium) - Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/

Description & Requirement:
    There are n cities connected by some number of flights. 
    You are given an array flights where flights[i] = [from_i, to_i, price_i] indicates that 
    there is a flight from city from_i to city to_i with cost price_i.

    You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
    If there is no such route, return -1.

Example 1:
    Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
    Output: 700
    Explanation:
        The graph is shown above.
        The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
        Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Example 2:
    Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
    Output: 200
    Explanation:
        The graph is shown above.
        The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
Example 3:
    Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
    Output: 500
    Explanation:
        The graph is shown above.
        The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

Constraints:
    1 <= n <= 100
    0 <= flights.length <= (n * (n - 1) / 2)
    flights[i].length == 3
    0 <= from_i, to_i < n
    from_i != to_i
    1 <= price_i <= 10^4
    There will not be any multiple flights between two cities.
    0 <= src, dst, k < n
    src != dst
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(src, int) and 0 <= src < n
        assert isinstance(dst, int) and 0 <= dst < n
        assert isinstance(k, int) and 0 <= k < n
        assert isinstance(flights, list)
        # main method: (dynamic programming)
        return self._findCheapestPrice(n, flights, src, dst, k)

    def _findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(src, int) and 0 <= src < n
        assert isinstance(dst, int) and 0 <= dst < n
        assert isinstance(k, int) and 0 <= k < n
        assert isinstance(flights, list)

        dp = [[float("inf")] * n for _ in range(k + 2)]
        dp[0][src] = 0
        for target in range(1, k + 2):
            for from_i, to_i, price_i in flights:
                dp[target][to_i] = min(dp[target][to_i], dp[target - 1][from_i] + price_i)

        res = min(dp[target][dst] for target in range(1, k + 2))

        return -1 if res == float("inf") else res


def main():
    # Example 1: Output: 700
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1

    # Example 2: Output: 200
    # n = 3
    # flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    # src = 0
    # dst = 2
    # k = 1

    # Example 3: Output: 500
    # n = 3
    # flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    # src = 0
    # dst = 2
    # k = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findCheapestPrice(n, flights, src, dst, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
