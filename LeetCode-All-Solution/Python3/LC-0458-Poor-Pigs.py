#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0458-Poor-Pigs.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-08-06
=================================================================="""

import sys
import time
import math
# from typing import List
# import collections
# import functools

"""
LeetCode - 0458 - (Hard) - Poor Pigs
https://leetcode.com/problems/poor-pigs/

Description & Requirement:
    There are buckets buckets of liquid, where exactly one of the buckets is poisonous. 
    To figure out which one is poisonous, you feed some number of (poor) pigs the liquid to see whether 
    they will die or not. Unfortunately, you only have minutesToTest minutes to determine which bucket is poisonous.

    You can feed the pigs according to these steps:
        Choose some live pigs to feed.
        For each pig, choose which buckets to feed it. 
            The pig will consume all the chosen buckets simultaneously and will take no time.
        Wait for minutesToDie minutes. You may not feed any other pigs during this time.
        After minutesToDie minutes have passed, any pigs that have been fed the poisonous bucket will die, 
            and all others will survive.
        Repeat this process until you run out of time.

    Given buckets, minutesToDie, and minutesToTest, 
    return the minimum number of pigs needed to figure out which bucket is poisonous within the allotted time.

Example 1:
    Input: buckets = 1000, minutesToDie = 15, minutesToTest = 60
    Output: 5
Example 2:
    Input: buckets = 4, minutesToDie = 15, minutesToTest = 15
    Output: 2
Example 3:
    Input: buckets = 4, minutesToDie = 15, minutesToTest = 30
    Output: 2

Constraints:
    1 <= buckets <= 1000
    1 <= minutesToDie <= minutesToTest <= 100
"""


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # exception case
        assert isinstance(buckets, int) and buckets >= 1
        assert isinstance(minutesToDie, int) and isinstance(minutesToTest, int) and 1 <= minutesToDie <= minutesToTest
        # main method: (Math or Dynamic programming)
        return self._poorPigs(buckets, minutesToDie, minutesToTest)

    def _poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        assert isinstance(buckets, int) and buckets >= 1
        assert isinstance(minutesToDie, int) and isinstance(minutesToTest, int) and 1 <= minutesToDie <= minutesToTest

        states = (minutesToTest // minutesToDie) + 1
        return  math.ceil(math.log(buckets) / math.log(states) - float(1e-5))


def main():
    # Example 1: Output: 5
    buckets = 1000
    minutesToDie = 15
    minutesToTest = 60

    # Example 2: Output: 2
    # buckets = 4
    # minutesToDie = 15
    # minutesToTest = 15

    # Example 3: Output: 2
    # buckets = 4
    # minutesToDie = 15
    # minutesToTest = 30

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.poorPigs(buckets, minutesToDie, minutesToTest)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
