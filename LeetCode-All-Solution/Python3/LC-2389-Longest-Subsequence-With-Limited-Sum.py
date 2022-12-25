#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2389-Longest-Subsequence-With-Limited-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-25
=================================================================="""

import sys
import time
from typing import List
import bisect
# import collections
# import functools

"""
LeetCode - 2389 - (Easy) - Longest Subsequence With Limited Sum
https://leetcode.com/problems/longest-subsequence-with-limited-sum/

Description & Requirement:
    You are given an integer array nums of length n, and an integer array queries of length m.

    Return an array answer of length m where answer[i] is the maximum size of a subsequence that 
    you can take from nums such that the sum of its elements is less than or equal to queries[i].

    A subsequence is an array that can be derived from another array by deleting some or no elements 
    without changing the order of the remaining elements.

Example 1:
    Input: nums = [4,5,2,1], queries = [3,10,21]
    Output: [2,3,4]
    Explanation: We answer the queries as follows:
    - The subsequence [2,1] has a sum less than or equal to 3. 
        It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
    - The subsequence [4,5,1] has a sum less than or equal to 10. 
        It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
    - The subsequence [4,5,2,1] has a sum less than or equal to 21. 
        It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
Example 2:
    Input: nums = [2,3,4,5], queries = [1]
    Output: [0]
    Explanation: The empty subsequence is the only subsequence 
        that has a sum less than or equal to 1, so answer[0] = 0.

Constraints:
    n == nums.length
    m == queries.length
    1 <= n, m <= 1000
    1 <= nums[i], queries[i] <= 10^6
"""


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(queries, list) and len(queries) >= 1
        # main method: (prefix sum)
        return self._answerQueries(nums, queries)

    def _answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        Time: beats 93.11%; Space: beats 40.29%
        """
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(queries, list) and len(queries) >= 1

        nums.sort()
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx - 1]

        for idx, q in enumerate(queries):
            queries[idx] = bisect.bisect_right(nums, q)

        return queries


def main():
    # Example 1: Output: [2,3,4]
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]

    # Example 2: Output: [0]
    # nums = [2, 3, 4, 5]
    # queries = [1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.answerQueries(nums, queries)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
