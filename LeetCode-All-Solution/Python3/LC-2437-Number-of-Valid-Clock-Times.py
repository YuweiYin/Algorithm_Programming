#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2437-Number-of-Valid-Clock-Times.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-05-09
=================================================================="""

import sys
import time
# from typing import List
# import collections
# import functools

"""
LeetCode - 2437 - (Medium) - Number of Valid Clock Times
https://leetcode.com/problems/number-of-valid-clock-times/

Description & Requirement:
    You are given a string of length 5 called time, representing the current time 
    on a digital clock in the format "hh:mm". 
    The earliest possible time is "00:00" and the latest possible time is "23:59".

    In the string time, the digits represented by the ? symbol are unknown, 
    and must be replaced with a digit from 0 to 9.

    Return an integer answer, the number of valid clock times that 
    can be created by replacing every ? with a digit from 0 to 9.

Example 1:
    Input: time = "?5:00"
    Output: 2
    Explanation: We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". 
        Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we have two choices.
Example 2:
    Input: time = "0?:0?"
    Output: 100
    Explanation: Each ? can be replaced by any digit from 0 to 9, so we have 100 total choices.
Example 3:
    Input: time = "??:??"
    Output: 1440
    Explanation: There are 24 possible choices for the hours, 
        and 60 possible choices for the minutes. In total, we have 24 * 60 = 1440 choices.

Constraints:
    time is a valid string of length 5 in the format "hh:mm".
    "00" <= hh <= "23"
    "00" <= mm <= "59"
    Some of the digits might be replaced with '?' and need to be replaced with digits from 0 to 9.
"""


class Solution:
    def countTime(self, time: str) -> int:
        # exception case
        assert isinstance(time, str) and len(time) == 5 and time[2] == ":"
        # main method: (two pointers)
        return self._countTime(time)

    def _countTime(self, time: str) -> int:
        assert isinstance(time, str) and len(time) == 5 and time[2] == ":"

        hour_cnt = 0
        minute_cnt = 0

        for i in range(24):
            hour_high = i // 10
            hour_low = i % 10
            if ((time[0] == "?" or int(time[0]) == hour_high) and
                    (time[1] == "?" or int(time[1]) == hour_low)):
                hour_cnt += 1

        for i in range(60):
            minute_high = i // 10
            minute_low = i % 10
            if ((time[3] == "?" or int(time[3]) == minute_high) and
                    (time[4] == "?" or int(time[4]) == minute_low)):
                minute_cnt += 1

        return hour_cnt * minute_cnt


def main():
    # Example 1: Output: 2
    _time = "?5:00"

    # Example 2: Output: 100
    # _time = "0?:0?"

    # Example 3: Output: 1440
    # _time = "??:??"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countTime(_time)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
