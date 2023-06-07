#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2611-Mice-and-Cheese.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-07
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2611 - (Medium) - Mice and Cheese
https://leetcode.com/problems/mice-and-cheese/

Description & Requirement:
    There are two mice and n different types of cheese, 
    each type of cheese should be eaten by exactly one mouse.

    A point of the cheese with index i (0-indexed) is:
        reward1[i] if the first mouse eats it.
        reward2[i] if the second mouse eats it.

    You are given a positive integer array reward1, a positive integer array reward2, 
    and a non-negative integer k.

    Return the maximum points the mice can achieve if 
    the first mouse eats exactly k types of cheese.

Example 1:
    Input: reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2
    Output: 15
    Explanation: In this example, the first mouse eats the 2nd (0-indexed) and the 3rd types of cheese, 
        and the second mouse eats the 0th and the 1st types of cheese.
        The total points are 4 + 4 + 3 + 4 = 15.
        It can be proven that 15 is the maximum total points that the mice can achieve.
Example 2:
    Input: reward1 = [1,1], reward2 = [1,1], k = 2
    Output: 2
    Explanation: In this example, the first mouse eats the 0th (0-indexed) and 1st types of cheese, 
        and the second mouse does not eat any cheese.
        The total points are 1 + 1 = 2.
        It can be proven that 2 is the maximum total points that the mice can achieve.

Constraints:
    1 <= n == reward1.length == reward2.length <= 10^5
    1 <= reward1[i], reward2[i] <= 1000
    0 <= k <= n
"""


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # exception case
        assert isinstance(reward1, list) and len(reward1) >= 1
        assert isinstance(reward2, list) and len(reward1) == len(reward2)
        assert isinstance(k, int) and 0 <= k <= len(reward1)
        # main method: (sorting)
        return self._miceAndCheese(reward1, reward2, k)

    def _miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        assert isinstance(reward1, list) and len(reward1) >= 1
        assert isinstance(reward2, list) and len(reward1) == len(reward2)
        assert isinstance(k, int) and 0 <= k <= len(reward1)

        n = len(reward1)
        res = sum(reward2)

        diffs = [(r1 - r2) for r1, r2 in zip(reward1, reward2)]
        diffs.sort()

        for i in range(1, k + 1):
            res += diffs[n - i]

        return res


def main():
    # Example 1: Output: 15
    reward1 = [1, 1, 3, 4]
    reward2 = [4, 4, 1, 1]
    k = 2

    # Example 2: Output: 2
    # reward1 = [1, 1]
    # reward2 = [1, 1]
    # k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.miceAndCheese(reward1, reward2, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
