#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0268-Missing-Number.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-28
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0268 - (Easy) - Missing Number
https://leetcode.com/problems/missing-number/

Description & Requirement:
    Given an array nums containing n distinct numbers in the range [0, n], 
    return the only number in the range that is missing from the array.

Example 1:
    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
        2 is the missing number in the range since it does not appear in nums.
Example 2:
    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
        2 is the missing number in the range since it does not appear in nums.
Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
        8 is the missing number in the range since it does not appear in nums.

Constraints:
    n == nums.length
    1 <= n <= 10^4
    0 <= nums[i] <= n
    All the numbers of nums are unique.

Follow up:
    Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (1. XOR; 2. Arithmetic Progression.)
        # return self._missingNumberXOR(nums)
        return self._missingNumberAP(nums)

    def _missingNumberXOR(self, nums: List[int]) -> int:
        """
        Runtime: 148 ms, faster than 77.79% of Python3 online submissions for Missing Number.
        Memory Usage: 15.3 MB, less than 34.52% of Python3 online submissions for Missing Number.
        """
        assert isinstance(nums, list) and len(nums) >= 1
        n = len(nums)

        res = nums[0]
        for num in nums[1:]:
            res ^= num
        for num in range(n + 1):
            res ^= num

        return res

    def _missingNumberAP(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        n = len(nums)

        expected_sum = int(n * (n + 1)) >> 1
        current_sum = sum(nums)

        return expected_sum - current_sum


def main():
    # Example 1: Output: 2
    # nums = [3, 0, 1]

    # Example 2: Output: 2
    # nums = [0, 1]

    # Example 3: Output: 8
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.missingNumber(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
