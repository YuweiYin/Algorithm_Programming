#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0933-Number-of-Recent-Calls.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-05-06
=================================================================="""

import sys
import time
import bisect
# from typing import List
# import functools

"""
LeetCode - 0933 - (Easy) - Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/

Description & Requirement:
    You have a RecentCounter class which counts the number of recent requests within a certain time frame.

    Implement the RecentCounter class:
        RecentCounter() Initializes the counter with zero recent requests.
        int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and 
            returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
            Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

    It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:
    Input
        ["RecentCounter", "ping", "ping", "ping", "ping"]
        [[], [1], [100], [3001], [3002]]
    Output
        [null, 1, 2, 3, 3]
    Explanation
        RecentCounter recentCounter = new RecentCounter();
        recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
        recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
        recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
        recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

Constraints:
    1 <= t <= 10^9
    Each test case will call ping with strictly increasing values of t.
    At most 10^4 calls will be made to ping.
"""


class RecentCounter:

    def __init__(self):
        self.ping_list = []
        self.INTERVAL = 3000

    def ping(self, t: int) -> int:
        if len(self.ping_list) == 0:
            self.ping_list.append(t)
            return 1
        # assert t > self.ping_list[-1]
        self.ping_list.append(t)
        target = t - self.INTERVAL
        if target <= 0:  # all items in the ping_list should be included
            return len(self.ping_list)
        else:  # binary search target in the ping_list
            # bs_idx = bisect.bisect(self.ping_list, target)
            bs_idx = bisect.bisect_left(self.ping_list, target)
            return len(self.ping_list) - bs_idx


def main():
    # Example 1: Output: [null, 1, 2, 3, 3]
    command_list = ["RecentCounter", "ping", "ping", "ping", "ping"]
    param_list = [[], [1], [100], [3001], [3002]]

    # init instance
    # solution = Solution()
    obj = RecentCounter()
    ans = ["null"]

    # run & time
    start = time.process_time()
    assert len(command_list) == len(param_list)
    for idx in range(1, len(command_list)):
        command = command_list[idx]
        param = param_list[idx]
        if command == "ping":
            if isinstance(param, list) and len(param) == 1:
                ans.append(obj.ping(param[0]))
            else:
                ans.append("null")
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
