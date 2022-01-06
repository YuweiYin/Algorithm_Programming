#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1094-Car-Pooling.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-06
=================================================================="""
# import functools
import sys
import time
from typing import List

"""
LeetCode - 1094 - (Medium) - Car Pooling
https://leetcode.com/problems/car-pooling/

Description:
    There is a car with `capacity` empty seats. The vehicle only drives east 
    (i.e., it cannot turn around and drive west).

    You are given the integer `capacity` and an array `trips` where `trip[i] = [numPassengers_i, from_i, to_i]` 
    indicates that the i-th trip has `numPassengers_i` passengers and 
    the locations to pick them up and drop them off are `from_i` and `to_i` respectively. 
    The locations are given as the number of kilometers due east from the car's initial location.

Requirement:
    Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Example 1:
    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Output: false
Example 2:
    Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    Output: true

Constraints:
    1 <= trips.length <= 1000
    trips[i].length == 3
    1 <= numPassengers_i <= 100
    0 <= from_i < to_i <= 1000
    1 <= capacity <= 10^5
"""


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # exception case
        if not isinstance(trips, list) or not isinstance(capacity, int) or capacity < 0:
            return False
        # border case
        if len(trips) == 0:  # no need
            return True
        else:
            if capacity == 0:  # have needs, but no capacity
                return False
        for trip in trips:
            if not isinstance(trip, list) or len(trip) != 3:
                return False  # Error input

        # main method: (Simulate process: incident/event response)
        # return self._carPooling(trips, capacity)
        return self._carPoolingPreSum(trips, capacity)  # differential array & pre_sum

    def _carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        len_trips = len(trips)
        finish_counter = 0  # how many orders have been finished

        dict_get_on = dict({})  # key: current kilometer; value: num_passengers that will get on the car
        dict_get_off = dict({})  # key: current kilometer; value: [num_passengers, num_order]
        # coz different orders may get off at the same time, num_order is used to deal with this combining situation
        max_kilometer = 0  # record the farthest kilometer (to_i) or all orders (to avoid exception dead loop)

        # trips.sort(key=lambda _list: _list[1])  # sort requests in a non-decreasing order according to the from_i
        for trip in trips:  # deal with each trip, judge if cur_capacity is enough to handle new trip orders
            num_passengers_i, from_i, to_i = trip[0], trip[1], trip[2]
            max_kilometer = max(max_kilometer, to_i)

            if from_i in dict_get_on:  # in some other orders, passengers want to get on at from_i, too
                dict_get_on[from_i] += num_passengers_i
            else:
                dict_get_on[from_i] = num_passengers_i

            if to_i in dict_get_off:  # in some other orders, passengers want to get off at to_i, too
                dict_get_off[to_i][0] += num_passengers_i
                dict_get_off[to_i][1] += 1
            else:
                dict_get_off[to_i] = [num_passengers_i, 1]

        max_kilometer += 1  # one free kilometer, just for fun

        # simulate the car-driving process, cur_kilometer from 0 till there's no order (or unable to finish all tasks)
        cur_capacity = capacity  # the rest available seats for passengers
        cur_kilometer = 0
        while finish_counter < len_trips and cur_kilometer <= max_kilometer:
            if (cur_kilometer not in dict_get_on) and (cur_kilometer not in dict_get_off):
                # nothing happened, keep driving
                # cur_kilometer += 1
                pass
            elif (cur_kilometer in dict_get_on) and (cur_kilometer not in dict_get_off):
                # there are some passengers want to get on, but no one want to get off
                get_on_p = dict_get_on[cur_kilometer]
                if cur_capacity < get_on_p:  # can't accommodate these passengers, order failed
                    return False
                else:  # get on and go go go
                    cur_capacity -= get_on_p
            elif (cur_kilometer not in dict_get_on) and (cur_kilometer in dict_get_off):
                # there are some passengers want to get on, but no one want to get off
                get_off_p = dict_get_off[cur_kilometer][0]
                num_finish_order = dict_get_off[cur_kilometer][1]
                cur_capacity += get_off_p  # make room for other passengers
                finish_counter += num_finish_order  # finish some orders (if finish all, the loop will break and exit)
            else:
                # there are some passengers want to get on, and also some passengers want to get off
                get_on_p = dict_get_on[cur_kilometer]
                get_off_p = dict_get_off[cur_kilometer][0]
                num_finish_order = dict_get_off[cur_kilometer][1]
                # get off first
                cur_capacity += get_off_p  # make room for other passengers
                finish_counter += num_finish_order  # finish some orders (if finish all, the loop will break and exit)
                # then get on
                if cur_capacity < get_on_p:  # can't accommodate these passengers, order failed
                    return False
                else:  # get on and go go go
                    cur_capacity -= get_on_p
            cur_kilometer += 1

        return True

    def _carPoolingPreSum(self, trips: List[List[int]], capacity: int) -> bool:
        MAX_KILO = 1000 + 1  # Constraints: 0 <= from_i < to_i <= 1000
        diff_array = [0 for _ in range(MAX_KILO)]  # differential array: 0 mens no passenger get on/off at the moment
        for trip in trips:
            num_passengers_i, from_i, to_i = trip[0], trip[1], trip[2]
            diff_array[from_i] += num_passengers_i  # num_passengers_i get on the car at from_i
            diff_array[to_i] -= num_passengers_i  # num_passengers_i get off the car at to_i

        # cur_in_car_p is the pre_sum: sum(diff_array[0: cur_kilometer + 1])
        cur_in_car_p = 0  # how many passengers are in car now
        for cur_kilometer in range(MAX_KILO):
            cur_in_car_p += diff_array[cur_kilometer]  # get on or get off or keep driving
            if cur_in_car_p > capacity:  # can't accommodate these passengers, order failed
                return False

        # ran MAX_KILO, finished all orders
        return True


def main():
    # Example 1: Output: false
    # trips = [[2, 1, 5], [3, 3, 7]]
    # capacity = 4

    # Example 2: Output: true
    # trips = [[2, 1, 5], [3, 3, 7]]
    # capacity = 5

    # Example 3: Output: true
    trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
    capacity = 11

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.carPooling(trips, capacity)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
