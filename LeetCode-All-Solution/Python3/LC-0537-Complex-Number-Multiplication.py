#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0537-Complex-Number-Multiplication.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-25
=================================================================="""

import sys
import time
# from typing import List
# import functools

"""
LeetCode - 0537 - (Medium) - Complex Number Multiplication
https://leetcode.com/problems/complex-number-multiplication/

Description & Requirement:
    A complex number can be represented as a string on the form "real + imaginary i" where:
        real is the real part and is an integer in the range [-100, 100].
        imaginary is the imaginary part and is an integer in the range [-100, 100].
        i^2 == -1.

    Given two complex numbers num1 and num2 as strings, 
    return a string of the complex number that represents their multiplications.

Example 1:
    Input: num1 = "1+1i", num2 = "1+1i"
    Output: "0+2i"
    Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
    Input: num1 = "1+-1i", num2 = "1+-1i"
    Output: "0+-2i"
    Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Constraints:
    num1 and num2 are valid complex numbers.
"""


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # exception case
        assert isinstance(num1, str) and len(num1) > 0 and "+" in num1 and "i" in num1
        assert isinstance(num2, str) and len(num2) > 0 and "+" in num2 and "i" in num2
        # main method: (convert str to real number part and imaginary number part, then do multiplication)
        #     the real number of result is (num1_real * num2_real - num1_imaginary * num2_imaginary)
        #     the imaginary number of result is (num1_real * num2_imaginary + num1_imaginary * num2_real)
        return self._complexNumberMultiply(num1, num2)

    def _complexNumberMultiply(self, num1: str, num2: str) -> str:
        # convert str to real number part and imaginary number part
        num1_real, num1_imaginary = num1.split("+")
        num1_real = int(num1_real)
        num1_imaginary = int(num1_imaginary[:-1])  # get rid of "i"

        num2_real, num2_imaginary = num2.split("+")
        num2_real = int(num2_real)
        num2_imaginary = int(num2_imaginary[:-1])  # get rid of "i"

        # do multiplication
        #     the real number of result is (num1_real * num2_real - num1_imaginary * num2_imaginary)
        #     the imaginary number of result is (num1_real * num2_imaginary + num1_imaginary * num2_real)
        res_real = num1_real * num2_real - num1_imaginary * num2_imaginary
        res_imaginary = num1_real * num2_imaginary + num1_imaginary * num2_real

        return str(res_real) + "+" + str(res_imaginary) + "i"


def main():
    # Example 1: Output: "0+2i"
    # num1 = "1+1i"
    # num2 = "1+1i"

    # Example 2: Output: "0+-2i"
    num1 = "1+-1i"
    num2 = "1+-1i"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.complexNumberMultiply(num1, num2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
