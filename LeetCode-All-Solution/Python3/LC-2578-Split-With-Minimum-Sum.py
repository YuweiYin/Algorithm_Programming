#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2578-Split-With-Minimum-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-10-09
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2578 - (Easy) Split With Minimum Sum
https://leetcode.com/problems/split-with-minimum-sum/

Description & Requirement:
    Given a positive integer num, split it into two non-negative integers num1 and num2 such that:
        - The concatenation of num1 and num2 is a permutation of num.
            - In other words, the sum of the number of occurrences of each digit in num1 and num2 
                is equal to the number of occurrences of that digit in num.
        - num1 and num2 can contain leading zeros.

    Return the minimum possible sum of num1 and num2.

    Notes:
        - It is guaranteed that num does not contain any leading zeros.
        - The order of occurrence of the digits in num1 and num2 may 
            differ from the order of occurrence of num.

Example 1:
    Input: num = 4325
    Output: 59
    Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59. 
        We can prove that 59 is indeed the minimal possible sum.
Example 2:
    Input: num = 687
    Output: 75
    Explanation: We can split 687 so that num1 is 68 and num2 is 7, 
        which would give an optimal sum of 75.

Constraints:
    10 <= num <= 10^9
"""


class Solution:
    def splitNum(self, num: int) -> int:
        # exception case
        assert isinstance(num, int) and num >= 10
        # main method: (greedy)
        return self._splitNum(num)

    def _splitNum(self, num: int) -> int:
        assert isinstance(num, int) and num >= 10

        num_str = "".join(sorted(str(num)))
        return int(num_str[::2]) + int(num_str[1::2])


def main():
    # Example 1: Output: 59
    num = 4325

    # Example 2: Output: 75
    # num = 687

    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.splitNum(num)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
