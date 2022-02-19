#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1675-Minimize-Deviation-in-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-19
=================================================================="""

import sys
import time
from typing import List
# import heapq
# import collections
from sortedcontainers import SortedList

"""
LeetCode - 1675 - (Hard) - Minimize Deviation in Array
https://leetcode.com/problems/minimize-deviation-in-array/

Description & Requirement:
    You are given an array nums of n positive integers.

    You can perform two types of operations on any element of the array any number of times:
        If the element is even, divide it by 2.
            For example, if the array is [1,2,3,4], then you can do this operation on the last element, 
            and the array will be [1,2,3,2].
        If the element is odd, multiply it by 2.
            For example, if the array is [1,2,3,4], then you can do this operation on the first element, 
            and the array will be [2,2,3,4].

    The deviation of the array is the maximum difference between any two elements in the array.
    Return the minimum deviation the array can have after performing some number of operations.

Example 1:
    Input: nums = [1,2,3,4]
    Output: 1
    Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
Example 2:
    Input: nums = [4,1,5,20,3]
    Output: 3
    Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
Example 3:
    Input: nums = [2,10,8]
    Output: 3

Constraints:
    n == nums.length
    2 <= n <= 10^5
    1 <= nums[i] <= 10^9
"""


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list):
            return 0  # Error input type
        assert len(nums) >= 2
        # main method: (Heap, use both max_heap and min_heap)
        #     the target is to minimize the max and maximize the min, meanwhile max >= min
        #     if the max number of max_heap is even, it can be divided by 2, else can do nothing
        #     if the min number of min_heap is odd, it can be multiplied by 2, else can do nothing
        #     after dealt with max_heap and min_heap, then get result == (max - min)
        # return self._minimumDeviationTodo(nums)

        # core trick: preprocess: multiply 2 for all odd numbers in nums
        #     then heapify nums, and divide 2 for every even max number
        return self._minimumDeviation(nums)

    def _minimumDeviationTodo(self, nums: List[int]) -> int:
        """
        pass: 75 / 76, the last one: Wrong, output 99980807; answer: 99934103.
        """
        assert len(nums) >= 2

        # from sortedcontainers import SortedList
        nums_sorted = SortedList(nums)

        res_min_gap = max(nums) - min(nums) + 1  # INF gap

        res_keep_still = 0  # the number of consecutive loops does res_min_gap keep the same value
        while res_min_gap > 0:
            # find max num and min num
            cur_gap = nums_sorted[-1] - nums_sorted[0]  # Time: O(1)
            if cur_gap < res_min_gap:
                res_min_gap = cur_gap
                res_keep_still = 0
                if res_min_gap == 0:
                    break

            can_max_change = True
            while nums_sorted[-1] & 0x01 == 0:
                # pop (cur_max_num) and push (cur_max_num >> 1)
                cur_max_num = nums_sorted[-1]
                nums_sorted.discard(cur_max_num)  # Time: O(log n)
                nums_sorted.add(cur_max_num >> 1)  # Time: O(log n)
                # get new gap
                cur_gap = nums_sorted[-1] - nums_sorted[0]  # Time: O(1)
                if cur_gap < res_min_gap:
                    res_min_gap = cur_gap
                    res_keep_still = 0
                    if res_min_gap == 0:
                        break

            while nums_sorted[0] & 0x01 == 1:
                # pop (cur_min_num) and push (cur_min_num << 1)
                cur_min_num = nums_sorted[0]
                nums_sorted.discard(cur_min_num)  # Time: O(log n)
                nums_sorted.add(cur_min_num << 1)  # Time: O(log n)
                # get new gap
                cur_gap = nums_sorted[-1] - nums_sorted[0]  # Time: O(1)
                if cur_gap < res_min_gap:
                    res_min_gap = cur_gap
                    res_keep_still = 0
                    if res_min_gap == 0:
                        break

            res_keep_still += 1
            # res_keep_still == 3 means the number of consecutive loops does res_min_gap keep the same value == 2
            if res_keep_still >= 3:
                break

        return res_min_gap

    def _minimumDeviation(self, nums: List[int]) -> int:
        assert len(nums) >= 2

        res_min_gap = max(nums) - min(nums)  # default gap

        # from sortedcontainers import SortedList

        # preprocess: multiply 2 for all odd numbers in nums
        for idx, num in enumerate(nums):
            if num & 0x01 == 1:
                nums[idx] = num << 1

        # then heapify nums, and divide 2 for every even max number
        nums_sorted = SortedList(nums)
        while nums_sorted[-1] & 0x01 == 0:
            cur_max_num = nums_sorted[-1]
            nums_sorted.discard(cur_max_num)  # Time: O(log n)
            nums_sorted.add(cur_max_num >> 1)  # Time: O(log n)
            res_min_gap = min(res_min_gap, nums_sorted[-1] - nums_sorted[0])  # Time: O(1)

        return min(res_min_gap, nums_sorted[-1] - nums_sorted[0])


def main():
    # Example 1: Output: 1
    #     Explanation: transform the array to [2,2,3,2], then the deviation will be 3 - 2 = 1.
    # nums = [1, 2, 3, 4]

    # Example 2: Output: 3
    #     Explanation: You can transform the array to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
    # nums = [4, 1, 5, 20, 3]

    # Example 3: Output: 3
    # nums = [2, 10, 8]

    # Example 4: Output: 1
    # nums = [3, 5]

    # Example 5: Output: 3
    # nums = [8, 10, 2, 1]

    # Example 6: Output: 1
    # nums = [2, 8, 6, 1, 6]
    # nums = [2, 8, 6, 1, 6, 6, 6, 6, 2, 2, 2, 1]

    # Example 7: Output: 315
    nums = [399, 908, 648, 357, 693, 502, 331, 649, 596, 698]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumDeviation(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
