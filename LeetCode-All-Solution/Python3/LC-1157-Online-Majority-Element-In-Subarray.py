#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1157-Online-Majority-Element-In-Subarray.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-16
=================================================================="""

import sys
import time
from typing import List
import bisect
import collections
# import functools

"""
LeetCode - 1157 - (Hard) - Online Majority Element In Subarray
https://leetcode.com/problems/online-majority-element-in-subarray/

Description & Requirement:
    Design a data structure that efficiently finds the majority element of a given subarray.

    The majority element of a subarray is an element that occurs threshold times or more in the subarray.

    Implementing the MajorityChecker class:
        MajorityChecker(int[] arr) Initializes the instance of the class with the given array arr.
        int query(int left, int right, int threshold) returns the element in the subarray arr[left...right] 
            that occurs at least threshold times, or -1 if no such element exists.

Example 1:
    Input
        ["MajorityChecker", "query", "query", "query"]
        [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
    Output
        [null, 1, -1, 2]
    Explanation
        MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
        majorityChecker.query(0, 5, 4); // return 1
        majorityChecker.query(0, 3, 3); // return -1
        majorityChecker.query(2, 3, 2); // return 2

Constraints:
    1 <= arr.length <= 2 * 10^4
    1 <= arr[i] <= 2 * 10^4
    0 <= left <= right < arr.length
    threshold <= right - left + 1
    2 * threshold > right - left + 1
    At most 104 calls will be made to query.
"""


class Node:
    def __init__(self, x: int = 0, cnt: int = 0):
        self.x = x
        self.cnt = cnt

    def __iadd__(self, that: "Node") -> "Node":
        if self.x == that.x:
            self.cnt += that.cnt
        elif self.cnt >= that.cnt:
            self.cnt -= that.cnt
        else:
            self.x = that.x
            self.cnt = that.cnt - self.cnt
        return self


class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.arr = arr
        self.loc = collections.defaultdict(list)

        for i, val in enumerate(arr):
            self.loc[val].append(i)

        self.tree = [Node() for _ in range(self.n * 4)]
        self.seg_build(0, 0, self.n - 1)

    def query(self, left: int, right: int, threshold: int) -> int:
        # Method: Boyer-Moore + Segment Tree
        loc_ = self.loc

        ans = Node()
        self.seg_query(0, 0, self.n - 1, left, right, ans)
        pos = loc_[ans.x]
        occ = bisect.bisect_right(pos, right) - bisect.bisect_left(pos, left)
        return ans.x if occ >= threshold else -1

    def seg_build(self, idx: int, l: int, r: int):
        arr_ = self.arr
        tree_ = self.tree

        if l == r:
            tree_[idx] = Node(arr_[l], 1)
            return

        mid = (l + r) >> 1
        self.seg_build(idx * 2 + 1, l, mid)
        self.seg_build(idx * 2 + 2, mid + 1, r)
        tree_[idx] += tree_[idx * 2 + 1]
        tree_[idx] += tree_[idx * 2 + 2]

    def seg_query(self, idx: int, l: int, r: int, ql: int, qr: int, ans: Node):
        tree_ = self.tree

        if l > qr or r < ql:
            return

        if ql <= l and r <= qr:
            ans += tree_[idx]
            return

        mid = (l + r) >> 1
        self.seg_query(idx * 2 + 1, l, mid, ql, qr, ans)
        self.seg_query(idx * 2 + 2, mid + 1, r, ql, qr, ans)


def main():
    # Example 1: Output: [null, 1, -1, 2]
    command_list = ["MajorityChecker", "query", "query", "query"]
    param_list = [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]

    # init instance
    obj = MajorityChecker(param_list[0][0])
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "query" and isinstance(param, list) and len(param) == 3:
            ans.append(obj.query(param[0], param[1], param[2]))
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
