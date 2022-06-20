#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0715-Range-Module.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-20
=================================================================="""

import sys
import time
from sortedcontainers import SortedDict
# from typing import List
# import functools

"""
LeetCode - 0715 - (Hard) - Range Module
https://leetcode.com/problems/range-module/

Description & Requirement:
    A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges 
    represented as half-open intervals and query about them.

    A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

    Implement the RangeModule class:
        RangeModule() Initializes the object of the data structure.
        void addRange(int left, int right) Adds the half-open interval [left, right), 
            tracking every real number in that interval. Adding an interval that partially overlaps with currently 
            tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
        boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) 
            is currently being tracked, and false otherwise.
        void removeRange(int left, int right) Stops tracking every real number currently being tracked 
            in the half-open interval [left, right).
 

Example 1:
    Input
        ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
        [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
    Output
        [null, null, null, true, false, true]
    Explanation
        RangeModule rangeModule = new RangeModule();
        rangeModule.addRange(10, 20);
        rangeModule.removeRange(14, 16);
        rangeModule.queryRange(10, 14); // return True,
            (Every number in [10, 14) is being tracked)
        rangeModule.queryRange(13, 15); // return False,
            (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
        rangeModule.queryRange(16, 17); // return True, 
            (The number 16 in [16, 17) is still being tracked, despite the remove operation)

Constraints:
    1 <= left < right <= 10^9
    At most 10^4 calls will be made to addRange, queryRange, and removeRange.
"""


class RangeModule:

    def __init__(self):
        # sorted dictionary
        self.ranges = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        # consider merging intervals after adding new intervals
        intervals = self.ranges

        x = intervals.bisect_right(left)
        if x != 0:
            start = x - 1
            if intervals.values()[start] >= right:
                return
            if intervals.values()[start] >= left:
                left = intervals.keys()[start]
                intervals.popitem(start)
                x -= 1

        while x < len(intervals) and intervals.keys()[x] <= right:
            right = max(right, intervals.values()[x])
            intervals.popitem(x)

        intervals[left] = right

    def queryRange(self, left: int, right: int) -> bool:
        intervals = self.ranges

        x = intervals.bisect_right(left)
        if x == 0:
            return False

        return right <= intervals.values()[x - 1]

    def removeRange(self, left: int, right: int) -> None:
        intervals = self.ranges

        x = intervals.bisect_right(left)
        if x != 0:
            start = x - 1
            if (ri := intervals.values()[start]) >= right:
                if (li := intervals.keys()[start]) == left:
                    intervals.popitem(start)
                else:
                    intervals[li] = left
                if right != ri:
                    intervals[right] = ri
                return
            elif ri > left:
                intervals[intervals.keys()[start]] = left

        while x < len(intervals) and intervals.keys()[x] < right:
            if intervals.values()[x] <= right:
                intervals.popitem(x)
            else:
                intervals[right] = intervals.values()[x]
                intervals.popitem(x)
                break


def main():
    # Example 1: Output: [null, null, null, true, false, true]
    command_list = ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
    param_list = [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]

    # init instance
    # solution = Solution()
    obj = RangeModule()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "addRange":
            if isinstance(param, list) and len(param) == 2:
                obj.addRange(param[0], param[1])
            ans.append("null")
        elif command == "removeRange":
            if isinstance(param, list) and len(param) == 2:
                obj.removeRange(param[0], param[1])
            ans.append("null")
        elif command == "queryRange":
            if isinstance(param, list) and len(param) == 2:
                ans.append(obj.queryRange(param[0], param[1]))
            else:
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
