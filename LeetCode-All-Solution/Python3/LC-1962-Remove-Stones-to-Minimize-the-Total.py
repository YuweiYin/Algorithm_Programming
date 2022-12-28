#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1962-Remove-Stones-to-Minimize-the-Total.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-28
=================================================================="""

import sys
import time
from typing import List
import heapq
# import collections
# import functools

"""
LeetCode - 1962 - (Medium) - Remove Stones to Minimize the Total
https://leetcode.com/problems/remove-stones-to-minimize-the-total/

Description & Requirement:
    You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the i-th pile, 
    and an integer k. You should apply the following operation exactly k times:

        Choose any piles[i] and remove floor(piles[i] / 2) stones from it.

    Notice that you can apply the operation on the same pile more than once.

    Return the minimum possible total number of stones remaining after applying the k operations.

    floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).

Example 1:
    Input: piles = [5,4,9], k = 2
    Output: 12
    Explanation: Steps of a possible scenario are:
        - Apply the operation on pile 2. The resulting piles are [5,4,5].
        - Apply the operation on pile 0. The resulting piles are [3,4,5].
        The total number of stones in [3,4,5] is 12.
Example 2:
    Input: piles = [4,3,6,7], k = 3
    Output: 12
    Explanation: Steps of a possible scenario are:
        - Apply the operation on pile 2. The resulting piles are [4,3,3,7].
        - Apply the operation on pile 3. The resulting piles are [4,3,3,4].
        - Apply the operation on pile 0. The resulting piles are [2,3,3,4].
        The total number of stones in [2,3,3,4] is 12.

Constraints:
    1 <= piles.length <= 10^5
    1 <= piles[i] <= 10^4
    1 <= k <= 10^5
"""


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # exception case
        assert isinstance(piles, list) and len(piles) >= 1
        assert isinstance(k, int) and k >= 1
        # main method: (heap / priority queue)
        return self._minStoneSum(piles, k)

    def _minStoneSum(self, piles: List[int], k: int) -> int:
        """
        Time: beats 83.88%; Space: beats 95.88%
        """
        assert isinstance(piles, list) and len(piles) >= 1
        assert isinstance(k, int) and k >= 1

        for idx in range(len(piles)):
            piles[idx] = -piles[idx]

        heapq.heapify(piles)

        for _ in range(k):
            pile = heapq.heappop(piles)
            heapq.heappush(piles, pile + ((-pile) >> 1))

        return -sum(piles)


def main():
    # Example 1: Output: 12
    # piles = [5, 4, 9]
    # k = 2

    # Example 2: Output: 12
    piles = [4, 3, 6, 7]
    k = 3

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.minStoneSum(piles, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
