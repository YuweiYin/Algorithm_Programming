#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0630-Course-Schedule-III.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-23
=================================================================="""

import sys
import time
from typing import List
import heapq
# import functools

"""
LeetCode - 0630 - (Hard) - Course Schedule III
https://leetcode.com/problems/course-schedule-iii/

Description & Requirement:
    There are n different online courses numbered from 1 to n. 
    You are given an array courses where courses[i] = [duration_i, lastDay_i] indicate that 
    the i-th course should be taken continuously for duration_i days and must be finished before or on lastDay_i.

    You will start on the 1st day and you cannot take two or more courses simultaneously.

    Return the maximum number of courses that you can take.

Example 1:
    Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
    Output: 3
    Explanation: 
        There are totally 4 courses, but you can take 3 courses at most:
        First, take the 1st course, it costs 100 days so you will finish it on the 100th day, 
            and ready to take the next course on the 101st day.
        Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, 
            and ready to take the next course on the 1101st day. 
        Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
        The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Example 2:
    Input: courses = [[1,2]]
    Output: 1
Example 3:
    Input: courses = [[3,2],[4,3]]
    Output: 0

Constraints:
    1 <= courses.length <= 10^4
    1 <= duration_i, lastDay_i <= 10^4
"""


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # exception case
        assert isinstance(courses, list) and len(courses) >= 1
        for course in courses:
            assert isinstance(course, list) and len(course) == 2 and course[0] >= 1 and course[1] >= 1
        # main method: (Greedy + sort + heap)
        return self._scheduleCourse(courses)

    def _scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        Runtime: 1196 ms, faster than 30.90% of Python3 online submissions for Course Schedule III.
        Memory Usage: 19.3 MB, less than 90.62% of Python3 online submissions for Course Schedule III.
        """
        assert isinstance(courses, list) and len(courses) >= 1

        courses.sort(key=lambda x: x[1])

        heap = []
        max_day = 0
        for course in courses:
            duration, last_day = course
            if max_day + duration <= last_day:
                max_day += duration
                heapq.heappush(heap, -duration)
            elif len(heap) > 0 and -heap[0] > duration:
                max_day -= -heap[0] - duration
                heapq.heappop(heap)
                heapq.heappush(heap, -duration)

        return len(heap)


def main():
    # Example 1: Output: 3
    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]

    # Example 2: Output: 1
    # courses = [[1, 2]]

    # Example 3: Output: 0
    # courses = [[3, 2], [4, 3]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.scheduleCourse(courses)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
