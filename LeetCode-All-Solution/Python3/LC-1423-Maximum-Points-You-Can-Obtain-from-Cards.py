#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1423-Maximum-Points-You-Can-Obtain-from-Cards.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-26
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1423 - (Medium) - Maximum Points You Can Obtain from Cards
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

Description & Requirement:
    There are several cards arranged in a row, and each card has an associated number of points. 
    The points are given in the integer array cardPoints.

    In one step, you can take one card from the beginning or from the end of the row. 
    You have to take exactly k cards.

    Your score is the sum of the points of the cards you have taken.

    Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:
    Input: cardPoints = [1,2,3,4,5,6,1], k = 3
    Output: 12
    Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:
    Input: cardPoints = [2,2,2], k = 2
    Output: 4
    Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:
    Input: cardPoints = [9,7,7,9,7,7,9], k = 7
    Output: 55
    Explanation: You have to take all the cards. Your score is the sum of points of all cards.

Constraints:
    1 <= cardPoints.length <= 10^5
    1 <= cardPoints[i] <= 10^4
    1 <= k <= cardPoints.length
"""


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # exception case
        assert isinstance(k, int) and k >= 1
        assert isinstance(cardPoints, list) and len(cardPoints) >= 1
        for cardPoint in cardPoints:
            assert isinstance(cardPoint, int) and cardPoint >= 1
        # main method: (sliding window)
        return self._maxScore(cardPoints, k)

    def _maxScore(self, cardPoints: List[int], k: int) -> int:
        assert isinstance(k, int) and k >= 1
        assert isinstance(cardPoints, list) and len(cardPoints) >= 1

        num_card = len(cardPoints)
        window_size = num_card - k

        cur_sum = sum(cardPoints[:window_size])  # init: the sum of left window_size numbers
        min_sum = cur_sum

        for right in range(window_size, num_card):
            cur_sum += cardPoints[right] - cardPoints[right - window_size]  # add up right item, remove left item
            min_sum = min(min_sum, cur_sum)

        return sum(cardPoints) - min_sum


def main():
    # Example 1: Output: 12
    # cardPoints = [1, 2, 3, 4, 5, 6, 1]
    # k = 3

    # Example 2: Output: 4
    # cardPoints = [2, 2, 2]
    # k = 2

    # Example 3: Output: 55
    cardPoints = [9, 7, 7, 9, 7, 7, 9]
    k = 7

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxScore(cardPoints, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
