#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0031-Next-Permutation.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-03
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0031 - (Medium) - Next Permutation
https://leetcode.com/problems/next-permutation/

Description & Requirement:
    A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

    For example, for arr = [1,2,3], the following are considered permutations of arr: 
        [1,2,3], [1,3,2], [3,1,2], [2,3,1].
    The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
    More formally, if all the permutations of the array are sorted in one container 
    according to their lexicographical order, then the next permutation of that array is 
    the permutation that follows it in the sorted container. If such arrangement is not possible, 
    the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    While the next permutation of arr = [3,2,1] is [1,2,3] 
        because [3,2,1] does not have a lexicographical larger rearrangement.

    Given an array of integers nums, find the next permutation of nums.

    The replacement must be in place and use only constant extra memory.

Example 1:
    Input: nums = [1,2,3]
    Output: [1,3,2]
Example 2:
    Input: nums = [3,2,1]
    Output: [1,2,3]
Example 3:
    Input: nums = [1,1,5]
    Output: [1,5,1]

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 100
"""


class Solution:
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
    # Example 1: Output: [1,3,2]
    # nums = [1, 2, 3]

    # Example 2: Output: [1,2,3]
    # nums = [3, 2, 1]

    # Example 3: Output: [1,5,1]
    # nums = [1, 1, 5]

    nums = [1, 4, 3, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.nextPermutation(nums)
    ans = nums
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
