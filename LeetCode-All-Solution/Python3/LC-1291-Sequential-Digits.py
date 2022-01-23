#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-1291-Sequential-Digits.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-01-23
=================================================================="""

import sys
import time
from typing import List
# import collections

"""
LeetCode - 1291 - (Medium) - Sequential Digits
https://leetcode.com/problems/sequential-digits/

Description & Requirement:
    An integer has sequential digits if and only if 
    each digit in the number is one more than the previous digit.

    Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
    Input: low = 100, high = 300
    Output: [123,234]
Example 2:
    Input: low = 1000, high = 13000
    Output: [1234,2345,3456,4567,5678,6789,12345]

Constraints:
    10 <= low <= high <= 10^9
"""


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # exception case
        if not isinstance(low, int) or not isinstance(high, int) or low > high:
            return []  # Error input type
        # main method: (just try all possible sequential digits, start from number 1, 2, ..., 8), not 9
        # return self._sequentialDigits(low, high)
        return self._sequentialDigitsHack(low, high)

    def _sequentialDigits(self, low: int, high: int) -> List[int]:
        """
        Runtime: 28 ms, faster than 84.52% of Python3 online submissions for Sequential Digits.
        Memory Usage: 14.4 MB, less than 22.22% of Python3 online submissions for Sequential Digits.
        """
        assert 10 <= low <= high <= int(1e9)

        res_list = []

        def __dfs(cur_num: int, cur_digit: int):
            cur_num = cur_num * 10 + cur_digit  # construct sequential digits
            if low <= cur_num <= high:
                res_list.append(cur_num)
            if cur_num > high or cur_digit >= 9:
                return
            __dfs(cur_num, cur_digit + 1)  # next sequential digits

        for start_number in range(1, 9):  # start 1, 2, ... 8 (not 9)
            __dfs(start_number, start_number + 1)

        return sorted(res_list)

    def _sequentialDigitsHack(self, low: int, high: int) -> List[int]:
        assert 10 <= low <= high <= int(1e9)

        all_possible_res = [
            12, 23, 34, 45, 56, 67, 78, 89,
            123, 234, 345, 456, 567, 678, 789,
            1234, 2345, 3456, 4567, 5678, 6789,
            12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789,
            1234567, 2345678, 3456789, 12345678, 23456789, 123456789
        ]

        if high < all_possible_res[0] or low > all_possible_res[len(all_possible_res) - 1]:
            return []

        start_index = 0
        end_index = len(all_possible_res) - 1
        while start_index < end_index and all_possible_res[start_index] < low:
            start_index += 1

        while end_index > start_index and all_possible_res[end_index] > high:
            end_index -= 1

        if start_index == end_index:
            return [all_possible_res[start_index]] if low <= all_possible_res[start_index] <= high else []
        return all_possible_res[start_index: end_index + 1]


def main():
    # Example 1: Output: [123,234]
    # low = 100
    # high = 300

    # Example 2: Output: [1234,2345,3456,4567,5678,6789,12345]
    # low = 1000
    # high = 13000

    # Example 3: Output: [
    #     12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789,
    #     23, 234, 2345, 23456, 234567, 2345678, 23456789,
    #     34, 345, 3456, 34567, 345678, 3456789,
    #     45, 456, 4567, 45678, 456789,
    #     56, 567, 5678, 56789,
    #     67, 678, 6789,
    #     78, 789,
    #     89]
    low = 10
    high = int(1e9)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.sequentialDigits(low, high)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
