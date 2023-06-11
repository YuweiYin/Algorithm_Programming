#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1146-Snapshot-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-11
=================================================================="""

import sys
import time
import bisect
# from typing import List
# import collections
# import functools

"""
LeetCode - 1146 - (Medium) - Snapshot Array
https://leetcode.com/problems/snapshot-array/

Description & Requirement:
    Implement a SnapshotArray that supports the following interface:
        - SnapshotArray(int length) initializes an array-like data structure with the given length. 
            Initially, each element equals 0.
        - void set(index, val) sets the element at the given index to be equal to val.
        - int snap() takes a snapshot of the array and returns the snap_id: 
            the total number of times we called snap() minus 1.
        - int get(index, snap_id) returns the value at the given index, 
            at the time we took the snapshot with the given snap_id

Example 1:
    Input: ["SnapshotArray","set","snap","set","get"]
        [[3],[0,5],[],[0,6],[0,0]]
    Output: [null,null,0,null,5]
    Explanation: 
        SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
        snapshotArr.set(0,5);  // Set array[0] = 5
        snapshotArr.snap();  // Take a snapshot, return snap_id = 0
        snapshotArr.set(0,6);
        snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5

Constraints:
    1 <= length <= 5 * 10^4
    0 <= index < length
    0 <= val <= 10^9
    0 <= snap_id < (the total number of times we call snap())
    At most 5 * 10^4 calls will be made to set, snap, and get.
"""


class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [{0: 0} for _ in range(length)]
        self.sid = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index][self.sid] = val

    def snap(self) -> int:
        self.sid += 1
        return self.sid - 1

    def get(self, index: int, snap_id: int) -> int:
        dic = self.arr[index]
        if snap_id in dic:
            return dic[snap_id]
        k = list(dic.keys())
        i = bisect.bisect_left(k, snap_id)
        return dic[k[i - 1]]


def main():
    # Example 1: Output: [null,null,0,null,5]
    command_list = ["SnapshotArray","set","snap","set","get"]
    param_list = [[3],[0,5],[],[0,6],[0,0]]

    # init instance
    obj = SnapshotArray(param_list[0][0])
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "set" and isinstance(param, list) and len(param) == 2:
            obj.set(param[0], param[1])
            ans.append("null")
        elif command == "get" and isinstance(param, list) and len(param) == 2:
            ans.append(obj.get(param[0], param[1]))
        elif command == "snap":
            ans.append(obj.snap())
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
