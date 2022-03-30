#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0215-Kth-Largest-Element-in-an-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-30
=================================================================="""

import sys
import time
from typing import List
import random
# import functools

"""
LeetCode - 0215 - (Medium) - Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Description & Requirement:
    Given an integer array nums and an integer k, return the kth largest element in the array.

    Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5
Example 2:
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

Constraints:
    1 <= k <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # exception case
        assert isinstance(k, int) and k >= 1
        assert isinstance(nums, list) and len(nums) >= k
        # main method: (find k-th number, similar to quick sort process, O(n) Time)
        return self._findKthLargest(nums, k)

    def _findKthLargest(self, nums: List[int], k: int) -> int:
        def __quick_select(left: int, right: int, target_order: int):
            cur_order = __partition(left, right)  # now, cur_order numbers are less than or equal to nums[cur_order]
            if cur_order == target_order:
                return nums[cur_order]
            elif cur_order < target_order:
                return __quick_select(cur_order + 1, right, target_order)
            else:
                return __quick_select(left, cur_order - 1, target_order)

        def __partition(left: int, right: int) -> int:
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]  # swap pivot and right number
            # partition
            pivot_num = nums[right]
            slow_ptr = left - 1
            for fast_ptr in range(left, right):  # fast_ptr always moves on, but slow_ptr doesn't
                if nums[fast_ptr] <= pivot_num:  # any number that <= pivot_num should be put in left part
                    slow_ptr += 1
                    nums[fast_ptr], nums[slow_ptr] = nums[slow_ptr], nums[fast_ptr]
            # now, put pivot_num to the correct position
            slow_ptr += 1
            nums[right], nums[slow_ptr] = nums[slow_ptr], nums[right]
            return slow_ptr

        return __quick_select(0, len(nums) - 1, len(nums) - k)


def main():
    # Example 1: Output: 5
    # nums = [3, 2, 1, 5, 6, 4]
    # k = 2

    # Example 2: Output: 4
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findKthLargest(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
