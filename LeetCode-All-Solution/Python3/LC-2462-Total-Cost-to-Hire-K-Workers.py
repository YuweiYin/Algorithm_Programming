#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2462-Total-Cost-to-Hire-K-Workers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-06-26
=================================================================="""

import sys
import time
from typing import List
import heapq
# import collections
# import functools
# import itertools

"""
LeetCode - 2462 - (Medium) - Total Cost to Hire K Workers
https://leetcode.com/problems/total-cost-to-hire-k-workers/

Description & Requirement:
    You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

    You are also given two integers k and candidates. 
    We want to hire exactly k workers according to the following rules:
        - You will run k sessions and hire exactly one worker in each session.
        - In each hiring session, choose the worker with the lowest cost from either the first candidates workers 
            or the last candidates workers. Break the tie by the smallest index.
            - For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, 
                we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
            - In the second hiring session, we will choose 1st worker because they have the same lowest cost 
                as 4th worker but they have the smallest index [3,2,7,7,2]. 
                Please note that the indexing may be changed in the process.
        - If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. 
            Break the tie by the smallest index.
        - A worker can only be chosen once.

    Return the total cost to hire exactly k workers.

Example 1:
    Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
    Output: 11
    Explanation: We hire 3 workers in total. The total cost is initially 0.
        - In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. 
            The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
        - In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. 
            The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
        - In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. 
            The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. 
            Notice that the worker with index 3 was common in the first and last four workers.
        The total hiring cost is 11.
Example 2:
    Input: costs = [1,2,4,1], k = 3, candidates = 3
    Output: 4
    Explanation: We hire 3 workers in total. The total cost is initially 0.
        - In the first hiring round we choose the worker from [1,2,4,1]. 
            The lowest cost is 1, and we break the tie by the smallest index, which is 0. 
            The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 
            are common in the first and last 3 workers.
        - In the second hiring round we choose the worker from [2,4,1]. 
            The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
        - In the third hiring round there are less than three candidates. 
            We choose the worker from the remaining workers [2,4]. 
            The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
        The total hiring cost is 4.

Constraints:
    1 <= costs.length <= 10^5 
    1 <= costs[i] <= 10^5
    1 <= k, candidates <= costs.length
"""


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # exception case
        assert isinstance(costs, list) and len(costs) >= 1
        assert isinstance(k, int) and 1 <= k <= len(costs)
        assert isinstance(candidates, int) and 1 <= candidates <= len(costs)
        # main method: (min heap)
        return self._totalCost(costs, k, candidates)

    def _totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        assert isinstance(costs, list) and len(costs) >= 1
        assert isinstance(k, int) and 1 <= k <= len(costs)
        assert isinstance(candidates, int) and 1 <= candidates <= len(costs)

        res, n = 0, len(costs)

        if candidates * 2 < n:
            prefix, suffix = costs[:candidates], costs[-candidates:]
            heapq.heapify(prefix)
            heapq.heapify(suffix)

            i, j = candidates, n - 1 - candidates
            while k and i <= j:
                if prefix[0] <= suffix[0]:
                    res += heapq.heapreplace(prefix, costs[i])
                    i += 1
                else:
                    res += heapq.heapreplace(suffix, costs[j])
                    j -= 1
                k -= 1

            costs = prefix + suffix

        costs.sort()

        return res + sum(costs[:k])


def main():
    # Example 1: Output: 11
    costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
    k = 3
    candidates = 4

    # Example 2: Output: 4
    # costs = [1, 2, 4, 1]
    # k = 3
    # candidates = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.totalCost(costs, k, candidates)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
