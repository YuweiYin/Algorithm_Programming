#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1342-Number-of-Steps-to-Reduce-a-Number-to-Zero.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-31
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 1342 - (Easy) - Number of Steps to Reduce a Number to Zero
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

Description & Requirement:
    Given an integer num, return the number of steps to reduce it to zero.

    In one step, if the current number is even, you have to divide it by 2, 
    otherwise, you have to subtract 1 from it.

Example 1:
    Input: num = 14
    Output: 6
    Explanation: 
        Step 1) 14 is even; divide by 2 and obtain 7. 
        Step 2) 7 is odd; subtract 1 and obtain 6.
        Step 3) 6 is even; divide by 2 and obtain 3. 
        Step 4) 3 is odd; subtract 1 and obtain 2. 
        Step 5) 2 is even; divide by 2 and obtain 1. 
        Step 6) 1 is odd; subtract 1 and obtain 0.
Example 2:
    Input: num = 8
    Output: 4
    Explanation: 
        Step 1) 8 is even; divide by 2 and obtain 4. 
        Step 2) 4 is even; divide by 2 and obtain 2. 
        Step 3) 2 is even; divide by 2 and obtain 1. 
        Step 4) 1 is odd; subtract 1 and obtain 0.
Example 3:
    Input: num = 123
    Output: 12

Constraints:
    0 <= num <= 10^6
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        # exception case
        if not isinstance(num, int) or num <= 0:
            return 0  # Error input type
        # main method: (simulate the process)
        return self._numberOfSteps(num)

    def _numberOfSteps(self, num: int) -> int:
        assert num >= 1

        res = 0  # step counter
        while num > 0:
            if num & (num - 1) == 0:  # num is 2^k, where k >= 0
                res += len(bin(num)) - 2  # bin(num) is string s == "0b100..00", so need len(s) - 2 steps
                break
            if num & 0x01 == 1:  # odd, minus 1
                num -= 1
            else:  # even, divided by 2
                num >>= 1
            res += 1  # count steps

        return res


def main():
    # Example 1: Output: 6
    # num = 14

    # Example 2: Output: 4
    # num = 8

    # Example 3: Output: 12
    # num = 123

    # Example 4: Output: 26
    num = int(1e6)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numberOfSteps(num)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
