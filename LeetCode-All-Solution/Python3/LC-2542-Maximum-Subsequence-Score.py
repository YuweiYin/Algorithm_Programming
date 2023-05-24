#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2542-Maximum-Subsequence-Score.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-24
=================================================================="""

import sys
import time
from typing import List
import heapq
# import collections
# import functools

"""
LeetCode - 2542 - (Medium) - Maximum Subsequence Score
https://leetcode.com/problems/maximum-subsequence-score/

Description & Requirement:
    You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and 
    a positive integer k. You must choose a subsequence of indices from nums1 of length k.

    For chosen indices i0, i1, ..., ik - 1, your score is defined as:
        The sum of the selected elements from nums1 multiplied with 
            the minimum of the selected elements from nums2.
        It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0], 
            nums2[i1], ... ,nums2[ik - 1]).

    Return the maximum possible score.

    A subsequence of indices of an array is a set that can be derived from the set 
    {0, 1, ..., n-1} by deleting some or no elements.

Example 1:
    Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
    Output: 12
    Explanation: 
        The four possible subsequence scores are:
        - We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
        - We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
        - We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
        - We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
        Therefore, we return the max score, which is 12.
Example 2:
    Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
    Output: 30
    Explanation: 
        Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.

Constraints:
    n == nums1.length == nums2.length
    1 <= n <= 10^5
    0 <= nums1[i], nums2[j] <= 10^5
    1 <= k <= n
"""


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # exception case
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums1) == len(nums2)
        assert isinstance(k, int) and k >= 1
        # main method: (heap)
        return self._maxScore(nums1, nums2, k)

    def _maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums1) == len(nums2)
        assert isinstance(k, int) and k >= 1

        array = sorted(zip(nums1, nums2), key=lambda p: -p[1])
        heap = [x for x, _ in array[:k]]
        heapq.heapify(heap)
        h_sum = sum(heap)

        res = h_sum * array[k - 1][1]
        for x, y in array[k:]:
            if x > heap[0]:
                h_sum += x - heapq.heapreplace(heap, x)
                res = max(res, h_sum * y)

        return res


def main():
    # Example 1: Output: 12
    # nums1 = [1, 3, 3, 2]
    # nums2 = [2, 1, 3, 4]
    # k = 3

    # Example 2: Output: 30
    nums1 = [4, 2, 3, 1, 1]
    nums2 = [7, 5, 10, 9, 6]
    k = 1

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxScore(nums1, nums2, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
