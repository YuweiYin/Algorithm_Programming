#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0398-Random-Pick-Index.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-04-25
=================================================================="""

import sys
import time
from typing import List
import random
# import functools

"""
LeetCode - 0398 - (Medium) - Random Pick Index
https://leetcode.com/problems/random-pick-index/

Description & Requirement:
    Given an integer array nums with possible duplicates, randomly output the index of a given target number. 
    You can assume that the given target number must exist in the array.

    Implement the Solution class:
        Solution(int[] nums) Initializes the object with the array nums.
        int pick(int target) Picks a random index i from nums where nums[i] == target. 
            If there are multiple valid i's, then each index should have an equal probability of returning.

Example 1:
    Input
        ["Solution", "pick", "pick", "pick"]
        [[[1, 2, 3, 3, 3]], [3], [1], [3]]
    Output
        [null, 4, 0, 2]
    Explanation
        Solution solution = new Solution([1, 2, 3, 3, 3]);
        solution.pick(3); // It should return either index 2, 3, or 4 randomly. 
            Each index should have equal probability of returning.
        solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
        solution.pick(3); // It should return either index 2, 3, or 4 randomly. 
            Each index should have equal probability of returning.

Constraints:
    1 <= nums.length <= 2 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    target is an integer from nums.
    At most 10^4 calls will be made to pick.
"""


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums_dict = dict({})
        for idx, num in enumerate(nums):
            if num not in self.nums_dict:
                self.nums_dict[num] = [idx]
            else:
                self.nums_dict[num].append(idx)

    def pick(self, target: int) -> int:
        if target not in self.nums_dict:
            return -1
        else:
            idx_list = self.nums_dict[target]
            # assert isinstance(idx_list, list) and len(idx_list) >= 1
            random_idx = random.randint(0, len(idx_list) - 1)
            return idx_list[random_idx]


def main():
    # Example 1: Output: [null, 4, 0, 2]
    command_list = ["Solution", "pick", "pick", "pick"]
    param_list = [[[1, 2, 3, 3, 3]], [3], [1], [3]]

    # init instance
    # solution = Solution()
    obj = Solution(param_list[0][0])
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for cursor in range(1, len(command_list)):
        command = command_list[cursor]
        param = param_list[cursor]
        if command == "pick":
            if isinstance(param, list) and len(param) == 1:
                ans.append(obj.pick(param[0]))
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
