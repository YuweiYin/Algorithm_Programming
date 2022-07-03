#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0556-Next-Greater-Element-III.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-03
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0556 - (Medium) - Next Greater Element III
https://leetcode.com/problems/next-greater-element-iii/

Description & Requirement:
    Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n 
    and is greater in value than n. If no such positive integer exists, return -1.

    Note that the returned integer should fit in 32-bit integer, 
    if there is a valid answer but it does not fit in 32-bit integer, return -1.

Example 1:
    Input: n = 12
    Output: 21
Example 2:
    Input: n = 21
    Output: -1

Constraints:
    1 <= n <= 2^31 - 1
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        # main method: (find the next permutation: LC-0031-Next-Permutation)
        return self._nextGreaterElement(n)

    def _nextGreaterElement(self, n: int) -> int:
        assert isinstance(n, int) and n >= 1

        if n <= 11:
            return -1

        nums = [int(num) for num in str(n)]
        self.nextPermutation(nums)
        res_num = int("".join([str(num) for num in nums]))

        return res_num if res_num > n and 1 <= res_num < (1 << 31) else -1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        if len(nums) == 1:
            return
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return
        # main method: (from right to left, find the first ascending number pair)
        #     next, from right to left, find a bigger number
        #     swap these two numbers, and then reorder the right part to make sure it is the smallest
        self._nextPermutation(nums)

    def _nextPermutation(self, nums: List[int]) -> None:
        """
        Runtime: 32 ms, faster than 99.77% of Python3 online submissions for Next Permutation.
        Memory Usage: 13.9 MB, less than 79.00% of Python3 online submissions for Next Permutation.
        """
        len_nums = len(nums)
        assert len_nums >= 3

        left_idx = len_nums - 2  # from right to left, find the first ascending number pair
        while left_idx >= 0:
            if nums[left_idx] >= nums[left_idx + 1]:  # descending, move on
                left_idx -= 1
            else:
                break

        if left_idx >= 0:
            right_idx = len_nums - 1  # from right to left, find a bigger number
            while right_idx >= 0:
                if nums[left_idx] >= nums[right_idx]:
                    right_idx -= 1
                else:
                    break
            # swap
            nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]

        # now, nums[left_idx+1: ] is in descending order, change it to ascending order
        left, right = left_idx + 1, len_nums - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


def main():
    # Example 1: Output: 21
    n = 12

    # Example 2: Output: -1
    # n = 21

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.nextGreaterElement(n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
