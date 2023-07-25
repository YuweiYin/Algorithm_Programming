#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2208-Minimum-Operations-to-Halve-Array-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-25
=================================================================="""

import sys
import time
from typing import List
import heapq
# import functools
# import itertools

"""
LeetCode - 2208 - (Medium) - Minimum Operations to Halve Array Sum
https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

Description & Requirement:
    You are given an array nums of positive integers. In one operation, 
    you can choose any number from nums and reduce it to exactly half the number. 
    (Note that you may choose this reduced number in future operations.)

    Return the minimum number of operations to reduce the sum of nums by at least half.

Example 1:
    Input: nums = [5,19,8,1]
    Output: 3
    Explanation: The initial sum of nums is equal to 5 + 19 + 8 + 1 = 33.
        The following is one of the ways to reduce the sum by at least half:
        Pick the number 19 and reduce it to 9.5.
        Pick the number 9.5 and reduce it to 4.75.
        Pick the number 8 and reduce it to 4.
        The final array is [5, 4.75, 4, 1] with a total sum of 5 + 4.75 + 4 + 1 = 14.75. 
        The sum of nums has been reduced by 33 - 14.75 = 18.25, 
            which is at least half of the initial sum, 18.25 >= 33/2 = 16.5.
        Overall, 3 operations were used so we return 3.
        It can be shown that we cannot reduce the sum by at least half in less than 3 operations.
Example 2:
    Input: nums = [3,8,20]
    Output: 3
    Explanation: The initial sum of nums is equal to 3 + 8 + 20 = 31.
        The following is one of the ways to reduce the sum by at least half:
        Pick the number 20 and reduce it to 10.
        Pick the number 10 and reduce it to 5.
        Pick the number 3 and reduce it to 1.5.
        The final array is [1.5, 8, 5] with a total sum of 1.5 + 8 + 5 = 14.5. 
        The sum of nums has been reduced by 31 - 14.5 = 16.5, 
            which is at least half of the initial sum, 16.5 >= 31/2 = 15.5.
        Overall, 3 operations were used so we return 3.
        It can be shown that we cannot reduce the sum by at least half in less than 3 operations.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^7
"""


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        # main method: (priority queue)
        return self._halveArray(nums)

    def _halveArray(self, nums: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1

        pq = []
        for num in nums:
            heapq.heappush(pq, -num)

        res = 0
        sum1 = sum(nums)
        sum2 = 0
        while sum2 < sum1 / 2:
            x = -heapq.heappop(pq)
            sum2 += int(x / 2)
            heapq.heappush(pq, -int(x / 2))
            res += 1

        return int(res)


def main():
    # Example 1: Output: 3
    nums = [5, 19, 8, 1]

    # Example 2: Output: 3
    # nums = [3, 8, 20]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.halveArray(nums)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
