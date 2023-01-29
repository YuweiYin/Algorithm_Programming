#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0460-LFU-Cache.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-29
=================================================================="""

import sys
import time
import collections
# from typing import List
# import functools

"""
LeetCode - 0460 - (Hard) - LFU Cache
https://leetcode.com/problems/lfu-cache/

Description & Requirement:
    Design and implement a data structure for a Least Frequently Used (LFU) cache.

    Implement the LFUCache class:
        LFUCache(int capacity) Initializes the object with the capacity of the data structure.
        int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
        void put(int key, int value) Update the value of the key if present, or inserts the key if not already present.
            When the cache reaches its capacity, it should invalidate and remove the least frequently used key before 
            inserting a new item. For this problem, when there is a tie 
            (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

    To determine the least frequently used key, a use counter is maintained for each key in the cache. 
    The key with the smallest use counter is the least frequently used key.

    When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). 
    The use counter for a key in the cache is incremented either a get or put operation is called on it.

    The functions get and put must each run in O(1) average time complexity.

Example 1:
    Input
        ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    Output
        [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
    Explanation
        // cnt(x) = the use counter for key x
        // cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
        LFUCache lfu = new LFUCache(2);
        lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
        lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
        lfu.get(1);      // return 1
                         // cache=[1,2], cnt(2)=1, cnt(1)=2
        lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                         // cache=[3,1], cnt(3)=1, cnt(1)=2
        lfu.get(2);      // return -1 (not found)
        lfu.get(3);      // return 3
                         // cache=[3,1], cnt(3)=2, cnt(1)=2
        lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                         // cache=[4,3], cnt(4)=1, cnt(3)=2
        lfu.get(1);      // return -1 (not found)
        lfu.get(3);      // return 3
                         // cache=[3,4], cnt(4)=1, cnt(3)=3
        lfu.get(4);      // return 4
                         // cache=[4,3], cnt(4)=2, cnt(3)=3

Constraints:
    0 <= capacity <= 10^4
    0 <= key <= 10^5
    0 <= value <= 10^9
    At most 2 * 10^5 calls will be made to get and put.
"""


class Node:
    def __init__(self, key, val, pre=None, nex=None, freq=0):
        self.pre = pre
        self.nex = nex
        self.freq = freq
        self.val = val
        self.key = key

    def insert(self, nex):
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.freq_map = collections.defaultdict(LFUCache.create_linked_list)
        self.key_map = {}

    @staticmethod
    def create_linked_list():
        head = Node(0, 0)
        tail = Node(0, 0)
        head.nex = tail
        tail.pre = head
        return head, tail

    def delete(self, node):
        if node.pre:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            if node.pre is self.freq_map[node.freq][0] and node.nex is self.freq_map[node.freq][-1]:
                self.freq_map.pop(node.freq)
        return node.key

    def increase(self, node):
        node.freq += 1
        self.delete(node)
        self.freq_map[node.freq][-1].pre.insert(node)
        if node.freq == 1:
            self.minFreq = 1
        elif self.minFreq == node.freq - 1:
            head, tail = self.freq_map[node.freq - 1]
            if head.nex is tail:
                self.minFreq = node.freq

    def get(self, key: int) -> int:
        if key in self.key_map:
            self.increase(self.key_map[key])
            return self.key_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.key_map:
                node = self.key_map[key]
                node.val = value
            else:
                node = Node(key, value)
                self.key_map[key] = node
                self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                deleted = self.delete(self.freq_map[self.minFreq][0].nex)
                self.key_map.pop(deleted)
            self.increase(node)


def main():
    # Example 1: Output: [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
    command_list = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    param_list = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

    # init instance
    capacity = param_list[0][0]
    obj = LFUCache(capacity)
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
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
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
