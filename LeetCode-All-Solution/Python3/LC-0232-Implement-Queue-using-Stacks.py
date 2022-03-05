#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0232-Implement-Queue-using-Stacks.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-05
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0232 - (Easy) - Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

Description & Requirement:
    Implement a first in first out (FIFO) queue using only two stacks. 
    The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

    Implement the MyQueue class:
        void push(int x) Pushes element x to the back of the queue.
        int pop() Removes the element from the front of the queue and returns it.
        int peek() Returns the element at the front of the queue.
        boolean empty() Returns true if the queue is empty, false otherwise.

    Notes:
        You must use only standard operations of a stack, which means only push to top, 
            peek/pop from top, size, and is empty operations are valid.
        Depending on your language, the stack may not be supported natively. 
            You may simulate a stack using a list or deque (double-ended queue) 
            as long as you use only a stack's standard operations.

Example 1:
    Input
        ["MyQueue", "push", "push", "peek", "pop", "empty"]
        [[], [1], [2], [], [], []]
    Output
        [null, null, null, 1, 1, false]
    Explanation
        MyQueue myQueue = new MyQueue();
        myQueue.push(1); // queue is: [1]
        myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
        myQueue.peek(); // return 1
        myQueue.pop(); // return 1, queue is [2]
        myQueue.empty(); // return false

Constraints:
    1 <= x <= 9
    At most 100 calls will be made to push, pop, peek, and empty.
    All the calls to pop and peek are valid.

Follow-up:
    Can you implement the queue such that each operation is amortized O(1) time complexity? 
    In other words, performing n operations will take overall O(n) time 
    even if one of those operations may take longer.
"""


class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack_bottom = 0  # to indicate where is the stack bottom, pseudo-pop

    def push(self, x: int) -> None:  # O(1)
        self.stack.append(x)

    def pop(self) -> int:  # O(1)
        if len(self.stack) > self.stack_bottom:
            pop_element = self.stack[self.stack_bottom]
            self.stack_bottom += 1
        else:
            pop_element = None
        return pop_element

    def peek(self) -> int:  # O(1)
        return self.stack[self.stack_bottom] if len(self.stack) > self.stack_bottom else None

    def empty(self) -> bool:  # O(1)
        return len(self.stack) <= self.stack_bottom


def main():
    # Example 1: Output: [null, null, null, 1, 1, false]
    command_list = ["MyQueue", "push", "push", "peek", "pop", "empty"]
    param_list = [[], [1], [2], [], [], []]

    # init instance
    # solution = Solution()

    obj = MyQueue()

    # run & time
    start = time.process_time()
    cursor = 1
    assert len(command_list) == len(param_list)
    while cursor < len(command_list):
        cur_command = command_list[cursor]
        if cur_command == "push":
            obj.push(param_list[cursor][0])
            print("null")
        elif cur_command == "pop":
            print(obj.pop())
        elif cur_command == "peek":
            print(obj.peek())
        elif cur_command == "empty":
            print(obj.empty())
        else:
            pass
        cursor += 1
    end = time.process_time()

    # show answer
    # print('\nAnswer:')
    # print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
