#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1502-Can-Make-Arithmetic-Progression-From-Sequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-06
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1502 - (Easy) - Can Make Arithmetic Progression From Sequence
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

Description & Requirement:
    A sequence of numbers is called an arithmetic progression if 
    the difference between any two consecutive elements is the same.

    Given an array of numbers arr, return true if the array can be rearranged to 
    form an arithmetic progression. Otherwise, return false.

Example 1:
    Input: arr = [3,5,1]
    Output: true
    Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, 
        between each consecutive elements.
Example 2:
    Input: arr = [1,2,4]
    Output: false
    Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

Constraints:
    2 <= arr.length <= 1000
    -10^6 <= arr[i] <= 10^6
"""


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 2
        # main method: (sorting)
        return self._canMakeArithmeticProgression(arr)

    def _canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        assert isinstance(arr, list) and len(arr) >= 2

        arr.sort()
        for i in range(1, len(arr) - 1):
            if arr[i] * 2 != (arr[i - 1] + arr[i + 1]):
                return False

        return True


def main():
    # Example 1: Output: true
    arr = [3, 5, 1]

    # Example 2: Output: false
    # arr = [1, 2, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canMakeArithmeticProgression(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
