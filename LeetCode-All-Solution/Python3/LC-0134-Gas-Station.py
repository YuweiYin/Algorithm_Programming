#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0134-Gas-Station.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-21
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 0134 - (Medium) - Gas Station
https://leetcode.com/problems/gas-station/

Description & Requirement:
    There are n gas stations along a circular route, 
    where the amount of gas at the ith station is gas[i].

    You have a car with an unlimited gas tank and 
    it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
    You begin the journey with an empty tank at one of the gas stations.

    Given two integer arrays gas and cost, 
    return the starting gas station's index if you can travel around the circuit once in the clockwise direction, 
    otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:
    Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    Output: 3
    Explanation:
        Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
        Travel to station 4. Your tank = 4 - 1 + 5 = 8
        Travel to station 0. Your tank = 8 - 2 + 1 = 7
        Travel to station 1. Your tank = 7 - 3 + 2 = 6
        Travel to station 2. Your tank = 6 - 4 + 3 = 5
        Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
        Therefore, return 3 as the starting index.
Example 2:
    Input: gas = [2,3,4], cost = [3,4,3]
    Output: -1
    Explanation:
        You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
        Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
        Travel to station 0. Your tank = 4 - 3 + 2 = 3
        Travel to station 1. Your tank = 3 - 3 + 3 = 3
        You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
        Therefore, you can't travel around the circuit once no matter where you start.

Constraints:
    gas.length == n
    cost.length == n
    1 <= n <= 10^5
    0 <= gas[i], cost[i] <= 10^4
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # exception case
        if not isinstance(gas, list) or len(gas) <= 0 or not isinstance(cost, list) or len(cost) != len(gas):
            return -1  # Error input type
        if len(gas) == 1:
            return 0 if gas[0] >= cost[0] else -1  # only one station
        # main method: (simply try all stations)
        return self._canCompleteCircuit(gas, cost)

    def _canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        assert n > 1 and n == len(cost)

        valid_start = -1

        start = 0
        while start < n:
            # trick: if gas[i] == cost[i], ignore it
            if gas[start] <= cost[start]:  # if True, the car can't even go to the second station
                start += 1
                continue
            # check if the car can travel a loop from the current start station
            valid_flag = True
            cur_gas = gas[start] - cost[start]  # go to the second station
            for travel_next in range(1, n + 1):
                cur_station = (start + travel_next) % n
                cur_gas += gas[cur_station] - cost[cur_station]
                if cur_gas < 0:  # can't move on, not valid
                    # optimize: if from start (gas[start] > cost[start]) can't reach cur_station
                    #     then in no way will the car start from anyone of [start, cur_station] can reach cur_station!
                    valid_flag = False
                    if cur_station > start:
                        start = cur_station  # big jump
                    break
            if valid_flag:
                return start
            start += 1

        return valid_start


def main():
    # Example 1: Output: 3
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    # Example 2: Output: -1
    # gas = [2, 3, 4]
    # cost = [3, 4, 3]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.canCompleteCircuit(gas, cost)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
