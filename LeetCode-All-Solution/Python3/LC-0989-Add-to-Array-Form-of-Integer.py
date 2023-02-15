#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0989-Add-to-Array-Form-of-Integer.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-15
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0989 - (Easy) - Add to Array-Form of Integer
https://leetcode.com/problems/add-to-array-form-of-integer/

Description & Requirement:
    The array-form of an integer num is an array representing its digits in left to right order.

        For example, for num = 1321, the array form is [1,3,2,1].

    Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

Example 1:
    Input: num = [1,2,0,0], k = 34
    Output: [1,2,3,4]
    Explanation: 1200 + 34 = 1234
Example 2:
    Input: num = [2,7,4], k = 181
    Output: [4,5,5]
    Explanation: 274 + 181 = 455
Example 3:
    Input: num = [2,1,5], k = 806
    Output: [1,0,2,1]
    Explanation: 215 + 806 = 1021

Constraints:
    1 <= num.length <= 10^4
    0 <= num[i] <= 9
    num does not contain any leading zeros except for the zero itself.
    1 <= k <= 10^4
"""


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # exception case
        assert isinstance(num, list) and len(num) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (simulate the process)
        return self._addToArrayForm(num, k)

    def _addToArrayForm(self, num: List[int], k: int) -> List[int]:
        assert isinstance(num, list) and len(num) >= 1
        assert isinstance(k, int) and k >= 1

        array = "".join([str(n) for n in num])
        res = [int(i) for i in str(int(array) + k)]

        return res


def main():
    # Example 1: Output: [1,2,3,4]
    # num = [1, 2, 0, 0]
    # k = 34

    # Example 2: Output: [4,5,5]
    # num = [2, 7, 4]
    # k = 181

    # Example 3: Output: [1,0,2,1]
    num = [2, 1, 5]
    k = 806

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.addToArrayForm(num, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
