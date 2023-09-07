#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2594-Minimum-Time-to-Repair-Cars.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-07
=================================================================="""

import sys
import time
from typing import List
import math
# import collections
# import functools
# import itertools

"""
LeetCode - 2594 - (Medium) Minimum Time to Repair Cars
https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

Description & Requirement:
    You are given an integer array ranks representing the ranks of some mechanics. 
    ranks_i is the rank of the i-th mechanic. 
    A mechanic with a rank r can repair n cars in r * n^2 minutes.

    You are also given an integer cars representing the total number of cars 
    waiting in the garage to be repaired.

    Return the minimum time taken to repair all the cars.

    Note: All the mechanics can repair the cars simultaneously.

Example 1:
    Input: ranks = [4,2,3,1], cars = 10
    Output: 16
    Explanation: 
        - The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
        - The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
        - The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
        - The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
        It can be proved that the cars cannot be repaired in less than 16 minutes.
Example 2:
    Input: ranks = [5,1,8], cars = 6
    Output: 16
    Explanation: 
        - The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
        - The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
        - The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
        It can be proved that the cars cannot be repaired in less than 16 minutes.

Constraints:
    1 <= ranks.length <= 10^5
    1 <= ranks[i] <= 100
    1 <= cars <= 10^6
"""


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # exception case
        assert isinstance(ranks, list) and len(ranks) >= 1
        assert isinstance(cars, int) and cars >= 1
        # main method: (binary search)
        return self._repairCars(ranks, cars)

    def _repairCars(self, ranks: List[int], cars: int) -> int:
        assert isinstance(ranks, list) and len(ranks) >= 1
        assert isinstance(cars, int) and cars >= 1

        left, right = 1, ranks[0] * cars * cars

        def __check(m: int) -> bool:
            return sum([math.floor(math.sqrt(m // x)) for x in ranks]) >= cars

        while left < right:
            mid = left + right >> 1
            if __check(mid):
                right = mid
            else:
                left = mid + 1

        return left


def main():
    # Example 1: Output: 16
    ranks = [4, 2, 3, 1]
    cars = 10

    # Example 2: Output: 16
    # ranks = [5, 1, 8]
    # cars = 6

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.repairCars(ranks, cars)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
