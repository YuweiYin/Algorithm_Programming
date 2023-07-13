#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0207-Course-Schedule.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-13
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 0207 - (Medium) - Course Schedule
https://leetcode.com/problems/course-schedule/

Description & Requirement:
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
    you must take course bi first if you want to take course ai.

        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

    Return true if you can finish all courses. Otherwise, return false.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
        To take course 1 you should have finished course 0. So it is possible.
Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
        To take course 1 you should have finished course 0, and to take course 0 
        you should also have finished course 1. So it is impossible.

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # exception case
        assert isinstance(numCourses, int) and numCourses >= 1
        assert isinstance(prerequisites, list)
        # main method: (DFS)
        return self._canFinish(numCourses, prerequisites)

    def _canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        assert isinstance(numCourses, int) and numCourses >= 1
        assert isinstance(prerequisites, list)

        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = []
        valid = True

        for pre in prerequisites:
            edges[pre[1]].append(pre[0])

        def __dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    __dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)

        for i in range(numCourses):
            if valid and not visited[i]:
                __dfs(i)

        return valid


def main():
    # Example 1: Output: true
    # numCourses = 2
    # prerequisites = [[1, 0]]

    # Example 2: Output: false
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.canFinish(numCourses, prerequisites)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
