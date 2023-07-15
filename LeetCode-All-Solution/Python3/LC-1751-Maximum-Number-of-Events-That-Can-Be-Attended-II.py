#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1751-Maximum-Number-of-Events-That-Can-Be-Attended-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-15
=================================================================="""

import sys
import time
from typing import List
import bisect
# import functools
# import itertools

"""
LeetCode - 1751 - (Hard) - Maximum Number of Events That Can Be Attended II
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

Description & Requirement:
    You are given an array of events where events[i] = [startDayi, endDayi, valuei]. 
    The i-th event starts at startDayi and ends at endDayi, and if you attend this event, 
    you will receive a value of valuei. You are also given an integer k which 
    represents the maximum number of events you can attend.

    You can only attend one event at a time. If you choose to attend an event, 
    you must attend the entire event. Note that the end day is inclusive: that is, 
    you cannot attend two events where one of them starts and the other ends on the same day.

    Return the maximum sum of values that you can receive by attending events.

Example 1:
    Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
    Output: 7
    Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
Example 2:
    Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
    Output: 10
    Explanation: Choose event 2 for a total value of 10.
        Notice that you cannot attend any other event as they overlap, 
        and that you do not have to attend k events.
Example 3:
    Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
    Output: 9
    Explanation: Although the events do not overlap, you can only attend 3 events. 
        Pick the highest valued three.

Constraints:
    1 <= k <= events.length
    1 <= k * events.length <= 10^6
    1 <= startDayi <= endDayi <= 10^9
    1 <= valuei <= 10^6
"""


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # exception case
        assert isinstance(k, int) and k >= 1
        assert isinstance(events, list) and len(events) >= k
        # main method: (dynamic programming & binary search)
        return self._maxValue(events, k)

    def _maxValue(self, events: List[List[int]], k: int) -> int:
        assert isinstance(k, int) and k >= 1
        assert isinstance(events, list) and len(events) >= k

        n = len(events)
        events.sort(key=lambda x: x[1])
        dp = [0] * (n + 1)

        for j in range(k):
            dp_next = [0]

            for i in range(n):
                startDay, endDay, value = events[i]
                l_idx, r_idx = 0, i - 1
                if events[l_idx][1] >= startDay:
                    curValue = value
                else:
                    while l_idx < r_idx:
                        mid_idx = (l_idx + r_idx + 1) >> 1
                        if events[mid_idx][1] < startDay:
                            l_idx = mid_idx
                        else:
                            r_idx = mid_idx - 1
                    curValue = dp[l_idx + 1] + value
                dp_next.append(max(dp_next[i], curValue))

            dp = dp_next[:]

        return dp[-1]


def main():
    # Example 1: Output: 7
    # events = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]
    # k = 2

    # Example 2: Output: 10
    # events = [[1, 2, 4], [3, 4, 3], [2, 3, 10]]
    # k = 2

    # Example 3: Output: 9
    events = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
    k = 3

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.maxValue(events, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
