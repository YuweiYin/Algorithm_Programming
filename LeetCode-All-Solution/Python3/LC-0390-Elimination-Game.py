#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0390-Elimination-Game.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-04
=================================================================="""

import sys
import time
# from typing import List

"""
LeetCode - 0390 - (Medium) - Elimination Game
https://leetcode.com/problems/elimination-game/

Description:
    You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. 
    Apply the following algorithm on arr:

    Starting from left to right, remove the first number and every other number afterward 
    until you reach the end of the list.
    Repeat the previous step again, but this time from right to left, 
    remove the rightmost number and every other number from the remaining numbers.
    Keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Requirement:
    Given the integer n, return the last number that remains in arr.

Example 1:
    Input: n = 9
    Output: 6
    Explanation:
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        arr = [2, 4, 6, 8]
        arr = [2, 6]
        arr = [6]
Example 2:
    Input: n = 1
    Output: 1

Constraints:
    1 <= n <= 10^9
"""


class Solution:
    def lastRemaining(self, n: int) -> int:
        # exception case
        if n <= 0:
            return 0
        # border case
        if n == 1:
            return 1
        # main method: (delete either odd or even index at a time until only one number remain)
        return self._lastRemaining(n)

    def _lastRemaining(self, n: int) -> int:
        # cur_list = [num for num in range(1, n + 1)]  # extremely slow than range (iterator)
        cur_list = range(1, n + 1)
        if_left_to_right = True
        del_index_gap = 2
        while len(cur_list) > 1:
            len_cur_list = len(cur_list)
            if if_left_to_right:  # left to right, the start index must be 0 -> even -> remove all even
                # only remain odd index (remove cur_list[0], cur_list[2], cur_list[4], ...)
                # new_list = [cur_list[index] for index in range(len_cur_list) if (index & 0x01)]
                new_list = cur_list[1: len_cur_list: del_index_gap]
            else:  # right to left, the start index is odd number if the len_cur_list is even, so remain all even index
                if len_cur_list & 0x01:  # if len_cur_list is odd, then only remain odd index
                    # new_list = [cur_list[index] for index in range(len_cur_list) if (index & 0x01)]
                    new_list = cur_list[1: len_cur_list: del_index_gap]
                else:  # if len_cur_list is even, then only remain odd index
                    # new_list = [cur_list[index] for index in range(len_cur_list) if not (index & 0x01)]
                    new_list = cur_list[0: len_cur_list: del_index_gap]
            cur_list = new_list
            if_left_to_right = not if_left_to_right
        # assert len(cur_list) == 1
        return cur_list[0]


def main():
    # Example 1:  Output: 6
    # n = 9

    # Example 2: Output: 1
    # n = 1

    # Example 3: Output: 32896342
    n = 100000000

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.lastRemaining(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
