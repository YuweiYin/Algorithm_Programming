#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2465-Number-of-Distinct-Averages.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-04
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2465 - (Easy) - Number of Distinct Averages
https://leetcode.com/problems/number-of-distinct-averages/

Description & Requirement:
    You are given a 0-indexed integer array nums of even length.

    As long as nums is not empty, you must repetitively:
        Find the minimum number in nums and remove it.
        Find the maximum number in nums and remove it.
        Calculate the average of the two removed numbers.

    The average of two numbers a and b is (a + b) / 2.
        For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.

    Return the number of distinct averages calculated using the above process.

    Note that when there is a tie for a minimum or maximum number, any can be removed.

Example 1:
    Input: nums = [4,1,4,0,3,5]
    Output: 2
    Explanation:
        1. Remove 0 and 5, and the average is (0 + 5) / 2 = 2.5. Now, nums = [4,1,4,3].
        2. Remove 1 and 4. The average is (1 + 4) / 2 = 2.5, and nums = [4,3].
        3. Remove 3 and 4, and the average is (3 + 4) / 2 = 3.5.
        Since there are 2 distinct numbers among 2.5, 2.5, and 3.5, we return 2.
Example 2:
    Input: nums = [1,100]
    Output: 1
    Explanation:
    There is only one average to be calculated after removing 1 and 100, so we return 1.

Constraints:
    2 <= nums.length <= 100
    nums.length is even.
    0 <= nums[i] <= 100
"""


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 2
        # main method: (sort, dict, two pointers)
        return self._distinctAverages(nums)

    def _distinctAverages(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 2

        nums.sort()
        visited = set()
        left, right = 0, len(nums) - 1
        while left < right:
            visited.add(nums[left] + nums[right])
            left += 1
            right -= 1

        return len(visited)


def main():
    # Example 1: Output: 2
    nums = [4, 1, 4, 0, 3, 5]

    # Example 2: Output: 1
    # nums = [1, 100]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.distinctAverages(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
