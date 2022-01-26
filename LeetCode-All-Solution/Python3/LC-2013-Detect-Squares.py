#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2013-Detect-Squares.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-26
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 2013 - (Medium) - Detect Squares
https://leetcode.com/problems/detect-squares/

Description & Requirement:
    You are given a stream of points on the X-Y plane. Design an algorithm that:

        Adds new points from the stream into a data structure. 
            Duplicate points are allowed and should be treated as different points.
        Given a query point, counts the number of ways to choose three points from the data structure 
            such that the three points and the query point form an axis-aligned square with positive area.
        An axis-aligned square is a square whose edges are all the same length and 
            are either parallel or perpendicular to the x-axis and y-axis.

    Implement the DetectSquares class:
        DetectSquares() Initializes the object with an empty data structure.
        void add(int[] point) Adds a new point point = [x, y] to the data structure.
        int count(int[] point) Counts the number of ways to form axis-aligned squares 
            with point point = [x, y] as described above.

Example 1:
    Input
        ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
        [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
    Output
        [null, null, null, null, 1, 0, null, 2]
    Explanation
        DetectSquares detectSquares = new DetectSquares();
        detectSquares.add([3, 10]);
        detectSquares.add([11, 2]);
        detectSquares.add([3, 2]);
        detectSquares.count([11, 10]); // return 1. You can choose:
                                       //   - The first, second, and third points
        detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points 
                                       //     in the data structure.
        detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
        detectSquares.count([11, 10]); // return 2. You can choose:
                                       //   - The first, second, and third points
                                       //   - The first, third, and fourth points

Constraints:
    point.length == 2
    0 <= x, y <= 1000
    At most 3000 calls in total will be made to add and count.
"""


class DetectSquares:

    def __init__(self):
        # from sortedcontainers import SortedList
        # self.points_list = SortedList()
        self.points_list = []
        self.points_dict = dict({})  # key: point tuple(x, y); value: point counter

    def add(self, point: List[int]) -> None:
        # self.points_list.add(point)
        if tuple(point) in self.points_dict:
            self.points_dict[tuple(point)] += 1
        else:
            self.points_list.append(point)  # only append to list once
            self.points_dict[tuple(point)] = 1

    def count(self, point: List[int]) -> int:
        ways = 0

        x_same_list = []  # all points that have the same x-axis index (but different y) with the target_point
        y_same_list = []  # all points that have the same y-axis index (but different x) with the target_point
        for p in self.points_list:
            if p[0] == point[0] and p[1] != point[1]:
                x_same_list.append(p)
            elif p[1] == point[1] and p[0] != point[0]:
                y_same_list.append(p)

        for x in x_same_list:  # x[0] == target_point[0]
            for y in y_same_list:  # y[1] == target_point[1]
                # if (y[0], x[1]) exist, then a valid square can be formed
                if abs(x[1] - point[1]) != abs(y[0] - point[0]):  # guarantee the edge length property of a square
                    continue
                if (y[0], x[1]) in self.points_dict:
                    # 3 points, if each point is A/B/C duplicated, then can form A * B * C squares
                    assert tuple(x) in self.points_dict and tuple(y) in self.points_dict
                    ways += self.points_dict[(y[0], x[1])] * self.points_dict[tuple(x)] * self.points_dict[tuple(y)]

        return ways


# class DetectSquares:
#
#     def __init__(self):
#         from collections import defaultdict, Counter
#         # 2-dim dict method
#         self.point_hash = defaultdict(Counter)  # key1: x-axis index; key2: y-axis index; value: counter of point (x, y)
#
#     def add(self, point: List[int]) -> None:
#         # assert isinstance(point, list) and len(point) == 2 and isinstance(point[0], int) and isinstance(point[1], int)
#         self.point_hash[point[0]][point[1]] += 1  # 2-dim hash, consider x-axis first, then y-axis
#
#     def count(self, point: List[int]) -> int:
#         ways = 0
#         target_x, target_y = point
#
#         # consider x-axis first, if x is the same with the target point, then consider y-axis
#         if target_x not in self.point_hash:
#             return 0
#         target_y_dict = self.point_hash[target_x]
#
#         for cur_x, cur_y_dict in self.point_hash.items():
#             if cur_x != target_x:  # guarantee the area of square is larger than 0
#                 edge_len = cur_x - target_x  # x-axis edge length, the same to y-axis edge length (coz it's square)
#                 # 3 points, if each point is A/B/C duplicated, then can form A * B * C squares
#                 # 2 cases: target_y + edge_len  /  target_y - edge_len
#                 # cur_y_dict[target_y] means the number of point (cur_x, cur_y_dict[target_y])
#                 ways += cur_y_dict[target_y] * cur_y_dict[target_y + edge_len] * target_y_dict[target_y + edge_len]
#                 ways += cur_y_dict[target_y] * cur_y_dict[target_y - edge_len] * target_y_dict[target_y - edge_len]
#
#         return ways


def main():
    # Example 1: Output: [null, null, null, null, 1, 0, null, 2]
    # command_list = ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
    # param_list = [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]

    # Example 2: Output:
    command_list = ["DetectSquares", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add",
                    "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count",
                    "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add",
                    "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add",
                    "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add",
                    "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count",
                    "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add",
                    "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add",
                    "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add",
                    "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count",
                    "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add",
                    "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add",
                    "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add",
                    "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count",
                    "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add",
                    "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add",
                    "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add",
                    "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count",
                    "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add",
                    "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add",
                    "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add",
                    "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count",
                    "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add",
                    "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add",
                    "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add",
                    "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count",
                    "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add",
                    "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add",
                    "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add",
                    "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count",
                    "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add",
                    "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add",
                    "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add",
                    "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count",
                    "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add",
                    "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add",
                    "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add",
                    "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count",
                    "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add",
                    "add", "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add",
                    "add", "count", "add", "add", "add", "count", "add", "add", "add", "count", "add", "add", "add",
                    "count", "add", "add", "add", "count", "add", "add", "add", "count"]
    param_list = [[], [[5, 10]], [[10, 5]], [[10, 10]], [[5, 5]], [[3, 0]], [[8, 0]], [[8, 5]], [[3, 5]], [[9, 0]],
                  [[9, 8]], [[1, 8]], [[1, 0]], [[0, 0]], [[8, 0]], [[8, 8]], [[0, 8]], [[1, 9]], [[2, 9]], [[2, 10]],
                  [[1, 10]], [[7, 8]], [[2, 3]], [[2, 8]], [[7, 3]], [[9, 10]], [[9, 5]], [[4, 5]], [[4, 10]], [[0, 9]],
                  [[4, 5]], [[4, 9]], [[0, 5]], [[1, 10]], [[10, 1]], [[10, 10]], [[1, 1]], [[10, 0]], [[2, 0]],
                  [[2, 8]], [[10, 8]], [[7, 6]], [[4, 6]], [[4, 9]], [[7, 9]], [[10, 9]], [[10, 0]], [[1, 0]], [[1, 9]],
                  [[0, 9]], [[8, 1]], [[0, 1]], [[8, 9]], [[3, 9]], [[10, 9]], [[3, 2]], [[10, 2]], [[3, 8]], [[9, 2]],
                  [[3, 2]], [[9, 8]], [[0, 9]], [[7, 9]], [[0, 2]], [[7, 2]], [[10, 1]], [[1, 10]], [[10, 10]],
                  [[1, 1]], [[6, 10]], [[2, 6]], [[6, 6]], [[2, 10]], [[6, 0]], [[6, 2]], [[8, 2]], [[8, 0]], [[6, 5]],
                  [[7, 4]], [[6, 4]], [[7, 5]], [[2, 10]], [[8, 4]], [[2, 4]], [[8, 10]], [[2, 6]], [[2, 5]], [[1, 5]],
                  [[1, 6]], [[10, 9]], [[10, 0]], [[1, 9]], [[1, 0]], [[0, 9]], [[5, 9]], [[0, 4]], [[5, 4]], [[3, 6]],
                  [[9, 0]], [[3, 0]], [[9, 6]], [[0, 2]], [[1, 1]], [[0, 1]], [[1, 2]], [[1, 7]], [[8, 0]], [[8, 7]],
                  [[1, 0]], [[2, 7]], [[4, 5]], [[2, 5]], [[4, 7]], [[6, 7]], [[3, 7]], [[6, 4]], [[3, 4]], [[10, 2]],
                  [[2, 10]], [[2, 2]], [[10, 10]], [[10, 1]], [[1, 10]], [[1, 1]], [[10, 10]], [[2, 10]], [[2, 9]],
                  [[3, 9]], [[3, 10]], [[10, 1]], [[1, 10]], [[1, 1]], [[10, 10]], [[10, 4]], [[10, 3]], [[9, 4]],
                  [[9, 3]], [[6, 6]], [[6, 10]], [[10, 6]], [[10, 10]], [[9, 7]], [[4, 7]], [[9, 2]], [[4, 2]],
                  [[2, 3]], [[2, 1]], [[0, 3]], [[0, 1]], [[2, 8]], [[10, 8]], [[2, 0]], [[10, 0]], [[8, 4]], [[2, 10]],
                  [[8, 10]], [[2, 4]], [[0, 0]], [[9, 9]], [[0, 9]], [[9, 0]], [[5, 7]], [[5, 8]], [[4, 7]], [[4, 8]],
                  [[10, 10]], [[10, 1]], [[1, 1]], [[1, 10]], [[6, 8]], [[7, 8]], [[6, 9]], [[7, 9]], [[4, 6]],
                  [[1, 6]], [[4, 3]], [[1, 3]], [[10, 1]], [[1, 10]], [[10, 10]], [[1, 1]], [[7, 7]], [[7, 10]],
                  [[4, 7]], [[4, 10]], [[0, 0]], [[8, 0]], [[0, 8]], [[8, 8]], [[3, 5]], [[2, 4]], [[3, 4]], [[2, 5]],
                  [[0, 6]], [[0, 2]], [[4, 2]], [[4, 6]], [[5, 2]], [[9, 6]], [[9, 2]], [[5, 6]], [[1, 1]], [[1, 10]],
                  [[10, 10]], [[10, 1]], [[7, 5]], [[2, 0]], [[2, 5]], [[7, 0]], [[1, 9]], [[1, 2]], [[8, 2]], [[8, 9]],
                  [[3, 8]], [[3, 3]], [[8, 3]], [[8, 8]], [[3, 10]], [[9, 10]], [[3, 4]], [[9, 4]], [[0, 2]], [[0, 10]],
                  [[8, 10]], [[8, 2]], [[9, 4]], [[8, 4]], [[8, 5]], [[9, 5]], [[9, 8]], [[4, 3]], [[4, 8]], [[9, 3]],
                  [[4, 9]], [[0, 5]], [[0, 9]], [[4, 5]], [[1, 3]], [[3, 5]], [[1, 5]], [[3, 3]], [[0, 0]], [[0, 8]],
                  [[8, 0]], [[8, 8]], [[2, 8]], [[10, 0]], [[10, 8]], [[2, 0]], [[8, 1]], [[0, 9]], [[8, 9]], [[0, 1]],
                  [[4, 9]], [[4, 6]], [[1, 9]], [[1, 6]], [[0, 9]], [[0, 8]], [[1, 9]], [[1, 8]], [[5, 1]], [[5, 6]],
                  [[10, 1]], [[10, 6]], [[9, 2]], [[2, 2]], [[2, 9]], [[9, 9]], [[5, 5]], [[8, 5]], [[5, 8]], [[8, 8]],
                  [[8, 0]], [[1, 0]], [[8, 7]], [[1, 7]], [[8, 2]], [[5, 5]], [[5, 2]], [[8, 5]], [[6, 6]], [[6, 8]],
                  [[8, 6]], [[8, 8]], [[2, 10]], [[10, 2]], [[2, 2]], [[10, 10]], [[1, 9]], [[8, 2]], [[1, 2]],
                  [[8, 9]], [[7, 4]], [[7, 2]], [[9, 4]], [[9, 2]], [[1, 9]], [[1, 0]], [[10, 0]], [[10, 9]], [[2, 10]],
                  [[2, 3]], [[9, 10]], [[9, 3]], [[10, 0]], [[1, 0]], [[1, 9]], [[10, 9]], [[8, 10]], [[1, 10]],
                  [[1, 3]], [[8, 3]], [[0, 9]], [[9, 9]], [[0, 0]], [[9, 0]], [[7, 9]], [[8, 9]], [[7, 8]], [[8, 8]],
                  [[3, 1]], [[9, 7]], [[9, 1]], [[3, 7]], [[5, 9]], [[6, 9]], [[5, 8]], [[6, 8]], [[0, 1]], [[0, 10]],
                  [[9, 10]], [[9, 1]], [[8, 0]], [[8, 2]], [[10, 2]], [[10, 0]], [[8, 0]], [[0, 8]], [[8, 8]], [[0, 0]],
                  [[6, 7]], [[5, 8]], [[5, 7]], [[6, 8]], [[0, 9]], [[0, 2]], [[7, 9]], [[7, 2]], [[5, 0]], [[5, 5]],
                  [[10, 0]], [[10, 5]], [[1, 10]], [[10, 10]], [[10, 1]], [[1, 1]], [[9, 2]], [[9, 10]], [[1, 2]],
                  [[1, 10]], [[1, 10]], [[10, 1]], [[10, 10]], [[1, 1]], [[9, 9]], [[0, 9]], [[0, 0]], [[9, 0]],
                  [[9, 6]], [[9, 3]], [[6, 3]], [[6, 6]], [[10, 4]], [[6, 0]], [[10, 0]], [[6, 4]], [[6, 8]], [[0, 2]],
                  [[0, 8]], [[6, 2]], [[7, 9]], [[0, 9]], [[7, 2]], [[0, 2]], [[9, 1]], [[9, 10]], [[0, 10]], [[0, 1]],
                  [[10, 0]], [[10, 9]], [[1, 9]], [[1, 0]], [[1, 6]], [[1, 9]], [[4, 9]], [[4, 6]], [[0, 8]], [[1, 9]],
                  [[0, 9]], [[1, 8]], [[1, 1]], [[9, 1]], [[1, 9]], [[9, 9]], [[2, 5]], [[2, 9]], [[6, 5]], [[6, 9]],
                  [[7, 3]], [[2, 3]], [[2, 8]], [[7, 8]], [[9, 4]], [[4, 4]], [[9, 9]], [[4, 9]], [[4, 4]], [[2, 4]],
                  [[4, 2]], [[2, 2]], [[0, 3]], [[0, 2]], [[1, 3]], [[1, 2]], [[10, 9]], [[10, 2]], [[3, 2]], [[3, 9]],
                  [[5, 6]], [[10, 6]], [[10, 1]], [[5, 1]], [[9, 0]], [[0, 9]], [[9, 9]], [[0, 0]], [[5, 6]], [[9, 2]],
                  [[9, 6]], [[5, 2]], [[3, 3]], [[10, 3]], [[10, 10]], [[3, 10]], [[2, 4]], [[2, 10]], [[8, 4]],
                  [[8, 10]], [[4, 9]], [[1, 9]], [[4, 6]], [[1, 6]], [[1, 8]], [[9, 0]], [[1, 0]], [[9, 8]], [[10, 3]],
                  [[5, 8]], [[5, 3]], [[10, 8]], [[8, 2]], [[0, 10]], [[8, 10]], [[0, 2]], [[9, 0]], [[2, 7]], [[9, 7]],
                  [[2, 0]], [[0, 4]], [[5, 9]], [[0, 9]], [[5, 4]], [[5, 3]], [[10, 3]], [[5, 8]], [[10, 8]], [[6, 4]],
                  [[7, 4]], [[6, 5]], [[7, 5]], [[9, 1]], [[0, 1]], [[9, 10]], [[0, 10]], [[5, 10]], [[5, 7]], [[8, 7]],
                  [[8, 10]], [[8, 0]], [[8, 7]], [[1, 7]], [[1, 0]], [[1, 1]], [[9, 9]], [[1, 9]], [[9, 1]], [[3, 1]],
                  [[3, 5]], [[7, 5]], [[7, 1]], [[5, 8]], [[5, 3]], [[10, 8]], [[10, 3]], [[0, 9]], [[2, 7]], [[2, 9]],
                  [[0, 7]], [[9, 3]], [[9, 7]], [[5, 3]], [[5, 7]], [[0, 0]], [[9, 0]], [[9, 9]], [[0, 9]], [[6, 4]],
                  [[4, 2]], [[4, 4]], [[6, 2]], [[1, 9]], [[1, 5]], [[5, 5]], [[5, 9]], [[7, 7]], [[0, 7]], [[0, 0]],
                  [[7, 0]], [[1, 3]], [[1, 9]], [[7, 3]], [[7, 9]], [[0, 9]], [[9, 9]], [[9, 0]], [[0, 0]], [[1, 8]],
                  [[3, 6]], [[3, 8]], [[1, 6]]]

    # init instance
    # solution = Solution()

    # run & time
    start = time.process_time()
    obj = DetectSquares()
    assert len(command_list) == len(param_list)
    cursor = 1  # skip the class construction command
    while cursor < len(command_list):
        if command_list[cursor] == "add":
            obj.add(param_list[cursor][0])
        elif command_list[cursor] == "count":
            print(obj.count(param_list[cursor][0]))
        cursor += 1
    end = time.process_time()

    # show answer
    # print('\nAnswer:')
    # print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
