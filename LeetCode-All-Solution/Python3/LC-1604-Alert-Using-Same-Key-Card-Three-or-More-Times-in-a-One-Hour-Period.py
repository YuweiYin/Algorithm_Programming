#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1604-Alert-Using-Same-Key-Card-Three-or-More-Times-in-a-One-Hour-Period.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-02-07
=================================================================="""

import sys
import time
from typing import List
import collections
# import functools

"""
LeetCode - 1604 - (Medium) - Alert Using Same Key-Card Three or More Times in a One Hour Period
https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

Description & Requirement:
    LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, 
    the security system saves the worker's name and the time when it was used. 
    The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

    You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name 
    and the time when their key-card was used in a single day.

    Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

    Return a list of unique worker names who received an alert for frequent keycard use. 
    Sort the names in ascending order alphabetically.

    Notice that "10:00" - "11:00" is considered to be within a one-hour period, 
    while "22:51" - "23:52" is not considered to be within a one-hour period.

Example 1:
    Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], 
        keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
    Output: ["daniel"]
    Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").
Example 2:
    Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"], 
        keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
    Output: ["bob"]
    Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").

Constraints:
    1 <= keyName.length, keyTime.length <= 10^5
    keyName.length == keyTime.length
    keyTime[i] is in the format "HH:MM".
    [keyName[i], keyTime[i]] is unique.
    1 <= keyName[i].length <= 10
    keyName[i] contains only lowercase English letters.
"""


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        # exception case
        assert isinstance(keyName, list) and len(keyName) >= 1
        assert isinstance(keyTime, list) and len(keyTime) == len(keyName)
        # main method: (sorting and hast dict)
        return self._alertNames(keyName, keyTime)

    def _alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        """
        Time: beats 97.8%; Space: beats 93.7%
        """
        assert isinstance(keyName, list) and len(keyName) >= 1
        assert isinstance(keyTime, list) and len(keyTime) == len(keyName)

        time_map = collections.defaultdict(list)
        for k_name, k_time in zip(keyName, keyTime):
            hour, minute = int(k_time[:2]), int(k_time[3:])
            time_map[k_name].append(hour * 60 + minute)

        res = []
        for k_name, k_times in time_map.items():
            k_times.sort()
            if any(t2 - t1 <= 60 for t1, t2 in zip(k_times, k_times[2:])):
                res.append(k_name)

        res.sort()
        return res


def main():
    # Example 1: Output: ["daniel"]
    # keyName = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"]
    # keyTime = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]

    # Example 2: Output: ["bob"]
    keyName = ["alice", "alice", "alice", "bob", "bob", "bob", "bob"]
    keyTime = ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.alertNames(keyName, keyTime)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
