#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0352-Data-Stream-as-Disjoint-Intervals.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-28
=================================================================="""

import sys
import time
from typing import List
from sortedcontainers import SortedDict
# import collections
# import functools

"""
LeetCode - 0352 - (Hard) - Data Stream as Disjoint Intervals
https://leetcode.com/problems/data-stream-as-disjoint-intervals/

Description & Requirement:
    Given a data stream input of non-negative integers a1, a2, ..., an, 
    summarize the numbers seen so far as a list of disjoint intervals.

    Implement the SummaryRanges class:
        SummaryRanges() Initializes the object with an empty stream.
        void addNum(int value) Adds the integer value to the stream.
        int[][] getIntervals() Returns a summary of the integers in the stream currently 
            as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.

Example 1:
    Input
        ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", 
            "addNum", "getIntervals", "addNum", "getIntervals"]
        [[], [1], [], [3], [], [7], [], [2], [], [6], []]
    Output
        [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], 
            null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
    Explanation
        SummaryRanges summaryRanges = new SummaryRanges();
        summaryRanges.addNum(1);      // arr = [1]
        summaryRanges.getIntervals(); // return [[1, 1]]
        summaryRanges.addNum(3);      // arr = [1, 3]
        summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
        summaryRanges.addNum(7);      // arr = [1, 3, 7]
        summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
        summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
        summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
        summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
        summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]

Constraints:
    0 <= value <= 10^4
    At most 3 * 10^4 calls will be made to addNum and getIntervals.

Follow up:
    What if there are lots of merges and the number of disjoint intervals is small 
    compared to the size of the data stream?
"""


class SummaryRanges:

    def __init__(self):
        self.intervals = SortedDict()

    def addNum(self, val: int) -> None:
        intervals_ = self.intervals
        keys_ = self.intervals.keys()
        values_ = self.intervals.values()

        interval1 = intervals_.bisect_right(val)
        interval0 = (len(intervals_) if interval1 == 0 else interval1 - 1)

        if interval0 != len(intervals_) and keys_[interval0] <= val <= values_[interval0]:
            return
        else:
            left_aside = (interval0 != len(intervals_) and values_[interval0] + 1 == val)
            right_aside = (interval1 != len(intervals_) and keys_[interval1] - 1 == val)
            if left_aside and right_aside:
                left, right = keys_[interval0], values_[interval1]
                intervals_.popitem(interval1)
                intervals_.popitem(interval0)
                intervals_[left] = right
            elif left_aside:
                intervals_[keys_[interval0]] += 1
            elif right_aside:
                right = values_[interval1]
                intervals_.popitem(interval1)
                intervals_[val] = right
            else:
                intervals_[val] = val

    def getIntervals(self) -> List[List[int]]:
        return list(self.intervals.items())


def main():
    # Example 1: Output: [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]],
    #     null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
    command_list = ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals",
                    "addNum", "getIntervals", "addNum", "getIntervals"]
    param_list = [[], [1], [], [3], [], [7], [], [2], [], [6], []]

     # init instance
    obj = SummaryRanges()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "addNum" and isinstance(param, list) and len(param) == 1:
            obj.addNum(param[0])
            ans.append("null")
        elif command == "getIntervals":
            ans.append(obj.getIntervals())
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
