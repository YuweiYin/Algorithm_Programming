#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0384-Shuffle-an-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-02
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0384 - (Medium) - Shuffle an Array
https://leetcode.com/problems/shuffle-an-array/

Description & Requirement:
    Given an integer array nums, design an algorithm to randomly shuffle the array. 
    All permutations of the array should be equally likely as a result of the shuffling.

    Implement the Solution class:
        Solution(int[] nums) Initializes the object with the integer array nums.
        int[] reset() Resets the array to its original configuration and returns it.
        int[] shuffle() Returns a random shuffling of the array.

Example 1:
    Input
        ["Solution", "shuffle", "reset", "shuffle"]
        [[[1, 2, 3]], [], [], []]
    Output
        [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
    Explanation
        Solution solution = new Solution([1, 2, 3]);
        solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                               // Any permutation of [1,2,3] must be equally likely to be returned.
                               // Example: return [3, 1, 2]
        solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
        solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

Constraints:
    1 <= nums.length <= 200
    -10^6 <= nums[i] <= 10^6
    All the elements of nums are unique.
    At most 5 * 10^4 calls in total will be made to reset and shuffle.

-- To shuffle an array a of n elements (indices 0..n-1):

"""


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = self.nums.copy()  # original array back up

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        """
        Fisher–Yates shuffle (aka the Knuth shuffle) [Wiki](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)
        for i from n−1 downto 1 do
            j ← random integer such that 0 <= j <= i
            exchange a[j] and a[i]
        """
        import random

        # method 1: (trick) built-in function
        #     Runtime: 252 ms, faster than 98.23% of Python3 online submissions for Shuffle an Array.
        #     Memory Usage: 19.3 MB, less than 90.52% of Python3 online submissions for Shuffle an Array.
        # random.shuffle(self.nums)

        # method 2: Fisher–Yates shuffle (aka the Knuth shuffle)
        for i in reversed(range(len(self.nums))):
            j = random.randint(0, i)  # randomly choose a index j, such that 0 <= j <= i
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]  # swap

        return self.nums


def main():
    # Example 1: Output: [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
    #     Explanation
    #         Solution solution = new Solution([1, 2, 3]);
    #         solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
    #                                // Any permutation of [1,2,3] must be equally likely to be returned.
    #                                // Example: return [3, 1, 2]
    #         solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
    #         solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
    command_list = ["Solution", "shuffle", "reset", "shuffle"]
    param_list = [[[1, 2, 3]], [], [], []]
    nums = [1, 2, 3]

    # init instance
    # solution = Solution()

    # run & time
    start = time.process_time()
    obj = Solution(nums)
    assert len(command_list) == len(param_list)
    index = 1
    while index < len(command_list):
        if command_list[index] == "shuffle":
            print(obj.shuffle())
        elif command_list[index] == "reset":
            print(obj.reset())
        index += 1
    end = time.process_time()

    # show answer
    # print('\nAnswer:')
    # print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
