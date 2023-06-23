#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2496-Maximum-Value-of-a-String-in-an-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-22
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 2496 - (Easy) - Maximum Value of a String in an Array
https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

Description & Requirement:
    The value of an alphanumeric string can be defined as:
        The numeric representation of the string in base 10, if it comprises of digits only.
        The length of the string, otherwise.

    Given an array strs of alphanumeric strings, return the maximum value of any string in strs.

Example 1:
    Input: strs = ["alic3","bob","3","4","00000"]
    Output: 5
    Explanation: 
        - "alic3" consists of both letters and digits, so its value is its length, i.e. 5.
        - "bob" consists only of letters, so its value is also its length, i.e. 3.
        - "3" consists only of digits, so its value is its numeric equivalent, i.e. 3.
        - "4" also consists only of digits, so its value is 4.
        - "00000" consists only of digits, so its value is 0.
        Hence, the maximum value is 5, of "alic3".
Example 2:
    Input: strs = ["1","01","001","0001"]
    Output: 1
    Explanation: 
        Each string in the array has value 1. Hence, we return 1.

Constraints:
    1 <= strs.length <= 100
    1 <= strs[i].length <= 9
    strs[i] consists of only lowercase English letters and digits.
"""


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        # exception case
        assert isinstance(strs, list) and len(strs) >= 1 and all([isinstance(s, str) and len(s) >= 1 for s in strs])
        # main method: (scan the array)
        return self._maximumValue(strs)

    def _maximumValue(self, strs: List[str]) -> int:
        assert isinstance(strs, list) and len(strs) >= 1 and all([isinstance(s, str) and len(s) >= 1 for s in strs])

        res = 0
        for s in strs:
            is_digits = all(c.isdigit() for c in s)
            res = max(res, int(s) if is_digits else len(s))

        return res


def main():
    # Example 1: Output: 5
    strs = ["alic3", "bob", "3", "4", "00000"]

    # Example 2: Output: 1
    # strs = ["1", "01", "001", "0001"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximumValue(strs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
