#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0067-Add-Binary.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-10
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0067 - (Easy) - Add Binary
https://leetcode.com/problems/add-binary/

Description & Requirement:
    Given two binary strings a and b, return their sum as a binary string.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"
Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

Constraints:
    1 <= a.length, b.length <= 10^4
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # exception case
        if not isinstance(a, str) or len(a) <= 0 or ("1" not in a):
            return b
        if not isinstance(b, str) or len(b) <= 0 or ("1" not in b):
            return a
        # main method: (1. built-in function: int, bin. 2. simulate binary addition process)
        # return self._addBinaryBuiltin(a, b)
        return self._addBinarySimulate(a, b)

    def _addBinaryBuiltin(self, a: str, b: str) -> str:
        # test1 = int("0b" + a, 2)
        # test2 = int("0b" + b, 2)
        return bin(int(a, 2) + int(b, 2))[2:]  # get rid of "0b" from the result string

    def _addBinarySimulate(self, a: str, b: str) -> str:
        res_str = ""
        if len(a) < len(b):  # make sure len(a) >= len(b)
            temp = a
            a = b
            b = temp
        len_gap = len(a) - len(b)
        cur_bit_index = len(b) - 1
        extra_bit = "0"
        while cur_bit_index >= 0:  # from the lowest bit to the highest bit
            cur_bit_a = a[cur_bit_index + len_gap]
            cur_bit_b = b[cur_bit_index]
            # consider: cur_bit_a + cur_bit_b + extra_bit
            if cur_bit_a == "0":
                if extra_bit == "0":  # 0 + cur_bit_b + 0
                    res_str = cur_bit_b + res_str
                else:
                    if cur_bit_b == "1":  # 0 + 1 + 1
                        res_str = "0" + res_str
                    else:  # 0 + 0 + 1
                        res_str = "1" + res_str
                        extra_bit = "0"
            elif cur_bit_a == "1":
                if extra_bit == "1" and cur_bit_b == "1":  # 1 + 1 + 1
                    res_str = "1" + res_str
                elif extra_bit == "0" and cur_bit_b == "1":  # 1 + 1 + 0
                    res_str = "0" + res_str
                    extra_bit = "1"
                elif extra_bit == "1" and cur_bit_b == "0":  # 1 + 0 + 1
                    res_str = "0" + res_str
                else:   # 1 + 0 + 0
                    res_str = "1" + res_str
            else:
                pass  # error cur_bit_a
            cur_bit_index -= 1

        cur_a_index = len_gap - 1
        while cur_a_index >= 0 and extra_bit == "1":  # deal with the rest a
            cur_bit_a = a[cur_a_index]
            # consider: cur_bit_a + extra_bit
            if cur_bit_a == "1":
                res_str = "0" + res_str  # extra_bit is still 1
            else:  # cur_bit_a == "0"
                res_str = a[: cur_a_index] + "1" + res_str
                return res_str
            cur_a_index -= 1

        if cur_a_index >= 0:
            res_str = a[: (cur_a_index + 1)] + res_str
            return res_str

        if extra_bit == "1":  # both a and b are used up, extra_bit is still 1
            res_str = "1" + res_str

        return res_str


def main():
    # Example 1: Output: "100"
    # a = "11"
    # b = "1"

    # Example 2: Output: "10101"
    # a = "1010"
    # b = "1011"

    # Example 2: Output: "110001"
    a = "101111"
    b = "10"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.addBinary(a, b)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
