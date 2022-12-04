#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1774-Closest-Dessert-Cost.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-04
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 1774 - (Medium) - Closest Dessert Cost
https://leetcode.com/problems/closest-dessert-cost/

Description & Requirement:
    You would like to make dessert and are preparing to buy the ingredients. 
    You have n ice cream base flavors and m types of toppings to choose from. 
    You must follow these rules when making your dessert:
        There must be exactly one ice cream base.
        You can add one or more types of topping or have no toppings at all.
        There are at most two of each type of topping.

    You are given three inputs:
        baseCosts, an integer array of length n, 
            where each baseCosts[i] represents the price of the i-th ice cream base flavor.
        toppingCosts, an integer array of length m, where each toppingCosts[i] is the price of one of the ith topping.
        target, an integer representing your target price for dessert.

    You want to make a dessert with a total cost as close to target as possible.

    Return the closest possible cost of the dessert to target. If there are multiple, return the lower one.

Example 1:
    Input: baseCosts = [1,7], toppingCosts = [3,4], target = 10
    Output: 10
    Explanation: Consider the following combination (all 0-indexed):
        - Choose base 1: cost 7
        - Take 1 of topping 0: cost 1 x 3 = 3
        - Take 0 of topping 1: cost 0 x 4 = 0
        Total: 7 + 3 + 0 = 10.
Example 2:
    Input: baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
    Output: 17
    Explanation: Consider the following combination (all 0-indexed):
        - Choose base 1: cost 3
        - Take 1 of topping 0: cost 1 x 4 = 4
        - Take 2 of topping 1: cost 2 x 5 = 10
        - Take 0 of topping 2: cost 0 x 100 = 0
        Total: 3 + 4 + 10 + 0 = 17. You cannot make a dessert with a total cost of 18.
Example 3:
    Input: baseCosts = [3,10], toppingCosts = [2,5], target = 9
    Output: 8
    Explanation: It is possible to make desserts with cost 8 and 10. Return 8 as it is the lower cost.

Constraints:
    n == baseCosts.length
    m == toppingCosts.length
    1 <= n, m <= 10
    1 <= baseCosts[i], toppingCosts[i] <= 10^4
    1 <= target <= 10^4
"""


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # exception case
        assert isinstance(baseCosts, list) and len(baseCosts) >= 1
        assert isinstance(toppingCosts, list) and len(toppingCosts) >= 1
        assert isinstance(target, int) and target >= 1
        # main method: (dynamic programming)
        return self._closestCost(baseCosts, toppingCosts, target)

    def _closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        assert isinstance(baseCosts, list) and len(baseCosts) >= 1
        assert isinstance(toppingCosts, list) and len(toppingCosts) >= 1
        assert isinstance(target, int) and target >= 1

        x = min(baseCosts)
        if x > target:
            return x
        dp = [False] * (target + 1)

        res = 2 * target - x
        for b_cost in baseCosts:
            if b_cost <= target:
                dp[b_cost] = True
            else:
                res = min(res, b_cost)

        for t_cost in toppingCosts:
            for count in range(2):
                for idx in range(target, 0, -1):
                    if dp[idx] and idx + t_cost > target:
                        res = min(res, idx + t_cost)
                    if idx - t_cost > 0 and not dp[idx]:
                        dp[idx] = dp[idx - t_cost]

        for idx in range(res - target + 1):
            if dp[target - idx]:
                return target - idx

        return res


def main():
    # Example 1: Output: 10
    # baseCosts = [1, 7]
    # toppingCosts = [3, 4]
    # target = 10

    # Example 2: Output: 17
    # baseCosts = [2, 3]
    # toppingCosts = [4, 5, 100]
    # target = 18

    # Example 3: Output: 8
    baseCosts = [3, 10]
    toppingCosts = [2, 5]
    target = 9

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.closestCost(baseCosts, toppingCosts, target)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
