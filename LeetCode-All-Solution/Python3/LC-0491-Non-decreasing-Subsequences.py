#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0491-Non-decreasing-Subsequences.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-20
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0491 - (Medium) - Non-decreasing Subsequences
https://leetcode.com/problems/non-decreasing-subsequences/

Description & Requirement:
    Given an integer array nums, return all the different possible non-decreasing subsequences of the given array 
    with at least two elements. You may return the answer in any order.

Example 1:
    Input: nums = [4,6,7,7]
    Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
Example 2:
    Input: nums = [4,4,3,2,1]
    Output: [[4,4]]

Constraints:
    1 <= nums.length <= 15
    -100 <= nums[i] <= 100
"""


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (BFS + hash set)
        return self._findSubsequences(nums)

    def _findSubsequences(self, nums: List[int]) -> List[List[int]]:
        assert isinstance(nums, list) and len(nums) >= 1

        res = []
        queue = collections.deque([(nums, [])])
        while len(queue) > 0:
            cur_num, seq = queue.popleft()
            if len(seq) > 1:
                res.append(seq)
            hash_set = set()
            for idx, number in enumerate(cur_num):
                if number in hash_set:
                    continue
                if not seq or number >= seq[-1]:
                    hash_set.add(number)
                    queue.append((cur_num[idx + 1:], seq + [number]))

        return res


def main():
    # Example 1: Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
    # nums = [4, 6, 7, 7]

    # Example 2: Output: [[4,4]]
    nums = [4, 4, 3, 2, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findSubsequences(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
