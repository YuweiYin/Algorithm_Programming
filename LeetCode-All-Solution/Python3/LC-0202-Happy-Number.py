#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0202-Happy-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-03
=================================================================="""

import sys
import time
# from typing import List
# import collections

"""
LeetCode - 0202 - (Easy) - Happy Number
https://leetcode.com/problems/happy-number/

Description & Requirement:
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:
        Starting with any positive integer, replace the number by the sum of the squares of its digits.
        Repeat the process until the number equals 1 (where it will stay), 
            or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.

Example 1:
    Input: n = 19
    Output: true
    Explanation:
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1
Example 2:
    Input: n = 2
    Output: false

Constraints:
    1 <= n <= 2^31 - 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        # exception case
        if not isinstance(n, int) or n <= 0:
            return False  # Error input type
        if n == 1:
            return True
        if n == 2:
            return False
        # main method: (simulate the process, either ending with 1 or forming a loop (some number repeated))
        return self._isHappy(n)

    def _isHappy(self, n: int) -> bool:
        """
        Runtime: 32 ms, faster than 90.36% of Python3 online submissions for Happy Number.
        Memory Usage: 13.9 MB, less than 91.00% of Python3 online submissions for Happy Number.
        """
        assert n >= 3

        number_set = set({})

        def __get_new_number(num: int) -> int:
            new_num = 0
            while num > 0:
                new_num += (num % 10) * (num % 10)
                num //= 10
            return int(new_num)

        while n != 1:
            if n not in number_set:
                number_set.add(n)
            else:  # form a loop
                return False
            n = __get_new_number(n)

        return True if n == 1 else False


def main():
    # Example 1: Output: true
    #     Explanation:
    #         1^2 + 9^2 = 82
    #         8^2 + 2^2 = 68
    #         6^2 + 8^2 = 100
    #         1^2 + 0^2 + 0^2 = 1
    n = 19

    # Example 2: Output: false
    # n = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isHappy(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
