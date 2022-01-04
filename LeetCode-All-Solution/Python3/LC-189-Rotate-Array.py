#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-189-Rotate-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-02
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 189 - (Medium) - Rotate Array
https://leetcode.com/problems/rotate-array/

Description:
    Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation: 
        rotate 1 steps to the right: [99,-1,-100,3]
        rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

Follow up:
    Try to come up with as many solutions as you can. 
    There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # exception case
        if not isinstance(nums, list) or len(nums) <= 1 or k <= 0:
            return
        # main method
        self._rotate_double_reverse(nums, k)

    # Warning: the following method is correct only if gcd(len_num, k) == 1
    # def _rotate_gcd1(self, nums: List[int], k: int) -> None:
    #     len_num = len(nums)
    #     if k > len_num:
    #         k %= len_num  # avoid unnecessary rotate
    #     # old_start_index, old_end_index = 0, len_num - 1
    #     # new_start_index = len_num - k
    #     # new_end_index = new_start_index - 1
    #     # nums[old_start_index]...nums[new_end_index] go right (gap = +k)
    #     # nums[new_start_index]...nums[old_end_index] go left (gap = -(len_num - k))
    #     forward_move_gap = k
    #     backward_move_gap = len_num - k
    #     watershed = len_num - k
    #     # move one by one in order to get O(1) space efficiency
    #     # if O(n) space, then just init a new list and append numbers, quite easy
    #     cur_move_index = 0
    #     temp_from_num = nums[cur_move_index]  # store the number that is going to replace another number
    #     move_counter = 0  # move len_num times in total
    #     while move_counter < len_num:
    #         if cur_move_index < watershed:  # go right (gap = +k)
    #             temp_to_num = nums[cur_move_index + forward_move_gap]  # store the number that is going to be replaced
    #             nums[cur_move_index + forward_move_gap] = temp_from_num
    #             temp_from_num = temp_to_num
    #             cur_move_index = cur_move_index + forward_move_gap
    #         else:  # go left (gap = -(len_num - k))
    #             temp_to_num = nums[cur_move_index - backward_move_gap]  # store the number that is going to be replaced
    #             nums[cur_move_index - backward_move_gap] = temp_from_num
    #             temp_from_num = temp_to_num
    #             cur_move_index = cur_move_index - backward_move_gap
    #
    #         move_counter += 1

    # 1. reverse the whole list; 2. split; 3. reserve two small lists respectively; 4. combine.
    def _rotate_double_reverse(self, nums: List[int], k: int) -> None:
        len_num = len(nums)
        if k > len_num:
            k %= len_num  # avoid unnecessary rotate
        # split  nums[0]...nums[k]  and  nums[k]...nums[len_num]
        watershed = len_num - k
        nums.reverse()
        # Way 1:
        # nums[0: k] = reversed(nums[0: k])
        # nums[k: len_num] = reversed(nums[k: len_num])
        # Way 2
        self._reverse_list_in_place(nums, 0, k - 1)
        self._reverse_list_in_place(nums, k, len_num - 1)

    @staticmethod
    def _reverse_list_in_place(nums: List[int], start_index: int, end_index: int) -> None:
        while start_index < end_index:
            temp_num = nums[start_index]
            nums[start_index] = nums[end_index]
            nums[end_index] = temp_num
            start_index += 1
            end_index -= 1


def main():
    # Example 1: Output: [5,6,7,1,2,3,4]
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    # Example 2: Output: [3,99,-1,-100]
    # nums = [-1, -100, 3, 99]
    # k = 2

    # Example 3: Output: [4, 5, 6, 1, 2, 3]
    # nums = [1, 2, 3, 4, 5, 6]
    # k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    solution.rotate(nums, k)
    ans = nums
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
