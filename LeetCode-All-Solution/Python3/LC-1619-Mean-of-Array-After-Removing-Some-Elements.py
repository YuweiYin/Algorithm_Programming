#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1619-Mean-of-Array-After-Removing-Some-Elements.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-14
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1619 - (Easy) - Mean of Array After Removing Some Elements
https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

Description & Requirement:
    Given an integer array arr, 
    return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

    Answers within 10-5 of the actual answer will be considered accepted.

Example 1:
    Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
    Output: 2.00000
    Explanation: After erasing the minimum and the maximum values of this array, 
        all elements are equal to 2, so the mean is 2.
Example 2:
    Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
    Output: 4.00000
Example 3:
    Input: arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
    Output: 4.77778

Constraints:
    20 <= arr.length <= 1000
    arr.length is a multiple of 20.
    0 <= arr[i] <= 10^5
"""


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 20 and len(arr) % 20 == 0
        for num in arr:
            assert isinstance(num, int) and num >= 0
        # main method: (sort)
        return self._trimMean(arr)

    def _trimMean(self, arr: List[int]) -> float:
        assert isinstance(arr, list) and len(arr) >= 20 and len(arr) % 20 == 0

        arr.sort()
        trim_idx = int(len(arr) / 20)

        return float(sum(arr[trim_idx: -trim_idx]) / (len(arr) - (trim_idx << 1)))


def main():
    # Example 1: Output: 2.00000
    # arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]

    # Example 2: Output: 4.00000
    # arr = [6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]

    # Example 3: Output: 4.77778
    arr = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8,
           1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2, 3, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.trimMean(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
