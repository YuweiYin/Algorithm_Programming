#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0986-Interval-List-Intersections.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-17
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 0986 - (Medium) - Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/

Description & Requirement:
    You are given two lists of closed intervals, firstList and secondList, 
    where firstList[i] = [start_i, end_i] and secondList[j] = [start_j, end_j]. 
    Each list of intervals is pairwise disjoint and in sorted order.

    Return the intersection of these two interval lists.

    A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
    The intersection of two closed intervals is a set of real numbers that are 
    either empty or represented as a closed interval. 
    For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:
    Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
    Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:
    Input: firstList = [[1,3],[5,9]], secondList = []
    Output: []

Constraints:
    0 <= firstList.length, secondList.length <= 1000
    firstList.length + secondList.length >= 1
    0 <= start_i < end_i <= 10^9
    end_i < start_{i+1}
    0 <= start_j < end_j <= 10^9
    end_j < start_{j+1}
"""


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # exception case
        if not isinstance(firstList, list) or len(firstList) <= 0:
            return []
        if not isinstance(secondList, list) or len(secondList) <= 0:
            return []
        # main method: (greedy match intervals)
        return self._intervalIntersection(firstList, secondList)

    def _intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        assert len(firstList) > 0 and len(secondList) > 0
        len_first = len(firstList)
        len_second = len(secondList)

        res = []

        first_index = 0
        second_index = 0
        while first_index < len_first and second_index < len_second:
            first_start, first_end = firstList[first_index]
            second_start, second_end = secondList[second_index]
            assert first_start <= first_end and second_start <= second_end

            if second_start <= first_end <= second_end:  # first interval is (partly) in second interval
                res.append([max(first_start, second_start), first_end])
                first_index += 1
                continue

            if first_start <= second_end <= first_end:  # second interval is (partly) in first interval
                res.append([max(second_start, first_start), second_end])
                second_index += 1
                continue

            # else case: the two intervals must be disjoint, drop the left one and move on
            if first_end <= second_end:
                first_index += 1
            else:
                second_index += 1

        # drop the rest intervals, can't have more intersection
        return res


def main():
    # Example 1: Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]

    # Example 2: Output: []
    # firstList = [[1, 3], [5, 9]]
    # secondList = []

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.intervalIntersection(firstList, secondList)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
