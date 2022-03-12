#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0706-Design-HashMap.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-12
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0706 - (Easy) - Design HashMap
https://leetcode.com/problems/design-hashmap/

Description & Requirement:
    Design a HashMap without using any built-in hash table libraries.

    Implement the MyHashMap class:
        MyHashMap() initializes the object with an empty map.
        void put(int key, int value) inserts a (key, value) pair into the HashMap. 
            If the key already exists in the map, update the corresponding value.
        int get(int key) returns the value to which the specified key is mapped, 
            or -1 if this map contains no mapping for the key.
        void remove(key) removes the key and its corresponding value 
            if the map contains the mapping for the key.

Example 1:
    Input
        ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
        [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
    Output
        [null, null, null, 1, -1, null, 1, null, -1]
    Explanation
        MyHashMap myHashMap = new MyHashMap();
        myHashMap.put(1, 1); // The map is now [[1,1]]
        myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
        myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
        myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
        myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
        myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
        myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
        myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

Constraints:
    0 <= key, value <= 10^6
    At most 10^4 calls will be made to put, get, and remove.
"""


class MyHashMap:

    def __init__(self):
        # Constraint: 0 <= key, value <= 10^6
        self.hash_list = [-1 for _ in range(int(1e6+1))]  # key is index, value == -1 means it has been removed

    def put(self, key: int, value: int) -> None:
        self.hash_list[key] = value

    def get(self, key: int) -> int:
        return self.hash_list[key]

    def remove(self, key: int) -> None:
        self.hash_list[key] = -1

    # def show_hash_map(self):
    #     res = []
    #     for key, value in enumerate(self.hash_list):
    #         if value >= 0:
    #             res.append([key, value])
    #     return res


def main():
    # Example 1: Output: [null, null, null, 1, -1, null, 1, null, -1]
    command_list = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
    param_list = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

    # init instance
    # solution = Solution()
    obj = MyHashMap()

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for cursor in range(1, len(command_list)):
        command = command_list[cursor]
        param = param_list[cursor]
        if command == "put":
            if isinstance(param, list) and len(param) == 2:
                obj.put(param[0], param[1])
        elif command == "get":
            if isinstance(param, list) and len(param) == 1:
                obj.get(param[0])
        elif command == "remove":
            if isinstance(param, list) and len(param) == 1:
                obj.remove(param[0])
        else:
            continue
    end = time.process_time()

    # show answer
    # print('\nAnswer:')
    # print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
