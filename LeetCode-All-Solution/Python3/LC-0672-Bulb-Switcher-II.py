#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0672-Bulb-Switcher-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-15
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 0672 - (Medium) - Bulb Switcher II
https://leetcode.com/problems/bulb-switcher-ii/

Description & Requirement:
    There is a room with n bulbs labeled from 1 to n that all are turned on initially, and four buttons on the wall. 
    Each of the four buttons has a different functionality where:
        Button 1: Flips the status of all the bulbs.
        Button 2: Flips the status of all the bulbs with even labels (i.e., 2, 4, ...).
        Button 3: Flips the status of all the bulbs with odd labels (i.e., 1, 3, ...).
        Button 4: Flips the status of all the bulbs with a label j = 3k + 1 where k = 0, 1, 2, ... 
            (i.e., 1, 4, 7, 10, ...).

    You must make exactly presses button presses in total. 
    For each press, you may pick any of the four buttons to press.

    Given the two integers n and presses, 
    return the number of different possible statuses after performing all presses button presses.

Example 1:
    Input: n = 1, presses = 1
    Output: 2
    Explanation: Status can be:
        - [off] by pressing button 1
        - [on] by pressing button 2
Example 2:
    Input: n = 2, presses = 1
    Output: 3
    Explanation: Status can be:
        - [off, off] by pressing button 1
        - [on, off] by pressing button 2
        - [off, on] by pressing button 3
Example 3:
    Input: n = 3, presses = 1
    Output: 4
    Explanation: Status can be:
        - [off, off, off] by pressing button 1
        - [off, on, off] by pressing button 2
        - [on, off, on] by pressing button 3
        - [off, on, on] by pressing button 4

Constraints:
    1 <= n <= 1000
    0 <= presses <= 1000
"""


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(presses, int) and presses >= 0
        # main method: (find the cycle / rule as follows)
        # the light 6k+1 is controlled by buttons 1, 3, and 4 (k >= 0); and 6k+1 1,3,4 影响；
        # the light 6k+2 and 6k+6 are controlled by buttons 1 and 2 (k >= 0);
        # the light 6k+3 and 6k+5 are controlled by buttons 1 and 3 (k >= 0);
        # the light 6k+4 is controlled by button 1, 2, and 4 (k >= 0).
        return self._flipLights(n, presses)

    def _flipLights(self, n: int, presses: int) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(presses, int) and presses >= 0

        final_status = set()

        for i in range(1 << 4):  # 2 ** 4
            press_bitmap = [(i >> j) & 0x01 for j in range(4)]
            if sum(press_bitmap) % 2 == presses % 2 and sum(press_bitmap) <= presses:
                status = press_bitmap[0] ^ press_bitmap[1] ^ press_bitmap[3]
                if n >= 2:
                    status |= (press_bitmap[0] ^ press_bitmap[1]) << 1
                if n >= 3:
                    status |= (press_bitmap[0] ^ press_bitmap[2]) << 2
                if n >= 4:
                    status |= (press_bitmap[0] ^ press_bitmap[1] ^ press_bitmap[3]) << 3

                final_status.add(status)

        return len(final_status)


def main():
    # Example 1: Output: 2
    # n = 1
    # presses = 1

    # Example 2: Output: 3
    # n = 2
    # presses = 1

    # Example 3: Output: 4
    n = 3
    presses = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.flipLights(n, presses)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
