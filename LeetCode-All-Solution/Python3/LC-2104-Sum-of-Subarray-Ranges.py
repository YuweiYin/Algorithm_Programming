#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2104-Sum-of-Subarray-Ranges.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-04
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 2104 - (Medium) - Sum of Subarray Ranges
https://leetcode.com/problems/sum-of-subarray-ranges/

Description & Requirement:
    You are given an integer array nums. 
    The `range` of a subarray of nums is the difference between the largest and smallest element in the subarray.

    Return the sum of all subarray ranges of nums.

    A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,2,3]
    Output: 4
    Explanation: The 6 subarrays of nums are the following:
        [1], range = largest - smallest = 1 - 1 = 0 
        [2], range = 2 - 2 = 0
        [3], range = 3 - 3 = 0
        [1,2], range = 2 - 1 = 1
        [2,3], range = 3 - 2 = 1
        [1,2,3], range = 3 - 1 = 2
        So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:
    Input: nums = [1,3,3]
    Output: 4
    Explanation: The 6 subarrays of nums are the following:
        [1], range = largest - smallest = 1 - 1 = 0
        [3], range = 3 - 3 = 0
        [3], range = 3 - 3 = 0
        [1,3], range = 3 - 1 = 2
        [3,3], range = 3 - 3 = 0
        [1,3,3], range = 3 - 1 = 2
        So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:
    Input: nums = [4,-2,-3,4,1]
    Output: 59
    Explanation: The sum of all subarray ranges of nums is 59.

Constraints:
    1 <= nums.length <= 1000
    -10^9 <= nums[i] <= 10^9
