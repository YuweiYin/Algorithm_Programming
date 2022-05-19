#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0462-Minimum-Moves-to-Equal-Array-Elements-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-19
=================================================================="""

import sys
import time
from typing import List
import random
# import functools

"""
LeetCode - 0462 - (Medium) - Minimum Moves to Equal Array Elements II
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

Description & Requirement:
    Given an integer array nums of size n, 
    return the minimum number of moves required to make all array elements equal.

    In one move, you can increment or decrement an element of the array by 1.

    Test cases are designed so that the answer will fit in a 32-bit integer.

Example 1:
    Input: nums = [1,2,3]
    Output: 2
    Explanation:
        Only two moves are needed (remember each move increments or decrements one element):
        [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:
    Input: nums = [1,10,2,9]
    Output: 16

Constraints:
    n == nums.length
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (minimal moves: set all numbers to sorted nums[len(nums) / 2]. quick select, O(n))
        return self._minMoves2(nums)

    def _minMoves2(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        len_nums = len(nums)

        random.seed(time.time())
        target = self._findKthSmallest(nums, len_nums >> 1)
        res = sum([abs(num - target) for num in nums])
        return res

    def _findKthSmallest(self, nums: List[int], k: int) -> int:
        """
        LC-0215-Kth-Largest-Element-in-an-Array
        """
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

        # return __quick_select(0, len(nums) - 1, len(nums) - k)  # _findKthLargest
        return __quick_select(0, len(nums) - 1, k)  # _findKthSmallest


def main():
    # Example 1: Output: 2
    # nums = [1, 2, 3]

    # Example 2: Output: 16
    nums = [1, 10, 2, 9]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minMoves2(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
