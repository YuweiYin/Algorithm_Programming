#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0875-Koko-Eating-Bananas.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-20
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0875 - (Medium) - Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/

Description & Requirement:
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
    The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, 
    she chooses some pile of bananas and eats k bananas from that pile. 
    If the pile has less than k bananas, she eats all of them instead and 
    will not eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

    Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
    Input: piles = [3,6,7,11], h = 8
    Output: 4
Example 2:
    Input: piles = [30,11,23,4,20], h = 5
    Output: 30
Example 3:
    Input: piles = [30,11,23,4,20], h = 6
    Output: 23

Constraints:
    1 <= piles.length <= 10^4
    piles.length <= h <= 10^9
    1 <= piles[i] <= 10^9
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # exception case
        if not isinstance(piles, list) or len(piles) <= 0:
            return 0  # Error input type
        assert h >= len(piles)  # otherwise, won't finish eating all piles according to the rule
        if len(piles) == 1:
            quotient_floor = int(piles[0] / h)
            if quotient_floor * h >= piles[0]:
                return quotient_floor
            else:
                assert (quotient_floor + 1) * h >= piles[0]
                return quotient_floor + 1
        # main method: (try possible eating speed, using binary search)
        return self._minEatingSpeed(piles, h)

    def _minEatingSpeed(self, piles: List[int], h: int) -> int:
        len_piles = len(piles)
        assert 1 < len_piles <= h

        INF = sys.maxsize

        def __check_if_finish(test_speed: int) -> bool:
            """
            :return: True: can finish; False: can't finish, test_speed is too slow.
            """
            total_hours = 0
            for pile in piles:
                if pile % test_speed == 0:
                    total_hours += pile // test_speed
                else:
                    total_hours += (pile // test_speed) + 1
            return True if total_hours <= h else False

        def __binary_search_valid_speed(left_speed: int, right_speed: int) -> int:
            if left_speed == right_speed:
                return left_speed if __check_if_finish(left_speed) else INF
            if left_speed > right_speed:
                return INF

            mid_speed = (left_speed + right_speed) >> 1
            if __check_if_finish(mid_speed):
                return min(mid_speed, __binary_search_valid_speed(left_speed, mid_speed - 1))
            else:  # mid_speed can't finish, speed up
                return __binary_search_valid_speed(mid_speed + 1, right_speed)

        return __binary_search_valid_speed(1, max(piles))


def main():
    # Example 1: Output: 4
    piles = [3, 6, 7, 11]
    h = 8

    # Example 2: Output: 30
    # piles = [30, 11, 23, 4, 20]
    # h = 5

    # Example 3: Output: 23
    # piles = [30, 11, 23, 4, 20]
    # h = 6

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minEatingSpeed(piles, h)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
