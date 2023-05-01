#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1376-Time-Needed-to-Inform-All-Employees.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-01
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1376 - (Medium) - Time Needed to Inform All Employees
https://leetcode.com/problems/time-needed-to-inform-all-employees/

Description & Requirement:
    A company has n employees with a unique ID for each employee from 0 to n - 1. 
    The head of the company is the one with headID.

    Each employee has one direct manager given in the manager array where 
    manager[i] is the direct manager of the i-th employee, manager[headID] = -1. 
    Also, it is guaranteed that the subordination relationships have a tree structure.

    The head of the company wants to inform all the company employees of an urgent piece of news. 
    He will inform his direct subordinates, and they will inform their subordinates, and so on 
    until all employees know about the urgent news.

    The i-th employee needs informTime[i] minutes to inform all of his direct subordinates 
    (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

    Return the number of minutes needed to inform all the employees about the urgent news.

Example 1:
    Input: n = 1, headID = 0, manager = [-1], informTime = [0]
    Output: 0
    Explanation: The head of the company is the only employee in the company.
Example 2:
    Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
    Output: 1
    Explanation: The head of the company with id = 2 is the direct manager of all the employees 
        in the company and needs 1 minute to inform them all.
        The tree structure of the employees in the company is shown.

Constraints:
    1 <= n <= 10^5
    0 <= headID < n
    manager.length == n
    0 <= manager[i] < n
    manager[headID] == -1
    informTime.length == n
    0 <= informTime[i] <= 1000
    informTime[i] == 0 if employee i has no subordinates.
    It is guaranteed that all the employees can be informed.
"""


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(headID, int) and 0 <= headID < n
        assert isinstance(manager, list) and len(manager) == n
        assert isinstance(informTime, list) and len(informTime) == n
        # main method: (DFS or BFS)
        return self._numOfMinutes(n, headID, manager, informTime)

    def _numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(headID, int) and 0 <= headID < n
        assert isinstance(manager, list) and len(manager) == n
        assert isinstance(informTime, list) and len(informTime) == n

        graph = collections.defaultdict(list)
        for i in range(n):
            graph[manager[i]].append(i)

        def __dfs(cur):
            res = 0
            for ne in graph[cur]:
                res = max(res, __dfs(ne))
            return informTime[cur] + res

        return __dfs(headID)


def main():
    # Example 1: Output: 0
    # n = 1
    # headID = 0
    # manager = [-1]
    # informTime = [0]

    # Example 2: Output: 1
    n = 6
    headID = 2
    manager = [2, 2, -1, 2, 2, 2]
    informTime = [0, 0, 1, 0, 0, 0]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.numOfMinutes(n, headID, manager, informTime)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
