#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0912-Sort-an-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-01
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0912 - (Medium) - Sort an Array
https://leetcode.com/problems/sort-an-array/

Description & Requirement:
    Given an array of integers nums, sort the array in ascending order and return it.

    You must solve the problem without using any built-in functions in O(nlog(n)) time complexity 
    and with the smallest space complexity possible.

Example 1:
    Input: nums = [5,2,3,1]
    Output: [1,2,3,5]
    Explanation: After sorting the array, the positions of some numbers are not changed 
        (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:
    Input: nums = [5,1,1,2,0,0]
    Output: [0,0,1,1,2,5]
    Explanation: Note that the values of nums are not necessairly unique.

Constraints:
    1 <= nums.length <= 5 * 10^4
    -5 * 10^4 <= nums[i] <= 5 * 10^4
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (heap sort)
        return self._sortArray(nums)

    def _sortArray(self, nums: List[int]) -> List[int]:
        assert isinstance(nums, list) and len(nums) >= 1

        self.heap_sort(nums)
        return nums

    def heap_sort(self, nums):
        for i in range(len(nums) - 1, -1, -1):  # build heap
            self.max_heapify(nums, i, len(nums))

        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)

    @staticmethod
    def max_heapify(heap, root, heap_len):
        cur_node = root
        while (cur_node << 1) + 1 < heap_len:
            left, right = (cur_node << 1) + 1, (cur_node << 1) + 2

            if heap_len <= right or heap[right] < heap[left]:
                next_node = left
            else:
                next_node = right

            if heap[cur_node] < heap[next_node]:
                heap[cur_node], heap[next_node] = heap[next_node], heap[cur_node]
                cur_node = next_node
            else:
                break


def main():
    # Example 1: Output: [1,2,3,5]
    nums = [5, 2, 3, 1]

    # Example 1: Output: [0,0,1,1,2,5]
    # nums = [5, 1, 1, 2, 0, 0]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.sortArray(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
