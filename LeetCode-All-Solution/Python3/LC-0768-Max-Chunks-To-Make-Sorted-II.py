#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0768-Max-Chunks-To-Make-Sorted-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-13
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0768 - (Hard) - Max Chunks To Make Sorted II
https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

Description & Requirement:
    You are given an integer array arr.

    We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. 
    After concatenating them, the result should equal the sorted array.

    Return the largest number of chunks we can make to sort the array.

Example 1:
    Input: arr = [5,4,3,2,1]
    Output: 1
    Explanation:
        Splitting into two or more chunks will not return the required result.
        For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
Example 2:
    Input: arr = [2,1,3,4,4]
    Output: 4
    Explanation:
        We can split into two chunks, such as [2, 1], [3, 4, 4].
        However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.

Constraints:
    1 <= arr.length <= 2000
    0 <= arr[i] <= 10^8
"""


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 1
        for num in arr:
            assert isinstance(num, int) and num >= 0
        # main method: (monotonous stack)
        return self._maxChunksToSorted(arr)

    def _maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Runtime: 85 ms, faster than 88.01% of Python3 online submissions for Max Chunks To Make Sorted II.
        Memory Usage: 14.1 MB, less than 76.66% of Python3 online submissions for Max Chunks To Make Sorted II.
        """
        assert isinstance(arr, list) and len(arr) >= 1

        stack = []
        for num in arr:
            if len(stack) == 0 or num >= stack[-1]:  # append if empty or non-decreasing
                stack.append(num)
            else:
                cur_max = stack.pop()
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(cur_max)

        return len(stack)


def main():
    # Example 1: Output: 1
    # arr = [5, 4, 3, 2, 1]

    # Example 2: Output: 4
    arr = [2, 1, 3, 4, 4]

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
