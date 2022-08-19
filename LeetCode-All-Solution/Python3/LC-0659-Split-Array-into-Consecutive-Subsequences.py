#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0659-Split-Array-into-Consecutive-Subsequences.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-19
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0659 - (Medium) - Split Array into Consecutive Subsequences
https://leetcode.com/problems/split-array-into-consecutive-subsequences/

Description & Requirement:
    You are given an integer array nums that is sorted in non-decreasing order.

    Determine if it is possible to split nums into one or more subsequences such that 
    both of the following conditions are true:
        1. Each subsequence is a consecutive increasing sequence 
            (i.e. each integer is exactly one more than the previous integer).
        2. All subsequences have a length of 3 or more.

    Return true if you can split nums according to the above conditions, or false otherwise.

    A subsequence of an array is a new array that is formed from the original array 
    by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements.
    (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

Example 1:
    Input: nums = [1,2,3,3,4,5]
    Output: true
    Explanation: nums can be split into the following subsequences:
        [1,2,3,3,4,5] --> 1, 2, 3
        [1,2,3,3,4,5] --> 3, 4, 5
Example 2:
    Input: nums = [1,2,3,3,4,4,5,5]
    Output: true
    Explanation: nums can be split into the following subsequences:
        [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
        [1,2,3,3,4,4,5,5] --> 3, 4, 5
Example 3:
    Input: nums = [1,2,3,4,4,5]
    Output: false
    Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.

Constraints:
    1 <= nums.length <= 10^4
    -1000 <= nums[i] <= 1000
    nums is sorted in non-decreasing order.
"""


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (greedily append new numbers to the end of subsequences)
        return self._isPossible(nums)

    def _isPossible(self, nums: List[int]) -> bool:
        assert isinstance(nums, list) and len(nums) >= 1

        num_cnt = collections.Counter(nums)  # key: cur_num; val: the unused number of cur_num
        end_cnt = collections.Counter()  # key: cur_num; val: the number of subsequences that end with cur_num

        for num in nums:
            if num_cnt[num] > 0:
                end_cnt_prev = end_cnt.get(num - 1, 0)
                if end_cnt_prev > 0:
                    num_cnt[num] -= 1
                    end_cnt[num - 1] = end_cnt_prev - 1
                    end_cnt[num] += 1
                else:
                    if num_cnt.get(num + 1, 0) > 0 and num_cnt.get(num + 2, 0) > 0:
                        num_cnt[num] -= 1
                        num_cnt[num + 1] -= 1
                        num_cnt[num + 2] -= 1
                        end_cnt[num + 2] += 1
                    else:
                        return False

        return True


def main():
    # Example 1: Output: true
    # nums = [1, 2, 3, 3, 4, 5]

    # Example 2: Output: true
    nums = [1, 2, 3, 3, 4, 4, 5, 5]

    # Example 3: Output: false
    # nums = [1, 2, 3, 4, 4, 5]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.isPossible(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
