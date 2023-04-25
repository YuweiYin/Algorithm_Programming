#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2336-Smallest-Number-in-Infinite-Set.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-25
=================================================================="""

import sys
import time
from sortedcontainers import SortedSet
# from typing import List
# import collections
# import functools

"""
LeetCode - 2336 - (Medium) - Smallest Number in Infinite Set
https://leetcode.com/problems/smallest-number-in-infinite-set/

Description & Requirement:
    You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

    Implement the SmallestInfiniteSet class:
        SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
        int popSmallest() Removes and returns the smallest integer contained in the infinite set.
        void addBack(int num) Adds a positive integer num back into the infinite set, 
            if it is not already in the infinite set.

Example 1:
    Input
        ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", 
            "addBack", "popSmallest", "popSmallest", "popSmallest"]
        [[], [2], [], [], [], [1], [], [], []]
    Output
        [null, null, 1, 2, 3, null, 1, 4, 5]
    Explanation
        SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
        smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
        smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
        smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
        smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
        smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
        smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                           // is the smallest number, and remove it from the set.
        smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
        smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

Constraints:
    1 <= num <= 1000
    At most 1000 calls will be made in total to popSmallest and addBack.
"""


class SmallestInfiniteSet:

    def __init__(self):
        self.sorted_set = SortedSet(range(1, 1024))

    def popSmallest(self) -> int:
        return self.sorted_set.pop(0)

    def addBack(self, num: int) -> None:
        self.sorted_set.add(num)


def main():
    # Example 1: Output: [null, null, 1, 2, 3, null, 1, 4, 5]
    command_list = ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest",
                    "addBack", "popSmallest", "popSmallest", "popSmallest"]
    param_list = [[], [2], [], [], [], [1], [], [], []]

    # init instance
    obj = SmallestInfiniteSet()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "addBack" and isinstance(param, list) and len(param) == 1:
            obj.addBack(param[0])
            ans.append("null")
        elif command == "popSmallest":
            ans.append(obj.popSmallest())
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
