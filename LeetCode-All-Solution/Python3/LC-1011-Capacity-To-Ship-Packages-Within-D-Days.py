#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1011-Capacity-To-Ship-Packages-Within-D-Days.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-22
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1011 - (Medium) - Capacity To Ship Packages Within D Days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

Description & Requirement:
    A conveyor belt has packages that must be shipped from one port to another within days days.

    The ith package on the conveyor belt has a weight of weights[i]. Each day, 
    we load the ship with packages on the conveyor belt (in the order given by weights). 
    We may not load more weight than the maximum weight capacity of the ship.

    Return the least weight capacity of the ship that will result in 
    all the packages on the conveyor belt being shipped within days days.

Example 1:
    Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    Output: 15
    Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
        1st day: 1, 2, 3, 4, 5
        2nd day: 6, 7
        3rd day: 8
        4th day: 9
        5th day: 10
        Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and 
        splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2:
    Input: weights = [3,2,2,4,1,4], days = 3
    Output: 6
    Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
        1st day: 3, 2
        2nd day: 2, 4
        3rd day: 1, 4
Example 3:
    Input: weights = [1,2,3,1,1], days = 4
    Output: 3
    Explanation:
        1st day: 1
        2nd day: 2
        3rd day: 3
        4th day: 1, 1

Constraints:
    1 <= days <= weights.length <= 5 * 10^4
    1 <= weights[i] <= 500
"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # exception case
        assert isinstance(days, int) and days >= 1
        assert isinstance(weights, list) and len(weights) >= days
        # main method: (binary search)
        return self._shipWithinDays(weights, days)

    def _shipWithinDays(self, weights: List[int], days: int) -> int:
        assert isinstance(days, int) and days >= 1
        assert isinstance(weights, list) and len(weights) >= days

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) >> 1
            need_days, cur_weights = 1, 0
            for weight in weights:
                if cur_weights + weight > mid:
                    need_days += 1
                    cur_weights = 0
                cur_weights += weight

            if need_days <= days:
                right = mid
            else:
                left = mid + 1

        return left


def main():
    # Example 1: Output: 15
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5

    # Example 2: Output: 6
    # weights = [3, 2, 2, 4, 1, 4]
    # days = 3

    # Example 3: Output: 3
    # weights = [1, 2, 3, 1, 1]
    # days = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.shipWithinDays(weights, days)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
