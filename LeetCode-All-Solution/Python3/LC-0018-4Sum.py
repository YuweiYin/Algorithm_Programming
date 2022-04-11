#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0018-4Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-11
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0018 - (Medium) - 4Sum
https://leetcode.com/problems/4sum/

Description & Requirement:
    Given an array nums of n integers, 
    return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
        0 <= a, b, c, d < n
        a, b, c, and d are distinct.
        nums[a] + nums[b] + nums[c] + nums[d] == target

    You may return the answer in any order.

Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]

Constraints:
    1 <= nums.length <= 200
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # exception case
        assert isinstance(target, int)
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (sort, convert to 3Sum problem, then convert to 2Sum (two pointers))
        return self._fourSum(nums, target)

    def _fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        len_nums = len(nums)
        assert len_nums >= 1

        if len_nums < 4:
            return []
        if len_nums == 4:
            return [nums] if sum(nums) == target else []

        res = set()
        nums.sort()  # sort

        for i in range(len_nums):
            # now, 3 sum problem
            cur_target_jkl = target - nums[i]

            for j in range(i + 1, len_nums):
                # now, 2 sum problem
                cur_target_kl = cur_target_jkl - nums[j]

                k, _l = j + 1, len_nums - 1
                while k < _l:
                    cur_sum = nums[k] + nums[_l]
                    if cur_sum == cur_target_kl:  # bingo, store the result
                        cur_tuple = (nums[i], nums[j], nums[k], nums[_l])
                        if cur_tuple not in res:  # avoid duplicated result
                            res.add(cur_tuple)

                        while k < _l and nums[k] == nums[k + 1]:  # skip duplicated nums[k]
                            k += 1
                        k += 1

                        while k < _l and nums[_l] == nums[_l - 1]:  # skip duplicated nums[_l]
                            _l -= 1
                        _l -= 1
                    elif cur_sum < cur_target_kl:
                        k += 1
                    else:
                        _l -= 1

        return [list(item) for item in res]


def main():
    # Example 1: Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    # Example 2: Output: [[2,2,2,2]]
    # nums = [2, 2, 2, 2, 2]
    # target = 8

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.fourSum(nums, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
