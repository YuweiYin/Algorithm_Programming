#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0045-Jump-Game-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-26
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0045 - (Medium) - Jump Game II
https://leetcode.com/problems/jump-game-ii/

Description & Requirement:
    Given an array of non-negative integers nums, 
    you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Your goal is to reach the last index in the minimum number of jumps.

    You can assume that you can always reach the last index.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2. 
        Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
    Input: nums = [2,3,0,1,4]
    Output: 2

Constraints:
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 1000
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return 0  # don't need any jump
        if len(nums) == 2:
            assert nums[0] > 0  # You can assume that you can always reach the last index.
            return 1  # only need one jump
        # main method: (Dynamic Programming: dp[i] means the min jump number to get nums[i])
        #     consider each nums[i], update dp value. aim: dp[-1]
        return self._jump(nums)

    def _jump(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums > 2

        INF = int(1e9+7)
        dp = [INF for _ in range(len_nums)]  # dp[i] means the min jump number to get nums[i]
        dp[0] = 0
        cur_index = 0  # start position
        max_reach_index = nums[cur_index]  # init max reachable position

        while cur_index <= max_reach_index:  # consider each reachable position
            # if max_reach_index >= len_nums - 1:  # able to reach the end
            #     break
            max_reach_index = max(max_reach_index, cur_index + nums[cur_index])  # may expand the while loop boundary
            for index in range(cur_index + 1, cur_index + 1 + nums[cur_index]):
                if index >= len_nums:  # avoid out of index
                    break
                dp[index] = min(dp[index], dp[cur_index] + 1)  # update dp value
            if dp[-1] != INF:
                break
            cur_index += 1

        return dp[-1]


def main():
    # Example 1: Output: 2
    nums = [2, 3, 1, 1, 4]

    # Example 2: Output: 2
    # nums = [2, 3, 0, 1, 4]

    # Example 3: Output: 1
    # nums = [3, 2, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.jump(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
