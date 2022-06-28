#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0324-Wiggle-Sort-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-28
=================================================================="""

import sys
import time
import datetime
from typing import List
import random
# import functools

"""
LeetCode - 0324 - (Medium) - Wiggle Sort II
https://leetcode.com/problems/wiggle-sort-ii/

Description & Requirement:
    Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

    You may assume the input array always has a valid answer.

Example 1:
    Input: nums = [1,5,1,1,6,4]
    Output: [1,6,1,5,1,4]
    Explanation: [1,4,1,5,1,6] is also accepted.
Example 2:
    Input: nums = [1,3,2,2,3,1]
    Output: [2,3,1,3,1,2]

Constraints:
    1 <= nums.length <= 5 * 10^4
    0 <= nums[i] <= 5000
    It is guaranteed that there will be an answer for the given input nums.

Follow Up:
    Can you do it in O(n) time and/or in-place with O(1) extra space?
"""


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        for num in nums:
            assert isinstance(num, int) and num >= 0
        # main method: (three-direction cut + quick select)
        self._wiggleSort(nums)

    def _wiggleSort(self, nums: List[int]) -> None:
        assert isinstance(nums, list) and len(nums) >= 1

        len_nums = len(nums)
        x = (len_nums + 1) >> 1
        target = self._quick_select(nums, x - 1)

        def __trans_address(x: int):
            return ((len_nums << 1) - (x << 1) - 1) % (len_nums | 1)

        k, i, j = 0, 0, len_nums - 1
        while k <= j:
            k_t = __trans_address(k)
            if nums[k_t] > target:
                while j > k and nums[__trans_address(j)] > target:
                    j -= 1
                j_t = __trans_address(j)
                nums[k_t], nums[j_t] = nums[j_t], nums[k_t]
                j -= 1
            if nums[k_t] < target:
                i_t = __trans_address(i)
                nums[k_t], nums[i_t] = nums[i_t], nums[k_t]
                i += 1
            k += 1

    def _quick_select(self, array: List[int], k: int) -> int:
        random.seed(datetime.datetime.now())
        random.shuffle(array)
        left, right = 0, len(array) - 1
        while left < right:
            pivot = array[left]
            i, j = left, right + 1
            while True:
                i += 1
                while i < right and array[i] < pivot:
                    i += 1
                j -= 1
                while j > left and array[j] > pivot:
                    j -= 1
                if i >= j:
                    break
                array[i], array[j] = array[j], array[i]
            array[left], array[j] = array[j], pivot
            if j == k:
                break
            if j < k:
                left = j + 1
            else:
                right = j - 1
        return array[k]


def main():
    # Example 1: Output: [1,6,1,5,1,4]
    nums = [1, 5, 1, 1, 6, 4]

    # Example 2: Output: [2,3,1,3,1,2]
    # nums = [1, 3, 2, 2, 3, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.wiggleSort(nums)
    ans = nums
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
