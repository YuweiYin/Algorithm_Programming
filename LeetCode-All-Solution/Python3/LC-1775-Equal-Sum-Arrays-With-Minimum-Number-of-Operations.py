#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1775-Equal-Sum-Arrays-With-Minimum-Number-of-Operations.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-07
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1775 - (Medium) - Equal Sum Arrays With Minimum Number of Operations
https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

Description & Requirement:
    You are given two arrays of integers nums1 and nums2, possibly of different lengths. 
    The values in the arrays are between 1 and 6, inclusive.

    In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

    Return the minimum number of operations required to make the sum of values in nums1 equal to 
    the sum of values in nums2. Return -1 if it is not possible to make the sum of the two arrays equal.

Example 1:
    Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
    Output: 3
    Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
        - Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
        - Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
        - Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
Example 2:
    Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
    Output: -1
    Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
Example 3:
    Input: nums1 = [6,6], nums2 = [1]
    Output: 3
    Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
        - Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
        - Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
        - Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].

Constraints:
    1 <= nums1.length, nums2.length <= 10^5
    1 <= nums1[i], nums2[i] <= 6
"""


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # exception case
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1
        for num in nums1 + nums2:
            assert isinstance(num, int) and 1 <= num <= 6
        # main method: (greedy & counter)
        return self._minOperations(nums1, nums2)

    def _minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1

        n, m = len(nums1), len(nums2)
        TOTAL = 6
        if TOTAL * n < m or TOTAL * m < n:
            return -1

        cnt1 = [0 for _ in range(TOTAL + 1)]
        cnt2 = [0 for _ in range(TOTAL + 1)]
        diff = 0
        for i in nums1:
            cnt1[i] += 1
            diff += i
        for i in nums2:
            cnt2[i] += 1
            diff -= i

        if diff == 0:
            return 0

        if diff > 0:
            cnt1, cnt2 = cnt2, cnt1
        else:
            diff = -diff
        cnt = [0 for _ in range(TOTAL + 1)]
        for i in range(1, TOTAL + 1):
            cnt[6 - i] += cnt1[i]
            cnt[i - 1] += cnt2[i]

        res = 0
        for i in range(TOTAL - 1, 0, -1):
            if diff <= 0:
                break
            t = min((diff + i - 1) // i, cnt[i])
            res += t
            diff -= t * i

        return res


def main():
    # Example 1: Output: 3
    # nums1 = [1, 2, 3, 4, 5, 6]
    # nums2 = [1, 1, 2, 2, 2, 2]

    # Example 2: Output: -1
    # nums1 = [1, 1, 1, 1, 1, 1, 1]
    # nums2 = [6]

    # Example 3: Output: 3
    nums1 = [6, 6]
    nums2 = [1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minOperations(nums1, nums2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
