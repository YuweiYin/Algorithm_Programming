#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/Study-Plan/Algorithm/Algorithm-1
@File    : LC-35-Search-Insert-Position.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-01
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 35 - (Easy) - Search Insert Position
https://leetcode.com/problems/search-insert-position/

Description:
    Given a sorted array of distinct integers and a target value, return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.

Requirement:
    You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2
Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1
Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

Constraints:
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums contains distinct values sorted in ascending order.
    -10^4 <= target <= 10^4
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) == 0:
            return 0
        # main method: (loop) binary search of sorted list
        return self._searchInsert(nums, target)

    def _searchInsert(self, nums: List[int], target: int) -> int:
        start_index, end_index = 0, len(nums) - 1
        insert_index = 0
        while start_index <= end_index:
            cur_index = (end_index + start_index) >> 1  # current cursor
            cur_num = nums[cur_index]  # cache variable
            if start_index == end_index:  # border case: must decide the insert position now
                return start_index if (target <= cur_num) else (start_index + 1)
            if cur_num == target:  # 1. hit the target
                return cur_index
            elif cur_num < target:  # 2. go right
                start_index = cur_index + 1  # change interval
                insert_index = start_index  # adjust the possible insert index
            else:  # 3. go left
                end_index = cur_index - 1  # change interval
                insert_index = cur_index  # adjust the possible insert index
        return insert_index


def main():
    # Example 1: Output: 2
    # nums = [1, 3, 5, 6]
    # target = 5

    # Example 2: Output: 1
    # nums = [1, 3, 5, 6]
    # target = 2

    # Example 3: Output: 4
    # nums = [1,3,5,6]
    # target = 7

    # Example 4: Output: 0
    # nums = [1, 3, 5, 6]
    # target = 0

    # Example 5: Output: 0
    nums = [1, 3]
    target = 0

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.searchInsert(nums, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
