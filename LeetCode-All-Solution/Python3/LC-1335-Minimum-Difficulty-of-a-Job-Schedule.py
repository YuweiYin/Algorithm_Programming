#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1335-Minimum-Difficulty-of-a-Job-Schedule.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-10-16
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1335 - (Hard) - Minimum Difficulty of a Job Schedule
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

Description & Requirement:
    You want to schedule a list of jobs in d days. Jobs are dependent 
    (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

    You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties 
    of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

    You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

    Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Example 1:
    Input: jobDifficulty = [6,5,4,3,2,1], d = 2
    Output: 7
    Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
        Second day you can finish the last job, total difficulty = 1.
        The difficulty of the schedule = 6 + 1 = 7 
Example 2:
    Input: jobDifficulty = [9,9,9], d = 4
    Output: -1
    Explanation: If you finish a job per day you will still have a free day. 
        you cannot find a schedule for the given jobs.
Example 3:
    Input: jobDifficulty = [1,1,1], d = 3
    Output: 3
    Explanation: The schedule is one job per day. total difficulty will be 3.

Constraints:
    1 <= jobDifficulty.length <= 300
    0 <= jobDifficulty[i] <= 1000
    1 <= d <= 10
"""


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # exception case
        assert isinstance(jobDifficulty, list) and len(jobDifficulty) >= 1
        for j in jobDifficulty:
            assert isinstance(j, int) and j >= 0
        assert isinstance(d, int) and d >= 1
        # main method: (dynamic programming)
        return self._minDifficulty(jobDifficulty, d)

    def _minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        assert isinstance(jobDifficulty, list) and len(jobDifficulty) >= 1
        assert isinstance(d, int) and d >= 1

        n = len(jobDifficulty)
        ceil = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            cur = jobDifficulty[i]
            for j in range(i, n):
                cur = max(cur, jobDifficulty[j])
                ceil[i][j] = cur

        dp = [[int(1e9+7) for _ in range(d)] for _ in range(n)]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, n):
            dp[i][0] = max(jobDifficulty[i], dp[i - 1][0])
        for i in range(1, n):
            for j in range(d):
                dp[i][j] = min(dp[i][j], min(dp[k][j - 1] + ceil[k + 1][i] for k in range(i)))

        return dp[-1][-1] if dp[-1][-1] != int(1e9+7) else -1


def main():
    # Example 1: Output: 7
    # jobDifficulty = [6, 5, 4, 3, 2, 1]
    # d = 2

    # Example 2: Output: -1
    # jobDifficulty = [9, 9, 9]
    # d = 4

    # Example 3: Output: 3
    jobDifficulty = [1, 1, 1]
    d = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minDifficulty(jobDifficulty, d)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
