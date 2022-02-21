#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0300-Longest-Increasing-Subsequence.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-29
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0300 - (Medium) - Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

Description & Requirement:
    Given an integer array nums, return the length of the longest strictly increasing subsequence.

    A subsequence is a sequence that can be derived from an array by 
    deleting some or no elements without changing the order of the remaining elements. 
    For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4
Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

Constraints:
    1 <= nums.length <= 2500
    -10^4 <= nums[i] <= 10^4

Follow up:
    Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 2 if nums[0] < nums[1] else 1
        # main method:
        # (1. Dynamic Programming: dp[i] is the max lengthOfLIS using nums[0: i+1])
        #     dp equation: dp[i] = max(dp[j]) + 1, where 0 <= j <= i-1 and nums[i] > nums[j]
        #     dp init: dp[0] = 1.
        #     dp aim: get max(dp)
        # return self._lengthOfLISdp(nums)  # Time: O(n^2);  Space: O(n).

        # (2. Greedy: for every valid seq of diff len, record its end num, maintain this num as the smallest possible)
        #     in this way, seq will grow as slow as possible, and won't miss any new num that will make them grow
        return self._lengthOfLISGreedy(nums)  # Time: O(n log n);  Space: O(n).

    def _lengthOfLISdp(self, nums: List[int]) -> int:
        """
        Time: O(n^2);  Space: O(n).
        """
        len_nums = len(nums)
        assert len_nums >= 3

        dp = [1 for _ in range(len_nums)]  # dp[i] is the max lengthOfLIS using nums[0: i+1]

        for index in range(len_nums):  # for i = 0, 1, ..., -1
            for seg_index in range(index):  # for j = 0, 1, ..., i - 1
                if nums[index] > nums[seg_index]:  # dp equation: dp[i] = max(dp[j]) + 1
                    dp[index] = max(dp[index], dp[seg_index] + 1)

        return max(dp)

    def _lengthOfLISGreedy(self, nums: List[int]) -> int:
        """
        Time: O(n log n);  Space: O(n).
        Runtime: 84 ms, faster than 91.67% of Python3 online submissions for Longest Increasing Subsequence.
        Memory Usage: 14.4 MB, less than 58.16% of Python3 online submissions for Longest Increasing Subsequence.
        """
        len_nums = len(nums)
        assert len_nums >= 3

        def __binary_search(left_index: int, right_index: int) -> int:
            # use binary search to find an update position
            update_index = right_index
            while left_index <= right_index:
                mid_index = (left_index + right_index) >> 1
                if num <= min_end[mid_index]:  # num can update min_end[mid]
                    update_index = mid_index
                    right_index = mid_index - 1
                else:
                    left_index = mid_index + 1
            return update_index

        min_end = [nums[0]]  # min_end[i] means the min end num of seq, where len(seq) == i

        for idx, num in enumerate(nums[1:]):
            if num > min_end[-1]:  # get a bigger num (larger than the end num of the current longest seq, min_end[-1])
                min_end.append(num)  # get a longer seq, record its end num
            else:  # see if num can update any of the end num of former shorter seq
                # use binary search to find an update position
                update_idx = __binary_search(0, len(min_end) - 1)
                min_end[update_idx] = num  # do update

        return len(min_end)


def main():
    # Example 1: Output: 4
    #     Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    # Example 2: Output: 4
    # nums = [0, 1, 0, 3, 2, 3]

    # Example 3: Output: 1
    # nums = [7, 7, 7, 7, 7, 7, 7]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.lengthOfLIS(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
