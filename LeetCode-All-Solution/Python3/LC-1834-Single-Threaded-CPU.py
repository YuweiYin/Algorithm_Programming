#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1962-Remove-Stones-to-Minimize-the-Total.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-29
=================================================================="""

import sys
import time
from typing import List
import heapq
# import collections
# import functools

"""
LeetCode - 1962 - (Medium) - Single-Threaded CPU
https://leetcode.com/problems/single-threaded-cpu/

Description & Requirement:
    You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, 
    where tasks[i] = [enqueueTime_i, processingTime_i] means that the i-th task will be available to process 
    at enqueueTime_i and will take processingTime_i to finish processing.

    You have a single-threaded CPU that can process at most one task at a time and will act in the following way:
        If the CPU is idle and there are no available tasks to process, the CPU remains idle.
        If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time.
            If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
        Once a task is started, the CPU will process the entire task without stopping.
        The CPU can finish a task then start a new one instantly.

    Return the order in which the CPU will process the tasks.

Example 1:
    Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
    Output: [0,2,3,1]
    Explanation: The events go as follows: 
        - At time = 1, task 0 is available to process. Available tasks = {0}.
        - Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
        - At time = 2, task 1 is available to process. Available tasks = {1}.
        - At time = 3, task 2 is available to process. Available tasks = {1, 2}.
        - Also at time = 3, the CPU finishes task 0 and starts processing task 2 as 
            it is the shortest. Available tasks = {1}.
        - At time = 4, task 3 is available to process. Available tasks = {1, 3}.
        - At time = 5, the CPU finishes task 2 and starts processing task 3 as 
            it is the shortest. Available tasks = {1}.
        - At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
        - At time = 10, the CPU finishes task 1 and becomes idle.
Example 2:
    Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
    Output: [4,3,2,0,1]
    Explanation: The events go as follows:
        - At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
        - Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
        - At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
        - At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
        - At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
        - At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
        - At time = 40, the CPU finishes task 1 and becomes idle.

Constraints:
    tasks.length == n
    1 <= n <= 10^5
    1 <= enqueueTime_i, processingTime_i <= 10^9
"""


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # exception case
        assert isinstance(tasks, list) and len(tasks) >= 1
        # main method: (sorting & heap / priority queue)
        return self._getOrder(tasks)

    def _getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        Time: beats 97.87%; Space: beats 13.28%
        """
        assert isinstance(tasks, list) and len(tasks) >= 1

        n = len(tasks)
        indices = list(range(n))
        indices.sort(key=lambda x: tasks[x][0])

        res = []
        queue = []
        timestamp = 0
        ptr = 0

        for _ in range(n):
            if len(queue) == 0:
                timestamp = max(timestamp, tasks[indices[ptr]][0])

            while ptr < n and tasks[indices[ptr]][0] <= timestamp:
                heapq.heappush(queue, (tasks[indices[ptr]][1], indices[ptr]))
                ptr += 1

            process, index = heapq.heappop(queue)
            timestamp += process
            res.append(index)

        return res


def main():
    # Example 1: Output: [0,2,3,1]
    # tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]

    # Example 2: Output: [4,3,2,0,1]
    tasks = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.getOrder(tasks)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
