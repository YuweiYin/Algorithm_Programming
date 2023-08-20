#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1203-Sort-Items-by-Groups-Respecting-Dependencies.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-08-20
=================================================================="""

import sys
import time
from typing import List
import collections

# import functools
# import itertools

"""
LeetCode - 1203 - (Hard) Sort Items by Groups Respecting Dependencies
https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

Description & Requirement:
    There are n items each belonging to zero or one of m groups where group[i] is the group 
    that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. 
    The items and the groups are zero indexed. A group can have no item belonging to it.

    Return a sorted list of the items such that:
        - The items that belong to the same group are next to each other in the sorted list.
        - There are some relations between these items where beforeItems[i] is a list containing 
            all the items that should come before the i-th item 
            in the sorted array (to the left of the i-th item).

    Return any solution if there is more than one solution and return an empty list if there is no solution.

Example 1:
    Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
    Output: [6,3,4,1,5,2,0,7]
Example 2:
    Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
    Output: []
    Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.

Constraints:
    1 <= m <= n <= 3 * 10^4
    group.length == beforeItems.length == n
    -1 <= group[i] <= m - 1
    0 <= beforeItems[i].length <= n - 1
    0 <= beforeItems[i][j] <= n - 1
    i != beforeItems[i][j]
    beforeItems[i] does not contain duplicates elements.
"""


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(n, int) and isinstance(m, int) and 1 <= m <= n
        assert isinstance(group, list) and isinstance(beforeItems, list) and len(group) == len(beforeItems) == n
        # main method: (topology sorting)
        return self._sortItems(n, m, group, beforeItems)

    def _sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        assert isinstance(n, int) and isinstance(m, int) and 1 <= m <= n
        assert isinstance(group, list) and isinstance(beforeItems, list) and len(group) == len(beforeItems) == n

        max_group_id = m
        for task in range(n):
            if group[task] == -1:
                group[task] = max_group_id
                max_group_id += 1

        task_in_degree = [0] * n
        group_in_degree = [0] * max_group_id
        task_neighbors = [[] for _ in range(n)]
        group_neighbors = [[] for _ in range(max_group_id)]
        group_to_tasks = [[] for _ in range(max_group_id)]

        for task in range(n):
            group_to_tasks[group[task]].append(task)
            for prerequisite in beforeItems[task]:
                if group[prerequisite] != group[task]:
                    group_in_degree[group[task]] += 1
                    group_neighbors[group[prerequisite]].append(group[task])
                else:
                    task_in_degree[task] += 1
                    task_neighbors[prerequisite].append(task)

        res = []
        group_queue = self.topological_sort([i for i in range(max_group_id)], group_in_degree, group_neighbors)

        if len(group_queue) != max_group_id:
            return []

        for group_id in group_queue:
            task_queue = self.topological_sort(group_to_tasks[group_id], task_in_degree, task_neighbors)
            if len(task_queue) != len(group_to_tasks[group_id]):
                return []
            res += task_queue

        return res

    def topological_sort(self, items, in_degree, neighbors):
        queue = collections.deque()
        res = []

        for item in items:
            if not in_degree[item]:
                queue.append(item)

        if not queue:
            return []

        while queue:
            cur = queue.popleft()
            res.append(cur)
            for neighbor in neighbors[cur]:
                in_degree[neighbor] -= 1
                if not in_degree[neighbor]:
                    queue.append(neighbor)

        return res


def main():
    # Example 1: Output: [6,3,4,1,5,2,0,7]
    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]

    # Example 2: Output: []
    # n = 8
    # m = 2
    # group = [-1, -1, 1, 0, 0, 1, 0, -1]
    # beforeItems = [[], [6], [5], [6], [3], [], [4], []]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.sortItems(n, m, group, beforeItems)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
