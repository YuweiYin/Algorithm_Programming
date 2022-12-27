#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2279-Maximum-Bags-With-Full-Capacity-of-Rocks.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-27
=================================================================="""

import sys
import time
from typing import List
import bisect
from itertools import accumulate
# import collections
# import functools

"""
LeetCode - 2279 - (Medium) - Maximum Bags With Full Capacity of Rocks
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

Description & Requirement:
    You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks. 
    The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. 
    You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.

    Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.

Example 1:
    Input: capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
    Output: 3
    Explanation:
        Place 1 rock in bag 0 and 1 rock in bag 1.
        The number of rocks in each bag are now [2,3,4,4].
        Bags 0, 1, and 2 have full capacity.
        There are 3 bags at full capacity, so we return 3.
        It can be shown that it is not possible to have more than 3 bags at full capacity.
        Note that there may be other ways of placing the rocks that result in an answer of 3.
Example 2:
    Input: capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100
    Output: 3
    Explanation:
        Place 8 rocks in bag 0 and 2 rocks in bag 2.
        The number of rocks in each bag are now [10,2,2].
        Bags 0, 1, and 2 have full capacity.
        There are 3 bags at full capacity, so we return 3.
        It can be shown that it is not possible to have more than 3 bags at full capacity.
        Note that we did not use all of the additional rocks.

Constraints:
    n == capacity.length == rocks.length
    1 <= n <= 5 * 10^4
    1 <= capacity[i] <= 10^9
    0 <= rocks[i] <= capacity[i]
    1 <= additionalRocks <= 10^9
"""


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # exception case
        assert isinstance(capacity, list) and len(capacity) >= 1
        assert isinstance(rocks, list) and len(rocks) == len(capacity)
        assert isinstance(additionalRocks, int) and additionalRocks >= 1
        # main method: (greedy & prefix sum & binary search)
        return self._maximumBags(capacity, rocks, additionalRocks)

    def _maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        """
        Time: beats 98.36%; Space: beats 16.12%
        """
        assert isinstance(capacity, list) and len(capacity) >= 1
        assert isinstance(rocks, list) and len(rocks) == len(capacity)
        assert isinstance(additionalRocks, int) and additionalRocks >= 1

        prefix_sum = list(accumulate(sorted(x - y for x, y in zip(capacity, rocks))))
        return bisect.bisect_right(prefix_sum, additionalRocks)


def main():
    # Example 1: Output: 3
    # capacity = [2, 3, 4, 5]
    # rocks = [1, 2, 4, 4]
    # additionalRocks = 2

    # Example 2: Output: 3
    capacity = [10, 2, 2]
    rocks = [2, 2, 0]
    additionalRocks = 100

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximumBags(capacity, rocks, additionalRocks)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
