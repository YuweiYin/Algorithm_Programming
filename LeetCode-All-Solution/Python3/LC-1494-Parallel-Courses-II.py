#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1494-Parallel-Courses-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-16
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1494 - (Hard) - Parallel Courses II
https://leetcode.com/problems/parallel-courses-ii/

Description & Requirement:
    You are given an integer n, which indicates that there are n courses labeled from 1 to n. 
    You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], 
    representing a prerequisite relationship between course prevCoursei and course nextCoursei: 
    course prevCoursei has to be taken before course nextCoursei. Also, you are given the integer k.

    In one semester, you can take at most k courses as long as you have taken 
    all the prerequisites in the previous semesters for the courses you are taking.

    Return the minimum number of semesters needed to take all courses. 
    The testcases will be generated such that it is possible to take every course.

Example 1:
    Input: n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
    Output: 3
    Explanation: The figure above represents the given graph.
        In the first semester, you can take courses 2 and 3.
        In the second semester, you can take course 1.
        In the third semester, you can take course 4.
Example 2:
    Input: n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
    Output: 4
    Explanation: The figure above represents the given graph.
        In the first semester, you can only take courses 2 and 3 since you cannot take more than two per semester.
        In the second semester, you can take course 4.
        In the third semester, you can take course 1.
        In the fourth semester, you can take course 5.

Constraints:
    1 <= n <= 15
    1 <= k <= n
    0 <= relations.length <= n * (n-1) / 2
    relations[i].length == 2
    1 <= prevCoursei, nextCoursei <= n
    prevCoursei != nextCoursei
    All the pairs [prevCoursei, nextCoursei] are unique.
    The given graph is a directed acyclic graph.
"""


class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(relations, list) and len(relations) <= n * (n - 1) / 2
        assert isinstance(k, int) and 1 <= k <= n
        # main method: (dynamic programming)
        return self._minNumberOfSemesters(n, relations, k)

    def _minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(relations, list) and len(relations) <= n * (n - 1) / 2
        assert isinstance(k, int) and 1 <= k <= n

        need = [0] * (1 << n)
        for edge in relations:
            need[(1 << (edge[1] - 1))] |= 1 << (edge[0] - 1)

        INF = int(1e9 + 7)
        dp = [INF] * (1 << n)
        dp[0] = 0

        for i in range(1, (1 << n)):
            need[i] = need[i & (i - 1)] | need[i & (-i)]
            if (need[i] | i) != i:
                continue

            sub = valid = i ^ need[i]
            if bin(sub).count("1") <= k:  # if sub.bit_count() <= k:
                dp[i] = min(dp[i], dp[i ^ sub] + 1)
            else:
                while sub:
                    if bin(sub).count("1") <= k:  # if sub.bit_count() <= k:
                        dp[i] = min(dp[i], dp[i ^ sub] + 1)
                    sub = (sub - 1) & valid

        return dp[-1]


def main():
    # Example 1: Output: 3
    # n = 4
    # relations = [[2, 1], [3, 1], [1, 4]]
    # k = 2

    # Example 2: Output: 4
    n = 5
    relations = [[2, 1], [3, 1], [4, 1], [1, 5]]
    k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minNumberOfSemesters(n, relations, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
