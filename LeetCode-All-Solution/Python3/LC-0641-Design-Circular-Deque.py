#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0641-Design-Circular-Deque.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-15
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0641 - (Medium) - Design Circular Deque
https://leetcode.com/problems/design-circular-deque/

Description & Requirement:
    Design your implementation of the circular double-ended queue (deque).

    Implement the MyCircularDeque class:
        MyCircularDeque(int k) Initializes the deque with a maximum size of k.
        boolean insertFront() Adds an item at the front of Deque. 
            Returns true if the operation is successful, or false otherwise.
        boolean insertLast() Adds an item at the rear of Deque. 
            Returns true if the operation is successful, or false otherwise.
        boolean deleteFront() Deletes an item from the front of Deque. 
            Returns true if the operation is successful, or false otherwise.
        boolean deleteLast() Deletes an item from the rear of Deque. 
            Returns true if the operation is successful, or false otherwise.
        int getFront() Returns the front item from the Deque. 
            Returns -1 if the deque is empty.
        int getRear() Returns the last item from Deque. 
            Returns -1 if the deque is empty.
        boolean isEmpty() Returns true if the deque is empty, or false otherwise.
        boolean isFull() Returns true if the deque is full, or false otherwise.

Example 1:
    Input
        ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", 
            "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
        [[3], [1], [2], [3], [4], [], [], [], [4], []]
    Output
        [null, true, true, true, false, 2, true, true, true, 4]
    Explanation
        MyCircularDeque myCircularDeque = new MyCircularDeque(3);
        myCircularDeque.insertLast(1);  // return True
        myCircularDeque.insertLast(2);  // return True
        myCircularDeque.insertFront(3); // return True
        myCircularDeque.insertFront(4); // return False, the queue is full.
        myCircularDeque.getRear();      // return 2
        myCircularDeque.isFull();       // return True
        myCircularDeque.deleteLast();   // return True
        myCircularDeque.insertFront(4); // return True
        myCircularDeque.getFront();     // return 4

Constraints:
    1 <= k <= 1000
    0 <= value <= 1000
    At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, 
        getFront, getRear, isEmpty, isFull.
"""


class MyCircularDeque:

    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.items = [0 for _ in range(k + 1)]

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % len(self.items)
        self.items[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.items[self.rear] = value
        self.rear = (self.rear + 1) % len(self.items)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.items)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % len(self.items)
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.items[self.front]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.items[(self.rear - 1) % len(self.items)]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.items) == self.front


def main():
    # Example 1: Output: [null, true, true, true, false, 2, true, true, true, 4]
    command_list = ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull",
                    "deleteLast", "insertFront", "getFront"]
    param_list = [[3], [1], [2], [3], [4], [], [], [], [4], []]

    # init instance
    # solution = Solution()
    obj = MyCircularDeque(param_list[0][0])
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(param_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "insertFront":
            if isinstance(param, list) and len(param) == 1:
                ans.append(obj.insertFront(param[0]))
            else:
                ans.append("null")
        elif command == "insertLast":
            if isinstance(param, list) and len(param) == 1:
                ans.append(obj.insertLast(param[0]))
            else:
                ans.append("null")
        elif command == "deleteFront":
            ans.append(obj.deleteFront())
        elif command == "deleteLast":
            ans.append(obj.deleteLast())
        elif command == "getFront":
            ans.append(obj.getFront())
        elif command == "getRear":
            ans.append(obj.getRear())
        elif command == "isEmpty":
            ans.append(obj.isEmpty())
        elif command == "isFull":
            ans.append(obj.isFull())
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
