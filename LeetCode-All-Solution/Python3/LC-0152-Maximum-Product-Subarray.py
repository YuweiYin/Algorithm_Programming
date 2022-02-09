#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0152-Maximum-Product-Subarray.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-09
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0152 - (Medium) - Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Description & Requirement:
    Given an integer array nums, find a contiguous non-empty subarray within the array 
    that has the largest product, and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.

    A subarray is a contiguous subsequence of the array.

Example 1:
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
Example 2:
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
    1 <= nums.length <= 2 * 10^4
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Related Problem:
    LC-1567-Maximum-Length-of-Subarray-With-Positive-Product
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] * nums[1])
        # main method: (Dynamic Programming. consider positive number and negative number)
        #     dp_max[i] is the max product using nums[0: i+1], dp_min[i] is the min product using nums[0: i+1]
        #     dp equation 1: dp_max[i] = max(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i]), 1 <= i < len(nums)
        #     dp equation 2: dp_min[i] = min(dp_max[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i]), 1 <= i < len(nums)
        #     dp init: dp_max[0] = nums[0], dp_min[0] = nums[0]
        #     dp aim: get max(dp_max)
        # return self._maxProductDp(nums)
        return self._maxProductDpCompression(nums)

    def _maxProductDp(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums >= 3

        # dp_max = [0 for _ in range(len_nums)]
        # dp_min = [0 for _ in range(len_nums)]
        # dp_max[0] = nums[0]
        # dp_min[0] = nums[0]

        dp_max = nums[:]
        dp_min = nums[:]

        cur_index = 1
        while cur_index < len_nums:
            cur_num = nums[cur_index]
            dp_max[cur_index] = max(dp_max[cur_index - 1] * cur_num, dp_min[cur_index - 1] * cur_num, cur_num)
            dp_min[cur_index] = min(dp_max[cur_index - 1] * cur_num, dp_min[cur_index - 1] * cur_num, cur_num)
            cur_index += 1

        return max(dp_max)

    def _maxProductDpCompression(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums >= 3

        res, cur_max, cur_min = nums[0], nums[0], nums[0]

        cur_index = 1
        while cur_index < len_nums:
            cur_num = nums[cur_index]
            # if cur_num < 0, swap cur_min and cur_max
            if cur_num < 0:
                cur_max, cur_min = cur_min, cur_max

            # update cur_max and cur_min
            cur_max = max(cur_max * cur_num, cur_num)
            cur_min = min(cur_min * cur_num, cur_num)

            # update res
            res = max(res, cur_max)

            cur_index += 1

        return res


def main():
    # Example 1: Output: 6
    nums = [2, 3, -2, 4]

    # Example 2: Output: 0
    # nums = [-2, 0, -1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxProduct(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
