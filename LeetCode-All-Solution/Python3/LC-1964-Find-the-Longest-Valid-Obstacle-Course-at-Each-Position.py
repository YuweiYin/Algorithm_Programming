#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1964-Find-the-Longest-Valid-Obstacle-Course-at-Each-Position.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-07
=================================================================="""

import sys
import time
from typing import List
import bisect
# import collections
# import functools

"""
LeetCode - 1964 - (Hard) - Find the Longest Valid Obstacle Course at Each Position
https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

Description & Requirement:
    You want to build some obstacle courses. 
    You are given a 0-indexed integer array obstacles of length n, 
    where obstacles[i] describes the height of the ith obstacle.

    For every index i between 0 and n - 1 (inclusive), 
    find the length of the longest obstacle course in obstacles such that:

        You choose any number of obstacles between 0 and i inclusive.
        You must include the ith obstacle in the course.
        You must put the chosen obstacles in the same order as they appear in obstacles.
        Every obstacle (except the first) is taller than or 
            the same height as the obstacle immediately before it.

    Return an array ans of length n, where ans[i] is the length of 
    the longest obstacle course for index i as described above.

Example 1:
    Input: obstacles = [1,2,3,2]
    Output: [1,2,3,3]
    Explanation: The longest valid obstacle course at each position is:
        - i = 0: [1], [1] has length 1.
        - i = 1: [1,2], [1,2] has length 2.
        - i = 2: [1,2,3], [1,2,3] has length 3.
        - i = 3: [1,2,3,2], [1,2,2] has length 3.
Example 2:
    Input: obstacles = [2,2,1]
    Output: [1,2,1]
    Explanation: The longest valid obstacle course at each position is:
        - i = 0: [2], [2] has length 1.
        - i = 1: [2,2], [2,2] has length 2.
        - i = 2: [2,2,1], [1] has length 1.
Example 3:
    Input: obstacles = [3,1,5,6,4,2]
    Output: [1,1,2,3,2,2]
    Explanation: The longest valid obstacle course at each position is:
        - i = 0: [3], [3] has length 1.
        - i = 1: [3,1], [1] has length 1.
        - i = 2: [3,1,5], [3,5] has length 2. [1,5] is also valid.
        - i = 3: [3,1,5,6], [3,5,6] has length 3. [1,5,6] is also valid.
        - i = 4: [3,1,5,6,4], [3,4] has length 2. [1,4] is also valid.
        - i = 5: [3,1,5,6,4,2], [1,2] has length 2.

Constraints:
    n == obstacles.length
    1 <= n <= 10^5
    1 <= obstacles[i] <= 10^7
"""


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # exception case
        assert isinstance(obstacles, list) and len(obstacles) >= 1
        # main method: (dynamic programming & binary search) similar to 300. Longest Increasing Subsequence
        # https://leetcode.com/problems/longest-increasing-subsequence/
        return self._longestObstacleCourseAtEachPosition(obstacles)

    def _longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        assert isinstance(obstacles, list) and len(obstacles) >= 1

        res = []
        dp = []

        for obs in obstacles:
            if len(dp) == 0 or obs >= dp[-1]:
                dp.append(obs)
                res.append(len(dp))
            else:
                idx = bisect.bisect_right(dp, obs)
                res.append(idx + 1)
                dp[idx] = obs

        return res


def main():
    # Example 1: Output: [1,2,3,3]
    # obstacles = [1, 2, 3, 2]

    # Example 2: Output: [1,2,1]
    # obstacles = [2, 2, 1]

    # Example 3: Output: [1,1,2,3,2,2]
    obstacles = [3, 1, 5, 6, 4, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.longestObstacleCourseAtEachPosition(obstacles)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
