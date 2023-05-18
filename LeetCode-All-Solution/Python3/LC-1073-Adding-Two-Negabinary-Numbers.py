#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1073-Adding-Two-Negabinary-Numbers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-18
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1073 - (Medium) - Adding Two Negabinary Numbers
https://leetcode.com/problems/adding-two-negabinary-numbers/

Description & Requirement:
    Given two numbers arr1 and arr2 in base -2, 
    return the result of adding them together.

    Each number is given in array format:  as an array of 0s and 1s, 
    from most significant bit to least significant bit. 
    For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3. 
    A number arr in array, format is also guaranteed to have no leading zeros: 
    either arr == [0] or arr[0] == 1.

    Return the result of adding arr1 and arr2 in the same format: 
    as an array of 0s and 1s with no leading zeros.

Example 1:
    Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
    Output: [1,0,0,0,0]
    Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
Example 2:
    Input: arr1 = [0], arr2 = [0]
    Output: [0]
Example 3:
    Input: arr1 = [0], arr2 = [1]
    Output: [1]

Constraints:
    1 <= arr1.length, arr2.length <= 1000
    arr1[i] and arr2[i] are 0 or 1
    arr1 and arr2 have no leading zeros
"""


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # exception case
        assert isinstance(arr1, list) and len(arr1) >= 1
        assert isinstance(arr2, list) and len(arr2) >= 1
        # main method: (simulate the process)
        return self._addNegabinary(arr1, arr2)

    def _addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        assert isinstance(arr1, list) and len(arr1) >= 1
        assert isinstance(arr2, list) and len(arr2) >= 1

        res = []

        carry = 0
        idx1, idx2 = len(arr1) - 1, len(arr2) - 1
        while idx1 >= 0 or idx2 >= 0 or carry:
            digit = carry
            if idx1 >= 0:
                digit += arr1[idx1]
            if idx2 >= 0:
                digit += arr2[idx2]

            if digit >= 2:
                res.append(digit - 2)
                carry = -1
            elif digit >= 0:
                res.append(digit)
                carry = 0
            else:
                res.append(1)
                carry = 1
            idx1 -= 1
            idx2 -= 1

        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return res[::-1]


def main():
    # Example 1: Output: [1,0,0,0,0]
    arr1 = [1, 1, 1, 1, 1]
    arr2 = [1, 0, 1]

    # Example 2: Output: [0]
    # arr1 = [0]
    # arr2 = [0]

    # Example 3: Output: [1]
    # arr1 = [0]
    # arr2 = [1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.addNegabinary(arr1, arr2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
