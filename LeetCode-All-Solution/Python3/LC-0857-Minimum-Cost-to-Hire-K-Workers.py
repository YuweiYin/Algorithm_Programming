#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0857-Minimum-Cost-to-Hire-K-Workers.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-09-11
=================================================================="""

import sys
import time
from typing import List
import heapq
# import collections
# import functools

"""
LeetCode - 0857 - (Hard) - Minimum Cost to Hire K Workers
https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

Description & Requirement:
    There are n workers. You are given two integer arrays quality and wage 
    where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

    We want to hire exactly k workers to form a paid group. To hire a group of k workers, 
    we must pay them according to the following rules:
        Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
        Every worker in the paid group must be paid at least their minimum wage expectation.

    Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. 
    Answers within 10^{-5} of the actual answer will be accepted.

Example 1:
    Input: quality = [10,20,5], wage = [70,50,30], k = 2
    Output: 105.00000
    Explanation: We pay 70 to 0th worker and 35 to 2nd worker.
Example 2:
    Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
    Output: 30.66667
    Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.

Constraints:
    n == quality.length == wage.length
    1 <= k <= n <= 10^4
    1 <= quality[i], wage[i] <= 10^4
"""


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # exception case
        assert isinstance(k, int) and k >= 1
        assert isinstance(quality, list) and isinstance(wage, list) and len(quality) == len(wage) >= k
        # main method: (sort and heap)
        return self._mincostToHireWorkers(quality, wage, k)

    def _mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        """
        Runtime: 212 ms, faster than 94.44% of Python3 online submissions for Minimum Cost to Hire K Workers.
        Memory Usage: 16.3 MB, less than 76.44% of Python3 online submissions for Minimum Cost to Hire K Workers.
        """
        assert isinstance(k, int) and k >= 1
        assert isinstance(quality, list) and isinstance(wage, list) and len(quality) == len(wage) >= k

        pairs = sorted(zip(quality, wage), key=lambda p: p[1] / p[0])
        res = float(1e9+7)
        total_q = 0

        heap = []
        for q, w in pairs[:k - 1]:
            total_q += q
            heapq.heappush(heap, -q)

        for q, w in pairs[k - 1:]:
            total_q += q
            heapq.heappush(heap, -q)
            res = min(res, w / q * total_q)
            total_q += heapq.heappop(heap)

        return res


def main():
    # Example 1: Output: 105.00000
    # quality = [10, 20, 5]
    # wage = [70, 50, 30]
    # k = 2

    # Example 2: Output: 30.66667
    quality = [3, 1, 10, 10, 1]
    wage = [4, 8, 2, 2, 7]
    k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.mincostToHireWorkers(quality, wage, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