"""


class SparseTableRMQ:
    # Sparse Table construction, Time O(n log n)
    def __init__(self, array):
        self.st_len = len(array)
        self.inf = 0x3f3f3f3f  # 1061109567

        # construct log_table to calculate log_2 (len(array))
        # log_table[0]is null, and log_table[i] is floor(log_2 i)
        self.log_table = (self.st_len + 1) * [0]
        for i in range(2, self.st_len + 1):
            self.log_table[i] = self.log_table[i >> 1] + 1

        # Sparse Table: row = 1 + log_2 (self.st_len)，col = self.st_len
        # st[0] is the original array
        self.st = [[self.inf] * self.st_len for _ in range(1 + self.log_table[self.st_len])]
        self.st[0] = array

        # Dynamic Programming: st[i][j] = min( st[i-1][j], st[i-1][j + 2^(i-1)] )
        for i in range(1, len(self.st)):
            j = 0
            while j + (1 << i) <= self.st_len:
                self.st[i][j] = min(self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))])
                j += 1

    # if update any value in the array, the Sparse Table need to be reconstructed, Time O(n log n)
    # but if the length of array changes, it's better to reconstruct SparseTableRMQ object
    # and if the change of array is frequent, consider using Segment Tree instead of Sparse Table
    def update(self, index, value):
        if 0 <= index < len(self.st[0]) and self.st[0][index] != value:
            self.st[0][index] = value
            for i in range(1, len(self.st)):
                j = 0
                while j + (1 << i) <= self.st_len:
                    self.st[i][j] = min(self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))])
                    j += 1

    # get the minimum of [left, right] (closed interval), Time: O(1)
    # 0 <= left <= right <= n-1
    def query_minimum(self, left, right):
        if left > right:
            return self.inf

        if left < 0:
            left = 0
        if right >= self.st_len:
            right = self.st_len - 1

        # (right - left + 1) if the length of the interval, get the logarithm of this length
        log_2 = self.log_table[right - left + 1]

        # st[log_2][left] if the minimum in array[left: left + 2 ** log_2]
        return min(self.st[log_2][left], self.st[log_2][right - (1 << log_2) + 1])

    def print_st(self):
        for i in range(len(self.st)):
            print(self.st[i])


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0
        if len(nums) == 1:
            return 0
        # main method: (Data Structure, solve RMQ (Range Minimum/Maximum Query) problem)
        # Sparse Table: construction time O(n log n), each RMQ time O(1)
        #     https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/range-min-max-query.py
        # Segment Tree: construction time O(n), each RMQ time O(log n)
        #     https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/data-structure/segment-tree.py
        # or use Interval Tree to store and maintain the max/min information of all intervals
        # return self._subArrayRangesDS(nums)
        # method 2: monotonous stack (similar to LC-0084-Largest-Rectangle-in-Histogram)
        return self._subArrayRanges(nums)  # Time: O(n)

    def _subArrayRangesDS(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums >= 2

        # use Sparse Table to quickly get RMQ (Range Minimum/Maximum Query)
        # Sparse Table: construction time O(n log n), each RMQ time O(1)
        st_min = SparseTableRMQ(nums)
        st_max = SparseTableRMQ([- num for num in nums])

        res = 0
        for left_idx in range(len_nums):
            for right_idx in range(left_idx + 1, len_nums):
                cur_min = st_min.query_minimum(left_idx, right_idx)
                cur_max = - st_max.query_minimum(left_idx, right_idx)
                res += cur_max - cur_min

        return res

    def _subArrayRanges(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums >= 2

        left_smaller = [0 for _ in range (len_nums)]  # list[i] is the closest j < i such that nums[j] <= nums[i]
        left_larger = [0 for _ in range(len_nums)]  # list[i] is the closest j < i such that nums[j] > nums[i]
        min_mono_stack = []  # monotonously store the index of min number (first round: index from 0 to len_nums-1)
        max_mono_stack = []  # monotonously store the index of max number (first round: index from 0 to len_nums-1)

        left_idx = 0
        while left_idx < len_nums:
            num = nums[left_idx]

            # min_stack always store the minimum on its top, so if top number > current num, pop them
            while len(min_mono_stack) > 0 and nums[min_mono_stack[-1]] > num:
                min_mono_stack.pop()
            # -1 is the leftmost unreachable index
            left_smaller[left_idx] = min_mono_stack[-1] if len(min_mono_stack) > 0 else -1
            min_mono_stack.append(left_idx)

            # max_stack always store the maximum on its top, so if top number < current num, pop them
            # because max_stack[-1] < i, nums[max_stack[-1]] == num is the same case as nums[max_stack[-1]] < num
            while len(max_mono_stack) > 0 and nums[max_mono_stack[-1]] <= num:
                max_mono_stack.pop()
            # -1 is the leftmost unreachable index
            left_larger[left_idx] = max_mono_stack[-1] if len(max_mono_stack) > 0 else -1
            max_mono_stack.append(left_idx)

            left_idx += 1

        right_smaller = [0 for _ in range(len_nums)]  # list[i] is the closest i < j such that nums[i] > nums[j]
        right_larger = [0 for _ in range(len_nums)]  # list[i] is the closest i < j such that nums[i] <= nums[j]
        min_mono_stack = []  # monotonously store the index of min number (second round: index from len_nums-1 to 0)
        max_mono_stack = []  # monotonously store the index of max number (second round: index from len_nums-1 to 0)

        right_idx = len_nums - 1
        while right_idx >= 0:
            num = nums[right_idx]

            # min_stack always store the minimum on its top, so if top number > current num, pop them
            # because min_stack[-1] > i, nums[min_stack[-1]] == num is the same case as nums[max_stack[-1]] > num
            while len(min_mono_stack) > 0 and nums[min_mono_stack[-1]] >= num:
                min_mono_stack.pop()
            # len_nums is the rightmost unreachable index
            right_smaller[right_idx] = min_mono_stack[-1] if len(min_mono_stack) > 0 else len_nums
            min_mono_stack.append(right_idx)

            # max_stack always store the minimum on its top, so if top number < current num, pop them
            while len(max_mono_stack) > 0 and nums[max_mono_stack[-1]] < num:
                max_mono_stack.pop()
            # len_nums is the rightmost unreachable index
            right_larger[right_idx] = max_mono_stack[-1] if len(max_mono_stack) > 0 else len_nums
            max_mono_stack.append(right_idx)

            right_idx -= 1

        sum_max = 0  # the sum of the max numbers of all intervals
        sum_min = 0  # the sum of the min numbers of all intervals
        # left_smaller[i] is the closest j < i such that nums[j] <= nums[i]
        # left_larger[i] is the closest j < i such that nums[j] > nums[i]
        # right_smaller[i] is the closest i < j such that nums[i] > nums[j]
        # right_larger[i] is the closest i < j such that nums[i] <= nums[j]
        # so for each num = nums[i], imagine the interval expands from index=i, num can be the maximum of intervals
        #     only when left_larger[i] < i < right_larger[i], so consider how many such sub-intervals
        #     the length of left part varies from 1 to (i - left_larger[i])
        #     the length of right part varies from 1 to (right_larger[i] - i)
        #     so the counter of intervals that num is maximum is (i - left_larger[i]) * (right_larger[i] - i)
        # similarly, for each num = nums[i], num can be the minimum of intervals
        #     only when left_smaller[i] < i < right_smaller[i], so consider how many such sub-intervals
        #     the length of left part varies from 1 to (i - left_smaller[i])
        #     the length of right part varies from 1 to (right_smaller[i] - i)
        #     so the counter of intervals that num is maximum is (i - left_smaller[i]) * (right_smaller[i] - i)
        for idx, num in enumerate(nums):
            sum_max += (idx - left_larger[idx]) * (right_larger[idx] - idx) * num
            sum_min += (idx - left_smaller[idx]) * (right_smaller[idx] - idx) * num

        return int(sum_max - sum_min)


def main():
    # Example 1: Output: 4
    # nums = [1, 2, 3]

    # Example 2: Output: 4
    # nums = [1, 3, 3]

    # Example 3: Output: 59
    nums = [4, -2, -3, 4, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.subArrayRanges(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
