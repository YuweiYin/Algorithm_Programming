#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1206-Design-Skiplist.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-26
=================================================================="""

import sys
import time
import random
from typing import List
# import functools

"""
LeetCode - 1206 - (Hard) - Design Skiplist
https://leetcode.com/problems/design-skiplist/

Description & Requirement:
    Design a Skiplist without using any built-in libraries.
    Artyom Kalinin [CC BY-SA 3.0], see more about Skiplist: https://en.wikipedia.org/wiki/Skip_list

    A skiplist is a data structure that takes O(log(n)) time to add, erase and search. 
    Comparing with treap and red-black tree which has the same function and performance, 
    the code length of Skiplist can be comparatively short and the idea behind Skiplists is just simple linked lists.

    You can see there are many layers in the Skiplist. Each layer is a sorted linked list. 
    With the help of the top layers, add, erase and search can be faster than O(n). 
    It can be proven that the average time complexity for each operation is O(log(n)) and space complexity is O(n).

    Implement the Skiplist class:
        Skiplist() Initializes the object of the skiplist.
        bool search(int target) Returns true if the integer target exists in the Skiplist or false otherwise.
        void add(int num) Inserts the value num into the SkipList.
        bool erase(int num) Removes the value num from the Skiplist and returns true. 
            If num does not exist in the Skiplist, do nothing and return false. 
            If there exist multiple num values, removing any one of them is fine.

    Note that duplicates may exist in the Skiplist, your code needs to handle this situation.

Example 1:
    Input
        ["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
        [[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
    Output
        [null, null, null, null, false, null, true, false, true, false]
    Explanation
        Skiplist skiplist = new Skiplist();
        skiplist.add(1);
        skiplist.add(2);
        skiplist.add(3);
        skiplist.search(0); // return False
        skiplist.add(4);
        skiplist.search(1); // return True
        skiplist.erase(0);  // return False, 0 is not in skiplist.
        skiplist.erase(1);  // return True
        skiplist.search(1); // return False, 1 has already been erased.

Constraints:
    0 <= num, target <= 2 * 10^4
    At most 5 * 10^4 calls will be made to search, add, and erase.
"""


class SkiplistNode:
    __slots__ = 'val', 'forward'

    def __init__(self, val: int, max_level=32):
        self.val = val
        self.forward = [None for _ in range(max_level)]


class Skiplist:
    def __init__(self):
        self.MAX_LEVEL = 32
        self.P_FACTOR = 0.25
        self.head = SkiplistNode(-1, self.MAX_LEVEL)
        self.level = 0

    def random_level(self) -> int:
        lv = 1
        while lv < self.MAX_LEVEL and random.random() < self.P_FACTOR:
            lv += 1
        return lv

    def search(self, target: int) -> bool:
        cur_node = self.head
        for i in range(self.level - 1, -1, -1):
            # find a number in the i-th layer that is smaller than target and is the closest to target
            while isinstance(cur_node.forward[i], SkiplistNode) and cur_node.forward[i].val < target:
                cur_node = cur_node.forward[i]
        cur_node = cur_node.forward[0]
        # check if the val of current node is target 检测当前元素的值是否等于 target
        return isinstance(cur_node, SkiplistNode) and cur_node.val == target

    def add(self, num: int) -> None:
        update = [self.head for _ in range(self.MAX_LEVEL)]
        cur_node = self.head
        for i in range(self.level - 1, -1, -1):
            # find a number in the i-th layer that is smaller than num and is the closest to num
            while isinstance(cur_node.forward[i], SkiplistNode) and cur_node.forward[i].val < num:
                cur_node = cur_node.forward[i]
            update[i] = cur_node

        lv = self.random_level()
        self.level = max(self.level, lv)
        new_node = SkiplistNode(num, lv)
        for i in range(lv):
            # update the states of the i-th layer
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None for _ in range(self.MAX_LEVEL)]
        cur_node = self.head
        for i in range(self.level - 1, -1, -1):
            # find a number in the i-th layer that is smaller than num and is the closest to num
            while isinstance(cur_node.forward[i], SkiplistNode) and cur_node.forward[i].val < num:
                cur_node = cur_node.forward[i]
            update[i] = cur_node

        cur_node = cur_node.forward[0]
        if not isinstance(cur_node, SkiplistNode) or cur_node.val != num:
            return False
        for i in range(self.level):
            if update[i].forward[i] != cur_node:
                break
            # update the states of the i-th layer
            update[i].forward[i] = cur_node.forward[i]

        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1
        return True


def main():
    # Example 1: Output: [null, null, null, null, false, null, true, false, true, false]
    command_list = ["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
    param_list = [[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]

    # init instance
    # solution = Solution()
    obj = Skiplist()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "add":
            if isinstance(param, list) and len(param) == 1:
                obj.add(param[0])
            ans.append("null")
        elif command == "search":
            if isinstance(param, list) and len(param) == 1:
                ans.append(obj.search(param[0]))
            else:
                ans.append("null")
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
