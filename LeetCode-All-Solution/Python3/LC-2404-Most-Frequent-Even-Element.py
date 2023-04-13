#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2404-Most-Frequent-Even-Element.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-13
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 2404 - (Easy) - Most Frequent Even Element
https://leetcode.com/problems/most-frequent-even-element/

Description & Requirement:
    Given an integer array nums, return the most frequent even element.

    If there is a tie, return the smallest one. If there is no such element, return -1.

Example 1:
    Input: nums = [0,1,2,2,4,4,1]
    Output: 2
    Explanation:
        The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
        We return the smallest one, which is 2.
Example 2:
    Input: nums = [4,4,4,9,2,4]
    Output: 4
    Explanation: 4 is the even element appears the most.
Example 3:
    Input: nums = [29,47,21,41,13,37,25,7]
    Output: -1
    Explanation: There is no even element.

Constraints:
    1 <= nums.length <= 2000
    0 <= nums[i] <= 10^5
"""


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1 and all([num >= 0 for num in nums])
        # main method: (hash dict counter)
        return self._mostFrequentEven(nums)

    def _mostFrequentEven(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1 and all([num >= 0 for num in nums])

        counter = collections.Counter()
        for num in nums:
            if num & 0x01 == 0:
                counter[num] += 1

        res, count = -1, 0
        for cur_num, cur_cnt in counter.items():
            if res == -1 or cur_cnt > count or (cur_cnt == count and res > cur_num):
                res = cur_num
                count = cur_cnt

        return res


def main():
    # Example 1: Output: 2
    # nums = [0, 1, 2, 2, 4, 4, 1]

    # Example 2: Output: 4
    # nums = [4, 4, 4, 9, 2, 4]

    # Example 3: Output: -1
    nums = [29, 47, 21, 41, 13, 37, 25, 7]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.mostFrequentEven(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
