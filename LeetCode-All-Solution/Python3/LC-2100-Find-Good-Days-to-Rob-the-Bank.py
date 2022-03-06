#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2100-Find-Good-Days-to-Rob-the-Bank.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-06
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 2100 - (Medium) - Find Good Days to Rob the Bank
https://leetcode.com/problems/find-good-days-to-rob-the-bank/

Description & Requirement:
    You and a gang of thieves are planning on robbing a bank. 
    You are given a 0-indexed integer array security, 
    where security[i] is the number of guards on duty on the ith day. 
    The days are numbered starting from 0. You are also given an integer time.

    The ith day is a good day to rob the bank if:
        There are at least time days before and after the ith day,
        The number of guards at the bank for the time days before i are non-increasing, and
        The number of guards at the bank for the time days after i are non-decreasing.

    More formally, this means day i is a good day to rob the bank if and only if 
    security[i - time] >= security[i - time + 1] >= ... >= security[i] 
    <= ... <= security[i + time - 1] <= security[i + time].

    Return a list of all days (0-indexed) that are good days to rob the bank. 
    The order that the days are returned in does not matter.

Example 1:
    Input: security = [5,3,3,3,5,6,2], time = 2
    Output: [2,3]
    Explanation:
        On day 2, we have security[0] >= security[1] >= security[2] <= security[3] <= security[4].
        On day 3, we have security[1] >= security[2] >= security[3] <= security[4] <= security[5].
        No other days satisfy this condition, so days 2 and 3 are the only good days to rob the bank.
Example 2:
    Input: security = [1,1,1,1,1], time = 0
    Output: [0,1,2,3,4]
    Explanation:
        Since time equals 0, every day is a good day to rob the bank, so return every day.
Example 3:
    Input: security = [1,2,3,4,5,6], time = 2
    Output: []
    Explanation:
        No day has 2 days before it that have a non-increasing number of guards.
        Thus, no day is a good day to rob the bank, so return an empty list.

Constraints:
    1 <= security.length <= 10^5
    0 <= security[i], time <= 10^5
"""


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # exception case
        assert isinstance(security, list) and len(security) > 0
        # main method: (1-dim dynamic programming to get the non_increase_left and non_increase_right list)
        #     non_increase_left[i] is the number consecutive non-increasing security of day i (from left to right)
        #     non_increase_right[i] is the number consecutive non-increasing security of day i (from right to left)
        return self._goodDaysToRobBank(security, time)

    def _goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        len_security = len(security)
        assert len_security > 0

        # non_increase_left[i] is the number consecutive non-increasing security of day i (from left to right)
        # non_increase_right[i] is the number consecutive non-increasing security of day i (from right to left)
        non_increase_left = [1 for _ in range(len_security)]
        non_increase_right = [1 for _ in range(len_security)]

        index = 1
        while index < len_security:  # get non_increase_left
            if security[index] <= security[index - 1]:  # non-increasing
                non_increase_left[index] = non_increase_left[index - 1] + 1
            else:  # increasing
                non_increase_left[index] = 1  # reset
            index += 1

        index = len_security - 2
        while index >= 0:  # get non_increase_right
            if security[index] <= security[index + 1]:  # non-increasing
                non_increase_right[index] = non_increase_right[index + 1] + 1
            else:  # increasing
                non_increase_right[index] = 1  # reset
            index -= 1

        res = []
        index = 0
        while index < len_security:
            if non_increase_left[index] > time and non_increase_right[index] > time:
                res.append(index)
            index += 1

        return res


def main():
    # Example 1: Output: [2,3]
    # security = [5, 3, 3, 3, 5, 6, 2]
    # _time = 2

    # Example 2: Output: [0,1,2,3,4]
    # security = [1, 1, 1, 1, 1]
    # _time = 0

    # Example 3: Output: []
    security = [1, 2, 3, 4, 5, 6]
    _time = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.goodDaysToRobBank(security, _time)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
