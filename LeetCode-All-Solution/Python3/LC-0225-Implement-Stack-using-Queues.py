#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0225-Implement-Stack-using-Queues.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-30
=================================================================="""

import sys
import time
import collections
# from typing import List
# import functools

"""
LeetCode - 0225 - (Easy) - Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/

Description & Requirement:
    Implement a last-in-first-out (LIFO) stack using only two queues. 
    The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

    Implement the MyStack class:
        void push(int x) Pushes element x to the top of the stack.
        int pop() Removes the element on the top of the stack and returns it.
        int top() Returns the element on the top of the stack.
        boolean empty() Returns true if the stack is empty, false otherwise.

    Notes:
        You must use only standard operations of a queue, which means that only push to back, 
            peek/pop from front, size and is empty operations are valid.
        Depending on your language, the queue may not be supported natively. You may simulate a queue 
            using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

Example 1:
    Input
        ["MyStack", "push", "push", "top", "pop", "empty"]
        [[], [1], [2], [], [], []]
    Output
        [null, null, null, 2, 2, false]
    Explanation
        MyStack myStack = new MyStack();
        myStack.push(1);
        myStack.push(2);
        myStack.top(); // return 2
        myStack.pop(); // return 2
        myStack.empty(); // return False

Constraints:
    1 <= x <= 9
    At most 100 calls will be made to push, pop, top, and empty.
    All the calls to pop and top are valid.

Follow-up:
    Can you implement the stack using only one queue?
"""


class MyStack:

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        # popleft every element and append it
        q_len = len(self.queue)
        self.queue.append(x)
        for _ in range(q_len):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


def main():
    # Example 1: Output: [null, null, null, 2, 2, false]
    command_list = ["MyStack", "push", "push", "top", "pop", "empty"]
    param_list = [[], [1], [2], [], [], []]

    # init instance
    # solution = Solution()
    obj = MyStack()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "push":
            if isinstance(param, list) and len(param) == 1:
                obj.push(param[0])
            ans.append("null")
        elif command == "pop":
            ans.append(obj.pop())
        elif command == "top":
            ans.append(obj.top())
        elif command == "empty":
            ans.append(obj.empty())
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
