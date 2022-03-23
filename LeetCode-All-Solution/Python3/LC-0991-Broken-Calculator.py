#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0991-Broken-Calculator.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-23
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0991 - (Medium) - Broken Calculator
https://leetcode.com/problems/broken-calculator/

Description & Requirement:
    There is a broken calculator that has the integer startValue on its display initially. 
    In one operation, you can:
        multiply the number on display by 2, or
        subtract 1 from the number on display.

    Given two integers startValue and target, 
    return the minimum number of operations needed to display target on the calculator.

Example 1:
    Input: startValue = 2, target = 3
    Output: 2
    Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
Example 2:
    Input: startValue = 5, target = 8
    Output: 2
    Explanation: Use decrement and then double {5 -> 4 -> 8}.
Example 3:
    Input: startValue = 3, target = 10
    Output: 3
    Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.

Constraints:
    1 <= x, y <= 10^9
"""


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # exception case
        assert isinstance(startValue, int) and startValue > 0
        assert isinstance(target, int) and target > 0
        # main method: (greedy)
        return self._brokenCalc(startValue, target)

    def _brokenCalc(self, startValue: int, target: int) -> int:
        if startValue >= target:  # can only minus 1
            return startValue - target

        # always divide target by 2, if odd, plus 1, till target <= startValue
        step_counter = 0
        while target > startValue:
            if target & 0x01 == 1:
                target += 1
            else:
                target >>= 1
            step_counter += 1

        # now target <= startValue, can only perform addition
        return step_counter + startValue - target


def main():
    # Example 1: Output: 2
    # startValue = 2
    # target = 3

    # Example 2: Output: 2
    # startValue = 5
    # target = 8

    # Example 3: Output: 3
    startValue = 3
    target = 10

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.brokenCalc(startValue, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
