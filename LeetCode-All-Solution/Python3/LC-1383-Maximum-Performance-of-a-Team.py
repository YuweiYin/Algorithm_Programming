#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1383-Maximum-Performance-of-a-Team.py
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
LeetCode - 1383 - (Hard) - Maximum Performance of a Team
https://leetcode.com/problems/maximum-performance-of-a-team/

Description & Requirement:
    You are given two integers n and k and two integer arrays speed and efficiency both of length n. 
    There are n engineers numbered from 1 to n. 
    speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

    Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

    The performance of a team is the sum of their engineers' speeds multiplied 
    by the minimum efficiency among their engineers.

    Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.

Example 1:
    Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
    Output: 60
    Explanation: 
    We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and 
        engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
Example 2:
    Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
    Output: 68
    Explanation:
    This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 
        to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
Example 3:
    Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
    Output: 72

Constraints:
    1 <= k <= n <= 10^5
    speed.length == n
    efficiency.length == n
    1 <= speed[i] <= 10^5
    1 <= efficiency[i] <= 10^8
"""


class Solution:
    class Engineer:
        def __init__(self, s, e):
            self.s = s  # speed
            self.e = e  # efficiency

        def __lt__(self, obj):
            return self.s < obj.s

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # exception case
        assert isinstance(n, int) and isinstance(k, int) and 1 <= k <= n
        assert isinstance(speed, list) and len(speed) == n
        assert isinstance(efficiency, list) and len(efficiency) == n
        # main method: (heap)
        return self._maxPerformance(n, speed, efficiency, k)

    def _maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        assert isinstance(n, int) and isinstance(k, int) and 1 <= k <= n
        assert isinstance(speed, list) and len(speed) == n
        assert isinstance(efficiency, list) and len(efficiency) == n

        val = list()
        for idx in range(n):
            val.append(Solution.Engineer(speed[idx], efficiency[idx]))
        val.sort(key=lambda x: -x.e)

        heap = []
        res, total = 0, 0
        for idx in range(n):
            min_e, total_s = val[idx].e, total + val[idx].s
            res = max(res, min_e * total_s)
            heapq.heappush(heap, val[idx])
            total += val[idx].s
            if len(heap) == k:
                item = heapq.heappop(heap)
                total -= item.s

        return res % int(1e9+7)


def main():
    # Example 1: Output: 60
    # n = 6
    # speed = [2, 10, 3, 1, 5, 8]
    # efficiency = [5, 4, 3, 9, 7, 2]
    # k = 2

    # Example 2: Output: 68
    # n = 6
    # speed = [2, 10, 3, 1, 5, 8]
    # efficiency = [5, 4, 3, 9, 7, 2]
    # k = 3

    # Example 3: Output: 72
    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 4

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxPerformance(n, speed, efficiency, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
