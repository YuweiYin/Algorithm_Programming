#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1710-Maximum-Units-on-a-Truck.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-07-01
=================================================================="""

import sys
import time
from typing import List
# import functools

"""
LeetCode - 1710 - (Easy) - Maximum Units on a Truck
https://leetcode.com/problems/maximum-units-on-a-truck/

Description & Requirement:
    You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, 
    where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
        numberOfBoxesi is the number of boxes of type i.
        numberOfUnitsPerBoxi is the number of units in each box of the type i.

    You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. 
    You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

    Return the maximum total number of units that can be put on the truck.

Example 1:
    Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
    Output: 8
    Explanation: There are:
        - 1 box of the first type that contains 3 units.
        - 2 boxes of the second type that contain 2 units each.
        - 3 boxes of the third type that contain 1 unit each.
        You can take all the boxes of the first and second types, and one box of the third type.
        The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
Example 2:
    Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
    Output: 91

Constraints:
    1 <= boxTypes.length <= 1000
    1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
    1 <= truckSize <= 10^6
"""


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # exception case
        assert isinstance(truckSize, int) and truckSize >= 1
        assert isinstance(boxTypes, list) and len(boxTypes) >= 1
        for box in boxTypes:
            assert isinstance(box, list) and len(box) == 2 and box[0] >= 1 and box[1] >= 1
        # main method: (sort & greedy)
        return self._maximumUnits(boxTypes, truckSize)

    def _maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        assert isinstance(truckSize, int) and truckSize >= 1
        assert isinstance(boxTypes, list) and len(boxTypes) >= 1

        boxTypes.sort(key=lambda x: (-x[1], -x[0]))
        res = 0
        cur_size = 0
        for box in boxTypes:
            box_num, units = box[0], box[1]
            if cur_size + box_num <= truckSize:
                res += box_num * units
                cur_size += box_num
                continue
            else:
                rest_num = truckSize - cur_size
                res += rest_num * units
                break

        return res


def main():
    # Example 1: Output: 8
    # boxTypes = [[1, 3], [2, 2], [3, 1]]
    # truckSize = 4

    # Example 2: Output: 91
    boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truckSize = 10

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.maximumUnits(boxTypes, truckSize)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
