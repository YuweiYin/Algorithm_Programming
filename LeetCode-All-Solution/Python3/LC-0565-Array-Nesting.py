#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0565-Array-Nesting.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-17
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 0565 - (Medium) - Array Nesting
https://leetcode.com/problems/array-nesting/

Description & Requirement:
    You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

    You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:
        The first element in s[k] starts with the selection of the element nums[k] of index = k.
        The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
        We stop adding right before a duplicate element occurs in s[k].

    Return the longest length of a set s[k].

Example 1:
    Input: nums = [5,4,0,3,1,6,2]
    Output: 4
    Explanation: 
        nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
        One of the longest sets s[k]:
        s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}
Example 2:
    Input: nums = [0,1,2]
    Output: 1

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] < nums.length
    All the values of nums are unique.
"""


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        len_nums = len(nums)
        if len_nums == 1:
            return len_nums
        for num in nums:
            assert isinstance(num, int) and 0 <= num < len_nums
        # main method: (multi-source BFS)
        return self._longestConsecutive(nums)

    def _longestConsecutive(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 2

        visited = set()
        res = 0

        for start_num in nums:
            if start_num in visited:
                continue
            bfs_queue = collections.deque()
            bfs_queue.append(start_num)
            visited.add(start_num)
            cur_set_len = 1

            while len(bfs_queue) > 0:
                cur_num = bfs_queue.popleft()
                next_num = nums[cur_num]
                if next_num not in visited:
                    visited.add(next_num)
                    cur_set_len += 1
                    bfs_queue.append(next_num)
            res = max(res, cur_set_len)

        return res


def main():
    # Example 1: Output: 4
    nums = [5, 4, 0, 3, 1, 6, 2]

    # Example 2: Output: 1
    # nums = [0, 1, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.arrayNesting(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
