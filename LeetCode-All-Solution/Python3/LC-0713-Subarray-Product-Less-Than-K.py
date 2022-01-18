#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0713-Subarray-Product-Less-Than-K.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-18
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0713 - (Medium) - Subarray Product Less Than K
https://leetcode.com/problems/subarray-product-less-than-k/

Description & Requirement:
    Given an array of integers nums and an integer k, 
    return the number of contiguous subarrays 
    where the product of all the elements in the subarray is strictly less than k.

Example 1:
    Input: nums = [10,5,2,6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are:
        [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
        Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:
    Input: nums = [1,2,3], k = 0
    Output: 0

Constraints:
    1 <= nums.length <= 3 * 10^4
    1 <= nums[i] <= 1000
    0 <= k <= 10^6
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return 1 if nums[0] > k else 0
        # main method: (two pointer, slide window)
        return self._numSubarrayProductLessThanK(nums, k)

    def _numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        len_nums = len(nums)
        assert len_nums > 1

        res = 0
        MOD = int(1e9+7)

        # def __factorial_n(n: int):
        #     return sum([int_num for int_num in range(1, n + 1)])

        window_start = 0  # the start index of slide window
        cur_product = 1  # the number product in the current window
        for window_end, end_num in enumerate(nums):  # consider interval [0:1], [0:2], ..., [0: max]
            # tip: if product is too large, use math.log and convert multiplication to addition
            cur_product = int(cur_product * end_num) % MOD  # each for loop, window_end move right, so prod number
            while window_start <= window_end and cur_product >= k:
                # if cur_product is greater than or equal to k, shrink window by moving window_start
                cur_product = int(cur_product / nums[window_start]) % MOD
                window_start += 1
            # now, if cur_product < k, all the following new subarrays are valid:
            #     [nums[w_s], num[w_s+1], ..., nums[w_e]], [nums[w_s+1], num[w_s+2], ..., nums[w_e]], ... [nums[w_e]]
            #     in total, there are (w_e - w_s + 1) new valid subarrays
            if cur_product < k:
                res += window_end - window_start + 1
            else:
                continue

        return res


def main():
    # Example 1: Output: 8
    #     Explanation: The 8 subarrays that have product less than 100 are:
    #         [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
    #         Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
    nums = [10, 5, 2, 6]
    k = 100

    # Example 2: Output: 0
    # nums = [1, 2, 3]
    # k = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numSubarrayProductLessThanK(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
