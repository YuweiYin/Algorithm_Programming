#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0622-Design-Circular-Queue.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-02
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0622 - (Medium) - Design Circular Queue
https://leetcode.com/problems/design-circular-queue/

Description & Requirement:
    Design your implementation of the circular queue. 
    The circular queue is a linear data structure in which the operations are performed based on FIFO 
    (First In First Out) principle and the last position is connected back to the first position to make a circle. 
    It is also called "Ring Buffer".

    One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. 
    In a normal queue, once the queue becomes full, we cannot insert the next element 
    even if there is a space in front of the queue. But using the circular queue, 
    we can use the space to store new values.

    Implementation the MyCircularQueue class:
        MyCircularQueue(k) Initializes the object with the size of the queue to be k.
        int Front() Gets the front item from the queue. If the queue is empty, return -1.
        int Rear() Gets the last item from the queue. If the queue is empty, return -1.
        boolean enQueue(int value) Inserts an element into the circular queue. 
            Return true if the operation is successful.
        boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
        boolean isEmpty() Checks whether the circular queue is empty or not.
        boolean isFull() Checks whether the circular queue is full or not.
        You must solve the problem without using the built-in queue data structure in your programming language. 

Example 1:
    Input
        ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
        [[3], [1], [2], [3], [4], [], [], [], [4], []]
    Output
        [null, true, true, true, false, 3, true, true, true, 4]
    Explanation
        MyCircularQueue myCircularQueue = new MyCircularQueue(3);
        myCircularQueue.enQueue(1); // return True
        myCircularQueue.enQueue(2); // return True
        myCircularQueue.enQueue(3); // return True
        myCircularQueue.enQueue(4); // return False
        myCircularQueue.Rear();     // return 3
        myCircularQueue.isFull();   // return True
        myCircularQueue.deQueue();  // return True
        myCircularQueue.enQueue(4); // return True
        myCircularQueue.Rear();     // return 4

Constraints:
    1 <= k <= 1000
    0 <= value <= 1000
    At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.rear = 0
        self.elements = [0 for _ in range(k + 1)]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.elements[self.rear] = value
        self.rear = (self.rear + 1) % len(self.elements)  # use MOD operation to implement looping
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.elements)  # use MOD operation to implement looping
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.elements[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.elements[(self.rear - 1) % len(self.elements)]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.elements) == self.front


def main():
    # Example 1: Output: [null, true, true, true, false, 3, true, true, true, 4]
    command_list = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue",
                    "enQueue", "Rear"]
    param_list = [[3], [1], [2], [3], [4], [], [], [], [4], []]

    # init instance
    # solution = Solution()
    obj = MyCircularQueue(param_list[0][0])
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "enQueue":
            if isinstance(param, list) and len(param) == 1:
                ans.append(obj.enQueue(param[0]))
            else:
                ans.append("null")
        elif command == "deQueue":
            ans.append(obj.deQueue())
        elif command == "Front":
            ans.append(obj.Front())
        elif command == "Rear":
            ans.append(obj.Rear())
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
