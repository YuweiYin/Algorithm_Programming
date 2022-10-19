#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1700-Number-of-Students-Unable-to-Eat-Lunch.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-19
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1700 - (Easy) - Number of Students Unable to Eat Lunch
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

Description & Requirement:
    The school cafeteria offers circular and square sandwiches at lunch break, 
    referred to by numbers 0 and 1 respectively. All students stand in a queue. 
    Each student either prefers square or circular sandwiches.

    The number of sandwiches in the cafeteria is equal to the number of students. 
    The sandwiches are placed in a stack. At each step:
        If the student at the front of the queue prefers the sandwich on the top of the stack, 
            they will take it and leave the queue.
        Otherwise, they will leave it and go to the queue's end.

    This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

    You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i-th sandwich 
    in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j-th student 
    in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

Example 1:
    Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
    Output: 0 
    Explanation:
        - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
        - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
        - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
        - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
        - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
        - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
        - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
        - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
        Hence all students are able to eat.
Example 2:
    Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
    Output: 3

Constraints:
    1 <= students.length, sandwiches.length <= 100
    students.length == sandwiches.length
    sandwiches[i] is 0 or 1.
    students[i] is 0 or 1.
"""


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # exception case
        assert isinstance(students, list) and len(students) >= 1
        assert isinstance(sandwiches, list) and len(sandwiches) >= 1
        # main method: (process simulation)
        return self._countStudents(students, sandwiches)

    def _countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Runtime: 48 ms, faster than 80.56% of Python3 online submissions for Number of Students Unable to Eat Lunch.
        Memory Usage: 13.9 MB, less than 71.25% of Python3 online submissions for Number of Students Unable to Eat Lunch
        """
        assert isinstance(students, list) and len(students) >= 1
        assert isinstance(sandwiches, list) and len(sandwiches) >= 1

        s_circle = sum(students)  # the number of students that like sandwiches of circle shape
        s_square = len(students) - s_circle  # the number of students that like sandwiches of square shape

        for sandwich in sandwiches:
            if sandwich == 0 and s_square > 0:
                s_square -= 1
            elif sandwich == 1 and s_circle > 0:
                s_circle -= 1
            else:
                break

        return s_square + s_circle


def main():
    # Example 1: Output: 0
    # students = [1, 1, 0, 0]
    # sandwiches = [0, 1, 0, 1]

    # Example 2: Output: 3
    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countStudents(students, sandwiches)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
