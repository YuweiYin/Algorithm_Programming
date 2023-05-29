#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1603-Design-Parking-System.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-29
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 1603 - (Easy) - Design Parking System
https://leetcode.com/problems/design-parking-system/

Description & Requirement:
    Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: 
    big, medium, and small, with a fixed number of slots for each size.

    Implement the ParkingSystem class:
        ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. 
            The number of slots for each parking space are given as part of the constructor.
        bool addCar(int carType) Checks whether there is a parking space of carType for the car that 
            wants to get into the parking lot. carType can be of three kinds: big, medium, or small, 
            which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. 
            If there is no space available, return false, else park the car in that size space and return true.

Example 1:
    Input
        ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
        [[1, 1, 0], [1], [2], [3], [1]]
    Output
        [null, true, true, false, false]
    Explanation
        ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
        parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
        parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
        parkingSystem.addCar(3); // return false because there is no available slot for a small car
        parkingSystem.addCar(1); // return false because there is no available slot for a big car. 
            It is already occupied.

Constraints:
    0 <= big, medium, small <= 1000
    carType is 1, 2, or 3
    At most 1000 calls will be made to addCar
"""


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.car_dict = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.car_dict[carType] > 0:
            self.car_dict[carType] -= 1
            return True
        return False


def main():
    # Example 1: Output: [null, true, true, false, false]
    command_list = ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
    param_list = [[1, 1, 0], [1], [2], [3], [1]]

    # init instance
    big, medium, small = param_list[0]
    obj = ParkingSystem(big, medium, small)
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command, param = command_list[idx], param_list[idx]
        if command == "addCar" and isinstance(param, list) and len(param) == 1:
            ans.append(obj.addCar(param[0]))
        else:
            ans.append("null")
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
