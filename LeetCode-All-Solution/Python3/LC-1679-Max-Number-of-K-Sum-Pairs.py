#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1679-Max-Number-of-K-Sum-Pairs.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-04
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1679 - (Medium) - Max Number of K-Sum Pairs
https://leetcode.com/problems/max-number-of-k-sum-pairs/

Description & Requirement:
    You are given an integer array nums and an integer k.

    In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

    Return the maximum number of operations you can perform on the array.

Example 1:
    Input: nums = [1,2,3,4], k = 5
    Output: 2
    Explanation: Starting with nums = [1,2,3,4]:
        - Remove numbers 1 and 4, then nums = [2,3]
        - Remove numbers 2 and 3, then nums = []
        There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:
    Input: nums = [3,1,3,4,3], k = 6
    Output: 1
    Explanation: Starting with nums = [3,1,3,4,3]:
        - Remove the first two 3's, then nums = [1,4,3]
        There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    1 <= k <= 10^9
"""


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (two sum, greedy match)
        return self._maxOperations(nums, k)

    def _maxOperations(self, nums: List[int], k: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and k >= 1
        len_nums = len(nums)
        if len_nums == 1:
            return 0
        if len_nums == 2:
            return 1 if nums[0] + nums[1] == k else 0

        num_dict = dict({})
        for idx, num in enumerate(nums):
            if num not in num_dict:
                # num_dict[num] = [idx]
                num_dict[num] = 1
            else:
                # num_dict[num].append(idx)
                num_dict[num] += 1

        # visit_idx = [False for _ in range(len_nums)]
        res = 0
        for idx, num in enumerate(nums):
            target_num = k - num
            if target_num in num_dict:
                if target_num == num:
                    if num_dict[target_num] >= 2:
                        num_dict[target_num] -= 2
                        res += 1
                    else:
                        continue
                else:
                    if num_dict[target_num] >= 1 and num_dict[num] >= 1:
                        num_dict[target_num] -= 1
                        num_dict[num] -= 1
                        res += 1
                    else:
                        continue
            else:
                continue

        return res


def main():
    # Example 1: Output: 2
    nums = [1, 2, 3, 4]
    k = 5

    # Example 2: Output: 1
    # nums = [3, 1, 3, 4, 3]
    # k = 6

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxOperations(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
