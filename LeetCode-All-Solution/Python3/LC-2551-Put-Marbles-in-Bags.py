#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2551-Put-Marbles-in-Bags.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-08
=================================================================="""

import sys
import time
from typing import List
# import functools
# import itertools

"""
LeetCode - 2551 - (Hard) - Put Marbles in Bags
https://leetcode.com/problems/put-marbles-in-bags/

Description & Requirement:
    You have k bags. You are given a 0-indexed integer array weights where weights[i] 
    is the weight of the ith marble. You are also given the integer k.

    Divide the marbles into the k bags according to the following rules:
        No bag is empty.
        If the ith marble and jth marble are in a bag, then all marbles with an index between 
            the ith and jth indices should also be in that same bag.
        If a bag consists of all the marbles with an index from i to j inclusively, 
            then the cost of the bag is weights[i] + weights[j].

    The score after distributing the marbles is the sum of the costs of all the k bags.

    Return the difference between the maximum and minimum scores among marble distributions.

Example 1:
    Input: weights = [1,3,5,1], k = 2
    Output: 4
    Explanation: 
        The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6. 
        The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10. 
        Thus, we return their difference 10 - 6 = 4.
Example 2:
    Input: weights = [1, 3], k = 2
    Output: 0
    Explanation: The only distribution possible is [1],[3]. 
        Since both the maximal and minimal score are the same, we return 0.

Constraints:
    1 <= k <= weights.length <= 10^5
    1 <= weights[i] <= 10^9
"""


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # exception case
        assert isinstance(k, int) and k >= 1
        assert isinstance(weights, list) and len(weights) >= k
        # main method: (sorting)
        return self._putMarbles(weights, k)

    def _putMarbles(self, weights: List[int], k: int) -> int:
        assert isinstance(k, int) and k >= 1
        assert isinstance(weights, list) and len(weights) >= k

        for i in range(len(weights) - 1):
            weights[i] += weights[i + 1]

        weights.pop()
        weights.sort()

        return sum(weights[len(weights) - k + 1:]) - sum(weights[:k - 1])


def main():
    # Example 1: Output: 4
    weights = [1, 3, 5, 1]
    k = 2

    # Example 2: Output: 0
    # weights = [1, 3]
    # k = 2

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.putMarbles(weights, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
