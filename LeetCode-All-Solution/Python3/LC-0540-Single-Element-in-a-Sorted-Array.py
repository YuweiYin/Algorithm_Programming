#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0540-Single-Element-in-a-Sorted-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-14
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0540 - (Medium) - Single Element in a Sorted Array
https://leetcode.com/problems/single-element-in-a-sorted-array/

Description & Requirement:
    You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

    Return the single element that appears only once.

    Your solution must run in O(log n) time and O(1) space.

Example 1:
    Input: nums = [1,1,2,3,3,4,4,8,8]
    Output: 2
Example 2:
    Input: nums = [3,3,7,7,10,11,11]
    Output: 10

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^5
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) > 0 and len(nums) & 0x01 == 1
        # main method: (if O(n), just xor all numbers; if O(log n), use binary search)
        # return self._singleNonDuplicateXor(nums)  # O(n)
        # binary search idea: core: how to determine go left or right -> by the parity of left/right sub list
        #     find the middle number, if it is single, return it, else find its counterpart (mid-1 or mid+1)
        #         then the length of left and right sub list is clear, go to the odd one, do recursion
        return self._singleNonDuplicateBS(nums)  # O(log n)

    def _singleNonDuplicateXor(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

    def _singleNonDuplicateBS(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums > 0 and len_nums & 0x01 == 1

        if len(nums) == 1:
            return nums[0]

        def __binary_search(left_index: int, right_index: int) -> int:
            assert left_index <= right_index
            if left_index == right_index:
                return nums[left_index]
            mid_index = (left_index + right_index) >> 1

            # if mid_index is a border index
            if mid_index == 0:
                if nums[mid_index] != nums[mid_index + 1]:
                    return nums[mid_index]
                else:
                    return __binary_search(mid_index + 2, right_index)
            if mid_index == len_nums - 1:
                if nums[mid_index] != nums[mid_index - 1]:
                    return nums[mid_index]
                else:
                    return __binary_search(left_index, mid_index - 2)

            # now mid_index is not border index
            if nums[mid_index] != nums[mid_index + 1] and nums[mid_index] != nums[mid_index - 1]:
                return nums[mid_index]
            elif nums[mid_index] == nums[mid_index + 1]:
                left_sublist_length = mid_index  # (mid - 1) - 0 + 1
                right_sublist_length = right_index - mid_index - 1  # right - (mid + 2) + 1
                if left_sublist_length & 0x01 == 1:
                    return __binary_search(left_index, mid_index - 1)
                else:
                    assert right_sublist_length & 0x01 == 1
                    return __binary_search(mid_index + 2, right_index)
            elif nums[mid_index] == nums[mid_index - 1]:
                left_sublist_length = mid_index - 1  # (mid - 2) - 0 + 1
                right_sublist_length = right_index - mid_index  # right - (mid + 1) + 1
                if left_sublist_length & 0x01 == 1:
                    return __binary_search(left_index, mid_index - 2)
                else:
                    assert right_sublist_length & 0x01 == 1
                    return __binary_search(mid_index + 1, right_index)
            else:
                pass  # not way!

        return __binary_search(0, len_nums - 1)


def main():
    # Example 1: Output: 2
    # nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

    # Example 2: Output: 10
    nums = [3, 3, 7, 7, 10, 11, 11]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.singleNonDuplicate(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)
    # print(TreeNode.show_binary_tree_mid_order(ans))

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
