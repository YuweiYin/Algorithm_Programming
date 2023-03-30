#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1402-Reducing-Dishes.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-03-29
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1402 - (Hard) - Reducing Dishes
https://leetcode.com/problems/reducing-dishes/

Description & Requirement:
    A chef has collected data on the satisfaction level of his n dishes. 
    Chef can cook any dish in 1 unit of time.

    Like-time coefficient of a dish is defined as the time taken to cook that dish including 
    previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

    Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

    Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

Example 1:
    Input: satisfaction = [-1,-8,0,5,-9]
    Output: 14
    Explanation: After Removing the second and last dish, the maximum total like-time coefficient 
        will be equal to (-1*1 + 0*2 + 5*3 = 14).
        Each dish is prepared in one unit of time.
Example 2:
    Input: satisfaction = [4,3,2]
    Output: 20
    Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
Example 3:
    Input: satisfaction = [-1,-4,-5]
    Output: 0
    Explanation: People do not like the dishes. No dish is prepared.

Constraints:
    n == satisfaction.length
    1 <= n <= 500
    -1000 <= satisfaction[i] <= 1000
"""


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # exception case
        assert isinstance(satisfaction, list) and len(satisfaction) >= 1
        # main method: (prefix sum & sorting & greedy)
        return self._maxSatisfaction(satisfaction)

    def _maxSatisfaction(self, satisfaction: List[int]) -> int:
        assert isinstance(satisfaction, list) and len(satisfaction) >= 1

        res = 0

        satisfaction.sort(reverse=True)
        pre_sum = 0

        for s in satisfaction:
            if pre_sum + s > 0:
                pre_sum += s
                res += pre_sum
            else:
                break

        return res


def main():
    # Example 1: Output: 14
    satisfaction = [-1, -8, 0, 5, -9]

    # Example 2: Output: 20
    # satisfaction = [4, 3, 2]

    # Example 3: Output: 0
    # satisfaction = [-1, -4, -5]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maxSatisfaction(satisfaction)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
