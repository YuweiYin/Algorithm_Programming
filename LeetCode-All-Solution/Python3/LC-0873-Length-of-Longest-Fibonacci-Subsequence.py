#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0873-Length-of-Longest-Fibonacci-Subsequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-09
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0873 - (Medium) - Length of Longest Fibonacci Subsequence
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

Description & Requirement:
    A sequence x1, x2, ..., xn is Fibonacci-like if:
        n >= 3
        xi + xi+1 == xi+2 for all i + 2 <= n

    Given a strictly increasing array arr of positive integers forming a sequence, 
    return the length of the longest Fibonacci-like subsequence of arr. 
    If one does not exist, return 0.

    A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, 
    without changing the order of the remaining elements. 
    For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

Example 1:
    Input: arr = [1,2,3,4,5,6,7,8]
    Output: 5
    Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:
    Input: arr = [1,3,7,11,12,14,18]
    Output: 3
    Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].

Constraints:
    3 <= arr.length <= 1000
    1 <= arr[i] < arr[i + 1] <= 10^9
"""


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 3
        # main method: (dynamic programming)
        return self._lenLongestFibSubseq(arr)

    def _lenLongestFibSubseq(self, arr: List[int]) -> int:
        assert isinstance(arr, list) and len(arr) >= 3
        len_arr = len(arr)

        res = 0
        num_to_idx = dict({num: idx for idx, num in enumerate(arr)})

        # dp[m][n] means the max length of fib subseq with the last two numbers arr[m] and arr[n], where m < n
        dp = [[0 for _ in range(len_arr)] for _ in range(len_arr)]

        for i, num in enumerate(arr):
            for j in range(len_arr - 1, -1, -1):
                if (arr[j] << 1) <= num:  # arr[j] is so small that arr[k] + arr[j] (k < j) will not equal arr[i]
                    break
                if num - arr[j] in num_to_idx:  # the difference (arr[i] - arr[j]) exists
                    k = num_to_idx[num - arr[j]]  # get the index
                    dp[j][i] = max(dp[k][j] + 1, 3)
                    res = max(res, dp[j][i])

        return res


def main():
    # Example 1: Output: 5
    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    # Example 2: Output: 3
    # arr = [1, 3, 7, 11, 12, 14, 18]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.lenLongestFibSubseq(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
