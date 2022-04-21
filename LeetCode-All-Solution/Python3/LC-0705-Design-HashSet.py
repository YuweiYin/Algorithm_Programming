#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0705-Design-HashSet.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-21
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0705 - (Easy) - Design HashSet
https://leetcode.com/problems/design-hashset/

Description & Requirement:
    Design a HashSet without using any built-in hash table libraries.

    Implement MyHashSet class:
        void add(key) Inserts the value key into the HashSet.
        bool contains(key) Returns whether the value key exists in the HashSet or not.
        void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:
    Input
        ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
        [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    Output
        [null, null, null, true, false, null, true, null, false]
    Explanation
        MyHashSet myHashSet = new MyHashSet();
        myHashSet.add(1);      // set = [1]
        myHashSet.add(2);      // set = [1, 2]
        myHashSet.contains(1); // return True
        myHashSet.contains(3); // return False, (not found)
        myHashSet.add(2);      // set = [1, 2]
        myHashSet.contains(2); // return True
        myHashSet.remove(2);   // set = [1]
        myHashSet.contains(2); // return False, (already removed)

Constraints:
    0 <= key <= 10^6
    At most 10^4 calls will be made to add, remove, and contains.
"""


class MyHashSet:

    def __init__(self):
        self.MAX_INT = int(1e6+1)
        self.hash_set = [False for _ in range(self.MAX_INT)]  # 0 <= key <= 10^6

    def add(self, key: int) -> None:
        if 0 <= key < self.MAX_INT:
            self.hash_set[key] = True

    def remove(self, key: int) -> None:
        if 0 <= key < self.MAX_INT:
            self.hash_set[key] = False

    def contains(self, key: int) -> bool:
        return self.hash_set[key] if 0 <= key < self.MAX_INT else False


def main():
    # Example 1: Output: [null, null, null, true, false, null, true, null, false]
    # Example 1: Output: [null, null, null, 1, -1, null, 1, null, -1]
    command_list = ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
    param_list = [[], [1], [2], [1], [3], [2], [2], [2], [2]]

    # init instance
    # solution = Solution()
    obj = MyHashSet()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for cursor in range(1, len(command_list)):
        command = command_list[cursor]
        param = param_list[cursor]
        if command == "add":
            if isinstance(param, list) and len(param) == 1:
                obj.add(param[0])
                ans.append("null")
        elif command == "remove":
            if isinstance(param, list) and len(param) == 1:
                obj.remove(param[0])
                ans.append("null")
        elif command == "contains":
            if isinstance(param, list) and len(param) == 1:
                ans.append(obj.contains(param[0]))
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
