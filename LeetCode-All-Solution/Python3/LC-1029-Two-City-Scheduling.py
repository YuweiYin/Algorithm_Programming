#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1029-Two-City-Scheduling.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-03-25
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1029 - (Medium) - Two City Scheduling
https://leetcode.com/problems/two-city-scheduling/

Description & Requirement:
    A company is planning to interview 2n people. Given the array costs where costs[i] = [a_Cost_i, b_Cost_i], 
    the cost of flying the ith person to city a is a_Cost_i, 
    and the cost of flying the ith person to city b is b_Cost_i.

    Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Example 1:
    Input: costs = [[10,20],[30,200],[400,50],[30,20]]
    Output: 110
    Explanation: 
        The first person goes to city A for a cost of 10.
        The second person goes to city A for a cost of 30.
        The third person goes to city B for a cost of 50.
        The fourth person goes to city B for a cost of 20.
    The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
Example 2:
    Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    Output: 1859
Example 3:
    Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
    Output: 3086

Constraints:
    2 * n == costs.length
    2 <= costs.length <= 100
    costs.length is even.
    1 <= a_Cost_i, b_Cost_i <= 1000
"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # exception case
        assert isinstance(costs, list) and len(costs) >= 2 and len(costs) & 0x01 == 0
        for cost in costs:
            assert isinstance(cost, list) and len(cost) == 2
        # main method: (firstly, greedily choose the cheap one and record the fee diff)
        #     then modify the choices to balance the flight (sort diff, and modify the flights with the lowest diff)
        return self._twoCitySchedCost(costs)

    def _twoCitySchedCost(self, costs: List[List[int]]) -> int:
        assert isinstance(costs, list) and len(costs) >= 2 and len(costs) & 0x01 == 0

        # n = len(costs) >> 1
        choice_diff = []  # item: (True/False, abs(cost[0] - cost[1]))
        city_a_counter, city_b_counter, total_cost = 0, 0, 0
        for cost in costs:
            a_cost, b_cost = cost
            if a_cost <= b_cost:  # fly to city a
                choice_diff.append([True, b_cost - a_cost])
                city_a_counter += 1
                total_cost += a_cost
            else:  # fly to city b
                choice_diff.append([False, a_cost - b_cost])
                city_b_counter += 1
                total_cost += b_cost

        if city_a_counter == city_b_counter:
            return total_cost

        choice_diff.sort(key=lambda x: x[1])
        idx = 0
        while city_a_counter > city_b_counter:  # reduce city a (choice_diff[idx][0] True -> False)
            while not choice_diff[idx][0]:
                idx += 1
            # now choice_diff[idx][0] is True, change this flight
            city_a_counter -= 1
            city_b_counter += 1
            choice_diff[idx][0] = not choice_diff[idx][0]
            total_cost += choice_diff[idx][1]
        idx = 0
        while city_a_counter < city_b_counter:  # reduce city b (choice_diff[idx][0] False -> True)
            while choice_diff[idx][0]:
                idx += 1
            # now choice_diff[idx][0] is False, change this flight
            city_a_counter += 1
            city_b_counter -= 1
            choice_diff[idx][0] = not choice_diff[idx][0]
            total_cost += choice_diff[idx][1]

        return total_cost


def main():
    # Example 1: Output: 110
    # costs = [[10, 20], [30, 200], [400, 50], [30, 20]]

    # Example 2: Output: 1859
    # costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]

    # Example 3: Output: 3086
    costs = [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.twoCitySchedCost(costs)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
