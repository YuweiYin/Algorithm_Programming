#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2337-Move-Pieces-to-Obtain-a-String.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-21
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2337 - (Medium) Move Pieces to Obtain a String
https://leetcode.com/problems/move-pieces-to-obtain-a-string/

Description & Requirement:
    You are given two strings start and target, both of length n. 
    Each string consists only of the characters 'L', 'R', and '_' where:

        The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left 
            only if there is a blank space directly to its left, and a piece 'R' can move to 
            the right only if there is a blank space directly to its right.
        The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.

    Return true if it is possible to obtain the string target by moving the pieces of 
    the string start any number of times. Otherwise, return false.

Example 1:
    Input: start = "_L__R__R_", target = "L______RR"
    Output: true
    Explanation: We can obtain the string target from start by doing the following moves:
        - Move the first piece one step to the left, start becomes equal to "L___R__R_".
        - Move the last piece one step to the right, start becomes equal to "L___R___R".
        - Move the second piece three steps to the right, start becomes equal to "L______RR".
        Since it is possible to get the string target from start, we return true.
Example 2:
    Input: start = "R_L_", target = "__LR"
    Output: false
    Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
        After that, no pieces can move anymore, so it is impossible to obtain the string target from start.
Example 3:
    Input: start = "_R", target = "R_"
    Output: false
    Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.

Constraints:
    n == start.length == target.length
    1 <= n <= 10^5
    start and target consist of the characters 'L', 'R', and '_'.
"""


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # exception case
        assert isinstance(start, str) and isinstance(target, str) and len(start) == len(target) >= 1
        # main method: (two pointers)
        return self._canChange(start, target)

    def _canChange(self, start: str, target: str) -> bool:
        assert isinstance(start, str) and isinstance(target, str) and len(start) == len(target) >= 1

        n = len(start)
        i = j = 0
        while i < n and j < n:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            if i < n and j < n:
                if start[i] != target[j]:
                    return False
                c = start[i]
                if c == 'L' and i < j or c == 'R' and i > j:
                    return False
                i += 1
                j += 1

        while i < n:
            if start[i] != '_':
                return False
            i += 1

        while j < n:
            if target[j] != '_':
                return False
            j += 1

        return True


def main():
    # Example 1: Output: true
    start = "_L__R__R_"
    target = "L______RR"

    # Example 2: Output: false
    # start = "R_L_"
    # target = "__LR"

    # Example 3: Output: false
    # start = "_R"
    # target = "R_"

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.canChange(start, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
