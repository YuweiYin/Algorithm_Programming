#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0718-Maximum-Length-of-Repeated-Subarray.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-20
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0718 - (Medium) - Maximum Length of Repeated Subarray
https://leetcode.com/problems/maximum-length-of-repeated-subarray/

Description & Requirement:
    Given two integer arrays nums1 and nums2, 
    return the maximum length of a subarray that appears in both arrays.

Example 1:
    Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
    Output: 3
    Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:
    Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
    Output: 5

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 100
"""


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # exception case
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1
        for num in nums1 + nums2:
            assert isinstance(num, int) and num >= 0
        # main method: (dynamic programming)
        # return self._findLength(nums1, nums2)
        return self._findLengthFast(nums1, nums2)

    def _findLength(self, nums1: List[int], nums2: List[int]) -> int:
        assert isinstance(nums1, list) and len(nums1) >= 1
        assert isinstance(nums2, list) and len(nums2) >= 1

        len_nums1, len_nums2 = len(nums1), len(nums2)
        dp = [[0 for _ in range(len_nums2 + 1)] for _ in range(len_nums1 + 1)]

        res = 0
        for i in range(len_nums1 - 1, -1, -1):
            for j in range(len_nums2 - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if nums1[i] == nums2[j] else 0
                res = max(res, dp[i][j])

        return res

    def _findLengthFast(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Runtime: 327 ms, faster than 95.85% of Python3 online submissions for Maximum Length of Repeated Subarray.
        Memory Usage: 14.1 MB, less than 88.72% of Python3 online submissions for Maximum Length of Repeated Subarray.
        """
        base, mod = 113, int(1e9+9)

        def __check(length: int) -> bool:
            hash1 = 0
            for i in range(length):
                hash1 = (hash1 * base + nums1[i]) % mod
            bucket1 = {hash1}
            mult = pow(base, length - 1, mod)
            for i in range(length, len(nums1)):
                hash1 = ((hash1 - nums1[i - length] * mult) * base + nums1[i]) % mod
                bucket1.add(hash1)

            hash2 = 0
            for i in range(length):
                hash2 = (hash2 * base + nums2[i]) % mod
            if hash2 in bucket1:
                return True
            for i in range(length, len(nums2)):
                hash2 = ((hash2 - nums2[i - length] * mult) * base + nums2[i]) % mod
                if hash2 in bucket1:
                    return True

            return False

        left, right = 0, min(len(nums1), len(nums2))
        res = 0
        while left <= right:
            mid = (left + right) >> 1
            if __check(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res


def main():
    # Example 1: Output: 3
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]

    # Example 2: Output: 5
    # nums1 = [0, 0, 0, 0, 0]
    # nums2 = [0, 0, 0, 0, 0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findLength(nums1, nums2)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
