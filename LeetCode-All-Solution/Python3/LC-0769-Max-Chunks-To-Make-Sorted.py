#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0769-Max-Chunks-To-Make-Sorted.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-13
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0769 - (Medium) - Max Chunks To Make Sorted
https://leetcode.com/problems/max-chunks-to-make-sorted/

Description & Requirement:
    You are given an integer array arr of length n that 
    represents a permutation of the integers in the range [0, n - 1].

    We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. 
    After concatenating them, the result should equal the sorted array.

    Return the largest number of chunks we can make to sort the array.

Example 1:
    Input: arr = [4,3,2,1,0]
    Output: 1
    Explanation:
        Splitting into two or more chunks will not return the required result.
        For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:
    Input: arr = [1,0,2,3,4]
    Output: 4
    Explanation:
        We can split into two chunks, such as [1, 0], [2, 3, 4].
        However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

Constraints:
    n == arr.length
    1 <= n <= 10
    0 <= arr[i] < n
    All the elements of arr are unique.
"""


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 1
        n = len(arr)
        for num in arr:
            assert isinstance(num, int) and 0 <= num < n
        # main method
        return self._maxChunksToSorted(arr)

    def _maxChunksToSorted(self, arr: List[int]) -> int:
        assert isinstance(arr, list) and len(arr) >= 1

        res = 0
        cur_max = 0
        for idx, num in enumerate(arr):
            cur_max = max(cur_max, num)
            if cur_max == idx:
                res += 1

        return res


def main():
    # Example 1: Output: 1
    # arr = [4, 3, 2, 1, 0]

    # Example 2: Output: 4
    arr = [1, 0, 2, 3, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxChunksToSorted(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
