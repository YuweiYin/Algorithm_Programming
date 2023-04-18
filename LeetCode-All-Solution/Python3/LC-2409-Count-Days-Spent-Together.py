#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-2409-Count-Days-Spent-Together.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2023-04-17
=================================================================="""

import sys
import time
from typing import List
# import collections
# import functools

"""
LeetCode - 2409 - (Easy) - Count Days Spent Together
https://leetcode.com/problems/count-days-spent-together/

Description & Requirement:
    Alice and Bob are traveling to Rome for separate business meetings.

    You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. 
    Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), 
    while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). 
    Each will be a 5-character string in the format "MM-DD", 
    corresponding to the month and day of the date.

    Return the total number of days that Alice and Bob are in Rome together.

    You can assume that all dates occur in the same calendar year, which is not a leap year. 
    Note that the number of days per month can be represented as: 
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

Example 1:
    Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
    Output: 3
    Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
Example 2:
    Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
    Output: 0
    Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.

Constraints:
    All dates are provided in the format "MM-DD".
    Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
    The given dates are valid dates of a non-leap year.
"""


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # exception case
        assert isinstance(arriveAlice, str) and len(arriveAlice) == 5
        assert isinstance(leaveAlice, str) and len(leaveAlice) == 5
        assert isinstance(arriveBob, str) and len(arriveBob) == 5
        assert isinstance(leaveBob, str) and len(leaveBob) == 5
        # main method: (prefix sum)
        return self._countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)

    def _countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        assert isinstance(arriveAlice, str) and len(arriveAlice) == 5
        assert isinstance(leaveAlice, str) and len(leaveAlice) == 5
        assert isinstance(arriveBob, str) and len(arriveBob) == 5
        assert isinstance(leaveBob, str) and len(leaveBob) == 5

        def __calculate_day_of_year(cur_day: str) -> int:
            cur_month = int(cur_day[:2])
            cur_date = int(cur_day[3:])
            return prefix_sum[cur_month - 1] + cur_date

        dates_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix_sum = [0]
        for date in dates_of_months:
            prefix_sum.append(prefix_sum[-1] + date)

        arriveAliceDay = __calculate_day_of_year(arriveAlice)
        leaveAliceDay = __calculate_day_of_year(leaveAlice)
        arriveBobDay = __calculate_day_of_year(arriveBob)
        leaveBobDay = __calculate_day_of_year(leaveBob)
        return max(0, min(leaveAliceDay, leaveBobDay) - max(arriveAliceDay, arriveBobDay) + 1)


def main():
    # Example 1: Output: 3
    arriveAlice = "08-15"
    leaveAlice = "08-18"
    arriveBob = "08-16"
    leaveBob = "08-19"

    # Example 2: Output: 0
    # arriveAlice = "10-01"
    # leaveAlice = "10-31"
    # arriveBob = "11-01"
    # leaveBob = "12-31"

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
