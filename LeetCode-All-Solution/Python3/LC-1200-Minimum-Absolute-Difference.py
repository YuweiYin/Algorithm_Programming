#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1200-Minimum-Absolute-Difference.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-04
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1200 - (Easy) - Minimum Absolute Difference
https://leetcode.com/problems/minimum-absolute-difference/

Description & Requirement:
    Given an array of distinct integers arr, 
    find all pairs of elements with the minimum absolute difference of any two elements.

    Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
        a, b are from arr
        a < b
        b - a equals to the minimum absolute difference of any two elements in arr

Example 1:
    Input: arr = [4,2,1,3]
    Output: [[1,2],[2,3],[3,4]]
    Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:
    Input: arr = [1,3,6,10,15]
    Output: [[1,3]]
Example 3:
    Input: arr = [3,8,-10,23,19,-4,-14,27]
    Output: [[-14,-10],[19,23],[23,27]]

Constraints:
    2 <= arr.length <= 10^5
    -10^6 <= arr[i] <= 10^6
"""


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 2
        # main method: (sort and find pairs with the minimum distance)
        return self._minimumAbsDifference(arr)

    def _minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        assert isinstance(arr, list) and len(arr) >= 2

        arr.sort()

        # get the minimum distance
        min_dist = arr[1] - arr[0]
        for idx in range(2, len(arr)):
            cur_dist = arr[idx] - arr[idx - 1]
            min_dist = min(min_dist, cur_dist)

        # find pairs with the minimum distance
        res = []
        for idx in range(1, len(arr)):
            if arr[idx] - arr[idx - 1] == min_dist:
                res.append([arr[idx - 1], arr[idx]])

        return res


def main():
    # Example 1: Output: [[1,2],[2,3],[3,4]]
    # arr = [4, 2, 1, 3]

    # Example 2: Output: [[1,3]]
    # arr = [1, 3, 6, 10, 15]

    # Example 3: Output: [[-14,-10],[19,23],[23,27]]
    arr = [3, 8, -10, 23, 19, -4, -14, 27]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumAbsDifference(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
