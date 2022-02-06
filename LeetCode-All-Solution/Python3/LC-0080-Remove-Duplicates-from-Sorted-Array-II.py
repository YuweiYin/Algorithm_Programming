#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0080-Remove-Duplicates-from-Sorted-Array-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-06
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0080 - (Medium) - Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Description & Requirement:
    Given an integer array nums sorted in non-decreasing order, 
    remove some duplicates in-place such that each unique element appears at most twice. 
    The relative order of the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages, 
    you must instead have the result be placed in the first part of the array nums. 
    More formally, if there are k elements after removing the duplicates, 
    then the first k elements of nums should hold the final result. 
    It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. 
    You must do this by modifying the input array in-place with O(1) extra memory.

    Custom Judge:
        The judge will test your solution with the following code:
        ```
        int[] nums = [...]; // Input array
        int[] expectedNums = [...]; // The expected answer with correct length
        
        int k = removeDuplicates(nums); // Calls your implementation
        
        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }
        If all assertions pass, then your solution will be accepted.
        ```

Example 1:
    Input: nums = [1,1,1,2,2,3]
    Output: 5, nums = [1,1,2,2,3,_]
    Explanation:
        Your function should return k = 5, 
        with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
        It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:
    Input: nums = [0,0,1,1,1,1,2,3,3]
    Output: 7, nums = [0,0,1,1,2,3,3,_,_]
    Explanation:
        Your function should return k = 7, 
        with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
        It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
    1 <= nums.length <= 3 * 10^4
    -10^4 <= nums[i] <= 10^4
    nums is sorted in non-decreasing order.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error head type
        if len(nums) <= 2:
            return len(nums)
        # main method: (count the occurrence of each number, then modify the current array)
        # other idea: two pointers - fast & slow. after scan, return slow pointer as the answer
        return self._removeDuplicates(nums)

    def _removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums >= 3

        fast_ptr = 0
        slow_ptr = 0

        while fast_ptr < len_nums:
            cur_num = nums[fast_ptr]
            cur_num_counter = 1  # counter of dupicate numbers
            while fast_ptr + 1 < len_nums and nums[fast_ptr] == nums[fast_ptr + 1]:
                cur_num_counter += 1
                fast_ptr += 1
            fast_ptr += 1  # fast_ptr move to the next new number, wait for the next loop

            # modify the current array
            if cur_num_counter == 1:
                nums[slow_ptr] = cur_num
                slow_ptr += 1
            else:  # cur_num_counter >= 1
                nums[slow_ptr] = cur_num
                if slow_ptr + 1 < len_nums:
                    nums[slow_ptr + 1] = cur_num
                slow_ptr += 2

        # now, slow_ptr is just the valid array length
        return slow_ptr


def main():
    # Example 1: Output: 5, nums = [1,1,2,2,3,_]
    nums = [1, 1, 1, 2, 2, 3]

    # Example 2: Output: 7, nums = [0,0,1,1,2,3,3,_,_]
    # nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.removeDuplicates(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
