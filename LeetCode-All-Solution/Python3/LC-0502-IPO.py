#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0502-IPO.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-23
=================================================================="""

import sys
import time
from typing import List
import heapq
# import collections

"""
LeetCode - 0502 - (Hard) - IPO
https://leetcode.com/problems/ipo/

Description & Requirement:
    Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, 
    LeetCode would like to work on some projects to increase its capital before the IPO. 
    Since it has limited resources, it can only finish at most k distinct projects before the IPO. 
    Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

    You are given n projects where the ith project has a pure profit profits[i] 
    and a minimum capital of capital[i] is needed to start it.

    Initially, you have w capital. When you finish a project, you will obtain its pure profit 
    and the profit will be added to your total capital.

    Pick a list of at most k distinct projects from given projects to maximize your final capital, 
    and return the final maximized capital.

    The answer is guaranteed to fit in a 32-bit signed integer.

Example 1:
    Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
    Output: 4
    Explanation: Since your initial capital is 0, you can only start the project indexed 0.
        After finishing it you will obtain profit 1 and your capital becomes 1.
        With capital 1, you can either start the project indexed 1 or the project indexed 2.
        Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
        Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:
    Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
    Output: 6

Constraints:
    1 <= k <= 10^5
    0 <= w <= 10^9
    n == profits.length
    n == capital.length
    1 <= n <= 10^5
    0 <= profits[i] <= 10^4
    0 <= capital[i] <= 10^9
"""


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # exception case
        assert isinstance(k, int) and k >= 1
        assert isinstance(w, int) and w >= 0
        assert isinstance(profits, list) and len(profits) >= 1
        assert isinstance(capital, list) and len(capital) == len(profits)
        # main method: (heap)
        return self._findMaximizedCapital(k, w, profits, capital)

    def _findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        assert isinstance(k, int) and k >= 1
        assert isinstance(w, int) and w >= 0
        assert isinstance(profits, list) and len(profits) >= 1
        assert isinstance(capital, list) and len(capital) == len(profits)

        n = len(profits)
        projects = sorted(zip(profits, capital), key=lambda x: x[1])

        cur_w = []
        idx = 0

        while k > 0:
            while idx < n and projects[idx][1] <= w:
                heapq.heappush(cur_w, -projects[idx][0])
                idx += 1

            if len(cur_w) > 0:
                w -= heapq.heappop(cur_w)
            else:
                break
            k -= 1

        return w


def main():
    # Example 1: Output: 4
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]

    # Example 2: Output: 6
    # k = 3
    # w = 0
    # profits = [1, 2, 3]
    # capital = [0, 1, 2]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findMaximizedCapital(k, w, profits, capital)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
