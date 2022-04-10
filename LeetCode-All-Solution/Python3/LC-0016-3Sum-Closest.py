#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0016-3Sum-Closest.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-10
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0016 - (Medium) - 3Sum Closest
https://leetcode.com/problems/3sum-closest/

Description & Requirement:
    Given an integer array nums of length n and an integer target, 
    find three integers in nums such that the sum is closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.

Example 1:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:
    Input: nums = [0,0,0], target = 1
    Output: 0

Constraints:
    3 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    -10^4 <= target <= 10^4
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # exception case
        assert isinstance(target, int)
        assert isinstance(nums, list) and len(nums) >= 3
        # main method: (sort + 2Sum (two pointers))
        return self._threeSumClosest(nums, target)

    def _threeSumClosest(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        assert len_nums >= 3

        if len_nums == 3:
            return sum(nums)

        nums.sort()
        res = nums[0] + nums[1] + nums[2]

        for first_index in range(len_nums):
            if first_index > 0 and nums[first_index] == nums[first_index - 1]:
                continue  # skip adjacent same number

            second_index = first_index + 1
            third_index = len_nums - 1  # set the third number as the last one

            # scan search all valid second number
            while second_index < third_index:
                # update res
                cur_sum = nums[first_index] + nums[second_index] + nums[third_index]
                if cur_sum == target:
                    return target
                if abs(target - cur_sum) < abs(target - res):
                    res = cur_sum
                # move either second_index or third_index, shrink the window
                if cur_sum > target:
                    third_index -= 1
                else:
                    second_index += 1
                # pointer cross, break
                if second_index >= third_index:
                    break

        return res


def main():
    # Example 1: Output: 2
    nums = [-1, 2, 1, -4]
    target = 1

    # Example 2: Output: 0
    # nums = [0, 0, 0]
    # target = 1

    # Example 3: Output: 2
    # nums = [-1, 0, 1, 1, 55]
    # target = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.threeSumClosest(nums, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
