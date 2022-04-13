#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0380-Insert-Delete-GetRandom-O1.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-13
=================================================================="""

import sys
import time
from random import choice
# from typing import List
# import functools

"""
LeetCode - 0380 - (Medium) - Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/

Description & Requirement:
    Implement the RandomizedSet class:
        RandomizedSet() Initializes the RandomizedSet object.
        bool insert(int val) Inserts an item val into the set if not present. 
            Returns true if the item was not present, false otherwise.
        bool remove(int val) Removes an item val from the set if present. 
            Returns true if the item was present, false otherwise.
        int getRandom() Returns a random element from the current set of elements 
            (it's guaranteed that at least one element exists when this method is called). 
            Each element must have the same probability of being returned.

    You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:
    Input
        ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
        [[], [1], [2], [2], [], [1], [2], []]
    Output
        [null, true, false, true, 2, true, false, 2]
    Explanation
        RandomizedSet randomizedSet = new RandomizedSet();
        randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
        randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
        randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
        randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
        randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
        randomizedSet.insert(2); // 2 was already in the set, so return false.
        randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

Constraints:
    -2^31 <= val <= 2^31 - 1
    At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
    There will be at least one element in the data structure when getRandom is called.
"""


class RandomizedSet:

    def __init__(self):
        self.r_dict = dict({})

    def insert(self, val: int) -> bool:
        if val in self.r_dict:
            return False
        else:
            self.r_dict[val] = None
            return True

    def remove(self, val: int) -> bool:
        if val in self.r_dict:
            del self.r_dict[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(list(self.r_dict.keys()))


def main():
    # Example 1: Output: [null, true, false, true, 2, true, false, 2]
    command_list = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    param_list = [[], [1], [2], [2], [], [1], [2], []]

    # init instance
    # solution = Solution()
    obj = RandomizedSet()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "insert":
            if isinstance(param, list) and len(param) == 1:
                ans.append(obj.insert(param[0]))
            else:
                ans.append("null")
        elif command == "remove":
            if isinstance(param, list) and len(param) == 1:
                ans.append(obj.remove(param[0]))
            else:
                ans.append("null")
        elif command == "getRandom":
            ans.append(obj.getRandom())
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
