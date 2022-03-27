#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2028-Find-Missing-Observations.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-27
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 2028 - (Medium) - Find Missing Observations
https://leetcode.com/problems/find-missing-observations/

Description & Requirement:
    You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. 
    n of the observations went missing, and you only have the observations of m rolls. 
    Fortunately, you have also calculated the average value of the n + m rolls.

    You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. 
    You are also given the two integers mean and n.

    Return an array of length n containing the missing observations 
    such that the average value of the n + m rolls is exactly mean. 
    If there are multiple valid answers, return any of them. 
    If no such array exists, return an empty array.

    The average value of a set of k numbers is the sum of the numbers divided by k.

    Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

Example 1:
    Input: rolls = [3,2,4,3], mean = 4, n = 2
    Output: [6,6]
    Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
Example 2:
    Input: rolls = [1,5,6], mean = 3, n = 4
    Output: [2,3,2,2]
    Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
Example 3:
    Input: rolls = [1,2,3,4], mean = 6, n = 4
    Output: []
    Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.

Constraints:
    m == rolls.length
    1 <= n, m <= 10^5
    1 <= rolls[i], mean <= 6
"""


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # exception case
        assert isinstance(rolls, list) and len(rolls) > 0
        assert isinstance(mean, int) and 1 <= mean <= 6
        assert isinstance(n, int) and n > 0
        # main method: (first, make up all n observations by 1, then add number)
        return self._missingRolls(rolls, mean, n)

    def _missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        assert m > 0 and n > 0 and 1 <= mean <= 6

        res = [1 for _ in range(n)]
        cur_sum = sum(rolls) + n
        target_sum = mean * (m + n)

        if cur_sum == target_sum:
            return res
        if cur_sum > target_sum:  # cur_sum can't be smaller
            return []

        res_idx = 0
        while cur_sum < target_sum:
            if res_idx < n:
                if res[res_idx] == 6:  # cur dice reaches max number, change it
                    res_idx += 1
                else:
                    res[res_idx] += 1
                    cur_sum += 1
            else:  # cur_sum can't be bigger
                return []

        return res


def main():
    # Example 1: Output: [6,6]
    # rolls = [3, 2, 4, 3]
    # mean = 4
    # n = 2

    # Example 2: Output: [2,3,2,2]
    # rolls = [1, 5, 6]
    # mean = 3
    # n = 4

    # Example 3: Output: []
    rolls = [1, 2, 3, 4]
    mean = 6
    n = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.missingRolls(rolls, mean, n)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
