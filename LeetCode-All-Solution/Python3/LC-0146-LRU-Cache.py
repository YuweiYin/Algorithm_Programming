#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0146-LRU-Cache.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-18
=================================================================="""

import sys
import time
# from typing import List
# import functools
# import itertools

"""
LeetCode - 0146 - (Medium) - LRU Cache
https://leetcode.com/problems/lru-cache/

Description & Requirement:
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

    Implement the LRUCache class:
        LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
        int get(int key) Return the value of the key if the key exists, otherwise return -1.
        void put(int key, int value) Update the value of the key if the key exists. 
            Otherwise, add the key-value pair to the cache. If the number of keys exceeds 
            the capacity from this operation, evict the least recently used key.

    The functions get and put must each run in O(1) average time complexity.

Example 1:
    Input
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Output
        [null, null, null, 1, null, -1, null, -1, 3, 4]
    Explanation
        LRUCache lRUCache = new LRUCache(2);
        lRUCache.put(1, 1); // cache is {1=1}
        lRUCache.put(2, 2); // cache is {1=1, 2=2}
        lRUCache.get(1);    // return 1
        lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        lRUCache.get(2);    // returns -1 (not found)
        lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        lRUCache.get(1);    // return -1 (not found)
        lRUCache.get(3);    // return 3
        lRUCache.get(4);    // return 4

Constraints:
    1 <= capacity <= 3000
    0 <= key <= 10^4
    0 <= value <= 10^5
    At most 2 * 10^5 calls will be made to get and put.
"""


class DoubleLinkedNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.pre = None
        self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DoubleLinkedNode(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.remove_tail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)

    def add_to_head(self, node):
        node.pre = self.head
        node.nxt = self.head.nxt
        self.head.nxt.pre = node
        self.head.nxt = node

    @staticmethod
    def remove_node(node):
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self):
        node = self.tail.pre
        self.remove_node(node)
        return node


def main():
    # Example 1: Output: [null, null, null, 1, null, -1, null, -1, 3, 4]
    command_list = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    param_list = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    # init instance
    capacity = param_list[0][0]
    obj = LRUCache(capacity)
    ans = ["null"]

    # run & time
    _start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command, param = command_list[idx], param_list[idx]
        if command == "put" and isinstance(param, list) and len(param) == 2:
            obj.put(param[0], param[1])
            ans.append("null")
        elif command == "get" and isinstance(param, list) and len(param) == 1:
            ans.append(obj.get(param[0]))
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
