#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1851-Minimum-Interval-to-Include-Each-Query.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-18
=================================================================="""

import sys
import time
from typing import List
import heapq
# import functools
# import itertools

"""
LeetCode - 1851 - (Hard) - Minimum Interval to Include Each Query
https://leetcode.com/problems/minimum-interval-to-include-each-query/

Description & Requirement:
    You are given a 2D integer array intervals, where intervals[i] = [left_i, right_i] describes 
    the ith interval starting at left_i and ending at right_i (inclusive). The size of an interval 
    is defined as the number of integers it contains, or more formally right_i - left_i + 1.

    You are also given an integer array queries. The answer to the jth query is the size of 
    the smallest interval i such that left_i <= queries[j] <= right_i. 
    If no such interval exists, the answer is -1.

    Return an array containing the answers to the queries.

Example 1:
    Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
    Output: [3,3,1,4]
    Explanation: The queries are processed as follows:
        - Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
        - Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
        - Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
        - Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
Example 2:
    Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
    Output: [2,-1,4,6]
    Explanation: The queries are processed as follows:
        - Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
        - Query = 19: None of the intervals contain 19. The answer is -1.
        - Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
        - Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.

Constraints:
    1 <= intervals.length <= 10^5
    1 <= queries.length <= 10^5
    intervals[i].length == 2
    1 <= left_i <= right_i <= 10^7
    1 <= queries[j] <= 10^7
"""


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # exception case
        assert isinstance(intervals, list) and len(intervals) >= 1
        assert isinstance(queries, list) and len(queries) >= 1
        # main method: (priority queue)
        return self._minInterval(intervals, queries)

    def _minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        assert isinstance(intervals, list) and len(intervals) >= 1
        assert isinstance(queries, list) and len(queries) >= 1

        q_index = list(range(len(queries)))
        q_index.sort(key=lambda x: queries[x])
        intervals.sort(key=lambda x: x[0])

        p_queue = []
        res = [-1] * len(queries)
        i = 0
        for qi in q_index:
            while i < len(intervals) and intervals[i][0] <= queries[qi]:
                heapq.heappush(p_queue, (intervals[i][1] - intervals[i][0] + 1, intervals[i][0], intervals[i][1]))
                i += 1
            while p_queue and p_queue[0][2] < queries[qi]:
                heapq.heappop(p_queue)
            if p_queue:
                res[qi] = p_queue[0][0]

        return res


def main():
    # Example 1: Output: [3,3,1,4]
    # intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
    # queries = [2, 3, 4, 5]

    # Example 2: Output: [2,-1,4,6]
    intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]
    queries = [2, 19, 5, 22]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.minInterval(intervals, queries)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
