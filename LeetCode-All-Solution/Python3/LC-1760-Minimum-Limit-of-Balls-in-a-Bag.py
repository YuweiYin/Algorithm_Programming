#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1760-Minimum-Limit-of-Balls-in-a-Bag.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-20
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1760 - (Medium) - Minimum Limit of Balls in a Bag
https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

Description & Requirement:
    You are given an integer array nums where the ith bag contains nums[i] balls. 
    You are also given an integer maxOperations.

    You can perform the following operation at most maxOperations times:
        Take any bag of balls and divide it into two new bags with a positive number of balls.
        For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
        Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

    Return the minimum possible penalty after performing the operations.

Example 1:
    Input: nums = [9], maxOperations = 2
    Output: 3
    Explanation: 
        - Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
        - Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
        The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.
Example 2:
    Input: nums = [2,4,8,2], maxOperations = 4
    Output: 2
    Explanation:
        - Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
        - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
        - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
        - Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
        The bag with the most number of balls has 2 balls, so your penalty is 2, and you should return 2.

Constraints:
    1 <= nums.length <= 10^5
    1 <= maxOperations, nums[i] <= 10^9
"""


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(maxOperations, int) and maxOperations >= 1
        # main method: (binary search)
        return self._minimumSize(nums, maxOperations)

    def _minimumSize(self, nums: List[int], maxOperations: int) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(maxOperations, int) and maxOperations >= 1

        res = 0
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) >> 1
            ops = sum((num - 1) // mid for num in nums)
            if ops <= maxOperations:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res


def main():
    # Example 1: Output: 3
    # nums = [9]
    # maxOperations = 2

    # Example 2: Output: 2
    nums = [2, 4, 8, 2]
    maxOperations = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minimumSize(nums, maxOperations)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
