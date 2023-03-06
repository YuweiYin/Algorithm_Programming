#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1539-Kth-Missing-Positive-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-06
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1539 - (Easy) - Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number/

Description & Requirement:
    Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

    Return the kth positive integer that is missing from this array.

Example 1:
    Input: arr = [2,3,4,7,11], k = 5
    Output: 9
    Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:
    Input: arr = [1,2,3,4], k = 2
    Output: 6
    Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Constraints:
    1 <= arr.length <= 1000
    1 <= arr[i] <= 1000
    1 <= k <= 1000
    arr[i] < arr[j] for 1 <= i < j <= arr.length

Follow up:
    Could you solve this problem in less than O(n) complexity?
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (binary search)
        return self._findKthPositive(arr, k)

    def _findKthPositive(self, arr: List[int], k: int) -> int:
        assert isinstance(arr, list) and len(arr) >= 1
        assert isinstance(k, int) and k >= 1

        if arr[0] > k:
            return k

        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) >> 1
            num = arr[mid] if mid < len(arr) else int(1e9+7)
            if num - mid - 1 >= k:
                right = mid
            else:
                left = mid + 1

        return k - (arr[left - 1] - (left - 1) - 1) + arr[left - 1]


def main():
    # Example 1: Output: 9
    arr = [2, 3, 4, 7, 11]
    k = 5

    # Example 2: Output: 6
    # arr = [1, 2, 3, 4]
    # k = 2

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.findKthPositive(arr, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
