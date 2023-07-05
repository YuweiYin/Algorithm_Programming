#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1493-Longest-Subarray-of-1s-After-Deleting-One-Element.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-05
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 1493 - (Medium) - Longest Subarray of 1's After Deleting One Element
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

Description & Requirement:
    Given a binary array nums, you should delete one element from it.

    Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
    Return 0 if there is no such subarray.

Example 1:
    Input: nums = [1,1,0,1]
    Output: 3
    Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:
    Input: nums = [0,1,1,1,0,1,1,0,1]
    Output: 5
    Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] 
        longest subarray with value of 1's is [1,1,1,1,1].
Example 3:
    Input: nums = [1,1,1]
    Output: 2
    Explanation: You must delete one element.

Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (sliding window)
        return self._longestSubarray(nums)

    def _longestSubarray(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        n = len(nums)
        res = 0
        left, right = 0, 0
        cnt_zeros = 0

        while right < n:
            if nums[right] == 0:
                cnt_zeros += 1
            while cnt_zeros > 1:
                if nums[left] == 0:
                    cnt_zeros -= 1
                left += 1
            res = max(res, right - left)
            right += 1

        return res


def main():
    # Example 1: Output: 3
    # nums = [1, 1, 0, 1]

    # Example 2: Output: 5
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]

    # Example 3: Output: 2
    # nums = [1, 1, 1]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.longestSubarray(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
