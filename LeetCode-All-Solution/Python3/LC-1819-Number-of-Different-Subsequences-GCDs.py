#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1819-Number-of-Different-Subsequences-GCDs.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-14
=================================================================="""

import sys
import time
import math
from typing import List
# import collections
# import functools

"""
LeetCode - 1819 - (Hard) - Number of Different Subsequences GCDs
https://leetcode.com/problems/number-of-different-subsequences-gcds/

Description & Requirement:
    You are given an array nums that consists of positive integers.

    The GCD of a sequence of numbers is defined as the greatest integer that divides all the numbers in the sequence evenly.
        For example, the GCD of the sequence [4,6,16] is 2.

    A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.
        For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].

    Return the number of different GCDs among all non-empty subsequences of nums.

Example 1:
    Input: nums = [6,10,3]
    Output: 5
    Explanation: The figure shows all the non-empty subsequences and their GCDs.
        The different GCDs are 6, 10, 3, 2, and 1.
Example 2:
    Input: nums = [5,15,40,5,6]
    Output: 7

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 2 * 10^5
"""


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (enumerate)
        return self._countDifferentSubsequenceGCDs(nums)

    def _countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        """
        Time: beats 92.86%; Space: beats 92.86%
        """
        assert isinstance(nums, list) and len(nums) >= 1

        max_num = max(nums)
        occurred = [False] * (max_num + 1)
        for num in nums:
            occurred[num] = True

        res = 0
        for i in range(1, max_num + 1):
            sub_gcd = 0
            for j in range(i, max_num + 1, i):
                if occurred[j]:
                    if sub_gcd == 0:
                        sub_gcd = j
                    else:
                        sub_gcd = math.gcd(sub_gcd, j)
                    if sub_gcd == i:
                        res += 1
                        break

        return res


def main():
    # Example 1: Output: 5
    # nums = [6, 10, 3]

    # Example 2: Output: 7
    nums = [5, 15, 40, 5, 6]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countDifferentSubsequenceGCDs(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
