#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0415-Add-Strings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-16
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0415 - (Easy) - Add Strings
https://leetcode.com/problems/add-strings/

Description & Requirement:
    Given two non-negative integers, num1 and num2 represented as string, 
    return the sum of num1 and num2 as a string.

    You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
    You must also not convert the inputs to integers directly.

Example 1:
    Input: num1 = "11", num2 = "123"
    Output: "134"
Example 2:
    Input: num1 = "456", num2 = "77"
    Output: "533"
Example 3:
    Input: num1 = "0", num2 = "0"
    Output: "0"

Constraints:
    1 <= num1.length, num2.length <= 10^4
    num1 and num2 consist of only digits.
    num1 and num2 don't have any leading zeros except for the zero itself.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # exception case
        assert isinstance(num1, str) and len(num1) > 0
        assert isinstance(num2, str) and len(num2) > 0
        # main method: (convert integers and add them)
        return self._addStrings(num1, num2)

    def _addStrings(self, num1: str, num2: str) -> str:
        # get rid of all leading 0s
        # non_zero_idx = 0
        # while non_zero_idx < len(num1) and num1[non_zero_idx] == "0":
        #     non_zero_idx += 1
        # if non_zero_idx == len(num1):  # now num1 is 0
        #     return num2
        # num1 = num1[non_zero_idx:]

        # non_zero_idx = 0
        # while non_zero_idx < len(num2) and num2[non_zero_idx] == "0":
        #     non_zero_idx += 1
        # if non_zero_idx == len(num2):  # now num2 is 0
        #     return num1
        # num2 = num2[non_zero_idx:]

        # make sure num1 is longer
        # if len(num1) < len(num2):
        #     num1, num2 = num2, num1

        # convert num_str to num_int
        num_int_1 = 0
        num_int_2 = 0

        str_to_int = dict({
            "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
        })

        base = 1
        for ch_idx in reversed(range(len(num1))):
            if num1[ch_idx] in str_to_int:
                num_int_1 += str_to_int[num1[ch_idx]] * base
                base *= 10

        base = 1
        for ch_idx in reversed(range(len(num2))):
            if num2[ch_idx] in str_to_int:
                num_int_2 += str_to_int[num2[ch_idx]] * base
                base *= 10

        return str(num_int_1 + num_int_2)


def main():
    # Example 1: Output: "134"
    # num1 = "11"
    # num2 = "123"

    # Example 2: Output: "533"
    # num1 = "456"
    # num2 = "77"

    # Example 3: Output: "0"
    num1 = "0"
    num2 = "0"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.addStrings(num1, num2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
