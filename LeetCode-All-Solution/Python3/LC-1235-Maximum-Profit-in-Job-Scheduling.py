#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1235-Maximum-Profit-in-Job-Scheduling.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-22
=================================================================="""

import sys
import time
from typing import List, Callable
# import bisect
# import collections
# import functools

"""
LeetCode - 1235 - (Hard) - Maximum Profit in Job Scheduling
https://leetcode.com/problems/maximum-profit-in-job-scheduling/

Description & Requirement:
    We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], 
    obtaining a profit of profit[i].

    You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that 
    there are no two jobs in the subset with overlapping time range.

    If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:
    Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
    Output: 120
    Explanation: The subset chosen is the first and fourth job. 
        Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:
    Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
    Output: 150
    Explanation: The subset chosen is the first, fourth and fifth job. 
        Profit obtained 150 = 20 + 70 + 60.
Example 3:
    Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
    Output: 6

Constraints:
    1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
    1 <= startTime[i] < endTime[i] <= 10^9
    1 <= profit[i] <= 10^4
"""


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # exception case
        assert isinstance(startTime, list) and len(startTime) >= 1
        assert isinstance(endTime, list) and len(startTime) == len(endTime)
        assert isinstance(profit, list) and len(startTime) == len(profit)
        for i in range(len(startTime)):
            assert 1 <= startTime[i] < endTime[i] and 1 <= profit[i]
        # main method: (dynamic programming and binary search)
        return self._jobScheduling(startTime, endTime, profit)

    def _jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        assert isinstance(startTime, list) and len(startTime) >= 1
        assert isinstance(endTime, list) and len(startTime) == len(endTime)
        assert isinstance(profit, list) and len(startTime) == len(profit)

        def _bisect_right(a, x, lo=0, hi=None, key: Callable = None):
            if lo < 0:
                raise ValueError('lo must be non-negative')
            if hi is None:
                hi = len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if x < key(a[mid]):
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        n = len(startTime)
        dp = [0 for _ in range(n + 1)]
        jobs = sorted(zip(startTime, endTime, profit), key=lambda p: p[1])

        for i in range(1, n + 1):
            k = _bisect_right(jobs, jobs[i - 1][0], hi=i, key=lambda p: p[1])
            dp[i] = max(dp[i - 1], dp[k] + jobs[i - 1][2])

        return dp[-1]


def main():
    # Example 1: Output: 120
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]

    # Example 2: Output: 150
    # startTime = [1, 2, 3, 4, 6]
    # endTime = [3, 5, 10, 6, 9]
    # profit = [20, 20, 100, 70, 60]

    # Example 3: Output: 6
    # startTime = [1, 1, 1]
    # endTime = [2, 3, 4]
    # profit = [5, 6, 4]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.jobScheduling(startTime, endTime, profit)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
