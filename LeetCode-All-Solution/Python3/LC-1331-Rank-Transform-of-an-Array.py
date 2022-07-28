#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1331-Rank-Transform-of-an-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-28
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1331 - (Easy) - Rank Transform of an Array
https://leetcode.com/problems/rank-transform-of-an-array/

Description & Requirement:
    Given an array of integers arr, replace each element with its rank.

    The rank represents how large the element is. The rank has the following rules:
        Rank is an integer starting from 1.
        The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
        Rank should be as small as possible.

Example 1:
    Input: arr = [40,10,20,30]
    Output: [4,1,2,3]
    Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
Example 2:
    Input: arr = [100,100,100]
    Output: [1,1,1]
    Explanation: Same elements share the same rank.
Example 3:
    Input: arr = [37,12,28,9,100,56,80,5,12]
    Output: [5,3,4,2,8,6,7,1,3]

Constraints:
    0 <= arr.length <= 10^5
    -10^9 <= arr[i] <= 10^9
"""


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # exception case
        assert isinstance(arr, list)
        if len(arr) == 0:
            return []
        # main method: (sort and map)
        return self._arrayRankTransform(arr)

    def _arrayRankTransform(self, arr: List[int]) -> List[int]:
        assert isinstance(arr, list) and len(arr) >= 1

        arr_sort = sorted(list(set(arr)))
        arr_dict = dict({})
        for idx, num in enumerate(arr_sort):
            arr_dict[num] = idx + 1

        return [arr_dict[num] for num in arr]


def main():
    # Example 1: Output: [4,1,2,3]
    # arr = [40, 10, 20, 30]

    # Example 2: Output: [1,1,1]
    # arr = [100, 100, 100]

    # Example 3: Output: [5,3,4,2,8,6,7,1,3]
    arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.arrayRankTransform(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
