#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-312-Burst-Balloons.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-04
=================================================================="""
import functools
import sys
import time
from typing import List

"""
LeetCode - 312 - (Hard) - Burst Balloons
https://leetcode.com/problems/burst-balloons/

Description:
    You are given n balloons, indexed from 0 to n - 1. 
    Each balloon is painted with a number on it represented by an array nums. 
    You are asked to burst all the balloons.

    If you burst the i-th balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
    If i - 1 or i + 1 goes out of bounds of the array, 
    then treat it as if there is a balloon with a 1 painted on it.

Requirement:
    Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:
    Input: nums = [3,1,5,8]
    Output: 167
    Explanation:
        nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
        coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:
    Input: nums = [1,5]
    Output: 10

Constraints:
    n == nums.length
    1 <= n <= 500
    0 <= nums[i] <= 100
"""


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # exception case
        if len(nums) <= 0:
            return 0
        # border case
        if len(nums) == 1:
            return nums[0]
        # main method: (Dynamic Programming & Memorized DFS): find all possible combinations and select the optimal one
        # return self._maxCoinsMemDFS(nums)
        return self._maxCoinsLoopDP(nums)

    def _maxCoinsMemDFS(self, nums: List[int]) -> int:
        len_num = len(nums)

        # @functools.lru_cache(maxsize=None)
        # def mem_dfs(left_index: int, right_index: int, leftmost_num: int, rightmost_num: int) -> int:
        #     """
        #     (Error) Burst balloons in the ordinary order: first burst A, then B, then C, etc.
        #     If a balloon burst, the neighbors of its left balloon and right balloon will change,
        #     so the `leftmost_num` and `rightmost_num` are used to tell the value of both ends in current interval.
        #     """
        #     # end recursion condition: there is no number in current interval
        #     if left_index > right_index:
        #         return 0
        #     # border case: there is only one number in current interval
        #     if left_index == right_index:
        #         return leftmost_num * nums[left_index] * rightmost_num
        #
        #     best_sum = 0  # the lowest sum
        #     for cur_index in range(left_index, right_index + 1):  # eg. [3, 5, 7] consider dfs lm*3*5 / 3*5*7 / 5*7*rm
        #         if cur_index == left_index:
        #             cur_balloon_coin = leftmost_num * nums[cur_index] * nums[cur_index + 1]
        #             cur_left_sum = 0
        #             cur_right_sum = mem_dfs(cur_index + 1, right_index, leftmost_num, rightmost_num)
        #         elif cur_index == right_index:
        #             cur_balloon_coin = nums[cur_index - 1] * nums[cur_index] * rightmost_num
        #             cur_left_sum = mem_dfs(left_index, cur_index - 1, leftmost_num, rightmost_num)
        #             cur_right_sum = 0
        #         else:
        #             cur_balloon_coin = nums[cur_index - 1] * nums[cur_index] * nums[cur_index + 1]
        #             # TODO: error: the left part and right part still interfere with each other
        #             #     eg. [3, 7, 5] cur_balloon = 7, then if 3 bursts first, then the left number of 5 is 1
        #             #         but if 5 bursts first, then the left number of 5 is 3.
        #             #         so, it's better to consider the reverse burst order: check the last burst one first
        #             cur_left_sum = mem_dfs(left_index, cur_index - 1, leftmost_num, nums[cur_index + 1])
        #             cur_right_sum = mem_dfs(cur_index + 1, right_index, nums[cur_index - 1], rightmost_num)
        #
        #         # update the sum
        #         cur_total_sum = cur_balloon_coin + cur_left_sum + cur_right_sum
        #         best_sum = max(best_sum, cur_total_sum)
        #
        #     return best_sum
        #
        # return mem_dfs(0, len_num - 1, 1, 1)

        extended_nums = [1] + nums + [1]  # add element 1 to both ends in order to avoid array index error

        @functools.lru_cache(maxsize=None)
        def mem_dfs(left_index: int, right_index: int) -> int:
            """
            Consider the last burst balloon first.
            If cur_index is the last burst balloon, then its left one and right one must burst earlier,
            and more importantly, these two parts don't rely on each other!
            e.g. in [4, 3, 7, 5, 8] the last burst is 7, then when 3 burst, its right balloon must be 7;
            when 5 burst, its left balloon must be 7.
            This means left part [4, 3] and right part [5, 8] are independent!

            It's important to explain cur_sum is NOT e_nums[cur_i - 1] + e_nums[cur_i] + e_nums[cur_i + 1]
            if in [1, 4, 3, 7, 5, 8, 1] the last burst is 7, then when 7 burst, the coin is 1*7*1,
            where 1 and 1 are e_nums[left_i] and e_nums[right_i] (initial left_i=0, right_i=max_i=6).
            before 7, the left interval is [1, 4, 3, 7] and left_i=0, right_i=4 (index of number 7)
            now if 4 is the last one to burst, which means 3 has burst earlier, so the coin is 1*4*7,
            where 1 and 7 are exactly e_nums[left_i] (e_nums[0]) and e_nums[right_i] (e_nums[4]) too. Perfect!

            - Equation: cur_sum = e_nums[l_i] * e_nums[cur_i] * e_nums[r_i] + dfs(l_i, cur_i) + dfs(cur_i, r_i)
            """
            # end recursion condition: there are less than 3 numbers in current interval
            if left_index + 1 >= right_index:
                return 0

            best_sum = 0  # the lowest sum
            for cur_index in range(left_index + 1, right_index):
                # the coin of bursting cur_index balloon
                cur_sum = extended_nums[left_index] * extended_nums[cur_index] * extended_nums[right_index]
                # add the best sums of two smaller intervals
                cur_sum += mem_dfs(left_index, cur_index) + mem_dfs(cur_index, right_index)
                # update the sum
                best_sum = max(best_sum, cur_sum)

            return best_sum

        return mem_dfs(0, len_num + 1)

    def _maxCoinsLoopDP(self, nums: List[int]) -> int:
        """
        - Equation: cur_sum = e_nums[l_i] * e_nums[cur_i] * e_nums[r_i] + dfs(l_i, cur_i) + dfs(cur_i, r_i)
        """
        len_num = len(nums)
        dp = [[0 for _ in range(len_num + 2)] for _ in range(len_num + 2)]  # (n+2) * (n+2)
        extended_nums = [1] + nums + [1]  # add element 1 to both ends in order to avoid array index error

        for left_index in range(len_num - 1, -1, -1):  # reverse order, search from the smallest interval
            for right_index in range(left_index + 2, len_num + 2):  # the last index is (len_num + 1)
                for cur_index in range(left_index + 1, right_index):  # cut the interval into two small intervals
                    # the coin of bursting cur_index balloon
                    cur_sum = extended_nums[left_index] * extended_nums[cur_index] * extended_nums[right_index]
                    # add the best sums of two smaller intervals
                    cur_sum += dp[left_index][cur_index] + dp[cur_index][right_index]
                    # update the sum
                    dp[left_index][right_index] = max(dp[left_index][right_index], cur_sum)

        # get the best_sum of interval [0: n+2]
        return dp[0][len_num + 1]


def main():
    # Example 1: Output: 167
    nums = [3, 1, 5, 8]

    # Example 2: Output: 10
    # nums = [1, 5]

    # Example 3: Output: 35
    # nums = [3, 1, 5]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxCoins(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
