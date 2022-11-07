#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1323-Maximum-69-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-11-07
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1323 - (Easy) - Maximum 69 Number
https://leetcode.com/problems/maximum-69-number/

Description & Requirement:
    You are given a positive integer num consisting only of digits 6 and 9.

    Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:
    Input: num = 9669
    Output: 9969
    Explanation: 
        Changing the first digit results in 6669.
        Changing the second digit results in 9969.
        Changing the third digit results in 9699.
        Changing the fourth digit results in 9666.
        The maximum number is 9969.
Example 2:
    Input: num = 9996
    Output: 9999
    Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:
    Input: num = 9999
    Output: 9999
    Explanation: It is better not to apply any change.

Constraints:
    1 <= num <= 10^4
    num consists of only 6 and 9 digits.
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        # exception case
        assert isinstance(num, int) and num >= 1
        # main method: (just change the first "6" to "9", if there is any "6")
        return self._maximum69Number(num)

    def _maximum69Number(self, num: int) -> int:
        assert isinstance(num, int) and num >= 1

        num = str(num)
        num_str_max = ""
        has_change = False
        for digit in num:
            if digit == "6":
                if not has_change:
                    num_str_max += "9"
                    has_change = True
                else:
                    num_str_max += digit
            else:
                num_str_max += digit

        return int(num_str_max)


def main():
    # Example 1: Output: 9969
    # num = 9669

    # Example 2: Output: 9999
    # num = 9996

    # Example 3: Output: 9999
    num = 9999

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximum69Number(num)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
