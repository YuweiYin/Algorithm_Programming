#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0042-Trapping-Rain-Water.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-12
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0042 - (Hard) - Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Description & Requirement:
    Given n non-negative integers representing an elevation map 
    where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
        In this case, 6 units of rain water (blue section) are being trapped.
Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9

Constraints:
    n == height.length
    1 <= n <= 2 * 10^4
    0 <= height[i] <= 10^5
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        # exception case
        if not isinstance(height, list) or len(height) <= 0:
            return 0  # Error input type
        if len(height) <= 2:
            return 0
        # main method: (1. brute force; 2. dynamic programming; 3. stack; 4. two pointers.)
        return self._trap(height)

    def _trap(self, height: List[int]) -> int:
        len_height = len(height)
        assert len_height >= 3

        def __trap_brute_force() -> int:
            """
            Time: O(n^2);  Space: O(1).
            """
            res = 0
            for cur_center in range(1, len_height):
                max_left, max_right = 0, 0

                # find the peak on the left side
                for find_peak in reversed(range(cur_center + 1)):
                    max_left = max(max_left, height[find_peak])

                # find the peak on the right side
                for find_peak in range(cur_center, len_height):
                    max_right = max(max_right, height[find_peak])

                # each step, plus a square: its width == 1, its height == (min(max_left, max_right) - height[i])
                res += min(max_left, max_right) - height[cur_center]

            return res

        def __trap_dynamic_programming() -> int:
            """
            Time: O(n);  Space: O(n).
            """
            res = 0

            max_left_dp = [0 for _ in range(len_height)]  # max_left_dp[i] is the highest left bar of bar i
            max_left_dp[0] = height[0]

            # from left to right, for each bar, record its highest left bar in max_left_dp table
            for cur_center in range(1, len_height):
                max_left_dp[cur_center] = max(height[cur_center], max_left_dp[cur_center - 1])

            max_right_dp = [0 for _ in range(len_height)]  # max_right_dp[i] is the highest right bar of bar i
            max_right_dp[-1] = height[-1]

            # from right to left, for each bar, record its highest right bar in max_right_dp table
            for cur_center in reversed(range(len_height - 1)):
                max_right_dp[cur_center] = max(height[cur_center], max_right_dp[cur_center + 1])

            # now, similar to __trap_brute_force(), calculate the capacity of each bar
            for cur_center in range(1, len_height):
                res += min(max_left_dp[cur_center], max_right_dp[cur_center]) - height[cur_center]

            return res

        def __trap_stack() -> int:
            """
            Time: O(n);  Space: O(n).
            """
            res = 0

            bar_stack = []  # bar_stack record indices, height[bar_stack[i]] is in descending order (top is the lowest)
            cursor = 0
            while cursor < len_height:
                # when the height of the new bar is larger than stack top bar, pop the stack top and get a rain capacity
                while len(bar_stack) > 0 and height[cursor] > height[bar_stack[-1]]:
                    top_index = bar_stack.pop()
                    if len(bar_stack) == 0:  # no left boundary, can't form a cavity to store rain
                        break
                    # now, height[bar_stack[-1]] is left boundary bar, height[cursor] is right boundary bar
                    #     height[top_index] is the bottom height of the cavity
                    cur_width = cursor - bar_stack[-1] - 1
                    cur_height = min(height[cursor], height[bar_stack[-1]]) - height[top_index]
                    res += cur_width * cur_height
                bar_stack.append(cursor)
                cursor += 1

            return res

        def __trap_two_pointers() -> int:
            """
            Time: O(n);  Space: O(1).
            """
            res = 0

            # considering __trap_dynamic_programming(), if max_left_dp[i] < max_right_dp[i],
            #     the cavity height will be determined by max_left_dp[i] (the lower one) instead of max_right_dp[i]
            # similarly, if max_right_dp[i] < max_left_dp[i],
            #     the cavity height will be determined by max_right_dp[i] (the lower one) instead of max_left_dp[i]
            # so change scan strategy: if the right side has a higher bar, go towards right; else go towards left.

            left_index, right_index = 0, len_height - 1
            max_left, max_right = 0, 0  # two pointers, record the max height bar on the left/right side of cur bar

            while left_index < right_index:
                if height[left_index] < height[right_index]:
                    # if the right side has a higher bar, go towards right
                    if height[left_index] >= max_left:
                        # update max_left and keep going right
                        max_left = height[left_index]
                    else:
                        # accumulate a capacity with width == 1
                        res += max_left - height[left_index]
                    left_index += 1
                else:
                    # if the left side has a higher bar, go towards left
                    if height[right_index] >= max_right:
                        # update max_right and keep going left
                        max_right = height[right_index]
                    else:
                        # accumulate a capacity with width == 1
                        res += max_right - height[right_index]
                    right_index -= 1

            return res

        # return __trap_brute_force()
        # return __trap_dynamic_programming()
        # return __trap_stack()
        return __trap_two_pointers()


def main():
    # Example 1: Output: 6
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    # Example 2: Output: 9
    # height = [4, 2, 0, 3, 2, 5]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.trap(height)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
