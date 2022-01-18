#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0605-Can-Place-Flowers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-18
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0605 - (Easy) - Can Place Flowers
https://leetcode.com/problems/can-place-flowers/

Description & Requirement:
    You have a long flowerbed in which some of the plots are planted, and some are not. 
    However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, 
    where 0 means empty and 1 means not empty, and an integer n, 
    return if n new flowers can be planted in the flowerbed 
    without violating the no-adjacent-flowers rule.

Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true
Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false

Constraints:
    1 <= flowerbed.length <= 2 * 10^4
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # exception case
        if not isinstance(flowerbed, list) or len(flowerbed) <= 0:
            return False  # Error input type
        if n <= 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False
            else:
                return True if n <= 1 else False
        # main method: (rule based scan, find all adjacent plots (0s), and count the max available plots directly)
        return self._canPlaceFlowers(flowerbed, n)

    def _canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        len_flowerbed = len(flowerbed)
        assert len_flowerbed > 0

        # deal with the leftmost adjacent 0s
        # e.g., [0,0,0,1, ...]  get 1 == (3 >> 1) available plots in [0,0,0,1]
        # e.g., [0,0,0,0,1, ...]  get 2 == (4 >> 1) available plots in [0,0,0,0,1]
        first_1_index = 0
        leftmost_adjacent_0 = 0  # the number of leftmost adjacent 0 before the first 1
        while first_1_index < len_flowerbed:  # find the first 1
            if flowerbed[first_1_index] != 1:
                leftmost_adjacent_0 += 1
                first_1_index += 1
            else:
                break

        if first_1_index == len_flowerbed:  # all plots are available
            if len_flowerbed & 0x01 == 1:  # odd number
                return True if ((len_flowerbed >> 1) + 1) >= n else False
            else:  # even number
                return True if (len_flowerbed >> 1) >= n else False

        # deal with the rightmost adjacent 0s
        # e.g., [..., 1,0,0,0]  get 1 == (3 >> 1) available plots in [1,0,0,0]
        # e.g., [..., 0,0,0,0,1]  get 2 == (4 >> 1) available plots in [1,0,0,0,0]
        last_1_index = len_flowerbed - 1
        rightmost_adjacent_0 = 0  # the number of rightmost adjacent 0 after the last 1
        while last_1_index >= 0:  # find the last 1
            if flowerbed[last_1_index] != 1:
                rightmost_adjacent_0 += 1
                last_1_index -= 1
            else:
                break

        if last_1_index == -1:  # all plots are available
            if len_flowerbed & 0x01 == 1:  # odd number
                return True if ((len_flowerbed >> 1) + 1) >= n else False
            else:  # even number
                return True if (len_flowerbed >> 1) >= n else False

        available_plots = (leftmost_adjacent_0 >> 1) + (rightmost_adjacent_0 >> 1)

        # deal with the middle 0s
        # e.g., [..., 1,0,0,0,1, ...]  get 1 == ((3-1) >> 1) available plots in [1,0,0,0,1]
        # e.g., [..., 1,0,0,0,0,1, ...]  get 1 == ((4-1) >> 1) available plots in [1,0,0,0,0,1]
        # e.g., [..., 1,0,0,0,0,0,1, ...]  get 2 == ((5-1) >> 1) available plots in [1,0,0,0,0,0,1]
        cur_start_index = first_1_index + 1
        while cur_start_index < last_1_index:
            cur_end_index = cur_start_index
            while flowerbed[cur_end_index] == 0:
                cur_end_index += 1
            available_plots += max(0, (cur_end_index - cur_start_index - 1) >> 1)
            cur_start_index = cur_end_index + 1

        return True if available_plots >= n else False


def main():
    # Example 1: Output: true
    # flowerbed = [1, 0, 0, 0, 1]
    # n = 1

    # Example 2: Output: false
    # flowerbed = [1, 0, 0, 0, 1]
    # n = 2

    # Example 3: Output: true
    flowerbed = [0]
    n = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canPlaceFlowers(flowerbed, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
