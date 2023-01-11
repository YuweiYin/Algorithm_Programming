#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2283-Check-if-Number-Has-Equal-Digit-Count-and-Digit-Value.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-11
=================================================================="""

import sys
import time
import collections
# from typing import List
# import functools

"""
LeetCode - 2283 - (Easy) - Check if Number Has Equal Digit Count and Digit Value
https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

Description & Requirement:
    You are given a 0-indexed string num of length n consisting of digits.

    Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, 
    otherwise return false.

Example 1:
    Input: num = "1210"
    Output: true
    Explanation:
        num[0] = '1'. The digit 0 occurs once in num.
        num[1] = '2'. The digit 1 occurs twice in num.
        num[2] = '1'. The digit 2 occurs once in num.
        num[3] = '0'. The digit 3 occurs zero times in num.
        The condition holds true for every index in "1210", so return true.
Example 2:
    Input: num = "030"
    Output: false
    Explanation:
        num[0] = '0'. The digit 0 should occur zero times, but actually occurs twice in num.
        num[1] = '3'. The digit 1 should occur three times, but actually occurs zero times in num.
        num[2] = '0'. The digit 2 occurs zero times in num.
        The indices 0 and 1 both violate the condition, so return false.

Constraints:
    n == num.length
    1 <= n <= 10
    num consists of digits.
"""


class Solution:
    def digitCount(self, num: str) -> bool:
        # exception case
        assert isinstance(num, str) and len(num) >= 1
        # main method: (hash counter)
        return self._digitCount(num)

    def _digitCount(self, num: str) -> bool:
        assert isinstance(num, str) and len(num) >= 1

        cnt = collections.Counter(num)
        for idx, digit in enumerate(num):
            if cnt[str(idx)] != int(digit):
                return False

        return True


def main():
    # Example 1: Output: true
    num = "1210"

    # Example 2: Output: false
    # num = "030"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.digitCount(num)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
