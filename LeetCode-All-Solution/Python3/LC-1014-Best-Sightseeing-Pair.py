#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1014-Best-Sightseeing-Pair.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-02-10
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1014 - (Medium) - Best Sightseeing Pair
https://leetcode.com/problems/best-sightseeing-pair/

Description & Requirement:
    You are given an integer array values where values[i] represents the value of the ith sightseeing spot. 
    Two sightseeing spots i and j have a distance j - i between them.

    The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: 
    the sum of the values of the sightseeing spots, minus the distance between them.

    Return the maximum score of a pair of sightseeing spots.

Example 1:
    Input: values = [8,1,5,2,6]
    Output: 11
    Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:
    Input: values = [1,2]
    Output: 2

Constraints:
    2 <= values.length <= 5 * 10^4
    1 <= values[i] <= 1000
"""


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # exception case
        if not isinstance(values, list) or len(values) <= 0:
            return 0  # Error input type
        if len(values) == 1:
            return 0  # Error input type
        if len(values) == 2:
            return sum(values) - 1
        # main method: (Math trick)
        #     aim: max(values[i] + values[j] + i - j) == max(values[i] + i) + max(values[j] - j)
        #     scan by index j, when j is fixed, consider maximize (values[i] + i), where i < j --> needn't look forward!
        #         so just record the max value of every scanned (values[i] + i)
        return self._maxScoreSightseeingPair(values)

    def _maxScoreSightseeingPair(self, values: List[int]) -> int:
        len_values = len(values)
        assert len_values >= 3

        res = 0
        cur_max_vi_plus_i = values[0] + 0

        cur_j = 1
        while cur_j < len_values:
            # update max pair score
            res = max(res, cur_max_vi_plus_i + values[cur_j] - cur_j)
            # consider maximize (values[i] + i), where i < j --> needn't look forward!
            cur_max_vi_plus_i = max(cur_max_vi_plus_i, values[cur_j] + cur_j)
            cur_j += 1

        return res


def main():
    # Example 1: Output: 11
    values = [8, 1, 5, 2, 6]

    # Example 2: Output: 2
    # values = [1, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxScoreSightseeingPair(values)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
