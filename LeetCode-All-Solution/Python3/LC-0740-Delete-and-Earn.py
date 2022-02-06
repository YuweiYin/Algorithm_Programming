#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0740-Delete-and-Earn.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-06
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0740 - (Medium) - Delete and Earn
https://leetcode.com/problems/delete-and-earn/

Description & Requirement:
    You are given an integer array nums. You want to maximize the number of points you get 
    by performing the following operation any number of times:
        Pick any nums[i] and delete it to earn nums[i] points. 
            Afterwards, you must delete every element equal to nums[i] - 1 
            and every element equal to nums[i] + 1.

    Return the maximum number of points you can earn by applying the above operation some number of times.

Example 1:
    Input: nums = [3,4,2]
    Output: 6
    Explanation: You can perform the following operations:
        - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
        - Delete 2 to earn 2 points. nums = [].
        You earn a total of 6 points.
Example 2:
    Input: nums = [2,2,3,3,3,4]
    Output: 9
    Explanation: You can perform the following operations:
        - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
        - Delete a 3 again to earn 3 points. nums = [3].
        - Delete a 3 once more to earn 3 points. nums = [].
        You earn a total of 9 points.

Constraints:
    1 <= nums.length <= 2 * 10^4
    1 <= nums[i] <= 10^4
"""


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1]) if abs(nums[0] - nums[1]) == 1 else (nums[0] + nums[1])
        # main method: (hash dict + sort + Dynamic Programming)
        #     count each num (say, K different nums), and sort by num (get d_n_list), then consider choosing each num
        #     Dynamic Programming: dp[i] is the max gain after considered i-index num of d_n_list, i = 0, 1, 2, ..., K-1
        #     if choose d_n_list[i], then if d_n_list[i+1] - d_n_list[i] == 1, then d_n_list[i+1] can't be chosen
        #     dp equation:
        #         dp[i] = dp[i-1] + d_n_list[i] * d_n_count[i]  if  d_n_list[i-1] + 1 != d_n_list[i]
        #         dp[i] = max(dp[i-1], dp[i-2] + d_n_list[i] * d_n_count[i])  if  d_n_list[i-1] + 1 == d_n_list[i]
        #     dp init: dp[0] = d_n_list[0] * d_n_count[0]
        #     dp init: dp[1] = max(dp[0], d_n_list[1] * d_n_count[1])  if  d_n_list[0] + 1 == d_n_list[1]
        #              dp[1] = dp[0] + d_n_list[1] * d_n_count[1]  if  d_n_list[0] + 1 != d_n_list[1]
        #     dp aim: get dp[-1]
        return self._deleteAndEarn(nums)

    def _deleteAndEarn(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums >= 3

        dict_nums = dict({})  # key: number; value: the counter of key number
        for num in nums:
            if num not in dict_nums:
                dict_nums[num] = 1
            else:
                dict_nums[num] += 1

        d_n_list = list(dict_nums.items())  # d_n_list[i][0] is num, d_n_list[i][1] is the counter of d_n_list[i][0]
        d_n_list.sort(key=lambda x: x[0])

        len_diff_nums = len(d_n_list)  # the number of different numbers

        # dp[i] is the max gain after considered i-index num of d_n_list, i = 0, 1, 2, ..., K-1
        dp = [0 for _ in range(len_diff_nums)]

        # dp init
        dp[0] = d_n_list[0][0] * d_n_list[0][1]
        if d_n_list[0][0] + 1 == d_n_list[1][0]:
            dp[1] = max(dp[0], d_n_list[1][0] * d_n_list[1][1])
        else:
            dp[1] = dp[0] + d_n_list[1][0] * d_n_list[1][1]

        # apply dp equation
        for i in range(2, len_diff_nums):
            if d_n_list[i - 1][0] + 1 == d_n_list[i][0]:
                dp[i] = max(dp[i - 1], dp[i - 2] + d_n_list[i][0] * d_n_list[i][1])
            else:
                dp[i] = dp[i - 1] + d_n_list[i][0] * d_n_list[i][1]

        # get dp aim
        return dp[-1]


def main():
    # Example 1: Output: 6
    # nums = [3, 4, 2]

    # Example 2: Output: 9
    # nums = [2, 2, 3, 3, 3, 4]

    # # Example 3: Output: 18
    nums = [1, 1, 1, 2, 4, 5, 5, 5, 6]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.deleteAndEarn(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
