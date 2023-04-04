#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1000-Minimum-Cost-to-Merge-Stones.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-04
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1000 - (Hard) - Minimum Cost to Merge Stones
https://leetcode.com/problems/minimum-cost-to-merge-stones/

Description & Requirement:
    There are n piles of stones arranged in a row. The ith pile has stones[i] stones.

    A move consists of merging exactly k consecutive piles into one pile, and 
    the cost of this move is equal to the total number of stones in these k piles.

    Return the minimum cost to merge all piles of stones into one pile. 
    If it is impossible, return -1.

Example 1:
    Input: stones = [3,2,4,1], k = 2
    Output: 20
    Explanation: We start with [3, 2, 4, 1].
        We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
        We merge [4, 1] for a cost of 5, and we are left with [5, 5].
        We merge [5, 5] for a cost of 10, and we are left with [10].
        The total cost was 20, and this is the minimum possible.
Example 2:
    Input: stones = [3,2,4,1], k = 3
    Output: -1
    Explanation: After any merge operation, there are 2 piles left, and 
        we can't merge anymore.  So the task is impossible.
Example 3:
    Input: stones = [3,5,1,2,6], k = 3
    Output: 25
    Explanation: We start with [3, 5, 1, 2, 6].
        We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
        We merge [3, 8, 6] for a cost of 17, and we are left with [17].
        The total cost was 25, and this is the minimum possible.

Constraints:
    n == stones.length
    1 <= n <= 30
    1 <= stones[i] <= 100
    2 <= k <= 30
"""


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        # exception case
        assert isinstance(stones, list) and len(stones) >= 1
        assert isinstance(k, int) and k >= 2
        # main method: (dynamic programming)
        return self._mergeStones(stones, k)

    def _mergeStones(self, stones: List[int], k: int) -> int:
        assert isinstance(stones, list) and len(stones) >= 1
        assert isinstance(k, int) and k >= 2

        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        dp = [[int(1e9+7)] * n for _ in range(n)]
        cur_sum = [0] * n
        s = 0

        for i in range(n):
            dp[i][i] = 0
            s += stones[i]
            cur_sum[i] = s

        for i in range(2, n + 1):
            for left in range(n - i + 1):
                right = left + i - 1
                for p in range(left, right, k - 1):
                    dp[left][right] = min(dp[left][right], dp[left][p] + dp[p + 1][right])
                if (right - left) % (k - 1) == 0:
                    dp[left][right] += (cur_sum[right] - (0 if left == 0 else cur_sum[left - 1]))

        return dp[0][n - 1]


def main():
    # Example 1: Output: 20
    # stones = [3, 2, 4, 1]
    # k = 2

    # Example 2: Output: -1
    # stones = [3, 2, 4, 1]
    # k = 3

    # Example 3: Output: 25
    stones = [3, 5, 1, 2, 6]
    k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.mergeStones(stones, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
