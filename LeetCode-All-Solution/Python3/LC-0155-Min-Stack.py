#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0155-Min-Stack.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-24
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0155 - (Easy) - Min Stack
https://leetcode.com/problems/min-stack/

Description & Requirement:
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:
        MinStack() initializes the stack object.
        void push(int val) pushes the element val onto the stack.
        void pop() removes the element on the top of the stack.
        int top() gets the top element of the stack.
        int getMin() retrieves the minimum element in the stack.

Example 1:
    Input
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]
    Output
        [null,null,null,null,-3,null,0,-2]
    Explanation
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin(); // return -3
        minStack.pop();
        minStack.top();    // return 0
        minStack.getMin(); // return -2

Constraints:
    -2^31 <= val <= 2^31 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []  # self.min_stack[i] is the min of i+1 items when len(self.stack) == i+1

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


def main():
    # Example 1: Output: [null,null,null,null,-3,null,0,-2]
    command_list = ["MinStack","push","push","push","getMin","pop","top","getMin"]
    param_list = [[],[-2],[0],[-3],[],[],[],[]]

    # init instance
    # solution = Solution()
    obj = MinStack()

    # run & time
    start = time.process_time()
    ans = ["null"]
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "push":
            if isinstance(param, list) and len(param) == 1:
                obj.push(param[0])
            ans.append("null")
        elif command == "pop":
            obj.pop()
            ans.append("null")
        elif command == "top":
            ans.append(obj.top())
        elif command == "getMin":
            ans.append(obj.getMin())
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
