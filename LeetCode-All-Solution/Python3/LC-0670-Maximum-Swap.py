#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0670-Maximum-Swap.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-13
=================================================================="""

import sys
import time
# import heapq
# from typing import List
# import collections
# import functools

"""
LeetCode - 0670 - (Medium) - Maximum Swap
https://leetcode.com/problems/maximum-swap/

Description & Requirement:
    You are given an integer num. You can swap two digits at most once to get the maximum valued number.

    Return the maximum valued number you can get.

Example 1:
    Input: num = 2736
    Output: 7236
    Explanation: Swap the number 2 and the number 7.
Example 2:
    Input: num = 9973
    Output: 9973
    Explanation: No swap.

Constraints:
    0 <= num <= 10^8
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        # exception case
        assert isinstance(num, int) and num >= 0
        # main method: (check each digit, 9 is the best choice)
        return self._maximumSwap(num)

    def _maximumSwap(self, num: int) -> int:
        assert isinstance(num, int) and num >= 0

        digit_str = str(num)
        digit_list = [int(digit) for digit in digit_str]
        n = len(digit_list)

        for idx, digit in enumerate(digit_list[:-1]):
            if digit == 9:
                continue
            else:
                cur_max = max(digit_list[idx + 1:])
                if digit >= cur_max:
                    continue
                else:
                    max_idx = n - 1
                    while max_idx > idx:
                        if digit_list[max_idx] == cur_max:
                            break
                        max_idx -= 1
                    digit_list[idx] = cur_max
                    digit_list[max_idx] = digit
                    return int("".join([str(d) for d in digit_list]))

        return num


def main():
    # Example 1: Output: 7236
    num = 2736

    # Example 2: Output: 9973
    # num = 9973

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximumSwap(num)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
