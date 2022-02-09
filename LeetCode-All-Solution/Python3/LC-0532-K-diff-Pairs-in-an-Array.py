#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0532-K-diff-Pairs-in-an-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-09
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0532 - (Medium) - K-diff Pairs in an Array
https://leetcode.com/problems/k-diff-pairs-in-an-array/

Description & Requirement:
    Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

    A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

    0 <= i < j < nums.length
    |nums[i] - nums[j]| == k
    Notice that |val| denotes the absolute value of val.

Example 1:
    Input: nums = [3,1,4,1,5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
    Input: nums = [1,2,3,4,5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
    Input: nums = [1,3,1,5,4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).

Constraints:
    1 <= nums.length <= 10^4
    -10^7 <= nums[i] <= 10^7
    0 <= k <= 10^7

Related Problem:
    LC-2006-Count-Number-of-Pairs-With-Absolute-Difference-K
"""


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # exception case
        if not isinstance(nums, list) or len(nums) <= 0:
            return 0  # Error input type
        if len(nums) == 1 or k < 0:
            return 0
        if len(nums) == 2:
            return 1 if abs(nums[0] - nums[1]) == k else 0
        # main method: (create hash set nums_set, scan once)
        #     for each nums[i], check if (nums[i] - k) and (nums[i] + k) in nums_set
        return self._findPairs(nums, k)

    def _findPairs(self, nums: List[int], k: int) -> int:
        len_nums = len(nums)
        assert len_nums >= 3

        if k > 0:
            res_set = set()
            nums_set = set(nums)
            for num in nums:
                if num - k in nums_set:
                    if (num - k, num) not in res_set:  # avoid repeat answer
                        res_set.add((num - k, num))
                if num + k in nums_set:
                    if (num, num + k) not in res_set:
                        res_set.add((num, num + k))
            return len(res_set)
        else:  # k == 0
            res = 0
            nums_dict = dict({})  # key: number; counter of this number
            for num in nums:
                if num not in nums_dict:
                    nums_dict[num] = 1
                else:
                    nums_dict[num] += 1
            for num, counter in nums_dict.items():
                if counter >= 2:  # appear more than once, just count 1 pair
                    res += 1
            return res


def main():
    # Example 1: Output: 2
    # nums = [3, 1, 4, 1, 5]
    # k = 2

    # Example 2: Output: 4
    # nums = [1, 2, 3, 4, 5]
    # k = 1

    # Example 3: Output: 1
    # nums = [1, 3, 1, 5, 4]
    # k = 0

    # Example 4: Output: 2
    nums = [1, 2, 4, 4, 3, 3, 0, 9, 2, 3]
    k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findPairs(nums, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
