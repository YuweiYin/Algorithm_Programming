#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1636-Sort-Array-by-Increasing-Frequency.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-19
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1636 - (Easy) - Sort Array by Increasing Frequency
https://leetcode.com/problems/sort-array-by-increasing-frequency/

Description & Requirement:
    Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
    If multiple values have the same frequency, sort them in decreasing order.

    Return the sorted array.

Example 1:
    Input: nums = [1,1,2,2,2,3]
    Output: [3,1,1,2,2,2]
    Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:
    Input: nums = [2,3,1,3,2]
    Output: [1,3,3,2,2]
    Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:
    Input: nums = [-1,1,-6,4,5,-6,1,4,1]
    Output: [5,-1,4,4,-6,-6,1,1,1]

Constraints:
    1 <= nums.length <= 100
    -100 <= nums[i] <= 100
"""


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (hash dict & sort)
        return self._frequencySort(nums)

    def _frequencySort(self, nums: List[int]) -> List[int]:
        assert isinstance(nums, list) and len(nums) >= 1

        hash_dict = dict({})
        for num in nums:
            if num not in hash_dict:
                hash_dict[num] = 1
            else:
                hash_dict[num] += 1

        num_freq = list(hash_dict.items())
        num_freq.sort(key=lambda x: (x[1], -x[0]))

        res = []
        for num, freq in num_freq:
            for _ in range(freq):
                res.append(num)

        return res


def main():
    # Example 1: Output: [3,1,1,2,2,2]
    # nums = [1, 1, 2, 2, 2, 3]

    # Example 2: Output: [1,3,3,2,2]
    # nums = [2, 3, 1, 3, 2]

    # Example 3: Output: [5,-1,4,4,-6,-6,1,1,1]
    nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.frequencySort(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
