#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0855-Exam-Room.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-30
=================================================================="""

import sys
import time
import bisect
# from typing import List
# import collections
# import functools

"""
LeetCode - 0855 - (Medium) - Exam Room
https://leetcode.com/problems/exam-room/

Description & Requirement:
    There is an exam room with n seats in a single row labeled from 0 to n - 1.

    When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. 
    If there are multiple such seats, they sit in the seat with the lowest number. 
    If no one is in the room, then the student sits at seat number 0.

    Design a class that simulates the mentioned exam room.

    Implement the ExamRoom class:
        ExamRoom(int n) Initializes the object of the exam room with the number of the seats n.
        int seat() Returns the label of the seat at which the next student will set.
        void leave(int p) Indicates that the student sitting at seat p will leave the room. It is guaranteed that there will be a student sitting at seat p.

Example 1:
    Input
        ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
        [[10], [], [], [], [], [4], []]
    Output
        [null, 0, 9, 4, 2, null, 5]
    Explanation
        ExamRoom examRoom = new ExamRoom(10);
        examRoom.seat(); // return 0, no one is in the room, then the student sits at seat number 0.
        examRoom.seat(); // return 9, the student sits at the last seat number 9.
        examRoom.seat(); // return 4, the student sits at the last seat number 4.
        examRoom.seat(); // return 2, the student sits at the last seat number 2.
        examRoom.leave(4);
        examRoom.seat(); // return 5, the student sits at the last seat number 5.

Constraints:
    1 <= n <= 10^9
    It is guaranteed that there is a student sitting at seat p.
    At most 10^4 calls will be made to seat and leave.
"""


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            student = 0
        else:
            dist, student = self.students[0], 0
            for idx, stu in enumerate(self.students):
                if idx > 0:
                    prev = self.students[idx - 1]
                    cur_d = (stu - prev) >> 1
                    if cur_d > dist:
                        dist, student = cur_d, prev + cur_d

            cur_d = self.n - 1 - self.students[-1]
            if cur_d > dist:
                student = self.n - 1

        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)


def main():
    # Example 1: Output: [null, 0, 9, 4, 2, null, 5]
    command_list = ["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
    param_list = [[10], [], [], [], [], [4], []]

    # init instance
    n = param_list[0][0]
    obj = ExamRoom(n)
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "seat":
            ans.append(obj.seat())
        elif command == "leave" and len(param) == 1:
            obj.leave(param[0])
            ans.append("null")
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
