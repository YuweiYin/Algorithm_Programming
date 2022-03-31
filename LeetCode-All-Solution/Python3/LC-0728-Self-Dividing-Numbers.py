#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0728-Self-Dividing-Numbers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-31
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0728 - (Easy) - Self Dividing Numbers
https://leetcode.com/problems/self-dividing-numbers/

Description & Requirement:
    A self-dividing number is a number that is divisible by every digit it contains.

    For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
    A self-dividing number is not allowed to contain the digit zero.

    Given two integers left and right, 
    return a list of all the self-dividing numbers in the range [left, right].

Example 1:
    Input: left = 1, right = 22
    Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
Example 2:
    Input: left = 47, right = 85
    Output: [48,55,66,77]

Constraints:
    1 <= left <= right <= 10^4
"""


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # exception case
        assert isinstance(left, int) and isinstance(right, int) and 1 <= left <= right
        # main method: (test every number in the given interval)
        return self._selfDividingNumbers(left, right)

    def _selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def __check(num: int) -> bool:
            num_origin = num
            while num > 0:
                cur_digit = num % 10
                if cur_digit == 0:
                    return False
                if num_origin % cur_digit != 0:
                    return False
                num //= 10
            return True

        return [number for number in range(left, right + 1) if __check(number)]


def main():
    # Example 1: Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
    left = 1
    right = 22

    # Example 2: Output: [48,55,66,77]
    # left = 47
    # right = 85

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.selfDividingNumbers(left, right)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
