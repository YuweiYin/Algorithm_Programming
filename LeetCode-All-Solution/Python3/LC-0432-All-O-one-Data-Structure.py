#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0432-All-O-one-Data-Structure.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-16
=================================================================="""

import sys
import time
from sortedcontainers import SortedList
# from typing import List
# import functools

"""
LeetCode - 0432 - (Hard) - All O-one Data Structure
https://leetcode.com/problems/all-oone-data-structure/

Description & Requirement:
    Design a data structure to store the strings' count with the ability to 
    return the strings with minimum and maximum counts.

    Implement the AllOne class:
        AllOne() Initializes the object of the data structure.
        inc(String key) Increments the count of the string key by 1. 
            If key does not exist in the data structure, insert it with count 1.
        dec(String key) Decrements the count of the string key by 1. 
            If the count of key is 0 after the decrement, remove it from the data structure. 
            It is guaranteed that key exists in the data structure before the decrement.
        getMaxKey() Returns one of the keys with the maximal count.
            If no element exists, return an empty string "".
        getMinKey() Returns one of the keys with the minimum count.
            If no element exists, return an empty string "".

Example 1:
    Input
        ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
        [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
    Output
        [null, null, null, "hello", "hello", null, "hello", "leet"]
    Explanation
        AllOne allOne = new AllOne();
        allOne.inc("hello");
        allOne.inc("hello");
        allOne.getMaxKey(); // return "hello"
        allOne.getMinKey(); // return "hello"
        allOne.inc("leet");
        allOne.getMaxKey(); // return "hello"
        allOne.getMinKey(); // return "leet"

Constraints:
    1 <= key.length <= 10
    key consists of lowercase English letters.
    It is guaranteed that for each call to dec, key is existing in the data structure.
    At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.
"""


class AllOne:
    """
    other method: double-linked list + hash dict
    """

    def __init__(self):
        self.sorted_list = SortedList([])
        self.counter_to_key = dict({})
        self.key_to_counter = dict({})
        self.counter_to_key[1] = set()

    def inc(self, key: str) -> None:
        if key not in self.key_to_counter:
            self.key_to_counter[key] = 1
            self.counter_to_key[1].add(key)
            self.sorted_list.add(1)  # O(log n)
        else:
            former_counter = self.key_to_counter[key]
            self.key_to_counter[key] += 1
            self.counter_to_key[former_counter].discard(key)
            if (former_counter + 1) not in self.counter_to_key:
                self.counter_to_key[former_counter + 1] = set()
            self.counter_to_key[former_counter + 1].add(key)
            self.sorted_list.discard(former_counter)  # O(log n)
            self.sorted_list.add(former_counter + 1)  # O(log n)

    def dec(self, key: str) -> None:
        if key in self.key_to_counter:
            former_counter = self.key_to_counter[key]
            if former_counter > 1:
                self.key_to_counter[key] -= 1
                self.counter_to_key[former_counter].discard(key)
                if (former_counter - 1) not in self.counter_to_key:
                    self.counter_to_key[former_counter - 1] = set()
                self.counter_to_key[former_counter - 1].add(key)
                self.sorted_list.discard(former_counter)  # O(log n)
                self.sorted_list.add(former_counter - 1)  # O(log n)
            else:  # now former_counter == 1, after dec it is 0, so delete it
                del self.key_to_counter[key]
                self.counter_to_key[former_counter].discard(key)
                self.sorted_list.discard(former_counter)  # O(log n)
        else:
            pass

    def getMaxKey(self) -> str:
        if len(self.sorted_list) > 0:
            max_counter = self.sorted_list[-1]
            max_key_set = self.counter_to_key[max_counter]
            max_key_list = list(max_key_set)
            return max_key_list[0] if len(max_key_list) > 0 else ""
        else:
            return ""

    def getMinKey(self) -> str:
        if len(self.sorted_list) > 0:
            min_counter = self.sorted_list[0]
            min_key_set = self.counter_to_key[min_counter]
            min_key_list = list(min_key_set)
            return min_key_list[0] if len(min_key_list) > 0 else ""
        else:
            return ""


def main():
    # Example 1: Output: [null, null, null, "hello", "hello", null, "hello", "leet"]
    # command_list = ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
    # param_list = [[], ["hello"], ["hello"], [], [], ["leet"], [], []]

    # Example 2: [null,null,null,null,null,null,null,null,null,"a",null,"c","c"]
    command_list = [
        "AllOne", "inc", "inc", "inc", "inc", "inc", "inc", "dec", "dec", "getMinKey", "dec", "getMaxKey", "getMinKey"
    ]
    param_list = [[], ["a"], ["b"], ["b"], ["c"], ["c"], ["c"], ["b"], ["b"], [], ["a"], [], []]

    # init instance
    # solution = Solution()
    obj = AllOne()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        cur_command = command_list[idx]
        cur_param = param_list[idx]
        if cur_command == "inc":
            obj.inc(cur_param[0])
            ans.append("null")
        elif cur_command == "dec":
            obj.dec(cur_param[0])
            ans.append("null")
        elif cur_command == "getMaxKey":
            ans.append(obj.getMaxKey())
        elif cur_command == "getMinKey":
            ans.append(obj.getMinKey())
        else:
            continue
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
