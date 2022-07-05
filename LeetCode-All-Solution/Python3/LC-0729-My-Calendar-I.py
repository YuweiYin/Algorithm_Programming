#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0729-My-Calendar-I.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-05
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0729 - (Medium) - My Calendar I
https://leetcode.com/problems/my-calendar-i/

Description & Requirement:
    You are implementing a program to use as your calendar. 
    We can add a new event if adding the event will not cause a double booking.

    A double booking happens when two events have some non-empty intersection 
    (i.e., some moment is common to both events.).

    The event can be represented as a pair of integers start and end that 
    represents a booking on the half-open interval [start, end), 
    the range of real numbers x such that start <= x < end.

    Implement the MyCalendar class:
        MyCalendar() Initializes the calendar object.
        boolean book(int start, int end) Returns true if the event can be added to the calendar successfully 
            without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Example 1:
    Input
        ["MyCalendar", "book", "book", "book"]
        [[], [10, 20], [15, 25], [20, 30]]
    Output
        [null, true, false, true]
    Explanation
        MyCalendar myCalendar = new MyCalendar();
        myCalendar.book(10, 20); // return True
        myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
        myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

Constraints:
    0 <= start < end <= 10^9
    At most 1000 calls will be made to book.
"""


class MyCalendar:

    def __init__(self):
        # Segment Tree (dynamic)
        self.tree = set()
        self.lazy = set()  # lazy flag

    def query(self, start: int, end: int, left: int, right: int, idx: int) -> bool:
        if right < start or end < left:  # [start, end] and [left, right] have no overlapping
            return False
        if idx in self.lazy:  # this segment has been occupied
            return True
        if start <= left and right <= end:  # the [left, right] interval is in the [start, end] range
            return idx in self.tree
        # recursively query the left child and right child
        mid = (left + right) >> 1
        return self.query(start, end, left, mid, (idx << 1)) or \
               self.query(start, end, mid + 1, right, (idx << 1) + 1)

    def update(self, start: int, end: int, left: int, right: int, idx: int) -> None:
        if right < start or end < left:  # [start, end] and [left, right] have no overlapping
            return
        if start <= left and right <= end:  # the [left, right] interval is in the [start, end] range
            self.tree.add(idx)
            self.lazy.add(idx)
        else:
            # recursively update the left child and right child
            mid = (left + right) >> 1
            self.update(start, end, left, mid, (idx << 1))
            self.update(start, end, mid + 1, right, (idx << 1) + 1)
            # update tree node and lazy flag
            self.tree.add(idx)
            if (idx << 1) in self.lazy and (idx << 1) + 1 in self.lazy:
                self.lazy.add(idx)

    def book(self, start: int, end: int) -> bool:
        # Constraints: 0 <= start < end <= 10^9
        if self.query(start, end - 1, 0, int(1e9), 1):
            return False
        self.update(start, end - 1, 0, int(1e9), 1)
        return True


def main():
    # Example 1: Output: [null, true, false, true]
    command_list = ["MyCalendar", "book", "book", "book"]
    param_list = [[], [10, 20], [15, 25], [20, 30]]

    # init instance
    # solution = Solution()
    obj = MyCalendar()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "book" and isinstance(param, list) and len(param) == 2:
            ans.append(obj.book(param[0], param[1]))
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
