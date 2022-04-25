#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0284-Peeking-Iterator.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-25
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0284 - (Medium) - Peeking Iterator
https://leetcode.com/problems/peeking-iterator/

Description & Requirement:
    Design an iterator that supports the peek operation on an existing iterator 
    in addition to the hasNext and the next operations.

    Implement the PeekingIterator class:
        PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
        int next() Returns the next element in the array and moves the pointer to the next element.
        boolean hasNext() Returns true if there are still elements in the array.
        int peek() Returns the next element in the array without moving the pointer.

    Note: Each language may have a different implementation of the constructor and Iterator, 
    but they all support the int next() and boolean hasNext() functions.

Example 1:
    Input
        ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
        [[[1, 2, 3]], [], [], [], [], []]
    Output
        [null, 1, 2, 2, 3, false]
    Explanation
        PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
        peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
        peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
        peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]
        peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
        peekingIterator.hasNext(); // return False

Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 1000
    All the calls to next and peek are valid.
    At most 1000 calls will be made to next, hasNext, and peek.

Follow up:
    How would you extend your design to be generic and work with all types, not just integer?
"""


class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.pointer = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.pointer < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        if self.hasNext():
            next_num = self.nums[self.pointer]
            self.pointer += 1
            return next_num
        else:
            return 0


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peek_num = 0  # 1 <= nums[i] <= 1000

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peek_num == 0:
            self.peek_num = self.iterator.next()
        return self.peek_num

    def next(self):
        """
        :rtype: int
        """
        if self.peek_num == 0:
            return self.iterator.next()
        else:
            next_num = self.peek_num
            self.peek_num = 0  # reset peek_num
            return next_num

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peek_num == 0:
            return self.iterator.hasNext()
        else:
            return True


def main():
    # Example 1: Output: [null, 1, 2, 2, 3, false]
    command_list = ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
    param_list = [[[1, 2, 3]], [], [], [], [], []]

    # init instance
    # solution = Solution()
    iter = PeekingIterator(Iterator(param_list[0][0]))
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for cursor in range(1, len(command_list)):
        command = command_list[cursor]
        param = param_list[cursor]
        if command == "peek":
            ans.append(iter.peek())
        elif command == "next":
            ans.append(iter.next())
        elif command == "hasNext":
            ans.append(iter.hasNext())
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
