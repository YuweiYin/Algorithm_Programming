#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2044-Count-Number-of-Maximum-Bitwise-OR-Subsets.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-15
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 2044 - (Medium) - Count Number of Maximum Bitwise-OR Subsets
https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

Description & Requirement:
    Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and 
    return the number of different non-empty subsets with the maximum bitwise OR.

    An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. 
    Two subsets are considered different if the indices of the elements chosen are different.

    The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

Example 1:
    Input: nums = [3,1]
    Output: 2
    Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
    - [3]
    - [3,1]
Example 2:
    Input: nums = [2,2,2]
    Output: 7
    Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.
Example 3:
    Input: nums = [3,2,1,5]
    Output: 6
    Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
    - [3,5]
    - [3,1,5]
    - [3,2,5]
    - [3,2,1,5]
    - [2,5]
    - [2,1,5]

Constraints:
    1 <= nums.length <= 16
    1 <= nums[i] <= 10^5
"""


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) > 0
        # main method: (dfs & backtrace)
        return self._countMaxOrSubsets(nums)

    def _countMaxOrSubsets(self, nums: List[int]) -> int:
        len_nums = len(nums)
        assert len_nums > 0

        res = [0]
        max_or = [0]

        def __dfs(cur_idx: int, cur_or: int):
            if cur_idx == len_nums:
                if cur_or > max_or[0]:  # new max
                    max_or[0], res[0] = cur_or, 1
                elif cur_or == max_or[0]:  # another max
                    res[0] += 1
                return
            # next number
            __dfs(cur_idx + 1, cur_or | nums[cur_idx])  # bitwise or this number
            __dfs(cur_idx + 1, cur_or)  # don't bitwise or this number

        __dfs(0, 0)
        return res[0]


def main():
    # Example 1: Output: 2
    # nums = [3, 1]

    # Example 2: Output: 7
    # nums = [2, 2, 2]

    # Example 3: Output: 6
    nums = [3, 2, 1, 5]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countMaxOrSubsets(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
