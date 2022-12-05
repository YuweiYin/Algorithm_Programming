#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1687-Delivering-Boxes-from-Storage-to-Ports.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-12-05
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1687 - (Hard) - Delivering Boxes from Storage to Ports
https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

Description & Requirement:
    You have the task of delivering some boxes from storage to their ports using only one ship. 
    However, this ship has a limit on the number of boxes and the total weight that it can carry.

    You are given an array boxes, where boxes[i] = [ports_i, weight_i], 
    and three integers portsCount, maxBoxes, and maxWeight.
        ports_i is the port where you need to deliver the ith box and weightsi is the weight of the ith box.
        portsCount is the number of ports.
        maxBoxes and maxWeight are the respective box and weight limits of the ship.

    The boxes need to be delivered in the order they are given. The ship will follow these steps:
        The ship will take some number of boxes from the boxes queue, 
            not violating the maxBoxes and maxWeight constraints.
        For each loaded box in order, the ship will make a trip to the port the box needs to be delivered 
            to and deliver it. If the ship is already at the correct port, no trip is needed, 
            and the box can immediately be delivered.
        The ship then makes a return trip to storage to take more boxes from the queue.

    The ship must end at storage after all the boxes have been delivered.

    Return the minimum number of trips the ship needs to make to deliver all boxes to their respective ports.

Example 1:
    Input: boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3
    Output: 4
    Explanation: The optimal strategy is as follows: 
        - The ship takes all the boxes in the queue, goes to port 1, then port 2, 
            then port 1 again, then returns to storage. 4 trips.
        So the total number of trips is 4.
        Note that the first and third boxes cannot be delivered together because the boxes need to be delivered 
            in order (i.e. the second box needs to be delivered at port 2 before the third box).
Example 2:
    Input: boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6
    Output: 6
    Explanation: The optimal strategy is as follows: 
        - The ship takes the first box, goes to port 1, then returns to storage. 2 trips.
        - The ship takes the second, third and fourth boxes, goes to port 3, then returns to storage. 2 trips.
        - The ship takes the fifth box, goes to port 3, then returns to storage. 2 trips.
        So the total number of trips is 2 + 2 + 2 = 6.
Example 3:
    Input: boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7
    Output: 6
    Explanation: The optimal strategy is as follows:
        - The ship takes the first and second boxes, goes to port 1, then returns to storage. 2 trips.
        - The ship takes the third and fourth boxes, goes to port 2, then returns to storage. 2 trips.
        - The ship takes the fifth and sixth boxes, goes to port 3, then returns to storage. 2 trips.
        So the total number of trips is 2 + 2 + 2 = 6.

Constraints:
    1 <= boxes.length <= 10^5
    1 <= portsCount, maxBoxes, maxWeight <= 10^5
    1 <= ports_i <= portsCount
    1 <= weights_i <= maxWeight
"""


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        # exception case
        assert isinstance(boxes, list) and len(boxes) >= 1
        assert isinstance(portsCount, int) and portsCount >= 1
        assert isinstance(maxBoxes, int) and maxBoxes >= 1
        assert isinstance(maxWeight, int) and maxWeight >= 1
        # main method: (dynamic programming & monotonous stack)
        return self._boxDelivering(boxes, portsCount, maxBoxes, maxWeight)

    def _boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        assert isinstance(boxes, list) and len(boxes) >= 1
        assert isinstance(portsCount, int) and portsCount >= 1
        assert isinstance(maxBoxes, int) and maxBoxes >= 1
        assert isinstance(maxWeight, int) and maxWeight >= 1

        n = len(boxes)
        port, w_p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
        neg, weight = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]

        for idx in range(1, n + 1):
            port[idx], w_p[idx] = boxes[idx - 1]
            if idx > 1:
                neg[idx] = neg[idx - 1] + (port[idx - 1] != port[idx])
            weight[idx] = weight[idx - 1] + w_p[idx]

        queue = collections.deque([0])
        dp_1, dp_2 = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]

        for idx in range(1, n + 1):
            while idx - queue[0] > maxBoxes or weight[idx] - weight[queue[0]] > maxWeight:
                queue.popleft()

            dp_1[idx] = dp_2[queue[0]] + neg[idx] + 2

            if idx != n:
                dp_2[idx] = dp_1[idx] - neg[idx + 1]
                while queue and dp_2[idx] <= dp_2[queue[-1]]:
                    queue.pop()
                queue.append(idx)

        return dp_1[n]


def main():
    # Example 1: Output: 4
    # boxes = [[1, 1], [2, 1], [1, 1]]
    # portsCount = 2
    # maxBoxes = 3
    # maxWeight = 3

    # Example 2: Output: 6
    # boxes = [[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]]
    # portsCount = 3
    # maxBoxes = 3
    # maxWeight = 6

    # Example 3: Output: 6
    boxes = [[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]]
    portsCount = 3
    maxBoxes = 6
    maxWeight = 7

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.boxDelivering(boxes, portsCount, maxBoxes, maxWeight)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
