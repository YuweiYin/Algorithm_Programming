#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1185-Day-of-the-Week.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-04
=================================================================="""

import sys
import time
from typing import List

"""
LeetCode - 1185 - (Easy) - Day of the Week
https://leetcode.com/problems/day-of-the-week/

Description:
    Given a date, return the corresponding day of the week for that date.
    The input is given as three integers representing the day, month and year respectively.

Requirement:
    Return the answer as one of the following values 
    {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Example 1:
    Input: day = 31, month = 8, year = 2019
    Output: "Saturday"
Example 2:
    Input: day = 18, month = 7, year = 1999
    Output: "Sunday"
Example 3:
    Input: day = 15, month = 8, year = 1993
    Output: "Sunday"

Constraints:
    The given dates are valid dates between the years 1971 and 2100.
"""


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # exception case
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int) or\
                day <= 0 or day > 31 or month <= 0 or month > 12:
            return "Error"

        # Trick: use calendar package (But this is slow)
        # import calendar
        # return self._convert_wday_number_to_str(calendar.weekday(year, month, day))

        # main method: (1. get today's date information; 2. count the days diff; 3. find out the week day.)
        return self._dayOfTheWeek(day, month, year)

    def _dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # 1. get today's date information
        import time
        localtime = time.localtime(time.time())
        cur_year = localtime.tm_year
        cur_month = localtime.tm_mon
        cur_yday = localtime.tm_yday
        cur_wday = localtime.tm_wday

        # 2. count the days diff
        diff_day_count = 0
        if year < cur_year:
            # if_tgt_before = True
            # A 2.1. count the days of whole gap years
            start_whole_year = year + 1
            end_whole_year = cur_year - 1
            while start_whole_year <= end_whole_year:
                diff_day_count += self._get_day_count_of_a_year(start_whole_year)
                start_whole_year += 1

            # A 2.2. count the days of whole gap months in `year` and `cur_year`
            start_whole_month_of_tgt_year = month + 1
            end_whole_month_of_tgt_year = 12  # to December
            start_whole_month_of_cur_year = 1  # from January
            end_whole_month_of_cur_year = cur_month - 1
            while start_whole_month_of_tgt_year <= end_whole_month_of_tgt_year:
                diff_day_count += self._get_day_count_of_a_month(start_whole_month_of_tgt_year, year)
                start_whole_month_of_tgt_year += 1
            while start_whole_month_of_cur_year <= end_whole_month_of_cur_year:
                diff_day_count += self._get_day_count_of_a_month(start_whole_month_of_cur_year, cur_year)
                start_whole_month_of_cur_year += 1

            # A 2.3. count the rest days in `month` and `cur_month`
            start_rest_day_of_tgt_month = day
            end_rest_day_of_tgt_month = self._get_day_count_of_a_month(month, year)  # to the last day of this month
            start_rest_day_of_cur_month = 1  # from the first day of this month
            end_rest_day_of_cur_month = cur_yday
            if end_rest_day_of_tgt_month > start_rest_day_of_tgt_month:
                diff_day_count += (end_rest_day_of_tgt_month - start_rest_day_of_tgt_month)
            if end_rest_day_of_cur_month > start_rest_day_of_cur_month:
                diff_day_count += (end_rest_day_of_cur_month - start_rest_day_of_cur_month)

            # A 3. find out the week day
            diff_day_count += 1
            # tgt_wday = (cur_wday - diff_day_count) % 7
            tgt_wday = (cur_wday + 7 - (diff_day_count % 7)) % 7
            return self._convert_wday_number_to_str(tgt_wday)
        elif year > cur_year:
            # if_tgt_before = False
            # B 2.1. count the days of whole gap years
            start_whole_year = cur_year + 1
            end_whole_year = year - 1
            while start_whole_year <= end_whole_year:
                diff_day_count += self._get_day_count_of_a_year(start_whole_year)
                start_whole_year += 1

            # B 2.2. count the days of whole gap months in `year` and `cur_year`
            start_whole_month_of_tgt_year = 1  # from January
            end_whole_month_of_tgt_year = month - 1
            start_whole_month_of_cur_year = cur_month + 1
            end_whole_month_of_cur_year = 12  # to December
            while start_whole_month_of_tgt_year <= end_whole_month_of_tgt_year:
                diff_day_count += self._get_day_count_of_a_month(start_whole_month_of_tgt_year, year)
                start_whole_month_of_tgt_year += 1
            while start_whole_month_of_cur_year <= end_whole_month_of_cur_year:
                diff_day_count += self._get_day_count_of_a_month(start_whole_month_of_cur_year, cur_year)
                start_whole_month_of_cur_year += 1

            # B 2.3. count the rest days in `month` and `cur_month`
            start_rest_day_of_tgt_month = 1  # from the first day of this month
            end_rest_day_of_tgt_month = day
            start_rest_day_of_cur_month = cur_yday
            end_rest_day_of_cur_month = self._get_day_count_of_a_month(cur_month, cur_year)
            if end_rest_day_of_tgt_month > start_rest_day_of_tgt_month:
                diff_day_count += (end_rest_day_of_tgt_month - start_rest_day_of_tgt_month)
            if end_rest_day_of_cur_month > start_rest_day_of_cur_month:
                diff_day_count += (end_rest_day_of_cur_month - start_rest_day_of_cur_month)

            # B 3. find out the week day
            diff_day_count += 1
            tgt_wday = (cur_wday + diff_day_count) % 7
            return self._convert_wday_number_to_str(tgt_wday)
        else:  # the same year
            if month < cur_month:
                # if_tgt_before = True
                # C 2.2. count the days of whole gap months in `year` and `cur_year`
                start_whole_month_of_tgt_year = month + 1
                end_whole_month_of_tgt_year = 12  # to December
                start_whole_month_of_cur_year = 1  # from January
                end_whole_month_of_cur_year = cur_month - 1
                while start_whole_month_of_tgt_year <= end_whole_month_of_tgt_year:
                    diff_day_count += self._get_day_count_of_a_month(start_whole_month_of_tgt_year, year)
                    start_whole_month_of_tgt_year += 1
                while start_whole_month_of_cur_year <= end_whole_month_of_cur_year:
                    diff_day_count += self._get_day_count_of_a_month(start_whole_month_of_cur_year, cur_year)
                    start_whole_month_of_cur_year += 1

                # C 2.3. count the rest days in `month` and `cur_month`
                start_rest_day_of_tgt_month = day + 1
                end_rest_day_of_tgt_month = self._get_day_count_of_a_month(month, year)  # to the last day of this month
                start_rest_day_of_cur_month = 1  # from the first day of this month
                end_rest_day_of_cur_month = cur_yday - 1
                if end_rest_day_of_tgt_month > start_rest_day_of_tgt_month:
                    diff_day_count += (end_rest_day_of_tgt_month - start_rest_day_of_tgt_month)
                if end_rest_day_of_cur_month > start_rest_day_of_cur_month:
                    diff_day_count += (end_rest_day_of_cur_month - start_rest_day_of_cur_month)

                # C 3. find out the week day
                diff_day_count += 1
                tgt_wday = (cur_wday - diff_day_count) % 7
                return self._convert_wday_number_to_str(tgt_wday)
            elif month > cur_month:
                # if_tgt_before = False
                # D 2.2. count the days of whole gap months in `year` and `cur_year`
                start_whole_month_of_tgt_year = 1  # from January
                end_whole_month_of_tgt_year = month - 1
                start_whole_month_of_cur_year = cur_month + 1
                end_whole_month_of_cur_year = 12  # to December
                while start_whole_month_of_tgt_year <= end_whole_month_of_tgt_year:
                    diff_day_count += self._get_day_count_of_a_month(start_whole_month_of_tgt_year, year)
                    start_whole_month_of_tgt_year += 1
                while start_whole_month_of_cur_year <= end_whole_month_of_cur_year:
                    diff_day_count += self._get_day_count_of_a_month(start_whole_month_of_cur_year, cur_year)
                    start_whole_month_of_cur_year += 1

                # D 2.3. count the rest days in `month` and `cur_month`
                start_rest_day_of_tgt_month = 1  # from the first day of this month
                end_rest_day_of_tgt_month = day - 1
                start_rest_day_of_cur_month = cur_yday + 1
                end_rest_day_of_cur_month = self._get_day_count_of_a_month(cur_month, cur_year)
                if end_rest_day_of_tgt_month > start_rest_day_of_tgt_month:
                    diff_day_count += (end_rest_day_of_tgt_month - start_rest_day_of_tgt_month)
                if end_rest_day_of_cur_month > start_rest_day_of_cur_month:
                    diff_day_count += (end_rest_day_of_cur_month - start_rest_day_of_cur_month)

                # D 3. find out the week day
                diff_day_count += 1
                tgt_wday = (cur_wday + diff_day_count) % 7
                return self._convert_wday_number_to_str(tgt_wday)
            else:  # the same month & year
                if day < cur_yday:
                    # if_tgt_before = True
                    # E 2.3. count the rest days in `month` and `cur_month`
                    diff_day_count = cur_yday - day

                    # E 3. find out the week day
                    tgt_wday = (cur_wday - diff_day_count) % 7
                    return self._convert_wday_number_to_str(tgt_wday)
                if day > cur_yday:
                    # if_tgt_before = False
                    # F 2.3. count the rest days in `month` and `cur_month`
                    diff_day_count = day - cur_yday

                    # F 3. find out the week day
                    tgt_wday = (cur_wday + diff_day_count) % 7
                    return self._convert_wday_number_to_str(tgt_wday)
                else:  # the same day
                    return self._convert_wday_number_to_str(cur_wday)

    def _get_day_count_of_a_year(self, year: int) -> int:
        return 366 if self._if_leap_year(year) else 365

    def _get_day_count_of_a_month(self, month: int, year: int) -> int:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        elif month == 2:
            return 29 if self._if_leap_year(year) else 28
        else:
            return 0  # error month input

    @staticmethod
    def _if_leap_year(year: int) -> bool:
        # Leap Year: In the Gregorian calendar, any year divisible by 4 except centenary years not divisible by 400
        # There are 366 days in a leap year (February 29 exists), while 355 days in a non-leap year.
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # eg. 2000 is a leap year
            else:
                return False  # eg. 1900 is not a leap year
        elif year % 4 == 0:
            return True  # eg. 2004 is a leap year
        else:
            return False  # eg. 1989 is not a leap year

    @staticmethod
    def _convert_wday_number_to_str(wday: int) -> str:
        # {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
        if wday == 0:
            return "Monday"
        elif wday == 1:
            return "Tuesday"
        elif wday == 2:
            return "Wednesday"
        elif wday == 3:
            return "Thursday"
        elif wday == 4:
            return "Friday"
        elif wday == 5:
            return "Saturday"
        elif wday == 6:
            return "Sunday"
        else:
            return "Error Week Day"


def main():
    # Example 1: Output: "Saturday"
    # day = 31
    # month = 8
    # year = 2019

    # Example 2: Output: "Sunday"
    # day = 18
    # month = 7
    # year = 1999

    # Example 3: Output: "Sunday"
    day = 15
    month = 8
    year = 1993

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.dayOfTheWeek(day, month, year)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
