#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1664-Ways-to-Make-a-Fair-Array.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-01-28
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1664 - (Medium) - Ways to Make a Fair Array
https://leetcode.com/problems/ways-to-make-a-fair-array/

Description & Requirement:
    You are given an integer array nums. You can choose exactly one index (0-indexed) and remove the element. 
    Notice that the index of the elements may change after the removal.

    For example, if nums = [6,1,7,4,1]:
        Choosing to remove index 1 results in nums = [6,7,4,1].
        Choosing to remove index 2 results in nums = [6,1,4,1].
        Choosing to remove index 4 results in nums = [6,1,7,4].

    An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.

    Return the number of indices that you could choose such that after the removal, nums is fair.

Example 1:
    Input: nums = [2,1,6,4]
    Output: 1
    Explanation:
        Remove index 0: [1,6,4] -> Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
        Remove index 1: [2,6,4] -> Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
        Remove index 2: [2,1,4] -> Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
        Remove index 3: [2,1,6] -> Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
        There is 1 index that you can remove to make nums fair.
Example 2:
    Input: nums = [1,1,1]
    Output: 3
    Explanation: You can remove any index and the remaining array is fair.
Example 3:
    Input: nums = [1,2,3]
    Output: 0
    Explanation: You cannot make a fair array after removing any index.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4
"""


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (dynamic programming)
        return self._waysToMakeFair(nums)

    def _waysToMakeFair(self, nums: List[int]) -> int:
        """
        Time: beats 88.73%; Space: beats 95.31%
        """
        assert isinstance(nums, list) and len(nums) >= 1

        res = 0
        odd1 = even1 = 0
        odd2 = even2 = 0

        for idx, num in enumerate(nums):
            if idx & 0x01 == 1:
                odd2 += num
            else:
                even2 += num

        for idx, num in enumerate(nums):
            if idx & 0x01 == 1:
                odd2 -= num
            else:
                even2 -= num

            if odd1 + even2 == odd2 + even1:
                res += 1

            if idx & 0x01 == 1:
                odd1 += num
            else:
                even1 += num

        return res


def main():
    # Example 1: Output: 1
    nums = [2, 1, 6, 4]

    # Example 2: Output: 3
    # nums = [1, 1, 1]

    # Example 3: Output: 0
    # nums = [1, 2, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.waysToMakeFair(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
