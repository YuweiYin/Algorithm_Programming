#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0985-Sum-of-Even-Numbers-After-Queries.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-21
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 0985 - (Medium) - Sum of Even Numbers After Queries
https://leetcode.com/problems/sum-of-even-numbers-after-queries/

Description & Requirement:
    You are given an integer array nums and an array queries where queries[i] = [val_i, index_i].

    For each query i, first, apply nums[index_i] = nums[index_i] + val_i, then print the sum of the even values of nums.

    Return an integer array answer where answer[i] is the answer to the ith query.

Example 1:
    Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
    Output: [8,6,2,4]
    Explanation: At the beginning, the array is [1,2,3,4].
        After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
        After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
        After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
        After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
Example 2:
    Input: nums = [1], queries = [[4,0]]
    Output: [0]

Constraints:
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    1 <= queries.length <= 10^4
    -10^4 <= val_i <= 10^4
    0 <= index_i < nums.length
"""


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(queries, list) and len(queries) >= 1
        # main method: (adjust the sum of even numbers after each step)
        return self._sumEvenAfterQueries(nums, queries)

    def _sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(queries, list) and len(queries) >= 1

        _sum = sum(val for val in nums if val & 0x01 == 0)
        res = []

        for val, index in queries:
            if nums[index] & 0x01 == 0:
                _sum -= nums[index]
            nums[index] += val

            if nums[index] & 0x01 == 0:
                _sum += nums[index]
            res.append(_sum)

        return res


def main():
    # Example 1: Output: [8,6,2,4]
    nums = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]

    # Example 2: Output: [0]
    # nums = [1]
    # queries = [[4, 0]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sumEvenAfterQueries(nums, queries)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
