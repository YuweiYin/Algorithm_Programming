#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2532-Time-to-Cross-a-Bridge.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-07-07
=================================================================="""

import sys
import time
from typing import List
import heapq
# import functools
# import itertools

"""
LeetCode - 2532 - (Hard) - Time to Cross a Bridge
https://leetcode.com/problems/time-to-cross-a-bridge/

Description & Requirement:
    There are k workers who want to move n boxes from an old warehouse to a new one. 
    You are given the two integers n and k, and a 2D integer array time of size k x 4 
    where time[i] = [leftToRight_i, pickOld_i, rightToLeft_i, putNew_i].

    The warehouses are separated by a river and connected by a bridge. 
    The old warehouse is on the right bank of the river, and the new warehouse is on the left bank of the river. 
    Initially, all k workers are waiting on the left side of the bridge. 
    To move the boxes, the ith worker (0-indexed) can:
        Cross the bridge from the left bank (new warehouse) to the right bank (old warehouse) in leftToRight_i minutes.
        Pick a box from the old warehouse and return to the bridge in pickOld_i minutes. 
            Different workers can pick up their boxes simultaneously.
        Cross the bridge from the right bank (old warehouse) to the left bank (new warehouse) in rightToLeft_i minutes.
        Put the box in the new warehouse and return to the bridge in putNew_i minutes. 
            Different workers can put their boxes simultaneously.

    A worker i is less efficient than a worker j if either condition is met:
        leftToRight_i + rightToLeft_i > leftToRightj + rightToLeftj
        leftToRight_i + rightToLeft_i == leftToRightj + rightToLeftj and i > j

    The following rules regulate the movement of the workers through the bridge :
        If a worker x reaches the bridge while another worker y is crossing the bridge, 
            x waits at their side of the bridge.
        If the bridge is free, the worker waiting on the right side of the bridge gets to cross the bridge. 
            If more than one worker is waiting on the right side, the one with the lowest efficiency crosses first.
        If the bridge is free and no worker is waiting on the right side, and at least one box remains 
            at the old warehouse, the worker on the left side of the river gets to cross the bridge. 
            If more than one worker is waiting on the left side, the one with the lowest efficiency crosses first.

    Return the instance of time at which the last worker reaches the left bank of the river 
    after all n boxes have been put in the new warehouse.

Example 1:
    Input: n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
    Output: 6
    Explanation: 
        From 0 to 1: worker 2 crosses the bridge from the left bank to the right bank.
        From 1 to 2: worker 2 picks up a box from the old warehouse.
        From 2 to 6: worker 2 crosses the bridge from the right bank to the left bank.
        From 6 to 7: worker 2 puts a box at the new warehouse.
        The whole process ends after 7 minutes. We return 6 because the problem 
        asks for the instance of time at which the last worker reaches the left bank.
Example 2:
    Input: n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]
    Output: 50
    Explanation: 
        From 0  to 10: worker 1 crosses the bridge from the left bank to the right bank.
        From 10 to 20: worker 1 picks up a box from the old warehouse.
        From 10 to 11: worker 0 crosses the bridge from the left bank to the right bank.
        From 11 to 20: worker 0 picks up a box from the old warehouse.
        From 20 to 30: worker 1 crosses the bridge from the right bank to the left bank.
        From 30 to 40: worker 1 puts a box at the new warehouse.
        From 30 to 31: worker 0 crosses the bridge from the right bank to the left bank.
        From 31 to 39: worker 0 puts a box at the new warehouse.
        From 39 to 40: worker 0 crosses the bridge from the left bank to the right bank.
        From 40 to 49: worker 0 picks up a box from the old warehouse.
        From 49 to 50: worker 0 crosses the bridge from the right bank to the left bank.
        From 50 to 58: worker 0 puts a box at the new warehouse.
        The whole process ends after 58 minutes. We return 50 because the problem 
        asks for the instance of time at which the last worker reaches the left bank.

Constraints:
    1 <= n, k <= 10^4
    time.length == k
    time[i].length == 4
    1 <= leftToRight_i, pickOld_i, rightToLeft_i, putNew_i <= 1000
"""


class Solution:
    def findCrossingTime(self, n: int, k: int, _time: List[List[int]]) -> int:
        # exception case
        assert isinstance(n, int) and n >= 1
        assert isinstance(k, int) and k >= 1
        assert isinstance(_time, list) and len(_time) == k
        # main method: (priority queue)
        return self._findCrossingTime(n, k, _time)

    def _findCrossingTime(self, n: int, k: int, _time: List[List[int]]) -> int:
        assert isinstance(n, int) and n >= 1
        assert isinstance(k, int) and k >= 1
        assert isinstance(_time, list) and len(_time) == k

        _time.sort(key=lambda x: x[0] + x[2])
        cur = 0
        wait_in_left, wait_in_right = [], []
        work_in_left, work_in_right = [], []
        for i in range(k):
            heapq.heappush(wait_in_left, -i)

        while True:
            while work_in_left:
                t, i = work_in_left[0]
                if t > cur:
                    break
                heapq.heappop(work_in_left)
                heapq.heappush(wait_in_left, -i)
            while work_in_right:
                t, i = work_in_right[0]
                if t > cur:
                    break
                heapq.heappop(work_in_right)
                heapq.heappush(wait_in_right, -i)

            left_to_go = n > 0 and wait_in_left
            right_to_go = bool(wait_in_right)
            if not left_to_go and not right_to_go:
                nxt = int(1e9+7)
                if work_in_left:
                    nxt = min(nxt, work_in_left[0][0])
                if work_in_right:
                    nxt = min(nxt, work_in_right[0][0])
                cur = nxt
                continue
            if right_to_go:
                i = -heapq.heappop(wait_in_right)
                cur += _time[i][2]
                if n == 0 and not wait_in_right and not work_in_right:
                    return cur
                heapq.heappush(work_in_left, (cur + _time[i][3], i))
            else:
                i = -heapq.heappop(wait_in_left)
                cur += _time[i][0]
                n -= 1
                heapq.heappush(work_in_right, (cur + _time[i][1], i))


def main():
    # Example 1: Output: 6
    # n = 1
    # k = 3
    # _time = [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]]

    # Example 2: Output: 50
    n = 3
    k = 2
    _time = [[1, 9, 1, 8], [10, 10, 10, 10]]

    # init instance
    solution = Solution()

    # run & time
    _start = time.process_time()
    ans = solution.findCrossingTime(n, k, _time)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - _start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
