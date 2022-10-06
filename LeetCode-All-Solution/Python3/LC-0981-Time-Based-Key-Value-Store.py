#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0981-Time-Based-Key-Value-Store.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-06
=================================================================="""

import sys
import time
import collections
# import bisect
# from typing import List
# import functools

"""
LeetCode - 0981 - (Medium) - Time Based Key-Value Store
https://leetcode.com/problems/time-based-key-value-store/

Description & Requirement:
    Design a time-based key-value data structure that can store multiple values for the same key 
    at different time stamps and retrieve the key's value at a certain timestamp.

    Implement the TimeMap class:
        TimeMap() Initializes the object of the data structure.
        void set(String key, String value, int timestamp) Stores the key key 
            with the value value at the given time timestamp.
        String get(String key, int timestamp) Returns a value such that set was called previously, 
            with timestamp_prev <= timestamp. If there are multiple such values, 
            it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

Example 1:
    Input
        ["TimeMap", "set", "get", "get", "set", "get", "get"]
        [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    Output
        [null, null, "bar", "bar", null, "bar2", "bar2"]
    Explanation
        TimeMap timeMap = new TimeMap();
        timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
        timeMap.get("foo", 1);         // return "bar"
        timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 
            and timestamp 2, then the only value is at timestamp 1 is "bar".
        timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
        timeMap.get("foo", 4);         // return "bar2"
        timeMap.get("foo", 5);         // return "bar2"

Constraints:
    1 <= key.length, value.length <= 100
    key and value consist of lowercase English letters and digits.
    1 <= timestamp <= 10^7
    All the timestamps timestamp of set are strictly increasing.
    At most 2 * 10^5 calls will be made to set and get.
"""


class TimeMap:

    def __init__(self):
        self.key_val = collections.defaultdict(list)
        self.key_ts = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_val[key].append(value)
        self.key_ts[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        """
        Runtime: 1480 ms, faster than 42.06% of Python3 online submissions for Time Based Key-Value Store.
        Memory Usage: 68.5 MB, less than 95.62% of Python3 online submissions for Time Based Key-Value Store.
        """
        lo, hi = 0, len(self.key_ts[key]) - 1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if self.key_ts[key][mid] > timestamp:
                hi = mid - 1
            else:
                lo = mid + 1
        return self.key_val[key][lo - 1] if lo > 0 else ""

    @staticmethod
    def bisect_left(a, x, lo=0, hi=None):
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(a)
        while lo < hi:
            mid = (lo + hi) >> 1
            # if a[mid] < x:
            if a[mid][0] < x[0] or (a[mid][0] == x[0] and a[mid][1] < x[1]):
                lo = mid + 1
            else:
                hi = mid
        return lo

    @staticmethod
    def bisect_right(a, x, lo=0, hi=None):
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(a)
        while lo < hi:
            mid = (lo + hi) >> 1
            # if x < a[mid]:
            if x[0] < a[mid][0] or (x[0] == a[mid][0] and x[1] < a[mid][1]):
                hi = mid
            else:
                lo = mid + 1
        return lo


def main():
    # Example 1: Output: [null, null, "bar", "bar", null, "bar2", "bar2"]
    command_list = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    param_list = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

    # init instance
    # solution = Solution()
    obj = TimeMap()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "set" and len(param) == 3:
            obj.set(param[0], param[1], param[2])
            ans.append("null")
        elif command == "get" and len(param) == 2:
            ans.append(obj.get(param[0], param[1]))
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
