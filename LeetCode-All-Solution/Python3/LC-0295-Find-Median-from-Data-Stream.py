#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0295-Find-Median-from-Data-Stream.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-12
=================================================================="""

import sys
import time
import heapq
# from typing import List
# import collections
# import functools

"""
LeetCode - 0295 - (Hard) - Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

Description & Requirement:
    The median is the middle value in an ordered integer list. If the size of the list is even, 
    there is no middle value, and the median is the mean of the two middle values.
        For example, for arr = [2,3,4], the median is 3.
        For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

    Implement the MedianFinder class:
        MedianFinder() initializes the MedianFinder object.
        void addNum(int num) adds the integer num from the data stream to the data structure.
        double findMedian() returns the median of all elements so far. 
            Answers within 10-5 of the actual answer will be accepted.

Example 1:
    Input
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
        [[], [1], [2], [], [3], []]
    Output
        [null, null, null, 1.5, null, 2.0]
    Explanation
        MedianFinder medianFinder = new MedianFinder();
        medianFinder.addNum(1);    // arr = [1]
        medianFinder.addNum(2);    // arr = [1, 2]
        medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
        medianFinder.addNum(3);    // arr[1, 2, 3]
        medianFinder.findMedian(); // return 2.0

Constraints:
    -10^5 <= num <= 10^5
    There will be at least one element in the data structure before calling findMedian.
    At most 5 * 10^4 calls will be made to addNum and findMedian.

Follow up:
    If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""


class MedianFinder:
    """
    Runtime: 1420 ms, faster than 39.89% of Python3 online submissions for Find Median from Data Stream.
    Memory Usage: 35.7 MB, less than 86.34% of Python3 online submissions for Find Median from Data Stream.
    """

    def __init__(self):
        self.queue_min = list()
        self.queue_max = list()

    def addNum(self, num: int) -> None:
        queue_min_ = self.queue_min
        queue_max_ = self.queue_max

        if not queue_min_ or num <= -queue_min_[0]:
            heapq.heappush(queue_min_, -num)
            if len(queue_max_) + 1 < len(queue_min_):
                heapq.heappush(queue_max_, -heapq.heappop(queue_min_))
        else:
            heapq.heappush(queue_max_, num)
            if len(queue_max_) > len(queue_min_):
                heapq.heappush(queue_min_, -heapq.heappop(queue_max_))

    def findMedian(self) -> float:
        queue_min_ = self.queue_min
        queue_max_ = self.queue_max

        if len(queue_min_) > len(queue_max_):
            return -queue_min_[0]
        return (-queue_min_[0] + queue_max_[0]) / 2


def main():
    # Example 1: Output: [null, null, null, 1.5, null, 2.0]
    command_list = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    param_list = [[], [1], [2], [], [3], []]

    # init instance
    # solution = Solution()
    obj = MedianFinder()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "addNum" and isinstance(param, list) and len(param) == 1:
            obj.addNum(param[0])
            ans.append("null")
        elif command == "findMedian":
            ans.append(obj.findMedian())
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
