#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0731-My-Calendar-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-19
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0731 - (Medium) - My Calendar II
https://leetcode.com/problems/my-calendar-ii/

Description & Requirement:
    You are implementing a program to use as your calendar. 
    We can add a new event if adding the event will not cause a triple booking.

    A triple booking happens when three events have some non-empty intersection 
    (i.e., some moment is common to all the three events.).

    The event can be represented as a pair of integers start and end that 
    represents a booking on the half-open interval [start, end), 
    the range of real numbers x such that start <= x < end.

    Implement the MyCalendarTwo class:
        MyCalendarTwo() Initializes the calendar object.
        boolean book(int start, int end) Returns true if the event can be added to the calendar successfully 
            without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Example 1:
    Input
        ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
        [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    Output
        [null, true, true, true, false, true, true]
    Explanation
        MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
        myCalendarTwo.book(10, 20); // return True, The event can be booked. 
        myCalendarTwo.book(50, 60); // return True, The event can be booked. 
        myCalendarTwo.book(10, 40); // return True, The event can be double booked. 
        myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, 
            because it would result in a triple booking.
        myCalendarTwo.book(5, 10); // return True, The event can be booked, 
            as it does not use time 10 which is already double booked.
        myCalendarTwo.book(25, 55); // return True, The event can be booked, 
            as the time in [25, 40) will be double booked with the third event, 
            the time [40, 50) will be single booked, 
            and the time [50, 55) will be double booked with the second event.

Constraints:
    0 <= start < end <= 10^9
    At most 1000 calls will be made to book.
"""


class MyCalendarTwo:

    def __init__(self):
        # segment tree
        self.seg_tree = dict()

    def book(self, start: int, end: int) -> bool:
        self._update(start, end - 1, 1, 0, int(1e9), 1)
        if self.seg_tree[1][0] > 2:
            self._update(start, end - 1, -1, 0, int(1e9), 1)
            return False
        return True

    def _update(self, start: int, end: int, val: int, left: int, right: int, idx: int) -> None:
        if right < start or end < left:
            return
        if start <= left and right <= end:
            p = self.seg_tree[idx] if idx in self.seg_tree else [0, 0]
            p[0] += val
            p[1] += val
            self.seg_tree[idx] = p
            return
        mid = (left + right) >> 1
        self._update(start, end, val, left, mid, idx << 1)
        self._update(start, end, val, mid + 1, right, (idx << 1) + 1)

        p = self.seg_tree[idx] if idx in self.seg_tree else [0, 0]
        p_2 = self.seg_tree[idx << 1] if (idx << 1) in self.seg_tree else (0,)
        p_3 = self.seg_tree[(idx << 1) + 1] if ((idx << 1) + 1) in self.seg_tree else (0,)
        p[0] = p[1] + max(p_2[0], p_3[0])
        self.seg_tree[idx] = p


def main():
    # Example 1: Output: [null, true, true, true, false, true, true]
    command_list = ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
    param_list = [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]

    # init instance
    # solution = Solution()
    obj = MyCalendarTwo()
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
