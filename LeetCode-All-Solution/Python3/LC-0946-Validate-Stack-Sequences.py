#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0946-Validate-Stack-Sequences.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-16
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0946 - (Medium) - Validate Stack Sequences
https://leetcode.com/problems/validate-stack-sequences/

Description & Requirement:
    Given two integer arrays pushed and popped each with distinct values, 
    return true if this could have been the result of a sequence of push and pop operations 
    on an initially empty stack, or false otherwise.

Example 1:
    Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    Output: true
    Explanation: We might do the following sequence:
        push(1), push(2), push(3), push(4),
        pop() -> 4,
        push(5),
        pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:
    Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
    Output: false
    Explanation: 1 cannot be popped before 2.

Constraints:
    1 <= pushed.length <= 1000
    0 <= pushed[i] <= 1000
    All the elements of pushed are unique.
    popped.length == pushed.length
    popped is a permutation of pushed.
"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # exception case
        assert isinstance(pushed, list) and len(pushed) > 0
        assert isinstance(popped, list) and len(popped) == len(pushed)
        # main method: (simulate the push & pop process)
        return self._validateStackSequences(pushed, popped)

    def _validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        len_elements = len(pushed)
        assert 0 < len_elements == len(popped)

        stack = []
        pushed_idx = 0
        popped_idx = 0

        while pushed_idx < len_elements and popped_idx < len_elements:
            # start pushing until stack_top == cur_popped
            while len(stack) == 0 or stack[-1] != popped[popped_idx]:
                if pushed_idx < len_elements:
                    stack.append(pushed[pushed_idx])
                    pushed_idx += 1
                else:
                    return False
            # now stack[-1] == popped[popped_idx], start popping as many as possible
            while len(stack) > 0 and stack[-1] == popped[popped_idx]:
                if popped_idx < len_elements:
                    stack.pop()
                    popped_idx += 1
                else:
                    return pushed_idx == len_elements

        return pushed_idx == len_elements and popped_idx == len_elements


def main():
    # Example 1: Output: true
    # pushed = [1, 2, 3, 4, 5]
    # popped = [4, 5, 3, 2, 1]

    # Example 2: Output: false
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.validateStackSequences(pushed, popped)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
