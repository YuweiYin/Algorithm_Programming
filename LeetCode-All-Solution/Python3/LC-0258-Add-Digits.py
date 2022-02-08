#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0258-Add-Digits.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-08
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0258 - (Easy) - Add Digits
https://leetcode.com/problems/add-digits/

Description & Requirement:
    Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
    Input: num = 38
    Output: 2
    Explanation: The process is
        38 --> 3 + 8 --> 11
        11 --> 1 + 1 --> 2 
        Since 2 has only one digit, return it.
Example 2:
    Input: num = 0
    Output: 0

Constraints:
    0 <= num <= 2^31 - 1

Follow up:
    Could you do it without any loop/recursion in O(1) runtime?
"""


class Solution:
    def addDigits(self, num: int) -> int:
        # exception case
        assert isinstance(num, int) and num >= 0
        # main method: (Mathematics trick)
        #     for example, cur_num = 1000a + 100b + 10c + d, then next_num = a + b + c + d
        #     cur_num - next_num = 999a + 99b + 9c, obviously, the diff will always be 9k, where integer k >= 1
        #     which means each step, the cur_num will remove 9k and the residual is next_num
        #     so the final result is (num % 9) if num > 9 else num
        return self._addDigits(num)

    def _addDigits(self, num: int) -> int:

        if num > 9:  # if num <= 9, needn't change
            num %= 9  # O(1) math method
            if num == 0:  # num // 9 == 0, so the final result is 9
                num = 9

        return num


def main():
    # Example 1: Output: 2
    num = 38

    # Example 2: Output: 0
    # num = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.addDigits(num)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
