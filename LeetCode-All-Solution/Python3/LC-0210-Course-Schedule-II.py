#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0210-Course-Schedule-II.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-10
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools
# import itertools

"""
LeetCode - 0210 - (Medium) Course Schedule II
https://leetcode.com/problems/course-schedule-ii/

Description & Requirement:
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
    you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

    Return the ordering of courses you should take to finish all courses. 
    If there are many valid answers, return any of them. 
    If it is impossible to finish all courses, return an empty array.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. 
        To take course 1 you should have finished course 0. 
        So the correct course order is [0,1].
Example 2:
    Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]
    Explanation: There are a total of 4 courses to take. 
        To take course 3 you should have finished both courses 1 and 2. 
        Both courses 1 and 2 should be taken after you finished course 0.
        So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:
    Input: numCourses = 1, prerequisites = []
    Output: [0]

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= numCourses * (numCourses - 1)
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    ai != bi
    All the pairs [ai, bi] are distinct.
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(numCourses, int) and numCourses >= 1
        assert isinstance(prerequisites, list) and len(prerequisites) <= numCourses * (numCourses - 1)
        # main method: (BFS)
        return self._findOrder(numCourses, prerequisites)

    def _findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        assert isinstance(numCourses, int) and numCourses >= 1
        assert isinstance(prerequisites, list) and len(prerequisites) <= numCourses * (numCourses - 1)

        edges = collections.defaultdict(list)
        in_deg = [0] * numCourses
        res = []

        for info in prerequisites:
            edges[info[1]].append(info[0])
            in_deg[info[0]] += 1

        queue = collections.deque([u for u in range(numCourses) if in_deg[u] == 0])

        while len(queue) > 0:
            u = queue.popleft()
            res.append(u)
            for v in edges[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    queue.append(v)

        return res if len(res) == numCourses else []


def main():
    # Example 1: Output: [0,1]
    # numCourses = 2
    # prerequisites = [[1, 0]]

    # Example 2: Output: [0,2,1,3]
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

    # Example 3: Output: [0]
    # numCourses = 1
    # prerequisites = []

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.findOrder(numCourses, prerequisites)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
