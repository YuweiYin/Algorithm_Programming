#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0798-Smallest-Rotation-with-Highest-Score.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-09
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0798 - (Hard) - Smallest Rotation with Highest Score
https://leetcode.com/problems/smallest-rotation-with-highest-score/

Description & Requirement:
    You are given an array nums. You can rotate it by a non-negative integer k 
    so that the array becomes [nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]]. 
    Afterward, any entries that are less than or equal to their index are worth one point.

    For example, if we have nums = [2,4,1,3,0], and we rotate by k = 2, it becomes [1,3,0,2,4]. 
    This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points], 
    0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].

    Return the rotation index k that corresponds to the highest score we can achieve if we rotated nums by it. 
    If there are multiple answers, return the smallest such index k.

Example 1:
    Input: nums = [2,3,1,4,0]
    Output: 3
    Explanation: Scores for each k are listed below: 
        k = 0,  nums = [2,3,1,4,0],    score 2
        k = 1,  nums = [3,1,4,0,2],    score 3
        k = 2,  nums = [1,4,0,2,3],    score 3
        k = 3,  nums = [4,0,2,3,1],    score 4
        k = 4,  nums = [0,2,3,1,4],    score 3
        So we should choose k = 3, which has the highest score.
Example 2:
    Input: nums = [1,3,0,2,4]
    Output: 0
    Explanation: nums will always have 3 points no matter how it shifts.
        So we will choose the smallest k, which is 0.

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] < nums.length
"""


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) > 0
        len_nums = len(nums)
        for num in nums:
            assert isinstance(num, int) and 0 <= num < len_nums
        # main method: (Brute Force)
        # diff[i] = nums[i] - i,  if diff[i] <= 0, then the i-th number can gain 1 score
        # if rotate index == k, then every diff[i] plus k (k <= i < len(nums)),
        #     and every diff[j] minus (len(nums) - k) (0 <= j < k)
        # return self._bestRotation(nums)  # Time: O(n^2)
        # optimization: use Difference Array to perform +1/-1 to all numbers in an interval
        return self._bestRotationDA(nums)  # Time: O(n)

    def _bestRotation(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums > 0

        nums_diff = []  # if nums_diff[i] <= 0, then the i-th number can gain 1 score
        for idx, num in enumerate(nums):
            nums_diff.append(num - idx)
        # print(nums_diff)

        res = 0
        best_score = 0
        # if rotate index == k, then every diff[i] plus k (k <= i < len(nums)),
        #     and every diff[j] minus (len(nums) - k) (0 <= j < k)
        for k in range(len_nums):
            cur_score = 0
            for j in range(k):  # this part can be optimized by Difference Array
                if nums_diff[j] + k - len_nums <= 0:
                    cur_score += 1
            for i in range(k, len_nums):  # this part can be optimized by Difference Array
                if nums_diff[i] + k <= 0:
                    cur_score += 1
            if cur_score > best_score:
                best_score = cur_score
                res = k

        return res

    def _bestRotationDA(self, nums: List[int]) -> int:
        """
        Runtime: 1032 ms, faster than 87.67% of Python3 online submissions for Smallest Rotation with Highest Score.
        Memory Usage: 27.9 MB, less than 30.14% of Python3 online submissions for Smallest Rotation with Highest Score.
        """
        len_nums = len(nums)
        assert len_nums > 0

        # originally, let the index of number N is I,
        # if 0 <= N <= I (I \in [N, L-1]), where L = len(nums), then number N can get 1 score, otherwise 0 score
        # after rotation (index = K), new index of N is I_new = (I - k + L) % L
        # if 0 <= N <= I_new (I_new \in [N, L-1]), then number N can get 1 score, otherwise 0 score
        #     i.e., N <= (I - k + L) % L <= L - 1, it means 1 score can be obtained when I + 1 <= k <= I - N + L
        #     in other words, no scores can be obtained when I + 1 > k or k > I - N + L
        # let score_diff[i] be (the total score when k == i) minus (the total score when k == i - 1)
        score_diff = [0 for _ in range(len_nums)]
        for idx, num in enumerate(nums):
            # if k in [boundary_1, boundary_2] then num will get 1 score, otherwise 0 score
            boundary_1 = (idx + 1) % len_nums
            boundary_2 = (idx - num + len_nums) % len_nums

            # if k == boundary_1 - 1, the current num get 0 score; if k == boundary_1, the current num get 1 score
            score_diff[boundary_1] += 1  # score_diff[boundary_1] signify this change, so plus 1

            # if k == boundary_2, the current num get 1 score; if k == boundary_2 + 1, the current num get 0 score
            score_diff[(boundary_2 + 1) % len_nums] -= 1  # score_diff[boundary_2 + 1] signify this change, so minus 1

        # init: score_diff[0] is the total score of original nums list
        for idx, num in enumerate(nums):
            if idx >= num:
                score_diff[0] += 1

        res = 0
        best_score = 0
        cur_score = 0
        for idx, diff in enumerate(score_diff):
            cur_score += diff
            if cur_score > best_score:  # update best score and the rotation index k
                best_score = cur_score
                res = idx

        return res


def main():
    # Example 1: Output: 3
    nums = [2, 3, 1, 4, 0]

    # Example 2: Output: 0
    # nums = [1, 3, 0, 2, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.bestRotation(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
