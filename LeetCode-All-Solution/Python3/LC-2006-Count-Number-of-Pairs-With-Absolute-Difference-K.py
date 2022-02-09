#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2006-Count-Number-of-Pairs-With-Absolute-Difference-K.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-09
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 2006 - (Easy) - Count Number of Pairs With Absolute Difference K
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

Description & Requirement:
    Given an integer array nums and an integer k, 
    return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

    The value of |x| is defined as:
        x if x >= 0.
        -x if x < 0.

Example 1:
    Input: nums = [1,2,2,1], k = 1
    Output: 4
    Explanation: The pairs with an absolute difference of 1 are:
        - [*1*, *2*, 2, 1]
        - [*1*, 2, *2*, 1]
        - [1, *2*, 2, *1*]
        - [1, 2, *2*, *1*]
Example 2:
    Input: nums = [1,3], k = 3
    Output: 0
    Explanation: There are no pairs with an absolute difference of 3.
Example 3:
    Input: nums = [3,2,1,5,4], k = 2
    Output: 3
    Explanation: The pairs with an absolute difference of 2 are:
        - [*3*, 2, *1*, 5, 4]
        - [*3*, 2, 1, *5*, 4]
        - [3, *2*, 1, 5, *4*]

Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= 100
    1 <= k <= 99

Related Problem:
    LC-0532-K-diff-Pairs-in-an-Array
"""


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1 or k <= 0:
            return 0
        # main method: (create hash dict nums_dict, scan once)
        #     key: each number; value: (list) the indices.
        #     for each nums[i], check if (nums[i] - k) and (nums[i] + k) in nums_dict and `i` is the lower index
        return self._countKDifference(nums, k)

    def _countKDifference(self, nums: List[int], k: int) -> int:
        len_nums = len(nums)
        assert len_nums >= 2

        res = 0
        nums_dict = dict({})

        # record indices list
        for idx, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = [idx]
            else:
                nums_dict[num].append(idx)

        # for each nums[i], check if (nums[i] - k) and (nums[i] + k) in nums_dict and `i` is the lower index
        for idx, num in enumerate(nums):
            if (num - k) in nums_dict:
                index_list = nums_dict[num - k]
                for index in index_list:
                    if idx < index:
                        res += 1
            if (num + k) in nums_dict:
                index_list = nums_dict[num + k]
                for index in index_list:
                    if idx < index:
                        res += 1

        return res


def main():
    # Example 1: Output: 4
    nums = [1, 2, 2, 1]
    k = 1

    # Example 2: Output: 0
    # nums = [1, 3]
    # k = 3

    # Example 3: Output: 3
    # nums = [3, 2, 1, 5, 4]
    # k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countKDifference(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
