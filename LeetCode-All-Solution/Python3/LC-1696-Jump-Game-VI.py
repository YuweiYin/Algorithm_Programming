#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1696-Jump-Game-VI.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-09
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1696 - (Medium) - Jump Game VI
https://leetcode.com/problems/jump-game-vi/

Description & Requirement:
    You are given a 0-indexed integer array nums and an integer k.

    You are initially standing at index 0. In one move, you can jump at most k steps forward 
    without going outside the boundaries of the array. 
    That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

    You want to reach the last index of the array (index n - 1). 
    Your score is the sum of all nums[j] for each index j you visited in the array.

    Return the maximum score you can get.

Example 1:
    Input: nums = [1,-1,-2,4,-7,3], k = 2
    Output: 7
    Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:
    Input: nums = [10,-5,-2,4,0,3], k = 3
    Output: 17
    Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:
    Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
    Output: 0

Constraints:
    1 <= nums.length, k <= 10^5
    -10^4 <= nums[i] <= 10^4
"""


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (use a monotonous deque to record the maximum of interval [i-k, i-1])
        return self._maxResult(nums, k)

    def _maxResult(self, nums: List[int], k: int) -> int:
        """
        Runtime: 1251 ms, faster than 79.25% of Python3 online submissions for Jump Game VI.
        Memory Usage: 27.7 MB, less than 58.81% of Python3 online submissions for Jump Game VI.
        """
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(k, int) and k >= 1

        len_nums = len(nums)
        dp = nums[:]

        queue = collections.deque()  # monotonous deque
        queue.append(0)

        for i in range(1, len_nums):
            while len(queue) > 0 and i - queue[0] > k:  # popleft until i - queue[0] <= k
                queue.popleft()
            dp[i] = dp[queue[0]] + nums[i]  # cur maximum
            # maintain the monotonous deque
            while len(queue) > 0 and dp[i] > dp[queue[-1]]:  # pop until dp[i] <= dp[queue[-1]]
                queue.pop()
            queue.append(i)

        return dp[-1]


def main():
    # Example 1: Output: 7
    # nums = [1, -1, -2, 4, -7, 3]
    # k = 2

    # Example 2: Output: 17
    # nums = [10, -5, -2, 4, 0, 3]
    # k = 3

    # Example 3: Output: 0
    nums = [1, -5, -20, 4, -1, 3, -6, -3]
    k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxResult(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
