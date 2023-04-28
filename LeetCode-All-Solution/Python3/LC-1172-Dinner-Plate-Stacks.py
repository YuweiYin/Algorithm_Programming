#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1172-Dinner-Plate-Stacks.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-28
=================================================================="""

import sys
import time
from sortedcontainers import SortedSet
# from typing import List
# import collections
# import functools

"""
LeetCode - 1172 - (Hard) - Dinner Plate Stacks
https://leetcode.com/problems/dinner-plate-stacks/

Description & Requirement:
    You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, 
    each of the stacks has the same maximum capacity.

    Implement the DinnerPlates class:
        DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks capacity.
        void push(int val) Pushes the given integer val into the leftmost stack with a size less than capacity.
        int pop() Returns the value at the top of the rightmost non-empty stack and removes it from that stack, 
            and returns -1 if all the stacks are empty.
        int popAtStack(int index) Returns the value at the top of the stack with the given index index and 
            removes it from that stack or returns -1 if the stack with that given index is empty.

Example 1:
    Input
        ["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", 
            "popAtStack", "pop", "pop", "pop", "pop", "pop"]
        [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
    Output
        [null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]
    Explanation: 
        DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
        D.push(1);
        D.push(2);
        D.push(3);
        D.push(4);
        D.push(5);         // The stacks are now:  2  4
                                                   1  3  5
                                                   ﹈ ﹈ ﹈
        D.popAtStack(0);   // Returns 2.  The stacks are now:     4
                                                               1  3  5
                                                               ﹈ ﹈ ﹈
        D.push(20);        // The stacks are now: 20  4
                                                   1  3  5
                                                   ﹈ ﹈ ﹈
        D.push(21);        // The stacks are now: 20  4 21
                                                   1  3  5
                                                   ﹈ ﹈ ﹈
        D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
                                                                1  3  5
                                                                ﹈ ﹈ ﹈
        D.popAtStack(2);   // Returns 21.  The stacks are now:     4
                                                                1  3  5
                                                                ﹈ ﹈ ﹈ 
        D.pop()            // Returns 5.  The stacks are now:      4
                                                                1  3 
                                                                ﹈ ﹈  
        D.pop()            // Returns 4.  The stacks are now:   1  3 
                                                                ﹈ ﹈   
        D.pop()            // Returns 3.  The stacks are now:   1 
                                                                ﹈   
        D.pop()            // Returns 1.  There are no stacks.
        D.pop()            // Returns -1.  There are still no stacks.

Constraints:
    1 <= capacity <= 2 * 10^4
    1 <= val <= 2 * 10^4
    0 <= index <= 10^5
    At most 2 * 10^5 calls will be made to push, pop, and popAtStack.
"""


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.top = []
        self.pop_pos = SortedSet()

    def push(self, val: int) -> None:
        if not self.pop_pos:
            pos = len(self.stack)
            self.stack.append(val)
            if pos % self.capacity == 0:
                self.top.append(0)
            else:
                stackPos = len(self.top) - 1
                stackTop = self.top[stackPos]
                self.top[stackPos] = stackTop + 1
        else:
            pos = self.pop_pos.pop(0)
            self.stack[pos] = val
            index = pos // self.capacity
            stackTop = self.top[index]
            self.top[index] = stackTop + 1

    def pop(self) -> int:
        while self.stack and self.pop_pos and self.pop_pos[-1] == len(self.stack) - 1:
            self.stack.pop()
            pos = self.pop_pos.pop()
            if pos % self.capacity == 0:
                self.top.pop()
        if not self.stack:
            return -1
        else:
            pos = len(self.stack) - 1
            val = self.stack[pos]
            self.stack.pop()
            if pos % self.capacity == 0 and self.top:
                self.top.pop()
            elif self.top:
                self.top[-1] -= 1
            return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.top):
            return -1
        stackTop = self.top[index]
        if stackTop < 0:
            return -1
        self.top[index] = stackTop - 1
        pos = index * self.capacity + stackTop
        self.pop_pos.add(pos)
        return self.stack[pos]


def main():
    # Example 1: Output: [null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]
    command_list = ["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack",
                    "popAtStack", "pop", "pop", "pop", "pop", "pop"]
    param_list = [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]

    # init instance
    capacity = param_list[0][0]
    obj = DinnerPlates(capacity)
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "push" and isinstance(param, list) and len(param) == 1:
            obj.push(param[0])
            ans.append("null")
        elif command == "pop":
            ans.append(obj.pop())
        elif command == "push" and isinstance(param, list) and len(param) == 1:
            ans.append(obj.popAtStack(param[0]))
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
