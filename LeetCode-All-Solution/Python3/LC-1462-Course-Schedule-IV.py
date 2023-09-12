#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1462-Course-Schedule-IV.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-09-12
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools
# import itertools

"""
LeetCode - 1462 - (Medium) Course Schedule IV
https://leetcode.com/problems/course-schedule-iv/

Description & Requirement:
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
    you must take course ai first if you want to take course bi.

    For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
    
    Prerequisites can also be indirect. If course a is a prerequisite of course b, and 
    course b is a prerequisite of course c, then course a is a prerequisite of course c.

    You are also given an array queries where queries[j] = [uj, vj]. For the jth query, 
    you should answer whether course uj is a prerequisite of course vj or not.

    Return a boolean array answer, where answer[j] is the answer to the jth query.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
    Output: [false,true]
    Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
        Course 0 is not a prerequisite of course 1, but the opposite is true.
Example 2:
    Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
    Output: [false,false]
    Explanation: There are no prerequisites, and each course is independent.
Example 3:
    Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
    Output: [true,true]

Constraints:
    2 <= numCourses <= 100
    0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
    prerequisites[i].length == 2
    0 <= ai, bi <= n - 1
    ai != bi
    All the pairs [ai, bi] are unique.
    The prerequisites graph has no cycles.
    1 <= queries.length <= 10^4
    0 <= ui, vi <= n - 1
    ui != vi
"""


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # exception case
        assert isinstance(numCourses, int) and numCourses >= 2
        assert isinstance(prerequisites, list) and len(prerequisites) <= (numCourses * (numCourses - 1) / 2)
        assert isinstance(queries, list) and len(queries) >= 1
        # main method: (BFS and Topological Sorting)
        return self._checkIfPrerequisite(numCourses, prerequisites, queries)

    def _checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        assert isinstance(numCourses, int) and numCourses >= 2
        assert isinstance(prerequisites, list) and len(prerequisites) <= (numCourses * (numCourses - 1) / 2)
        assert isinstance(queries, list) and len(queries) >= 1

        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        is_pre = [[False] * numCourses for _ in range(numCourses)]

        for pre in prerequisites:
            in_degree[pre[1]] += 1
            graph[pre[0]].append(pre[1])

        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        while len(queue) > 0:
            cur = queue[0]
            queue.pop(0)
            for ne in graph[cur]:
                is_pre[cur][ne] = True
                for i in range(numCourses):
                    is_pre[i][ne] = is_pre[i][ne] or is_pre[i][cur]
                in_degree[ne] -= 1
                if in_degree[ne] == 0:
                    queue.append(ne)

        res = []
        for query in queries:
            res.append(is_pre[query[0]][query[1]])

        return res


def main():
    # Example 1: Output: [false,true]
    # numCourses = 2
    # prerequisites = [[1, 0]]
    # queries = [[0, 1], [1, 0]]

    # Example 2: Output: [false,false]
    # numCourses = 2
    # prerequisites = []
    # queries = [[1, 0], [0, 1]]

    # Example 3: Output: [true,true]
    numCourses = 3
    prerequisites = [[1, 2], [1, 0], [2, 0]]
    queries = [[1, 0], [1, 2]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.checkIfPrerequisite(numCourses, prerequisites, queries)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
