#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1770-Maximum-Score-from-Performing-Multiplication-Operations.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-16
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1770 - (Medium) - Maximum Score from Performing Multiplication Operations
https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

Description & Requirement:
    You are given two integer arrays nums and multipliers of size n and m respectively, 
    where n >= m. The arrays are 1-indexed.

    You begin with a score of 0. You want to perform exactly m operations. 
    On the ith operation (1-indexed), you will:
        Choose one integer x from either the start or the end of the array nums.
        Add multipliers[i] * x to your score.
        Remove x from the array nums.

    Return the maximum score after performing m operations.

Example 1:
    Input: nums = [1,2,3], multipliers = [3,2,1]
    Output: 14
    Explanation: An optimal solution is as follows:
        - Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
        - Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
        - Choose from the end, [1], adding 1 * 1 = 1 to the score.
        The total score is 9 + 4 + 1 = 14.
Example 2:
    Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
    Output: 102
    Explanation: An optimal solution is as follows:
        - Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
        - Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
        - Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
        - Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
        - Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
        The total score is 50 + 15 - 9 + 4 + 42 = 102.

Constraints:
    n == nums.length
    m == multipliers.length
    1 <= m <= 10^3
    m <= n <= 10^5
    -1000 <= nums[i], multipliers[i] <= 1000
"""


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and isinstance(multipliers, list) and 1 <= len(multipliers) <= len(nums)
        # main method: (dynamic programming)
        return self._maximumScore(nums, multipliers)

    def _maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
        Runtime: 7536 ms, faster than 63.29% of submissions for Maximum Score from Performing Multiplication Ops.
        Memory Usage: 23.3 MB, less than 97.48% of submissions for Maximum Score from Performing Multiplication Ops.
        """
        assert isinstance(nums, list) and isinstance(multipliers, list) and 1 <= len(multipliers) <= len(nums)
        m, n = len(multipliers), len(nums)

        # dp = [[0 for _ in range(1003)] for _ in range(1003)]
        # res = - int(1e9+7)
        # for i in range(1, m + 1):
        #     for j in range(i + 1):
        #         if j == 0:
        #             dp[j][i - j] = dp[j][i - j - 1] + nums[n - i - j] * multipliers[i - 1]
        #         elif j == i:
        #             dp[j][i - j] = dp[j - 1][i - j] + nums[j - 1] * multipliers[i - 1]
        #         else:
        #             dp[j][i - j] = max(dp[j][i - j - 1] + nums[n - i + j] * multipliers[i - 1],
        #                                dp[j - 1][i - j] + nums[j - 1] * multipliers[i - 1])
        #         if i == m:
        #             res = max(res, dp[j][i - j])
        #
        # return res

        dp = [0 for _ in range(m + 1)]
        for op in range(m - 1, -1, -1):
            next_row = dp.copy()
            for i in range(op, -1, -1):
                dp[i] = max(multipliers[op] * nums[i] + next_row[i + 1],
                            multipliers[op] * nums[n - 1 - (op - i)] + next_row[i])

        return dp[0]


def main():
    # Example 1: Output: 14
    # nums = [1, 2, 3]
    # multipliers = [3, 2, 1]

    # Example 2: Output: 102
    nums = [-5, -3, -3, -2, 7, 1]
    multipliers = [-10, -5, 3, 4, 6]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximumScore(nums, multipliers)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
