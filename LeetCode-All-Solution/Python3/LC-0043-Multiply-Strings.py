#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0043-Multiply-Strings.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-18
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0043 - (Medium) - Multiply Strings
https://leetcode.com/problems/multiply-strings/

Description & Requirement:
    Given two non-negative integers num1 and num2 represented as strings, 
    return the product of num1 and num2, also represented as a string.

    Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"
Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"

Constraints:
    1 <= num1.length, num2.length <= 200
    num1 and num2 consist of digits only.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # exception case
        assert isinstance(num1, str) and len(num1) > 0
        assert isinstance(num2, str) and len(num2) > 0
        # main method: (simulate)
        # other method: NTT: Number Theoretic Transform
        #     similar to FFT, NTT can be used to accelerate polynomial multiplication
        #     NTT has the advantage of using modulus
        #     common moduli (primitive root is 3) are 469762049, 998244353, 1004535809
        #     998244353 = ((7 * 17) << 23) + 1
        #     998244353 = 0b111011100000000000000000000001
        #     998244353 = 3943^2 + 31348^2
        #     998244353^2 = 247210328^2 + 967149855^2
        return self._multiply(num1, num2)

    def _multiply(self, num1: str, num2: str) -> str:
        # border case
        if len(num1) == 0 or len(num2) == 0:
            return "0"
        if num1 == "0" or num2 == "0":
            return "0"
        if num1 == "1":
            return num2
        if num2 == "1":
            return num1

        # make sure num1 is larger than num2
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        if len(num1) == len(num2) and num1 < num2:
            num1, num2 = num2, num1

        # reverse string
        num1 = num1[::-1]
        num2 = num2[::-1]

        def __multiply_two_string_number(s_num1: str, s_num2: str) -> str:
            _ans = ""
            _product = 0
            _carry = 0

            # assert len(s_num2) == 1
            int_num2 = int(s_num2)

            for idx in range(len(s_num1)):
                _product = int(s_num1[idx]) * int_num2 + _carry
                if _product >= 10:
                    _carry = int(_product / 10)
                    _product %= 10
                else:
                    _carry = 0

                _ans += str(_product)

            if _carry > 0:
                _ans += str(_carry)

            return _ans

        def __add_two_string_number(s_num1: str, s_num2: str) -> str:
            _ans = ""
            _sum = 0
            _carry = 0

            if len(s_num1) < len(s_num2):
                s_num1, s_num2 = s_num2, s_num1
            if len(s_num2) < len(s_num1):
                s_num2 += "".join(["0" for _ in range(len(s_num1) - len(s_num2))])

            for idx in range(len(s_num1)):
                _sum = int(s_num1[idx]) + int(s_num2[idx]) + _carry
                if _sum >= 10:
                    _carry = 1
                    _sum -= 10
                else:
                    _carry = 0

                _ans += str(_sum)

            if _carry > 0:
                _ans += str(_carry)

            return _ans

        res = "0"
        base = ""
        for i in range(len(num2)):
            cur_product = __multiply_two_string_number(num1, num2[i])
            cur_product = base + cur_product
            res = __add_two_string_number(res, cur_product)
            base += "0"

        res = res[::-1]
        return res


def main():
    # Example 1: Output: "6"
    # num1 = "2"
    # num2 = "3"

    # Example 2: Output: "56088"
    # num1 = "123"
    # num2 = "456"

    # Example 3: Output: "998001"
    num1 = "999"
    num2 = "999"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.multiply(num1, num2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
