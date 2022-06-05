#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0829-Consecutive-Numbers-Sum.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-05
=================================================================="""

import sys
import time
from typing import List
import random
import math
# import functools

"""
LeetCode - 0829 - (Hard) - Consecutive Numbers Sum
https://leetcode.com/problems/generate-random-point-in-a-circle/

Description & Requirement:
    Given the radius and the position of the center of a circle, 
    implement the function randPoint which generates a uniform random point inside the circle.

    Implement the Solution class:
        Solution(double radius, double x_center, double y_center) initializes the object 
            with the radius of the circle radius and the position of the center (x_center, y_center).
        randPoint() returns a random point inside the circle. A point on the circumference of the circle 
            is considered to be in the circle. The answer is returned as an array [x, y].

Example 1:
    Input
        ["Solution", "randPoint", "randPoint", "randPoint"]
        [[1.0, 0.0, 0.0], [], [], []]
    Output
        [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
    Explanation
        Solution solution = new Solution(1.0, 0.0, 0.0);
        solution.randPoint(); // return [-0.02493, -0.38077]
        solution.randPoint(); // return [0.82314, 0.38945]
        solution.randPoint(); // return [0.36572, 0.17248]

Constraints:
    0 < radius <= 10^8
    -10^7 <= x_center, y_center <= 10^7
    At most 3 * 104 calls will be made to randPoint.
"""


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # method 1: reject sampling
        def __reject_sampling() -> List[float]:
            while True:
                # generate x and y separately
                x, y = random.uniform(-self.radius, self.radius), random.uniform(-self.radius, self.radius)
                # judge if x^2 + y^2 <= r^2, if not, reject x and y, and then re-generate points (next loop)
                if x * x + y * y <= self.radius * self.radius:
                    return [self.x_center + x, self.y_center + y]

        # method 2: generate points based on the distribution function
        # x = r * \cos \theta; y = r * \sin \theta
        def __distribution_function() -> List[float]:
            r_square, theta = random.random(), random.random() * 2 * math.pi
            r = math.sqrt(r_square)
            return [self.x_center + r * math.cos(theta) * self.radius,
                    self.y_center + r * math.sin(theta) * self.radius]

        return __reject_sampling()
        # return __distribution_function()


def main():
    # Example 1: Output: [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
    command_list = ["Solution", "randPoint", "randPoint", "randPoint"]
    param_list = [[1.0, 0.0, 0.0], [], [], []]

    # init instance
    # solution = Solution()
    radius, x_center, y_center = param_list[0]
    obj = Solution(radius, x_center, y_center)

    # run & time
    start = time.process_time()
    ans = ["null"]
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        # param = param_list[idx]
        if command == "randPoint":
            ans.append(obj.randPoint())
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
