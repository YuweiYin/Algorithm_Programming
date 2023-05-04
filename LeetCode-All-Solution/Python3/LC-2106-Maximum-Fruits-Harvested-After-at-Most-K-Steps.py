#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2106-Maximum-Fruits-Harvested-After-at-Most-K-Steps.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-04
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2106 - (Hard) - Maximum Fruits Harvested After at Most K Steps
https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

Description & Requirement:
    Fruits are available at some positions on an infinite x-axis. 
    You are given a 2D integer array fruits where fruits[i] = [position_i, amount_i] 
    depicts amount_i fruits at the position position_i. 
    fruits is already sorted by position_i in ascending order, and each position_i is unique.

    You are also given an integer startPos and an integer k. 
    Initially, you are at the position startPos. 
    From any position, you can either walk to the left or right. 
    It takes one step to move one unit on the x-axis, and you can walk at most k steps in total. 
    For every position you reach, you harvest all the fruits at that position, 
    and the fruits will disappear from that position.

    Return the maximum total number of fruits you can harvest.

Example 1:
    Input: fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
    Output: 9
    Explanation: 
        The optimal way is to:
        - Move right to position 6 and harvest 3 fruits
        - Move right to position 8 and harvest 6 fruits
        You moved 3 steps and harvested 3 + 6 = 9 fruits in total.
Example 2:
    Input: fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
    Output: 14
    Explanation: 
        You can move at most k = 4 steps, so you cannot reach position 0 nor 10.
        The optimal way is to:
        - Harvest the 7 fruits at the starting position 5
        - Move left to position 4 and harvest 1 fruit
        - Move right to position 6 and harvest 2 fruits
        - Move right to position 7 and harvest 4 fruits
        You moved 1 + 3 = 4 steps and harvested 7 + 1 + 2 + 4 = 14 fruits in total.
Example 3:
    Input: fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
    Output: 0
    Explanation:
        You can move at most k = 2 steps and cannot reach any position with fruits.

Constraints:
    1 <= fruits.length <= 10^5
    fruits[i].length == 2
    0 <= startPos, position_i <= 2 * 10^5
    position_{i-1} < position_i for any i > 0 (0-indexed)
    1 <= amount_i <= 10^4
    0 <= k <= 2 * 10^5
"""


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # exception case
        assert isinstance(fruits, list) and len(fruits) >= 1
        assert isinstance(startPos, int) and startPos >= 0
        assert isinstance(k, int) and k >= 0
        # main method: (two pointers / sliding window)
        return self._maxTotalFruits(fruits, startPos, k)

    def _maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        assert isinstance(fruits, list) and len(fruits) >= 1
        assert isinstance(startPos, int) and startPos >= 0
        assert isinstance(k, int) and k >= 0

        n = len(fruits)
        res = 0

        def __step(_left: int, _right: int) -> int:
            if fruits[_right][0] <= startPos:
                return startPos - fruits[_left][0]
            elif fruits[_left][0] >= startPos:
                return fruits[_right][0] - startPos
            else:
                return min(abs(startPos - fruits[_right][0]), abs(startPos - fruits[_left][0])) + \
                    fruits[_right][0] - fruits[_left][0]

        left = 0
        right = 0
        cur_sum = 0
        while right < n:
            cur_sum += fruits[right][1]
            while left <= right and __step(left, right) > k:
                cur_sum -= fruits[left][1]
                left += 1

            res = max(res, cur_sum)
            right += 1

        return res


def main():
    # Example 1: Output: 9
    # fruits = [[2, 8], [6, 3], [8, 6]]
    # startPos = 5
    # k = 4

    # Example 2: Output: 14
    fruits = [[0, 9], [4, 1], [5, 7], [6, 2], [7, 4], [10, 9]]
    startPos = 5
    k = 4

    # Example 3: Output: 0
    # fruits = [[0, 3], [6, 4], [8, 5]]
    # startPos = 3
    # k = 2

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxTotalFruits(fruits, startPos, k)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
