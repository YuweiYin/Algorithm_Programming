#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0849-Maximize-Distance-to-Closest-Person.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-16
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0849 - (Medium) - Maximize Distance to Closest Person
https://leetcode.com/problems/maximize-distance-to-closest-person/

Description & Requirement:
    You are given an array representing a row of seats 
    where seats[i] = 1 represents a person sitting in the ith seat, 
    and seats[i] = 0 represents that the ith seat is empty (0-indexed).

    There is at least one empty seat, and at least one person sitting.

    Alex wants to sit in the seat such that the distance 
    between him and the closest person to him is maximized. 

    Return that maximum distance to the closest person.

Example 1:
    Input: seats = [1,0,0,0,1,0,1]
    Output: 2
    Explanation: 
        If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
        If Alex sits in any other open seat, the closest person has distance 1.
        Thus, the maximum distance to the closest person is 2.
Example 2:
    Input: seats = [1,0,0,0]
    Output: 3
    Explanation: 
        If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
        This is the maximum distance possible, so the answer is 3.
Example 3:
    Input: seats = [0,1]
    Output: 1

Constraints:
    2 <= seats.length <= 2 * 10^4
    seats[i] is 0 or 1.
    At least one seat is empty.
    At least one seat is occupied.
"""


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # exception case
        if not isinstance(seats, list) or len(seats) <= 1:
            return 0  # Error input type
        if len(seats) == 2:
            return 1  # must be [0, 1] or [1, 0]
        # main method: (just scan the list and record max gap)
        return self._maxDistToClosest(seats)

    def _maxDistToClosest(self, seats: List[int]) -> int:
        len_seats = len(seats)
        assert len_seats > 2

        first_one_index = 0
        while seats[first_one_index] != 1 and first_one_index < len_seats:  # find the first 1
            first_one_index += 1
        if first_one_index == len_seats:
            return 0  # error, no 1

        max_dis = first_one_index  # if sit in the seats[0]

        last_one_index = len_seats - 1
        while seats[last_one_index] != 1 and last_one_index >= 0:  # find the last 1
            last_one_index -= 1
        if last_one_index == -1:
            return 0  # error, no 1

        max_dis = max(max_dis, len_seats - 1 - last_one_index)

        second_one_index = first_one_index + 1
        while second_one_index <= last_one_index:
            while second_one_index <= last_one_index and seats[second_one_index] != 1:  # find the second 1
                second_one_index += 1
            # count the gap, update the max_dis
            max_dis = max(max_dis, (second_one_index - first_one_index) >> 1)
            first_one_index = second_one_index  # move on, find the next gap
            second_one_index += 1

        return max_dis


def main():
    # Example 1: Output: 2
    # seats = [1, 0, 0, 0, 1, 0, 1]

    # Example 2: Output: 3
    # seats = [1, 0, 0, 0]

    # Example 3: Output: 1
    seats = [0, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxDistToClosest(seats)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
