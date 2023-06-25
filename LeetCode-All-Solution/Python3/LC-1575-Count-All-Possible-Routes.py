#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1575-Count-All-Possible-Routes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-25
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 1575 - (Hard) - Count All Possible Routes
https://leetcode.com/problems/count-all-possible-routes/

Description & Requirement:
    You are given an array of distinct positive integers locations where 
    ocations[i] represents the position of city i. You are also given integers start, 
    finish and fuel representing the starting city, ending city, and 
    the initial amount of fuel you have, respectively.

    At each step, if you are at city i, you can pick any city j such that 
    j != i and 0 <= j < locations.length and move to city j. 
    Moving from city i to city j reduces the amount of fuel you have by |locations[i] - locations[j]|. 
    Please notice that |x| denotes the absolute value of x.

    Notice that fuel cannot become negative at any point in time, and 
    that you are allowed to visit any city more than once (including start and finish).

    Return the count of all possible routes from start to finish. 
    Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
    Input: locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
    Output: 4
    Explanation: The following are all possible routes, each uses 5 units of fuel:
        1 -> 3
        1 -> 2 -> 3
        1 -> 4 -> 3
        1 -> 4 -> 2 -> 3
Example 2:
    Input: locations = [4,3,1], start = 1, finish = 0, fuel = 6
    Output: 5
    Explanation: The following are all possible routes:
        1 -> 0, used fuel = 1
        1 -> 2 -> 0, used fuel = 5
        1 -> 2 -> 1 -> 0, used fuel = 5
        1 -> 0 -> 1 -> 0, used fuel = 3
        1 -> 0 -> 1 -> 0 -> 1 -> 0, used fuel = 5
Example 3:
    Input: locations = [5,2,1], start = 0, finish = 2, fuel = 3
    Output: 0
    Explanation: It is impossible to get from 0 to 2 using only 3 units of fuel since 
        the shortest route needs 4 units of fuel.

Constraints:
    2 <= locations.length <= 100
    1 <= locations[i] <= 10^9
    All integers in locations are distinct.
    0 <= start, finish < locations.length
    1 <= fuel <= 200
"""


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # exception case
        assert isinstance(locations, list) and len(locations) >= 2
        assert isinstance(start, int) and start >= 0
        assert isinstance(finish, int) and finish >= 0
        assert isinstance(fuel, int) and fuel >= 1
        # main method: (dynamic programming)
        return self._countRoutes(locations, start, finish, fuel)

    def _countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        assert isinstance(locations, list) and len(locations) >= 2
        assert isinstance(start, int) and start >= 0
        assert isinstance(finish, int) and finish >= 0
        assert isinstance(fuel, int) and fuel >= 1

        MOD = int(1e9+7)

        n = len(locations)
        startPos = locations[start]
        finishPos = locations[finish]
        locations.sort()
        start = locations.index(startPos)
        finish = locations.index(finishPos)

        dp_left = [[0] * (fuel + 1) for _ in range(n)]
        dp_right = [[0] * (fuel + 1) for _ in range(n)]
        dp_left[start][0] = dp_right[start][0] = 1

        for used in range(fuel + 1):
            for city in range(n - 2, -1, -1):
                if (delta := locations[city + 1] - locations[city]) <= used:
                    dp_left[city][used] = ((0 if used == delta else dp_left[city + 1][used - delta]) * 2 +
                                           dp_right[city + 1][used - delta]) % MOD
            for city in range(1, n):
                if (delta := locations[city] - locations[city - 1]) <= used:
                    dp_right[city][used] = ((0 if used == delta else dp_right[city - 1][used - delta]) * 2 +
                                            dp_left[city - 1][used - delta]) % MOD

        res = sum(dp_left[finish]) + sum(dp_right[finish])
        if start == finish:
            res -= 1

        return res % MOD


def main():
    # Example 1: Output: 4
    locations = [2, 3, 6, 8, 4]
    start = 1
    finish = 3
    fuel = 5

    # Example 2: Output: 5
    # locations = [4, 3, 1]
    # start = 1
    # finish = 0
    # fuel = 6

    # Example 3: Output: 0
    # locations = [5, 2, 1]
    # start = 0
    # finish = 2
    # fuel = 3

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.countRoutes(locations, start, finish, fuel)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
