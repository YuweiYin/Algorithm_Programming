#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1186-Maximum-Subarray-Sum-with-One-Deletion.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-27
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 1186 - (Medium) - Maximum Subarray Sum with One Deletion
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

Description & Requirement:
    Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) 
    with at most one element deletion. In other words, you want to choose a subarray and 
    optionally delete one element from it so that there is still at least one element left 
    and the sum of the remaining elements is maximum possible.

    Note that the subarray needs to be non-empty after deleting one element.

Example 1:
    Input: arr = [1,-2,0,3]
    Output: 4
    Explanation: Because we can choose [1, -2, 0, 3] and drop -2, 
        thus the subarray [1, 0, 3] becomes the maximum value.
Example 2:
    Input: arr = [1,-2,-2,3]
    Output: 3
    Explanation: We just choose [3] and it's the maximum sum.
Example 3:
    Input: arr = [-1,-1,-1,-1]
    Output: -1
    Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, 
        then get an empty subarray to make the sum equals to 0.

Constraints:
    1 <= arr.length <= 10^5
    -10^4 <= arr[i] <= 10^4
"""


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # exception case
        assert isinstance(arr, list) and len(arr) >= 1
        # main method: (dynamic programming)
        return self._maximumSum(arr)

    def _maximumSum(self, arr: List[int]) -> int:
        assert isinstance(arr, list) and len(arr) >= 1

        dp0, dp1, res = arr[0], 0, arr[0]
        for i in range(1, len(arr)):
            dp1 = max(dp0, dp1 + arr[i])
            dp0 = max(dp0, 0) + arr[i]
            res = max(res, max(dp0, dp1))

        return res


def main():
    # Example 1: Output: 4
    # arr = [1, -2, 0, 3]

    # Example 2: Output: 3
    # arr = [1, -2, -2, 3]

    # Example 3: Output: -1
    arr = [-1, -1, -1, -1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximumSum(arr)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
