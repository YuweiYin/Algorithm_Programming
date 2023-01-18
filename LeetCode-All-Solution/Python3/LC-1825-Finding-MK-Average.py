#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1825-Finding-MK-Average.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-18
=================================================================="""

import sys
import time
import collections
# from typing import List
# import functools

"""
LeetCode - 1825 - (Hard) - Finding MK Average
https://leetcode.com/problems/finding-mk-average/

Description & Requirement:
    You are given two integers, m and k, and a stream of integers. 
    You are tasked to implement a data structure that calculates the MKAverage for the stream.

    The MKAverage can be calculated using these steps:
        If the number of the elements in the stream is less than m you should consider the MKAverage to be -1. 
            Otherwise, copy the last m elements of the stream to a separate container.
        Remove the smallest k elements and the largest k elements from the container.
        Calculate the average value for the rest of the elements rounded down to the nearest integer.

    Implement the MKAverage class:
        MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
        void addElement(int num) Inserts a new element num into the stream.
        int calculateMKAverage() Calculates and returns the MKAverage for the current stream 
            rounded down to the nearest integer.

Example 1:
    Input
        ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", 
            "addElement", "addElement", "addElement", "calculateMKAverage"]
        [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
    Output
        [null, null, null, -1, null, 3, null, null, null, 5]
    Explanation
        MKAverage obj = new MKAverage(3, 1); 
        obj.addElement(3);        // current elements are [3]
        obj.addElement(1);        // current elements are [3,1]
        obj.calculateMKAverage(); // return -1, because m = 3 and only 2 elements exist.
        obj.addElement(10);       // current elements are [3,1,10]
        obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
                                  // After removing smallest and largest 1 element the container will be [3].
                                  // The average of [3] equals 3/1 = 3, return 3
        obj.addElement(5);        // current elements are [3,1,10,5]
        obj.addElement(5);        // current elements are [3,1,10,5,5]
        obj.addElement(5);        // current elements are [3,1,10,5,5,5]
        obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
                                  // After removing smallest and largest 1 element the container will be [5].
                                  // The average of [5] equals 5/1 = 5, return 5

Constraints:
    3 <= m <= 10^5
    1 <= k*2 < m
    1 <= num <= 10^5
    At most 10^5 calls will be made to addElement and calculateMKAverage.
"""


class MKAverage:
    """
    Time: beats 94.38%; Space: beats 74.16%
    """

    def __init__(self, m: int, k: int):
        from sortedcontainers import SortedList

        self.m = m
        self.k = k
        self.total = 0
        self.queue = collections.deque()
        self.low = SortedList()
        self.mid = SortedList()
        self.high = SortedList()

    def addElement(self, num: int) -> None:
        if not self.low or num <= self.low[-1]:
            self.low.add(num)
        elif not self.high or num >= self.high[0]:
            self.high.add(num)
        else:
            self.mid.add(num)
            self.total += num
        self.queue.append(num)
        if len(self.queue) > self.m:
            x = self.queue.popleft()
            if x in self.low:
                self.low.remove(x)
            elif x in self.high:
                self.high.remove(x)
            else:
                self.mid.remove(x)
                self.total -= x
        while len(self.low) > self.k:
            x = self.low.pop()
            self.mid.add(x)
            self.total += x
        while len(self.high) > self.k:
            x = self.high.pop(0)
            self.mid.add(x)
            self.total += x
        while len(self.low) < self.k and self.mid:
            x = self.mid.pop(0)
            self.low.add(x)
            self.total -= x
        while len(self.high) < self.k and self.mid:
            x = self.mid.pop()
            self.high.add(x)
            self.total -= x

    def calculateMKAverage(self) -> int:
        return -1 if len(self.queue) < self.m else self.total // (self.m - 2 * self.k)


def main():
    # Example 1: Output: [null, null, null, -1, null, 3, null, null, null, 5]
    command_list = ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage",
                    "addElement", "addElement", "addElement", "calculateMKAverage"]
    param_list = [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]

    # init instance
    m, k = param_list[0]
    obj = MKAverage(m, k)
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "addElement" and len(param) == 1:
            obj.addElement(param[0])
            ans.append("null")
        elif command == "calculateMKAverage":
            ans.append(obj.calculateMKAverage())
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
