#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1574-Shortest-Subarray-to-be-Removed-to-Make-Array-Sorted.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-25
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1574 - (Medium) - Shortest Subarray to be Removed to Make Array Sorted
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

Description & Requirement:
    Given an integer array arr, remove a subarray (can be empty) from arr such that 
    the remaining elements in arr are non-decreasing.

    Return the length of the shortest subarray to remove.

    A subarray is a contiguous subsequence of the array.

Example 1:
    Input: arr = [1,2,3,10,4,2,3,5]
    Output: 3
    Explanation: The shortest subarray we can remove is [10,4,2] of length 3. 
        The remaining elements after that will be [1,2,3,3,5] which are sorted.
        Another correct solution is to remove the subarray [3,10,4].
Example 2:
    Input: arr = [5,4,3,2,1]
    Output: 4
    Explanation: Since the array is strictly decreasing, we can only keep a single element. 
        Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:
    Input: arr = [1,2,3]
    Output: 0
    Explanation: The array is already non-decreasing. We do not need to remove any elements.

Constraints:
    1 <= arr.length <= 10^5
    0 <= arr[i] <= 10^9
"""


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 1
        # main method: (two pointers)
        return self._findLengthOfShortestSubarray(arr)

    def _findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        assert isinstance(arr, list) and len(arr) >= 1

        n = len(arr)
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        if right == 0:
            return 0

        res = right
        for left in range(n):
            while right < n and arr[right] < arr[left]:
                right += 1
            res = min(res, right - left - 1)
            if left + 1 < n and arr[left] > arr[left + 1]:
                break

        return res


def main():
    # Example 1: Output: 3
    arr = [1, 2, 3, 10, 4, 2, 3, 5]

    # Example 2: Output: 4
    # arr = [5, 4, 3, 2, 1]

    # Example 3: Output: 0
    # arr = [1, 2, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findLengthOfShortestSubarray(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
