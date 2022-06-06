#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0732-My-Calendar-III.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-06
=================================================================="""

import sys
import time
from sortedcontainers import SortedDict
# from typing import List
# import functools

"""
LeetCode - 0732 - (Hard) - My Calendar III
https://leetcode.com/problems/my-calendar-iii/

Description & Requirement:
A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.
 

Example 1:
    Input
        ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
        [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    Output
        [null, 1, 1, 2, 3, 3, 3]
    Explanation
        MyCalendarThree myCalendarThree = new MyCalendarThree();
        myCalendarThree.book(10, 20); // return 1, The first event can be booked and is disjoint, 
            so the maximum k-booking is a 1-booking.
        myCalendarThree.book(50, 60); // return 1, The second event can be booked and is disjoint, 
            so the maximum k-booking is a 1-booking.
        myCalendarThree.book(10, 40); // return 2, The third event [10, 40) intersects the first event, 
            and the maximum k-booking is a 2-booking.
        myCalendarThree.book(5, 15); // return 3, The remaining events cause the maximum K-booking 
            to be only a 3-booking.
        myCalendarThree.book(5, 10); // return 3
        myCalendarThree.book(25, 55); // return 3

Constraints:
    0 <= start < end <= 10^9
    At most 400 calls will be made to book.
"""


class MyCalendarThree:

    def __init__(self):
        self.sort_dict = SortedDict()

    def book(self, start: int, end: int) -> int:
        def __difference_array():
            # for each interval [cur_start, cur_end], counter of cur_start += 1, counter of cur_end -= 1
            self.sort_dict[start] = self.sort_dict.setdefault(start, 0) + 1
            self.sort_dict[end] = self.sort_dict.setdefault(end, 0) - 1

            ans = 0
            max_booking = 0
            for counter in self.sort_dict.values():
                max_booking += counter
                ans = max(ans, max_booking)
            return ans

        return __difference_array()


def main():
    # Example 1: Output: [null, 1, 1, 2, 3, 3, 3]
    command_list = ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
    param_list = [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]

    # init instance
    # solution = Solution()
    obj = MyCalendarThree()

    # run & time
    start = time.process_time()
    ans = ["null"]
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
