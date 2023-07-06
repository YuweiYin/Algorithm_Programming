#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2178-Maximum-Split-of-Positive-Even-Integers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-06
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 2178 - (Medium) - Maximum Split of Positive Even Integers
https://leetcode.com/problems/maximum-split-of-positive-even-integers/

Description & Requirement:
    You are given an integer finalSum. 
    Split it into a sum of a maximum number of unique positive even integers.

    For example, given finalSum = 12, the following splits are valid 
    (unique positive even integers summing up to finalSum): (12), (2 + 10), (2 + 4 + 6), 
    and (4 + 8). Among them, (2 + 4 + 6) contains the maximum number of integers. 
    Note that finalSum cannot be split into (2 + 2 + 4 + 4) as all the numbers should be unique.

    Return a list of integers that represent a valid split containing a maximum number of integers. 
    If no valid split exists for finalSum, return an empty list. 
    You may return the integers in any order.

Example 1:
    Input: finalSum = 12
    Output: [2,4,6]
    Explanation: The following are valid splits: (12), (2 + 10), (2 + 4 + 6), and (4 + 8).
        (2 + 4 + 6) has the maximum number of integers, which is 3. Thus, we return [2,4,6].
        Note that [2,6,4], [6,2,4], etc. are also accepted.
Example 2:
    Input: finalSum = 7
    Output: []
    Explanation: There are no valid splits for the given finalSum.
        Thus, we return an empty array.
Example 3:
    Input: finalSum = 28
    Output: [6,8,2,12]
    Explanation: The following are valid splits: (2 + 26), (6 + 8 + 2 + 12), and (4 + 24). 
        (6 + 8 + 2 + 12) has the maximum number of integers, which is 4. Thus, we return [6,8,2,12].
        Note that [10,2,4,12], [6,2,4,16], etc. are also accepted.

Constraints:
    1 <= finalSum <= 10^10
"""


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        # exception case
        assert isinstance(finalSum, int) and finalSum >= 1
        # main method: (greedy)
        return self._maximumEvenSplit(finalSum)

    def _maximumEvenSplit(self, finalSum: int) -> List[int]:
        assert isinstance(finalSum, int) and finalSum >= 1

        res = []
        if finalSum % 2 > 0:
            return res

        i = 2
        while i <= finalSum:
            res.append(i)
            finalSum -= i
            i += 2

        res[-1] += finalSum

        return res


def main():
    # Example 1: Output: [2,4,6]
    finalSum = 12

    # Example 2: Output: []
    # finalSum = 7

    # Example 3: Output: [6,8,2,12]
    # finalSum = 28

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.maximumEvenSplit(finalSum)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
