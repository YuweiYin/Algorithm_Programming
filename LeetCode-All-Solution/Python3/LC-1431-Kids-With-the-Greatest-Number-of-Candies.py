#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1431-Kids-With-the-Greatest-Number-of-Candies.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-17
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1431 - (Easy) - Kids With the Greatest Number of Candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

Description & Requirement:
    There are n kids with candies. You are given an integer array candies, 
    where each candies[i] represents the number of candies the ith kid has, and 
    an integer extraCandies, denoting the number of extra candies that you have.

    Return a boolean array result of length n, where result[i] is true if, 
    after giving the ith kid all the extraCandies, they will have the greatest number of candies 
    among all the kids, or false otherwise.

    Note that multiple kids can have the greatest number of candies.

Example 1:
    Input: candies = [2,3,5,1,3], extraCandies = 3
    Output: [true,true,true,false,true] 
    Explanation: If you give all extraCandies to:
        - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
        - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
        - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
        - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
        - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Example 2:
    Input: candies = [4,2,1,1,2], extraCandies = 1
    Output: [true,false,false,false,false] 
    Explanation: There is only 1 extra candy.
        Kid 1 will always have the greatest number of candies, 
        even if a different kid is given the extra candy.
Example 3:
    Input: candies = [12,1,12], extraCandies = 10
    Output: [true,false,true]

Constraints:
    n == candies.length
    2 <= n <= 100
    1 <= candies[i] <= 100
    1 <= extraCandies <= 50
"""


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # exception case
        assert isinstance(candies, list) and len(candies) >= 2
        assert isinstance(extraCandies, int) and extraCandies >= 1
        # main method: (scan the array)
        return self._kidsWithCandies(candies, extraCandies)

    def _kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        assert isinstance(candies, list) and len(candies) >= 2
        assert isinstance(extraCandies, int) and extraCandies >= 1

        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]


def main():
    # Example 1: Output: [true,true,true,false,true]
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3

    # Example 2: Output: [true,false,false,false,false]
    # candies = [4, 2, 1, 1, 2]
    # extraCandies = 1

    # Example 3: Output: [true,false,true]
    # candies = [12, 1, 12]
    # extraCandies = 10

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.kidsWithCandies(candies, extraCandies)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
