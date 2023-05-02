#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0970-Powerful-Integers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-02
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0970 - (Medium) - Powerful Integers
https://leetcode.com/problems/powerful-integers/

Description & Requirement:
    Given three integers x, y, and bound, return a list of all the powerful integers that 
    have a value less than or equal to bound.

    An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

    You may return the answer in any order. In your answer, each value should occur at most once.

Example 1:
    Input: x = 2, y = 3, bound = 10
    Output: [2,3,4,5,7,9,10]
    Explanation:
        2 = 20 + 30
        3 = 21 + 30
        4 = 20 + 31
        5 = 21 + 31
        7 = 22 + 31
        9 = 23 + 30
        10 = 20 + 32
Example 2:
    Input: x = 3, y = 5, bound = 15
    Output: [2,4,6,8,10,14]

Constraints:
    1 <= x, y <= 100
    0 <= bound <= 10^6
"""


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        # exception case
        assert isinstance(x, int) and x >= 1
        assert isinstance(y, int) and y >= 1
        assert isinstance(bound, int) and bound >= 0
        # main method: (enumerate)
        return self._powerfulIntegers(x, y, bound)

    def _powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        assert isinstance(x, int) and x >= 1
        assert isinstance(y, int) and y >= 1
        assert isinstance(bound, int) and bound >= 0

        res = set()
        NUM = 21
        val_1 = 1
        for i in range(NUM):
            val_2 = 1
            for j in range(NUM):
                value = val_1 + val_2
                if value <= bound:
                    res.add(value)
                else:
                    break
                val_2 *= y
            if val_1 > bound:
                break
            val_1 *= x

        return list(res)


def main():
    # Example 1: Output: [2,3,4,5,7,9,10]
    # x = 2
    # y = 3
    # bound = 10

    # Example 2: Output: [2,4,6,8,10,14]
    x = 3
    y = 5
    bound = 15

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.powerfulIntegers(x, y, bound)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
