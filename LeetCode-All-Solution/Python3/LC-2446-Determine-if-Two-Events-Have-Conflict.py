#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2446-Determine-if-Two-Events-Have-Conflict.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-17
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2446 - (Easy) - Determine if Two Events Have Conflict
https://leetcode.com/problems/determine-if-two-events-have-conflict/

Description & Requirement:
    You are given two arrays of strings that represent two inclusive events that 
    happened on the same day, event1 and event2, where:
        event1 = [startTime1, endTime1] and
        event2 = [startTime2, endTime2].

    Event times are valid 24 hours format in the form of HH:MM.

    A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

    Return true if there is a conflict between two events. Otherwise, return false.

Example 1:
    Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
    Output: true
    Explanation: The two events intersect at time 2:00.
Example 2:
    Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
    Output: true
    Explanation: The two events intersect starting from 01:20 to 02:00.
Example 3:
    Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
    Output: false
    Explanation: The two events do not intersect.

Constraints:
    evnet1.length == event2.length == 2.
    event1[i].length == event2[i].length == 5
    startTime1 <= endTime1
    startTime2 <= endTime2
    All the event times follow the HH:MM format.
"""


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # exception case
        assert isinstance(event1, list) and isinstance(event2, list) and len(event1) == len(event2) == 2
        # main method: (compare the strings)
        return self._haveConflict(event1, event2)

    def _haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        assert isinstance(event1, list) and isinstance(event2, list) and len(event1) == len(event2) == 2

        return not(event1[1] < event2[0] or event2[1] < event1[0])


def main():
    # Example 1: Output: true
    # event1 = ["01:15", "02:00"]
    # event2 = ["02:00", "03:00"]

    # Example 2: Output: true
    # event1 = ["01:00", "02:00"]
    # event2 = ["01:20", "03:00"]

    # Example 3: Output: false
    event1 = ["10:00", "11:00"]
    event2 = ["14:00", "15:00"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.haveConflict(event1, event2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
