#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1450-Number-of-Students-Doing-Homework-at-a-Given-Time.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-19
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1450 - (Easy) - Number of Students Doing Homework at a Given Time
https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

Description & Requirement:
    Given two integer arrays startTime and endTime and given an integer queryTime.

    The i-th student started doing their homework at the time startTime[i] and finished it at time endTime[i].

    Return the number of students doing their homework at time queryTime. More formally, 
    return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

Example 1:
    Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
    Output: 1
    Explanation: We have 3 students where:
        The first student started doing homework at time 1 and 
            finished at time 3 and wasn't doing anything at time 4.
        The second student started doing homework at time 2 and 
            finished at time 2 and also wasn't doing anything at time 4.
        The third student started doing homework at time 3 and 
            finished at time 7 and was the only student doing homework at time 4.
Example 2:
    Input: startTime = [4], endTime = [4], queryTime = 4
    Output: 1
    Explanation: The only student was doing their homework at the queryTime.

Constraints:
    startTime.length == endTime.length
    1 <= startTime.length <= 100
    1 <= startTime[i] <= endTime[i] <= 1000
    1 <= queryTime <= 1000
"""


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        # exception case
        assert isinstance(queryTime, int) and queryTime >= 1
        assert isinstance(startTime, list) and isinstance(endTime, list) and 1 <= len(startTime) == len(endTime)
        for st, et in zip(startTime, endTime):
            assert isinstance(st, int) and isinstance(et, int) and 1 <= st <= et
        # main method: (scan the zipped list)
        return self._busyStudent(startTime, endTime, queryTime)

    def _busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        assert isinstance(queryTime, int) and queryTime >= 1
        assert isinstance(startTime, list) and isinstance(endTime, list) and 1 <= len(startTime) == len(endTime)

        res = 0
        for st, et in zip(startTime, endTime):
            if st <= queryTime <= et:
                res += 1

        return res


def main():
    # Example 1: Output: 1
    startTime = [1, 2, 3]
    endTime = [3, 2, 7]
    queryTime = 4

    # Example 2: Output: 1
    # startTime = [4]
    # endTime = [4]
    # queryTime = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.busyStudent(startTime, endTime, queryTime)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
