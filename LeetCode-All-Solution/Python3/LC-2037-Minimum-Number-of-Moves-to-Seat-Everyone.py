#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2037-Minimum-Number-of-Moves-to-Seat-Everyone.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-31
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2037 - (Easy) - Minimum Number of Moves to Seat Everyone
https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

Description & Requirement:
    There are n seats and n students in a room. You are given an array seats of length n, 
    where seats[i] is the position of the i-th seat. You are also given the array students of length n, 
    where students[j] is the position of the j-th student.

    You may perform the following move any number of times:
        Increase or decrease the position of the ith student by 1 
            (i.e., moving the ith student from position x to x + 1 or x - 1)

    Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

    Note that there may be multiple seats or students in the same position at the beginning.

Example 1:
    Input: seats = [3,1,5], students = [2,7,4]
    Output: 4
    Explanation: The students are moved as follows:
        - The first student is moved from from position 2 to position 1 using 1 move.
        - The second student is moved from from position 7 to position 5 using 2 moves.
        - The third student is moved from from position 4 to position 3 using 1 move.
        In total, 1 + 2 + 1 = 4 moves were used.
Example 2:
    Input: seats = [4,1,5,9], students = [1,3,2,6]
    Output: 7
    Explanation: The students are moved as follows:
        - The first student is not moved.
        - The second student is moved from from position 3 to position 4 using 1 move.
        - The third student is moved from from position 2 to position 5 using 3 moves.
        - The fourth student is moved from from position 6 to position 9 using 3 moves.
        In total, 0 + 1 + 3 + 3 = 7 moves were used.
Example 3:
    Input: seats = [2,2,6,6], students = [1,3,2,6]
    Output: 4
    Explanation: Note that there are two seats at position 2 and two seats at position 6.
        The students are moved as follows:
        - The first student is moved from from position 1 to position 2 using 1 move.
        - The second student is moved from from position 3 to position 6 using 3 moves.
        - The third student is not moved.
        - The fourth student is not moved.
        In total, 1 + 3 + 0 + 0 = 4 moves were used.

Constraints:
    n == seats.length == students.length
    1 <= n <= 100
    1 <= seats[i], students[j] <= 100
"""


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # exception case
        assert isinstance(seats, list) and len(seats) >= 1
        assert isinstance(students, list) and len(students) == len(seats)
        # main method: (sorting)
        return self._minMovesToSeat(seats, students)

    def _minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        """
        Time: beats 78.32%; Space: beats 66.58%
        """
        assert isinstance(seats, list) and len(seats) >= 1
        assert isinstance(students, list) and len(students) == len(seats)

        seats.sort()
        students.sort()

        return sum([abs(seat - student) for seat, student in zip(seats, students)])


def main():
    # Example 1: Output: 4
    seats = [3, 1, 5]
    students = [2, 7, 4]

    # Example 2: Output: 7
    # seats = [4, 1, 5, 9]
    # students = [1, 3, 2, 6]

    # Example 3: Output: 4
    # seats = [2, 2, 6, 6]
    # students = [1, 3, 2, 6]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minMovesToSeat(seats, students)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
