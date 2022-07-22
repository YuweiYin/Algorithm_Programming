#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0757-Set-Intersection-Size-At-Least-Two.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-22
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 0757 - (Hard) - Set Intersection Size At Least Two
https://leetcode.com/problems/set-intersection-size-at-least-two/

Description & Requirement:
    An integer interval [a, b] (for integers a < b) is a set of 
    all consecutive integers from a to b, including a and b.

    Find the minimum size of a set S such that for every integer interval A in intervals, 
    the intersection of S with A has a size of at least two.

Example 1:
    Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
    Output: 3
    Explanation: Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
        Also, there isn't a smaller size set that fulfills the above condition.
        Thus, we output the size of this set, which is 3.
Example 2:
    Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
    Output: 5
    Explanation: An example of a minimum sized set is {1, 2, 3, 4, 5}.

Constraints:
    1 <= intervals.length <= 3000
    intervals[i].length == 2
    0 <= ai < bi <= 10^8
"""


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # exception case
        assert isinstance(intervals, list) and len(intervals) >= 1
        for interval in intervals:
            assert isinstance(interval, list) and len(interval) == 2 and 0 <= interval[0] < interval[1]
        # main method: (sort & greedy algorithm, similar to LC-0452-Minimum-Number-of-Arrows-to-Burst-Balloons)
        return self._intersectionSizeTwo(intervals)

    def _intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        assert isinstance(intervals, list) and len(intervals) >= 1
        len_intervals = len(intervals)

        res = 0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        vals = [[] for _ in range(len_intervals)]  # vals[i] is the minimal shrinkable interval of intervals[i]

        for idx in range(len_intervals - 1, -1, -1):
            left_border = intervals[idx][0]
            for _ in range(len(vals[idx]), 2):  # need expansion
                res += 1
                for next_idx in range(idx - 1, -1, -1):
                    if intervals[next_idx][1] < left_border:  # no intersection
                        break
                    vals[next_idx].append(left_border)
                left_border += 1

        return res


def main():
    # Example 1: Output: 3
    # intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]

    # Example 2: Output: 5
    intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.intersectionSizeTwo(intervals)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
