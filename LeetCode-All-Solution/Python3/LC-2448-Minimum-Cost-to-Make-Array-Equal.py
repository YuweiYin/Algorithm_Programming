#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2448-Minimum-Cost-to-Make-Array-Equal.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-21
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
import itertools

"""
LeetCode - 2448 - (Hard) - Minimum Cost to Make Array Equal
https://leetcode.com/problems/minimum-cost-to-make-array-equal/

Description & Requirement:
    You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

    You can do the following operation any number of times:
        Increase or decrease any element of the array nums by 1.

    The cost of doing one operation on the ith element is cost[i].

    Return the minimum total cost such that all the elements of the array nums become equal.

Example 1:
    Input: nums = [1,3,5,2], cost = [2,3,1,14]
    Output: 8
    Explanation: We can make all the elements equal to 2 in the following way:
        - Increase the 0th element one time. The cost is 2.
        - Decrease the 1st element one time. The cost is 3.
        - Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
        The total cost is 2 + 3 + 3 = 8.
        It can be shown that we cannot make the array equal with a smaller cost.
Example 2:
    Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
    Output: 0
    Explanation: All the elements are already equal, so no operations are needed.

Constraints:
    n == nums.length == cost.length
    1 <= n <= 10^5
    1 <= nums[i], cost[i] <= 10^6
"""


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # exception case
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(cost, list) and len(cost) == len(nums)
        # main method: (enumerate)
        return self._minCost(nums, cost)

    def _minCost(self, nums: List[int], cost: List[int]) -> int:
        assert isinstance(nums, list) and len(nums) >= 1
        assert isinstance(cost, list) and len(cost) == len(nums)

        def pairwise(iterable):
            # pairwise('ABCDEFG') --> AB BC CD DE EF FG
            a, b = itertools.tee(iterable)
            next(b, None)
            return zip(a, b)

        array = sorted(zip(nums, cost))
        res = total = sum((x - array[0][0]) * c for x, c in array)
        sum_cost = sum(cost)
        for (x0, c), (x1, _) in pairwise(array):
            sum_cost -= c * 2
            total -= sum_cost * (x1 - x0)
            res = min(res, total)

        return res


def main():
    # Example 1: Output: 8
    nums = [1, 3, 5, 2]
    cost = [2, 3, 1, 14]

    # Example 2: Output: 0
    # nums = [2, 2, 2, 2, 2]
    # cost = [4, 2, 8, 1, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minCost(nums, cost)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
