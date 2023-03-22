#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2469-Convert-the-Temperature.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-21
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2469 - (Easy) - Convert the Temperature
https://leetcode.com/problems/convert-the-temperature/

Description & Requirement:
    You are given a non-negative floating point number rounded to two decimal places celsius, 
    that denotes the temperature in Celsius.

    You should convert Celsius into Kelvin and Fahrenheit and 
    return it as an array ans = [kelvin, fahrenheit].

    Return the array ans. Answers within 10^{-5} of the actual answer will be accepted.

    Note that:
        Kelvin = Celsius + 273.15
        Fahrenheit = Celsius * 1.80 + 32.00

Example 1:
    Input: celsius = 36.50
    Output: [309.65000,97.70000]
    Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.
Example 2:
    Input: celsius = 122.11
    Output: [395.26000,251.79800]
    Explanation: Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.

Constraints:
    0 <= celsius <= 1000
"""


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # exception case
        assert isinstance(celsius, float) and celsius >= 0.0
        # main method: (use the math equation)
        return self._convertTemperature(celsius)

    def _convertTemperature(self, celsius: float) -> List[float]:
        assert isinstance(celsius, float) and celsius >= 0.0

        return [celsius + 273.15, celsius * 1.80 + 32.00]


def main():
    # Example 1: Output: [309.65000,97.70000]
    celsius = 36.50

    # Example 2: Output: [395.26000,251.79800]
    # celsius = 122.11

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.convertTemperature(celsius)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
