#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1460-Make-Two-Arrays-Equal-by-Reversing-Sub-arrays.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-24
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1460 - (Easy) - Make Two Arrays Equal by Reversing Sub-arrays
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

Description & Requirement:
    You are given two integer arrays of equal length target and arr. 
    In one step, you can select any non-empty sub-array of arr and reverse it. 
    You are allowed to make any number of steps.

    Return true if you can make arr equal to target or false otherwise.

Example 1:
    Input: target = [1,2,3,4], arr = [2,4,1,3]
    Output: true
    Explanation: You can follow the next steps to convert arr to target:
        1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
        2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
        3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
        There are multiple ways to convert arr to target, this is not the only way to do so.
Example 2:
    Input: target = [7], arr = [7]
    Output: true
    Explanation: arr is equal to target without any reverses.
Example 3:
    Input: target = [3,7,9], arr = [3,7,11]
    Output: false
    Explanation: arr does not have value 9 and it can never be converted to target.

Constraints:
    target.length == arr.length
    1 <= target.length <= 1000
    1 <= target[i] <= 1000
    1 <= arr[i] <= 1000
"""


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # exception case
        assert isinstance(target, list) and isinstance(arr, list) and len(target) == len(arr) >= 1
        for t, a in zip(target, arr):
            assert isinstance(t, int) and isinstance(a, int) and t >= 1 and a >= 1
        # main method: (since we are allowed to make any number of steps,)
        #     return True if target and arr have the same elements. hash dict
        return self._canBeEqual(target, arr)

    def _canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        assert isinstance(target, list) and isinstance(arr, list) and len(target) == len(arr) >= 1

        counter_t = dict({})

        for t in target:
            if t not in counter_t:
                counter_t[t] = 1
            else:
                counter_t[t] += 1

        for a in arr:
            if a not in counter_t:
                return False
            else:
                if counter_t[a] < 1:
                    return False
                else:
                    counter_t[a] -= 1

        return True


def main():
    # Example 1: Output: true
    # target = [1, 2, 3, 4]
    # arr = [2, 4, 1, 3]

    # Example 2: Output: true
    # target = [7]
    # arr = [7]

    # Example 3: Output: false
    target = [3, 7, 9]
    arr = [3, 7, 11]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canBeEqual(target, arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
