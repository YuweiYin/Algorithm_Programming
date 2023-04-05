#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2439-Minimize-Maximum-of-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-05
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2439 - (Medium) - Minimize Maximum of Array
https://leetcode.com/problems/minimize-maximum-of-array/

Description & Requirement:
    You are given a 0-indexed array nums comprising of n non-negative integers.

    In one operation, you must:
        Choose an integer i such that 1 <= i < n and nums[i] > 0.
        Decrease nums[i] by 1.
        Increase nums[i - 1] by 1.

    Return the minimum possible value of the maximum integer of nums after performing any number of operations.

Example 1:
    Input: nums = [3,7,1,6]
    Output: 5
    Explanation:
        One set of optimal operations is as follows:
        1. Choose i = 1, and nums becomes [4,6,1,6].
        2. Choose i = 3, and nums becomes [4,6,2,5].
        3. Choose i = 1, and nums becomes [5,5,2,5].
        The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
        Therefore, we return 5.
Example 2:
    Input: nums = [10,1]
    Output: 10
    Explanation: It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.

Constraints:
    n == nums.length
    2 <= n <= 10^5
    0 <= nums[i] <= 10^9
"""


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        # main method: (binary search)
        return self._minimizeArrayValue(nums)

    def _minimizeArrayValue(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 2

        def __check(k: int) -> bool:
            flag = 0
            for num in nums:
                if num <= k:
                    flag += k - num
                else:
                    if flag < num - k:
                        return False
                    else:
                        flag -= (num - k)
            return True

        left, right = 0, max(nums)
        while left < right:
            mid = (left + right) >> 1
            if __check(mid):
                right = mid
            else:
                left = mid + 1

        return left


def main():
    # Example 1: Output: 5
    nums = [3, 7, 1, 6]

    # Example 2: Output: 10
    # nums = [10, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimizeArrayValue(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
